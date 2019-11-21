from sklearn import metrics
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.utils.multiclass import unique_labels
import pandas as pd
from matplotlib import pyplot as plt
import numpy as np
from xgboost import XGBClassifier
import json

data = pd.read_csv("./ufcdata/data.csv")
data = data.truncate(0, 3500)

data["win"] = 0
data.loc[data.Winner == "Red", "win"] = 1

wins = data["win"]

def get_relevant_dictionary(df):
    dic = {}
    colunas = df.columns.values;
    for name in colunas:
        if name[0] == "R" and name != "Referee":
            oposer_name = "B"+name[1:]
            dic[name] = oposer_name
    return(dic)


def create_relative_df(data, relevant_categories):
    dic = {}
    for R_value, B_value in relevant_categories.items():
        if type(data[R_value].iloc[1]) == np.float64:
            dic["{}".format(R_value[2:])] = ((data[R_value] - data[B_value]) / data[B_value])
    relative_df = pd.DataFrame(dic)
    return relative_df


relevant_categories = get_relevant_dictionary(data)
relative_df = create_relative_df(data, relevant_categories)

relative_df["win"] = wins

y = relative_df["win"]
relative_df.drop(columns = "win")
X = relative_df[['wins', 'current_win_streak', 'current_lose_streak', 'losses', 'total_rounds_fought', 'total_time_fought(seconds)', 'age', ]]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=10)

model = XGBClassifier()
# model = KNeighborsClassifier()

model.fit(X_train, y_train)

y_pred = model.predict(X_test)

print("percent of red wins : " + str(relative_df.win.mean()))
print("model accuracy : " + str(metrics.accuracy_score(y_test, y_pred)))
print("percent model thinks red wins : " + str(y_pred.mean()))

def make_prediction(obj):
    dic = json.loads(obj)
    print(dic)
    df = pd.DataFrame(dic)
    print(df)
    single_prediction = model.predict(df)
    print(single_prediction)
    return single_prediction
