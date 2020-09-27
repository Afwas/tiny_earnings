import model
import secret
import view

url = "https://api.torn.com/company/?selections={}&key={}".format(
    'detailed,profile', secret.API_KEY
)

if __name__ == "__main__":
    data = model.get_data_from_api(url)
    model.store_data(data)

    view.view_sqltable()
    view.view_csv()
