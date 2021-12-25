LOCALHOST = "http://192.168.0.29:80"
SUCCESS_CODE = 200
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


def set_group_state(key, active):
    groups = get_groups(key)
    for group in groups:
        print(group)
        r = requests.put(LOCALHOST + "/api/" + key + "/groups/" + group + "/action", json={"on": active})
        if r.status_code != SUCCESS_CODE:
            print(r.status_code, r.text)
        
        

def main():
    api_key = get_api_key()
    if api_key is None:
        print("Unable to get API key")
    print(api_key, "????")
    key = api_key[0]["success"]["username"]
    set_group_state(key, True)
    state = False
    while True:
        input("press a button")
        state = not state
        set_group_state(key, state)
        

main()