import requests

def send_discord_webhook(url, message, username=None, avatar_url=None):
    data = {"content": message}
    if username:
        data["username"] = username
    if avatar_url:
        data["avatar_url"] = avatar_url
    response = requests.post(url, json=data)
    if response.status_code == 204:
        print(f"Webhook sent successfully to {url}!")
    else:
        print(f"Webhook failed to send to {url}:", response.text) # >>> DONT WORRY ABOUT ANYTHING ABOVE.

webhook_urls = [
    "https://discord.com/THIS-IS-YOUR-FUCKING-WEBHOOK.", #<<< THIS IS WHERE YOUR WEBHOOK LINK GOES.
]

message_to_send = "RATE LIMITED BY floppydsk3 | https://github.com/floppydsk3/rate-limiter-V1" #<<< CHANGE THIS TO THE MESSAGE (be nice and at the github repo to the end of the script.) https://github.com/floppydsk3/rate-limiter-V1
username = "RATE LIMITER V1" # <<< THE NAME OF THE WEBHOOK SENT (this isnt the same as the name of the webhook created, the script changes it to what you please.)
avatar_url = "https://example.com/avatar.png"
number_of_sends = change-me-to-number # <<< HOW MANY TIMES WILL THE WEBHOOK BE SENT. (RATE LIMITS WILL OCCUR QUICKLY, JUST SAYIN.)

for webhook_url in webhook_urls: # >>> DONT WORRY ABOUT ANYTHING BELOW.
    for _ in range(number_of_sends):
        send_discord_webhook(webhook_url, message_to_send, username, avatar_url)