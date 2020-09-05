# NSFG-RMDR

NSFG-RMDR is a customized implemenation of https://github.com/reminder-bot/bot modified to be unbranded, lighter and heroku ready

## Configuration

Configuration is managed through environemnt variables

ENVIRONMENT VARIABLE | REQUIRED
------------- | -------------
BOT_TOKEN | Y
MYSQL_ADDRESS | Y
MYSQL_DB_NAME | Y
MYSQL_USER | Y
MYSQL_PASSWORD | Y

## Setup

Get libs: `pip3 install --user -r requirements.txt`
Run: `python3 main.py`
