# IP Watchdog

This project is written in python. Its main purpose is to run on a raspberry pi and be a watch dog for ip changes. Whenever the public ip changes it will be logged on google sheets.

A json file with credentials is needed for this to work. The file must be named "client_secret.json" and be in the root of the project.

This json file can be fetched from the google api. Not the best way to do it, but it works, so idc for now...
