import requests
import json

URL = "http://127.0.0.1:8000/studentapi/"

def get_data(id=None):
    data = {}
    if id is not None:
        data = {'id': id}
    json_data = json.dumps(data)
    r = requests.get(url=URL, data=json_data,headers={'content-Type': 'application/json'})
    data = r.json()
    print(data)
# get_data(1)


def post_data():
    data = {
        'name': 'Ravi',
        'roll': 105,
        'city': 'Ranchi'
    }
    json_data = json.dumps(data)
    try:
        r = requests.post(url=URL, data=json_data, headers={'Content-Type': 'application/json'})
        r.raise_for_status()  # Raise an exception for HTTP errors

        response_data = r.json()
        print(response_data)
    except requests.exceptions.RequestException as e:
        print("Error sending data:", e)

def update_data():
    data = {
        'id': 2,
        'name': 'Ravi',
        'city': 'Ranchi'
    }
    json_data = json.dumps(data)
    try:
        r = requests.put(url=URL, data=json_data, headers={'Content-Type': 'application/json'})
        r.raise_for_status()

        response_data = r.json()
        print(response_data)
    except requests.exceptions.RequestException as e:
        print("Error sending data:", e)
# update_data()

def delete_data():
    data = {'id': 2}
    json_data = json.dumps(data)
    try:
        r = requests.delete(url=URL, data=json_data, headers={'Content-Type': 'application/json'})
        r.raise_for_status()

        response_data = r.json()
        print(response_data)
    except requests.exceptions.RequestException as e:
        print("Error sending data:", e)
# delete_data()

def patch_data():
    data = {
        'id': 3,
        'name': 'Ravi',
        'city': 'Ranchi'
    }
    json_data = json.dumps(data)
    try:
        r = requests.patch(url=URL, data=json_data, headers={'Content-Type': 'application/json'})
        r.raise_for_status()

        response_data = r.json()
        print(response_data)
    except requests.exceptions.RequestException as e:
        print("Error sending data:", e)
patch_data()
