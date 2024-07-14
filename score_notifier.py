import time
import requests
from bs4 import BeautifulSoup

# Telegram bot token and chat ID
#can be made using botfather in telegram
bot_token = '7017780310:AAHCASlt92bKMysJGGfozvybskT6mGX_jYU'
chat_id = '7195313832'

# Function to send a message to the Telegram bot
def send_telegram_message(message):
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    payload = {
        'chat_id': chat_id,
        'text': message
    }
    response = requests.post(url, data=payload)
    if response.status_code != 200:
        print("Failed to send message:", response.text)

#notification
def run(score):
    if score[0] == '6':
        return ("A six has been hit!\n" )
    elif score[0] == '4':
        return("A four has been hit!\n")
    elif score[0] == 'W':
        return("A wicket has fallen!\n" )
    else:
        print("Score updated\n")

#score parser
#can be changed
#option menu system
url = "https://www.espncricinfo.com/series/lanka-premier-league-2024-1421415/kandy-falcons-vs-dambulla-sixers-1st-match-1428459/live-cricket-score"
response = requests.get(url)
if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")
    recent_score_tag = soup.find("div", class_="ds-flex ds-flex-row ds-w-full ds-overflow-x-auto ds-scrollbar-hide ds-items-center ds-space-x-2")
    if recent_score_tag:
        prev_score = recent_score_tag.text.strip()
else:
    send_telegram_message("Failed to retrieve the webpage. Status code: " + str(response.status_code))
    prev_score = ""

while True:
    time.sleep(30)
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        recent_score_tag = soup.find("div", class_="ds-flex ds-flex-row ds-w-full ds-overflow-x-auto ds-scrollbar-hide ds-items-center ds-space-x-2")
        if recent_score_tag:
            recent_score = recent_score_tag.text.strip()
            if prev_score != recent_score:
                send_telegram_message(run(recent_score))
                prev_score = recent_score
            else:
                print("Score not updated :(")
        else:
            send_telegram_message("Recent scores not found.")
    else:
        send_telegram_message("Failed to retrieve the webpage. Status code: " + str(response.status_code))
