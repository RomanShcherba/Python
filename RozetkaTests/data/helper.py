import json
import requests

class ApiHelper:
    def __init__(self, test_instance):
        self.test_instance = test_instance

    def set_url(self, pokemon_name):
        return f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}"

    def get_request(self, url):
        return requests.get(url)
        
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
        }
        response = requests.delete(url, headers=headers)
        return response
    
