from .models import Telegram
import requests


def Send_Message(name, phone):
    obj = Telegram.objects.get(pk=1)
    app = 'https://api.telegram.org/bot'
    token = obj.tele_token
    chat_id = obj.tele_chat_id
    text = f'{obj.tele_text} \n от: {name} \n Телефон: {phone}'
    url = ''.join([app, token, '/sendMessage'])
    print(url)
    req = requests.post(url, data={'chat_id': chat_id, 'text': text})
