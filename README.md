# Serving the app

To host the web server, you will need to install Flask and XGBClassifier.
You may do this with the commands:
`pip install flask xgboost` or `conda install flask xgboost`

You will have to serve the flask backend on your machine, as the frontend makes requests to 127.0.0.1:5000

The jupyter notebook does not include the xgboost model, only sklearn models

## Alternatively, You can run pip install -r requirements.txt

from the directory "/website/back" , run the command: '''export FLASK_APP=server.py''' and then '''flask run'''
