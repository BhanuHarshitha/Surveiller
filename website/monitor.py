import time
from datetime import datetime
from json import dumps

from httplib2 import Http

from urllib.request import urlopen
from urllib.error import URLError
from urllib.error import HTTPError
from http import HTTPStatus

def print_time():   
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    data = "Current Time = " + current_time
    return data


already_alert_sent_websites = []

def get_website_status(url):
    try:
        with urlopen(url,timeout=3) as connection:
            code = connection.getcode()
            return code
    except HTTPError as e:
        return e.code
    except URLError as e:
        return e.reason


def sendAlert(website,url):
    code=get_website_status(website)
    message_headers = {'Content-Type': 'application/json; charset=UTF-8'}
    bot={'text':"The website {} is down and the status is {}.".format(website,code)}
    http_obj = Http()
    response = http_obj.request(uri=url,method='POST',headers=message_headers,body=dumps(bot),)
    print(website,code,print_time())


def check(li,url):
    flag = True
    while flag:
        for i in li:
            if 200 != get_website_status(i):
                if i not in already_alert_sent_websites:
                    sendAlert(i,url)
                    already_alert_sent_websites.append(i)
                else:
                    continue
        flag = False

def websiteChecking(file,url, checking_time_in_seconds, alert_time_in_seconds):
    l=[]
    file_op=open(file,'r')
    for i in file_op:
        l.append(i)
    # l = ["youtube", "google"]
    start_time = time.time()
    while True:
        end_time = time.time()
        print(end_time- start_time)
        if abs(end_time-start_time) >= (alert_time_in_seconds*60):
            global already_alert_sent_websites
            already_alert_sent_websites = []
            start_time = time.time()
        check(l,url)
        time.sleep(checking_time_in_seconds*60)
        

def main():
    file = "D:\webmonitoring\webs.txt"
    url=input()
    check_dur=int(input())
    alert_dur=int(input())
    websiteChecking(file,url,check_dur,alert_dur)
main()