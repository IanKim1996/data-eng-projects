import os
import requests
import json
import pandas as pd
import numpy as np

# Set pandas options
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)

# RIOT API
# Required Headers for all API calls
REQUEST_HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9",
    "Accept-Charset": "application/x-www-form-urlencoded; charset=UTF-8",
    "Origin": "https://developer.riotgames.com",
    "X-Riot-Token": os.environ['RIOT_API_KEY']
    }


# Getting account info by summoner name
def get_account_info(s_name, headers=REQUEST_HEADERS):
    s_name_url = 'https://na1.api.riotgames.com/lol/summoner/v4/summoners/by-name/' + s_name.replace(' ', '%20')
    req = requests.get(s_name_url, headers=headers)
    if req.status_code == 200:
        account_info_dict = json.loads(req.content.decode('utf-8'))
    else:
        account_info_dict = None

    return account_info_dict

nose_toucher_info = get_account_info('Nose Toucher')
print(nose_toucher_info)







