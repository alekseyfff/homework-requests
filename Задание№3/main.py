import time
import requests
from datetime import datetime
from datetime import timedelta
from pprint import pprint

final_day = int(time.mktime(datetime.now().timetuple()))
start_day = datetime.now() - timedelta(days=2)
start_day = int(time.mktime(start_day.timetuple()))

URL = "https://api.stackexchange.com/2.3/questions"
PARAMS = {
    "tagged": "python",
    "fromdate": start_day,
    "todate": final_day,
    "order": "desc",
    "site": "stackoverflow"
}

responce = requests.get(URL, params=PARAMS)

json_answer = responce.json()

questions = []

for i in json_answer['items']:
    questions.append(i['title'])
pprint(questions)