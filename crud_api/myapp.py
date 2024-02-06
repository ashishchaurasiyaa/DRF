import requests
import json


class StudentAPIClient:
    def __init__(self, base_url):
        self.base_url = base_url

    def get_data(self, id=None):
        endpoint = self.base_url
        if id is not None:
            endpoint += f"?id={id}"
        try:
            r = requests.get(url=endpoint)
            r.raise_for_status()
            return self._handle_response(r)
        except requests.exceptions.RequestException as e:
            print("Request failed:", e)

    def post_data(self, data):
        json_data = json.dumps(data)
        try:
            r = requests.post(url=self.base_url, data=json_data)
            r.raise_for_status()
            return self._handle_response(r)
        except requests.exceptions.RequestException as e:
            print("Request failed:", e)
            return None  # Return None when the request fails

    def update_data(self, data):
        json_data = json.dumps(data)
        try:
            r = requests.put(url=self.base_url, data=json_data)
            r.raise_for_status()
            return self._handle_response(r)
        except requests.exceptions.RequestException as e:
            print("Request failed:", e)

    def delete_data(self, id):
        data = {'id': id}
        json_data = json.dumps(data)
        try:
            r = requests.delete(url=self.base_url, data=json_data)
            r.raise_for_status()
            return self._handle_response(r)
        except requests.exceptions.RequestException as e:
            print("Request failed:", e)

    def _handle_response(self, response):
        if response.status_code in (200, 201):  # Updated to handle status code 201 as well
            print("Request successful. Status code:", response.status_code)
            return response.json(), response.headers.get('Content-Type')
        else:
            print("Request failed. Status code:", response.status_code)
            print("Response content:", response.content.decode('utf-8'))


def handle_response(response_content, content_type):
    if content_type == 'application/json':
        print("Response Content (JSON):")
        print(json.dumps(response_content, indent=4))
    else:
        print("Response Content:", response_content)


if __name__ == "__main__":
    URL = "http://localhost:8000/studentapi/"
    client = StudentAPIClient(URL)

    # # Get data
    # response_content, content_type = client.get_data()
    # handle_response(response_content, content_type)
    #
    # # Get data with id=1
    # response_content, content_type = client.get_data(1)
    # handle_response(response_content, content_type)
    #
    # # Delete data with id=5
    # response_content, content_type = client.delete_data(5)
    # handle_response(response_content, content_type)

    # Post new data
    response_content, content_type = client.post_data({'name': 'Abhishek', 'roll': 150, 'city': 'New Delhi'})
    handle_response(response_content, content_type)

    # # Update data with id=1
    # response_content, content_type = client.update_data({'id': 1, 'name': 'John', 'city': 'New York'})
    # handle_response(response_content, content_type)
