LOCALHOST = "http://192.168.0.29:80"
SUCCESS_CODE = 200
API_KEY = "123DD1E39A"
import requests
import json

def get_api_key(): 
    request_path = LOCALHOST + "/api"
    r = requests.post(request_path, json={"devicetype": "my application"})
    if r.status_code == SUCCESS_CODE:
        decoded_response = json.loads(r.text);
        return decoded_response
    else:
        print(r.status_code, r.text)
        return None

def get_groups(key):
    r = requests.get(LOCALHOST + "/api" + "/" + key + "/groups")
    if r.status_code == SUCCESS_CODE:
        decoded_response = json.loads(r.text);
        return decoded_response


def set_group_state(key, group, active):
    r = requests.put(LOCALHOST + "/api/" + key + "/groups/" + group + "/action", json={"on": active})
    if r.status_code != SUCCESS_CODE:
        print(r.status_code, r.text)
        
        
def main():
    api_key = API_KEY
    key = api_key[0]["success"]["username"]
    state = False
    while True:
        available_groups = get_groups(key)
        print("Available groups:")
        for group in available_groups:
            print("Group ID: ", group, "| Group name: ", available_groups[group]["name"])
        group_id = input("press a button")
        state = not state
        set_group_state(key, group_id, state)
        

main()