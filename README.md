## Pre-Requisites
* Python 3 (comes with MacOS)
* Pip `python -m ensurepip`
* Pipenv `pip install --user pipenv`


## Manual Setup
1- **Clone Repo**
* `git clone git@github.com:stackk1/iOS_Automation.git`

2- **Appium Server**
* Install XCode, Open and Accept Terms and Conditions
* Install XCode Command Line `xcode-select --install`
* Install HomeBrew `/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"`
* Install NPM `brew install npm`
* Install Carthage `npm install carthage`
* Install Appium `npm install -g appium@next`
* Install Appium xcuitest Driver `appium driver install xcuitest`
* (Optional) If you want recordings install ffmpeg `brew install ffmpeg`
* (Optional) Install Appium Doctor to check requirements are met`npm install -g appium-doctor` then run with `appium-doctor`

3- **Environment**

* Copy sample environment. `cp .env.sample .env`
* Edit `.env` file with applicable variables.

or
* Read `.env.sample` and set variables in your environment.

4- **Install Dependencies**
* `pipenv install`

5- Running Tests

* Ensure Appium Server Is Running
* Run `pytest tests/`