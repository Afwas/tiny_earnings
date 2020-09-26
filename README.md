# tiny_earnings

## Collect earnings for the company
This is a user contributed script for the game Torn.
It is able to collect daily income for the company and it will store data in a SQLite database.

This standalone script is meant to be run through a daily cron job.

## Usage
Starters:
* Create a file `secret.py` with contents `API_KEY = "YOUR API KEY HERE"`.
* Run the file `python setup.py` which should create the database.
* Create a cronjob that runs te script `python main.py` at least once a day.

For more information contact player Afwas [1337627] in game.

## Licence
This script uses several Open Source tools
* [Python3](https://www.python.org/about/)
* [SQLite](https://www.sqlite.org/about.html)

The script itself (as presented in this repository)
(c) Foppe Hemminga, 2020 under an Open Soucce [MIT Licence](https://opensource.org/licenses/MIT)
