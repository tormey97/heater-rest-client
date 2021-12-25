LOCALHOST = "http://192.168.0.29:80"
import requests

def get_api_key(): 
    request_path = LOCALHOST + "/api"
    r = requests.post(request_path, {"devicetype": "my application"})
    if r.status_code == 200:
        return r.text
    else:
        print(r.status_code, r.text)
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

main()