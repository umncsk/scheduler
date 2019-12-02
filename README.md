# Easy scheduling API tool for Toyo University students
[![Actions Status](https://github.com/umncsk/scheduler/workflows/Python%20application/badge.svg)](https://github.com/umncsk/scheduler/actions)
[![Language grade: Python](https://img.shields.io/lgtm/grade/python/g/umncsk/scheduler.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/umncsk/scheduler/context:python)

講義データを抜きとるぞい!

## Getting start this project
### Using virtual environment with pipenv
#### Install dependent libraries in pipenv.
`pipenv install`

#### Start virtual environment
`pipenv shell`

#### Stop virtual environment
`deactivate` & `exit`

#### Add new library
`pipenv install <library_name>`

### About chromedriver dependency
> install chromedriver-binary with version definition as manually

`pipenv install chromedriver-binary==<your_current_chrome_version>`

### Check your chrome version
#### macOS terminal
```console
$ /Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome --version
```

#### Windows PowerShell 
maybe...
```console
$ reg query "HKEY_CURRENT_USER\Software\Google\Chrome\BLBeacon" /v version
```

## env custom commands
run server
`pipenv run server`

makemigrations
`pipenv run makemigrations`

migrate
`pipenv run migrate`

createsuperuser
`pipenv run createsuperuser`

run django shell
`pipenv run shell`
