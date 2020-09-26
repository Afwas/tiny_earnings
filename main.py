import json
import requests
import sqlite3
import sys

from pprint import pprint

import secret

url = "https://api.torn.com/company/?selections={}&key={}".format(
    'detailed,profile', secret.API_KEY
)

if __name__ == "__main__":
    response = requests.get(url)
    company_json = json.loads(response.text)
    if "error" in company_json:
        # pprint(attacks_json);
        print("Error {}: {}".format(
            company_json["error"]["code"],
            company_json["error"]["error"]))
        sys.exit(1)

    pprint(company_json)
    daily_income = company_json['company']['daily_income']
    daily_customers = company_json['company']['daily_customers']
    weekly_income = company_json['company']['weekly_income']
    weekly_customers = company_json['company']['weekly_customers']
    advertising = company_json['company_detailed']['advertising_budget']
    query = """
    INSERT INTO earnings(
        daily_income, 
        daily_customers, 
        weekly_income, 
        weekly_customers,
        advertising)
    VALUES(?, ?, ?, ?, ?)
    ON CONFLICT(today) DO NOTHING;
    """
    conn = sqlite3.connect('earnings.sqlite')
    cur = conn.cursor()
    cur.execute(query, (
        daily_income,
        daily_customers,
        weekly_income,
        weekly_customers,
        advertising))
    conn.commit()
    conn.close()

    conn = sqlite3.connect('earnings.sqlite')
    for row in conn.execute("SELECT * FROM earnings;"):
        pprint(row)
    conn.close()
