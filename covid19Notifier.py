from bs4 import BeautifulSoup 
import urllib.request
import pandas as pd
from apscheduler.schedulers.blocking import BlockingScheduler
import requests
#import dbus
import notify2


def fetch_data():
	pos_cases = []
	cases = requests.get('https://api.covid19india.org/data.json')
	cases_json = cases.json()
	tested_cases = cases_json["tested"]
	for i in tested_cases:
		tested_pos = i['totalpositivecases']
		pos_cases.append(tested_pos)

	current_cases = int(pos_cases[-1])
	return current_cases
	

data_item = fetch_data()

#initialising the dbus connection
notify2.init('Covid19 Notifier')

#create notification object
n = notify2.Notification(None)

#set urgency level
n.set_urgency(notify2.URGENCY_NORMAL)

#timeout notification
n.set_timeout(20000)



