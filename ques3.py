'''
Write a Python script that checks the uptime of provided URLs and notifies the user if any of the URLs return 4xx or 5xx HTTP status codes (indicating client or server errors). For demonstration purposes, you can use the following URLs as inputs:
4xx (Client Error):
http://www.example.com/nonexistentpage or
http://httpstat.us/404
5xx (Server Error):
http://httpstat.us/500
200 (Successful Response):
https://www.google.com/

Bonus (Optional):
Implement an exponential backoff in case of multiple consecutive errors (e.g., retry after increasing intervals).
Add logging functionality to save the status check results to a log file.

'''

import requests
import time
import logging

urls = [
    "http://www.example.com/nonexistentpage",
    "http://httpstat.us/404",
    "http://httpstat.us/500",
    "https://www.google.com/"
]

logging.basicConfig(
    filename='uptime_monitor.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

failure_count = {url: 0 for url in urls}

def check_url_status(url):
    global failure_count
    try:
        response = requests.get(url, timeout=5)
        status_code = response.status_code

        if 200 <= status_code < 300:
            message = f"{url} - {status_code} OK: The website is UP and running."
            print(message)
            logging.info(message)
            failure_count[url] = 0

        elif 400 <= status_code < 500:
            message = f"{url} - {status_code} Client Error - ALERT : 4xx error encountered."
            print(message)
            logging.warning(message)
            failure_count[url] += 1

        elif 500 <= status_code < 600:
            message = f" {url} - {status_code} Server Error - ALERT : 5xx error encountered."
            print(message)
            logging.error(message)
            failure_count[url] += 1

        else:
            message = f"{url} - {status_code} Unexpected Status Code."
            print(message)
            logging.info(message)

    except requests.exceptions.RequestException as e:
        message = f" ERROR: Unable to reach {url} - {e}"
        print(message)
        logging.error(message)
        failure_count[url] += 1

def monitor_urls():
    while True:
        print("\n Checking URLs for uptime...\n")

        for url in urls:
            check_url_status(url)
            print("-" * 50)

            if failure_count[url] > 0:
                backoff_time = min(60, 2 ** failure_count[url])
                print(f"Exponential backoff: Waiting {backoff_time} seconds for {url}...\n")
                logging.info(f"Exponential backoff for {url}: {backoff_time} seconds")
                time.sleep(backoff_time)
            else:
                time.sleep(2)

        print("\n Waiting for the next round of checks...\n")
        time.sleep(10)

monitor_urls()
