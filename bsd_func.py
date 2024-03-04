import requests
import urllib.request
import json
import csv
import pandas as pd
from datetime import datetime
import time
import concurrent.futures

#### LOg in function. Pass env, email and password and as a result you've got header
def login(email, password, env):
    #loing to bsd
    loginpage = env+"login"
    credentials={
    "email": [str(email)],
    "password": [str(password)]
    }
    login = requests.request("POST", url=loginpage, headers={}, data=credentials, files=[])
    if login.status_code == 200:
        token="session="+login.cookies["session"]
        #headers={"Cookie": token}
        #print(login.cookies['session'])
        #print(headers)
        #logging.info(f"BSD login ok")
        headers = {"Connection": "keep-alive", "Content-Type":"application/json","Cookie": token}
        return (headers)
    else:
        return(False)
    
