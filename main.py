import datetime
import json

import requests


def get_conversion_rate():
    conversion_rate = {}
    response = requests.get("https://api.exchangerate-api.com/v4/latest/USD")
    rate_data = response.json()
    usd_idr_rate = rate_data["rates"]["IDR"]
    conversion_rate["USD"] = {"IDR": usd_idr_rate}

    dt_now = datetime.datetime.now()
    conversion_rate["datetime"] = dt_now.strftime("%Y-%m-%d %H:%M:%S")

    return conversion_rate


if __name__ == "__main__":
    conversion_rate = get_conversion_rate()
    with open("conversion_rate.json", "w") as outfile:
        json.dump(conversion_rate, outfile)
