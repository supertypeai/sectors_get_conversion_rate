# sectors_get_conversion_rate

Fetches the current USD to IDR exchange rate from the ExchangeRate-API, then saves the exchange rate along with the current datetime into a JSON file (`conversion_rate.json`).  

Sample content of `conversion_rate.json`:
```
{"USD": {"IDR": 15630.28}, "datetime": "2023-12-12 18:13:40"}
```
