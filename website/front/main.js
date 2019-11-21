const submitBtn = document.querySelector(".submit-btn");

const blueFighterDiv = document.querySelector(".blue");
const redFighterDiv = document.querySelector(".red");

submitBtn.addEventListener("click", () => {
  blueInputs = blueFighterDiv.querySelectorAll('input');
  redInputs = redFighterDiv.querySelectorAll('input');
  winnerAnswerDiv = document.querySelector('.winner > h1');

  let postObject = {
    'wins' : [ redInputs[0].value / blueInputs[0].value ],
    'current_win_streak' : [ redInputs[1].value / blueInputs[1].value ],
    'current_lose_streak' : [ redInputs[2].value / blueInputs[2].value ],
    'losses' : [ redInputs[4].value / blueInputs[4].value ],
    'total_rounds_fought' : [ redInputs[3].value / blueInputs[3].value ],
    'total_time_fought(seconds)' : [ redInputs[6].value / blueInputs[6].value ],
    'age' : [ redInputs[5].value / blueInputs[5].value ],
  };

  console.log(postObject);

  postJson = JSON.stringify(postObject);
  postJson = JSON.parse(postJson);

  axios.post("http://127.0.0.1:5000/api", postJson)
  .then(response => {
    console.log(response.data);
    winnerAnswerDiv.innerText = response.data;
  });
});