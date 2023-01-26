import requests
import time

def status(s):
    stat=requests.get(s)
    res=stat.status_code
    return res

# Your Google Chat webhook URL
webhook_url = input()

# The file containing the list of websites you want to monitor
website_list_file = 'websites.txt'

# Set a variable to track the last time an alert was sent
last_alert_time = 0

while True:
    current_time = time.time()
    try:
        # Read the list of websites from the file
        with open(website_list_file) as f:
            websites = f.read().splitlines()

        # Iterate through the list of websites
        for website_url in websites:
            # Send a GET request to the website and check the status code
            response = requests.get(website_url)
            if response.status_code != 200:
                # The website is down
                # Check if it's been at least 15 minutes since the last alert
                if current_time - last_alert_time > 900:
                    # Send an alert to Google Chat
                    message = {'text': f'{website_url} is down! Status code: {response.status_code}'}
                    requests.post(webhook_url, json=message)
                    last_alert_time = current_time
    except requests.exceptions.RequestException as e:
        # Send an alert to Google Chat
        message = {'text': f'Error: {e}'}
        requests.post(webhook_url, json=message)
    except Exception as e:
        # Send an alert to Google Chat
        message = {'text': f'Error: {e}'}
        requests.post(webhook_url, json=message)

    # Wait for 1 minute before checking the websites again
    time.sleep(60)