import requests

def notify_slack(message: str):
    webhook_url = "https://hooks.slack.com/services/XXX/YYY/ZZZ"
    requests.post(webhook_url, json={"text": message})
