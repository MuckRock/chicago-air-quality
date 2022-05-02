import requests
import json
import pandas as pd
import sqlite3 as db
from config import *
from utils import sqlite_insert, daterange
from datetime import date, timedelta
import time

conn = db.connect('data/readings.db')
start_date = date(2021, 7, 28)
end_date = date(2022, 4, 10)
city = "chicago"

for single_date in daterange(start_date, end_date):
    print(single_date)
    startDateTime = single_date.strftime("%Y-%m-%d %H:%M:%S")

    endDateTime = (single_date + timedelta(1)).strftime("%Y-%m-%d %H:%M:%S")

    response = requests.get(UrlGetReadings +
                                f"?city={city}" +
                                f"&startDateTime={startDateTime}" +
                                f"&endDateTime={endDateTime}",
                            headers={'ApiKey':access_token})

    ReadingsByDateRange = response.json()
    ReadingsByDateRangeDf = pd.DataFrame(ReadingsByDateRange)

    if ReadingsByDateRangeDf.empty:
        time.sleep(3)
        continue

    ReadingsByDateRangeDf['readingDateTimeUTC'] = pd.to_datetime(ReadingsByDateRangeDf.readingDateTimeUTC)
    ReadingsByDateRangeDf['readingDateTimeLocal'] = pd.to_datetime(ReadingsByDateRangeDf.readingDateTimeLocal)

    print(ReadingsByDateRangeDf)

    ReadingsByDateRangeDf.to_sql(name='Readings', con=conn, if_exists='append')
    time.sleep(3)