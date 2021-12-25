LOCALHOST = "localhost:8080"
import requests

def get_api_key(): 
    request_path = LOCALHOST + "/api"
    r = requests.get(request_path)
    if r.status_code == 200:
        return r.text
    else:
        return None

def get_groups():
    pass

def set_group_state():
    pass

def main():
    api_key = get_api_key()
    if api_key is None:
        print("Unable to get API key")
    print(api_key)