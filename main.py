import datetime
import time
import yagmail
import pandas as pd
from news import NewsFeed


def send_email():
    """A function to send the email"""
    current_date = datetime.datetime.now().strftime('%Y-%m-%d')
    news_feed = NewsFeed(interest=row['interest'], from_date=current_date)
    email = yagmail.SMTP(user="pee49678@gmail.com", password="Fr0g13gs@/")
    try:
        email.send(to=row['email'],
                   subject=f"Your {row['interest']} news for today!",
                   contents=f"Hi {row['name']}, \n\n See what's on about {row['interest']} today. {news_feed.get()} \n Harry")
    except:
        print('Some error message')


while True:
    if datetime.datetime.now().hour == 17 and datetime.datetime.now().minute == 4:
        people = pd.read_excel('people.xlsx')

        for index, row in people.iterrows():
            send_email()
        print(f'Email sent at {datetime.datetime.now()}')
    time.sleep(60)
