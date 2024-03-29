from base64 import b64encode
import requests


def get_doppler_env(token):
    token_b64 = b64encode(f"{token}:".encode()).decode()

    url = "https://api.doppler.com/v3/configs/config/secrets/download"

    querystring = {"format": "env"}

    headers = {
        "Accept": "application/json",
        "Authorization": f"Basic {token_b64}"
    }
    try:
        response = requests.request(
            "GET", url, headers=headers, params=querystring)
        if response.status_code == 200:
            return response.text
    except Exception:
        pass
    return ""


def update_doppler_evn(token, secrets):
    url = "https://api.doppler.com/v3/configs/config/secrets"

    payload = {
        "project": "foodsupbot",
        "config": "stg",
        "secrets": secrets
    }
    headers = {
        "accept": "application/json",
        "content-type": "application/json",
        "authorization": f"Bearer {token}"
    }

    response = requests.post(url, json=payload, headers=headers)
    return response
