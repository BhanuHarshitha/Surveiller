import time
from datetime import datetime
from json import dumps
#from celery import sharedTask
from httplib2 import Http
from .models import Dashboard
from urllib.request import urlopen
from urllib.error import URLError
from urllib.error import HTTPError
from http import HTTPStatus
from django.contrib.auth.models import User

def print_time():   
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    data = "Current Time = " + current_time
    return data


already_alert_sent_websites = []

def get_website_status(url):
    try:
        with urlopen(url) as connection:
            code = connection.getcode()
            #print(code)
            return code
    except HTTPError as e:
        return e.code
    except URLError as e:
        return e.reason
    except TimeoutError as e:
        return "Time out"

# result = get_website_status("https://www.amazon.ca/")

def sendAlert(user_id, website,url):
    print("called")
    code=get_website_status(website)
    message_headers = {'Content-Type': 'application/json; charset=UTF-8'}
    bot={'text':"The website {} is down and the status is {}.".format(website,code)}
    http_obj = Http()
    response = http_obj.request(uri=url,method='POST',headers=message_headers,body=dumps(bot),)
    user = User.objects.filter(id=user_id).first()
    print("user", user)
    if not Dashboard.objects.filter(url=website, user=user).exists():
        Dashboard.objects.create(user=user, url=website, status=code, status_send_to=user.username)
    else:
        dashboard = Dashboard.objects.filter(url=website, user=user).first()
        if dashboard:
            dashboard.status = code
            dashboard.save()
    print(website,code,print_time())


def check(user_id, li,url):
    user = User.objects.filter(id=user_id).first()
    print(li)
    for i in li:
        print("url",i, type(i))
        if 200 != get_website_status(i):
            print(i, "not 200")
            if i not in already_alert_sent_websites:
                sendAlert(user_id, i,url)
                already_alert_sent_websites.append(i)
            else:
                continue
        else:
            print('200')



def websiteChecking(user_id, final_urls,url, checking_time_in_seconds, alert_time_in_seconds):
    user = User.objects.filter(id=user_id).first()
    print("yes")
    start_time = time.time()
    while True:
        end_time = time.time()
        print(end_time- start_time)
        if abs(end_time-start_time) >= (float(alert_time_in_seconds)*60):
            global already_alert_sent_websites
            already_alert_sent_websites = []
            start_time = time.time()
        check(user.id,final_urls,url)
        time.sleep(float(checking_time_in_seconds)*60)
        

# def main():
#     file = "D:\webmonitoring\webs.txt"
#     url=input()
#     check_dur=int(input())
#     alert_dur=int(input())
#     websiteChecking(file,url,check_dur,alert_dur)
