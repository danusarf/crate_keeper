# crateDB_keeper
Hold crate db data with retention time of period

## It will:
    1. Backup your data to S3, by default backup data everyday
    2. Delete your old data from crateDB by default it will delete data longer than 60 days

## How to run:
    1. Install depedencies
    2. run main.py (./main.py)

## Best Practices:
    1. Setup depedencies
    2. Put cronjob to run main.py

