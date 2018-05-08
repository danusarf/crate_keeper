# importing the requests library
import requests
import os
import urllib.parse
import time
import calendar


def copy_api(API_ENDPOINT, size, current_time, backup_method, access_key, secret_key, bucket_name):

    current_date = time.strftime("%Y%m%d")
    # data to be sent to api
    payload = {"stmt":'COPY metrics WHERE "timestamp" > ' + repr(current_time - size * 86400) + ' TO DIRECTORY \'s3://' + access_key + ':' + secret_key + '@'+ bucket_name + current_date + '/\' WITH (compression=\'gzip\')'}

    # sending post request and saving response as response object
    r = requests.post(url = API_ENDPOINT, json = payload)

    # extracting response text
    response = "Successfully copied "+ repr(size) +" days of data"
    return response