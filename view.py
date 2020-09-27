import sqlite3

def view_sqltable():
    conn = sqlite3.connect('earnings.sqlite')
    header = "|  id |    date    | daily_income | daily_customers | weekly_income "
    header += "| weekly_customers | advertisement |"
    print(header)
    div = "+-----+------------+--------------+-----------------+---------------"
    div += "+------------------+---------------+"
    print(div)
    for row in conn.execute("SELECT * FROM earnings;"):
        items = [str(x) for x in row]
        line = "| {:>3} | {} |".format(*items[0:2])
        line += " {:>12} | {:>15} | {:>13} | {:>16} | {:>13} |".format(*items[2:8])
        print(line)
    conn.close()

def view_csv():
    conn = sqlite3.connect('earnings.sqlite')
    header = "id,date,daily_income,daily_customers,weekly_income,"
    header += "weekly_customers,advertisement"
    print(header)
    for row in conn.execute("SELECT * FROM earnings;"):
        items = [str(x) for x in row]
        line = ",".join(items)
        print(line)
    conn.close()
