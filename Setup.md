# Setup

## Clone Repository

* Make sure you have git installed
* I recommend cloning the repository from the command line using `git clone https://github.com/AWilde2000/Integral-Solutions`
* You can also download the zip but you will need to add the remote repository to add it to git using `git remote add origin https://github.com/AWilde2000/Integral-Solutions`

## Virtual Environment

Make sure you have python downloaded and installed already.
* Open a terminal (You can use cmd or vscode has an integrated terminal which you can open with `ctrl + shift + tilde`)
* Install virtualenv using `pip install virtualenv`
* Navigate to the src directory of Integral-Solutions using `cd src`. You can use `dir` to list files in the current folder and `cd folder-name` to change folders
* Create the virtual environment using `python -m virtualenv env`
* Activate it using `env\Scripts\activate`
* Install the required packages using `pip install -r requirements.txt`
* If you run in to errors installing the requirements, you can install them one by one using `pip install package-name` and the names from the `requirements.txt` file

## Add the .env file
* Add the `.env` file from the discord to the `src` directory. This file contains secret environment variables. It downloads as `env` from discord so make sure to rename it to `.env` so it doesn't interfere with the virtual environment

## Try running the Django server
* While in the `src` directory run `py manage.py runserver`
* In your browser, go to `http://127.0.0.1:8000/`

## Development
Create your own branch to work on and then create a pull request to merge with the main branch when you are done