# game-of-isolation-heroku
This will create a website to play the Game of Isolation. AI players are also introduced. 🎲

## User Guide

- AI players based on Algorithm:
  * Basic MinMax
  * MinMax with Alpha Beta Pruning

## Dev Guide

### Setting up local environment
- Clone the repo and create or use existing Miniconda Interpreter, choose python3
- `$ conda activate pyweb`
- `$ pip install -r requirements.txt`
- mark root folder as source.

### Deploy to Heroku
- Make sure you set `master` branch as the default branch in GitHub
- `$ heroku login`
- `$ heroku create weivdev-isolation-game` You can change the website name here 
- `$ git push heroku master`

You can now check the website here https://weivdev-isolation-game.herokuapp.com/ 

### Reference
- For AI Players: Gatech Artificial Intelligence Course https://omscs.gatech.edu/cs-6601-artificial-intelligence