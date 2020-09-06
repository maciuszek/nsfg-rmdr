# NSFG-RMDR

NSFG-RMDR is a customized implemenation of https://github.com/reminder-bot/bot modified to be unbranded, lighter and heroku ready

## Setup

Get libs: `pip3 install --user -r requirements.txt`\
Prepare database: `create.sql`\
Run: `pyton3 nsfg-rmdr_languages/to_database.py`

### Configuration

Files:
* `config.ini` 
* `languages/config.ini`

Environemnt variables:
VARIABLE | REQUIRED
------------- | -------------
BOT_TOKEN | Y
MYSQL_ADDRESS | Y
MYSQL_DB_NAME | Y
MYSQL_USER | Y
MYSQL_PASSWORD | Y

## Run

Run: `python3 main.py`\
Run: https://github.com/maciuszek/nsfg-rmdr_postman
