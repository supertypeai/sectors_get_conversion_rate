import datetime
import json

import requests


def get_conversion_rate():
    conversion_rate = {}
    
    response = requests.get("https://api.exchangerate-api.com/v4/latest/USD")
    usd_idr_rate = response.json()["rates"]["IDR"]
    usd_sgd_rate = response.json()["rates"]["SGD"]
    usd_myr_rate = response.json()["rates"]["MYR"]

    response = requests.get("https://api.exchangerate-api.com/v4/latest/AUD")
    aud_sgd_rate = response.json()["rates"]['SGD']

    response = requests.get("https://api.exchangerate-api.com/v4/latest/EUR")
    eur_sgd_rate = response.json()["rates"]['SGD']

    response = requests.get("https://api.exchangerate-api.com/v4/latest/GBP")
    gbp_sgd_rate = response.json()["rates"]['SGD']

    response = requests.get("https://api.exchangerate-api.com/v4/latest/HKD")
    hkd_sgd_rate = response.json()["rates"]['SGD']

    response = requests.get("https://api.exchangerate-api.com/v4/latest/CNY")
    cny_sgd_rate = response.json()["rates"]['SGD']
    cny_myr_rate = response.json()["rates"]['MYR']

    response = requests.get("https://api.exchangerate-api.com/v4/latest/IDR")
    idr_sgd_rate = response.json()["rates"]['SGD']

    response = requests.get("https://api.exchangerate-api.com/v4/latest/MYR")
    myr_sgd_rate = response.json()["rates"]['SGD']

    response = requests.get("https://api.exchangerate-api.com/v4/latest/PHP")
    php_sgd_rate = response.json()["rates"]['SGD']

    response = requests.get("https://api.exchangerate-api.com/v4/latest/THB")
    thb_sgd_rate = response.json()["rates"]['SGD']

    response = requests.get("https://api.exchangerate-api.com/v4/latest/TWD")
    twd_sgd_rate = response.json()["rates"]['SGD']


    conversion_rate["USD"] = {"IDR": usd_idr_rate,
                          "SGD":usd_sgd_rate,
                          "MYR":usd_myr_rate}

    conversion_rate["AUD"] = {"SGD":aud_sgd_rate}

    conversion_rate["EUR"] = {"SGD":eur_sgd_rate}

    conversion_rate["GBP"] = {"SGD":gbp_sgd_rate}

    conversion_rate["HKD"] = {"SGD":hkd_sgd_rate}

    conversion_rate["CNY"] = {"SGD":cny_sgd_rate,
                              "MYR":cny_myr_rate}

    conversion_rate["IDR"] = {"SGD":idr_sgd_rate}

    conversion_rate["MYR"] = {"SGD":myr_sgd_rate}

    conversion_rate["PHP"] = {"SGD":php_sgd_rate}

    conversion_rate["THB"] = {"SGD":thb_sgd_rate}

    conversion_rate["TWD"] = {"SGD":twd_sgd_rate}


    dt_now = datetime.datetime.now()
    conversion_rate["datetime"] = dt_now.strftime("%Y-%m-%d %H:%M:%S")

    return conversion_rate


if __name__ == "__main__":
    conversion_rate = get_conversion_rate()
    with open("conversion_rate.json", "w") as outfile:
        json.dump(conversion_rate, outfile)