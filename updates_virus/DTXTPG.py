import requests
import sys
# Replace 'YOUR_BOT_TOKEN' and 'YOUR_CHAT_ID' with your actual bot token and chat ID
bot_token = '6791408665:AAEDlPoAn_lwB3rMBNRjenRdEWIVgCSA7b4'
#message = 'Hello, this is a test message from Python.'
chat_id ='1653340086'





def send_text_file(bot_token, chat_id, file_path):
    url = f'https://api.telegram.org/bot{bot_token}/sendDocument'
    files = {'document': open(file_path, 'rb')}
    params = {'chat_id': chat_id}
    response = requests.post(url, files=files, params=params)
    print(response.json())

def send_image_file(bot_token, chat_id, file_path):
    url = f'https://api.telegram.org/bot{bot_token}/sendPhoto'
    files = {'photo': open(file_path, 'rb')}
    params = {'chat_id': chat_id}
    response = requests.post(url, files=files, params=params)
    print(response.json())

def main():
    if len(sys.argv) != 3:
        print("Usage: python script.py <text_file_path> <image_file_path>")
        sys.exit(1)

    text_file_path = sys.argv[1]
    image_file_path = sys.argv[2]

    send_text_file(bot_token, chat_id, text_file_path)
    send_image_file(bot_token, chat_id, image_file_path)

if __name__ == "__main__":
    main()
