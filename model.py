import json
import requests
import sqlite3
import sys


def get_data_from_api(url):
    response = requests.get(url)
    company_json = json.loads(response.text)
    if "error" in company_json:
        print("Error {}: {}".format(
            company_json["error"]["code"],
            company_json["error"]["error"]))
        sys.exit(1)
    return company_json

def store_data(company_json):
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
