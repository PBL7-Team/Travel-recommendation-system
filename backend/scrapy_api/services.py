import requests

def start_crawl(sender, message, url):
    payload = {
        'sender': sender,
        'message': message
    }
    
    response = requests.post(url, json=payload)
    
    # Check for a successful request
    if response.status_code == 200:
        return response.json()
    else:
        response.raise_for_status()