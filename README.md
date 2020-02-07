# calendar

# Requirements
* python 3
* pipenv
  - If you're on MacOS, you can install Pipenv easily with Homebrew:
      `$ brew install pipenv`
  - Debian Buster+:
      `$ sudo apt install pipenv`
  - Fedora:
      `$ sudo dnf install pipenv`
  - FreeBSD:
      `$ pkg install py36-pipenv`

# Setting up the project
* Clone the repo : `git clone https://github.com/graycadeau/calendar.git`
* Navigate to the cloned folder `$ cd calendar/`
* Run `$ pipenv shell` . This will create a virtual environment and pipfile for package requirements.
* Run `$ pipenv install` to install the packages in your environment.
* $ touch .env
* copy content of example_env.txt to .env and update the values to your own configs
* Run migrations `python manage.py migrate`
* Start the server `python manage.py runserver`

# Testing the project
* Create super user account `python manage.py createsuperuser`
* Start the server `python manage.py runserver`
* Open admin page `http://127.0.0.1:8000/admin/app/` and login with the    created credentials



