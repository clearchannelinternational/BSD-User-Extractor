import app_config
from bsd_func import login
import pandas as pd
import requests


env = app_config.ENV
user_endpoint = f"{env}api/v1/user/filter?active=true"


DOMAINS = app_config.DOMAINS


for index in range(0, len(DOMAINS)):
    try:
        email = DOMAINS[index][0]
        password = DOMAINS[index][1]
        file_name = DOMAINS[index][2]
    except IndexError:
        print(f"Missing item for domain nr {index+1}")
    else:
        
        headers = login(email, password, env)
        if headers != False:

            users = requests.request("GET", url=user_endpoint, headers=headers)
            if users.status_code == 200:
        
                data = pd.DataFrame.from_dict(users.json())

                data.to_csv(file_name, index=False)
                print(f"File for {email} has been created.")
            else:
                print(f"Cound't recive the list of user5s for domain {email}. Error code {users.status_code}")
            
        else:
            print(f"Login failed for user {email}")

print("Script finished")


