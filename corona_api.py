import requests
from datetime import date, timedelta

def get_current_corona_data():
    from_date = date.today() - timedelta(days=22)
    to_date = date.today()
    url="https://api.covid19api.com/country/germany/status/confirmed?from="+from_date.strftime("%Y-%m-%d")+"&to="+to_date.strftime("%Y-%m-%d")
    response=requests.get(url)
    return response.json()