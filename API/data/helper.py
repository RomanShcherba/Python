import requests
import json
import os


class ApiHelper:
    def __init__(self, api):
        self.api = api
        self.base_url = "https://pokeapi.co/api/v2/pokemon/"

    def set_url(self, endpoint):
        url = os.path.join(self.base_url, endpoint)
        return url
    
    def get_request(self, url):
        headers = {
            "Accept": "application/json",
        }
        response = requests.get(url, headers=headers)
        return response
    
    def post_request(self, url, data):
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
        }
        response = requests.post(url, headers=headers, data=json.dumps(data))
        return response

    
    def put_request(self, url, data):
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
        }
        response = requests.put(url, headers=headers, data=json.dumps(data))
        return response
    
    def patch_request(self, url, data):
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
        }
        response = requests.patch(url, headers=headers, data=json.dumps(data))
        return response
    
    def delete_request(self, url):
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
        }
        response = requests.delete(url, headers=headers)
        return response