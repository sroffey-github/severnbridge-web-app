
# Severn Bridge Web App

A git repository containing multiple scripts for checking the status of severn bridge, logging it and reporting it back to a web app


## Installation

Install my-project with bash

```bash
  cd severnbridge-web-app
  chmod +x setup.sh
  ./setup.sh
```

Edit `run.py` and add the mobile numbers you wish to notify to the `contacts` list

Add `run.py` as a cronjob
## Environment Variables

To run this project, you will need to add the following environment variables to your .env file

`LOG_PATH`

`DB_PATH`

`TWILIO_AUTH_TOKEN`

`TWILIO_ACCOUNT_SID`

