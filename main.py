# importing the requests library
import requests
import os
import urllib.parse
import time
import calendar
import controller.copy as copy
import controller.delete as delete

if __name__ == '__main__':
    # defining the api-endpoint
    API_ENDPOINT = "http://127.0.0.1:4200/_sql?pretty"
    retention = 60
    size = 1
    backup_method = "s3"
    current_time = calendar.timegm(time.gmtime())
    access_key  = urllib.parse.quote_plus(os.environ['AWS_ACCESS_KEY'])
    secret_key =  urllib.parse.quote_plus(os.environ['AWS_SECRET_KEY'])
    bucket_name = os.environ['CRATEDB_BUCKET_NAME']

    # CALL COPY API
    copy_response = copy.copy_api(API_ENDPOINT, size, current_time, backup_method, access_key, secret_key, bucket_name)
    print(copy_response)

    # CALL DELETE API
    delete_response = delete.delete_api(API_ENDPOINT, current_time, retention)
    print(delete_response)