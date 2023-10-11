import datetime
import json

from forex_python.converter import CurrencyRates


def get_conversion_rate():
    cr = CurrencyRates()
    conversion_rate = {}
    dt_now = datetime.datetime.now()
    conversion_rate["datetime"] = dt_now.strftime("%Y-%m-%d %H:%M:%S")
    conversion_rate["USD"] = {"IDR": cr.get_rate("USD", "IDR", dt_now)}
    return conversion_rate


if __name__ == "__main__":
    conversion_rate = get_conversion_rate()
    with open("conversion_rate.json", "w") as outfile:
        json.dump(conversion_rate, outfile)
