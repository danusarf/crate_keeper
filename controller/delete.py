# importing the requests library
import requests
import os
import urllib.parse
import time
import calendar

def delete_api(API_ENDPOINT, current_time, retention):
    # data to be sent to api
    payload = {'stmt':'DELETE FROM metrics WHERE "timestamp" < ' + repr(current_time - retention * 86400) }

    # sending post request and saving response as response object
    r = requests.post(url = API_ENDPOINT, json = payload)

    # extracting response text
    response = "Successfully deleting "+ repr(retention) +" days data"
    return response