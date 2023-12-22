import requests
import time

def send_discord_webhook(url, message, username=None, avatar_url=None):
    data = {"content": message}
    if username:
        data["username"] = username
    if avatar_url:
        data["avatar_url"] = avatar_url

    while True:
        response = requests.post(url, json=data)
        if response.status_code == 204:
            print(f"Webhook sent successfully to {url}!")
            break
        elif response.status_code == 429:
            print(f"Rate limit exceeded for {url}. Waiting for 30 seconds...") # <<< IF YOU WANT TO YOU CAN CHANGE THE TEXT WHEN OUTPUTTED IN THE TERMINAL (outside of discord.)
            time.sleep(30)  # << THIS CAN BE CHANGED >> [DON'T WORRY ABOUT ANYTHING ABOVE.]
        else:
            print(f"Webhook failed to send to {url}:", response.text)
            break  # Exit the loop for other errors
        
webhook_urls = [
    "https://discord.com/api/webhooks/1185304225194979460/d_t328Y2T3GuvCI-Ml9_L0V735if5AKdf7PpVJfEtUBnNZO9yMlVCqRvIOu6Rw9bzkRQ", #<<< THIS IS WHERE YOUR WEBHOOK LINK GOES.
]

message_to_send = "@everyone Testing Concluded." #<<< CHANGE THIS TO THE MESSAGE (be nice and at the github repo to the end of the script.) https://github.com/floppydsk3/rate-limiter-V1
username = "RATE LIMITER V1.1" # <<< THE NAME OF THE WEBHOOK SENT (this isnt the same as the name of the webhook created, the script changes it to what you please.)
avatar_url = "https://example.com/avatar.png" # <<< Webhook Icon.
number_of_sends = 5 # <<< HOW MANY TIMES WILL THE WEBHOOK BE SENT. (RATE LIMITS WILL OCCUR QUICKLY, JUST SAYIN.)

for webhook_url in webhook_urls: # >>> DONT WORRY ABOUT ANYTHING BELOW.
    for _ in range(number_of_sends):
        send_discord_webhook(webhook_url, message_to_send, username, avatar_url)
