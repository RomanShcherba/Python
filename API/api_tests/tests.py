import unittest
from data import list_of_pokemons
from data.helper import ApiHelper


class ApiTests(unittest.TestCase):

    def test_get_pokemon(self):
        api_helper = ApiHelper(self)
        url = api_helper.set_url("ditto")
        response = api_helper.get_request(url)
        self.assertEqual(response.status_code, 200, "Status code is not 200")
        pokemon_data = response.json()
        print(f"Name: {pokemon_data['name'].capitalize()}")
        print(f"ID: {pokemon_data['id']}")
        print(f"Height: {pokemon_data['height']}")
        print(f"Stats: {pokemon_data['stats']}")

    def test_get_unknown_pokemon(self):
        api_helper = ApiHelper(self)
        url = api_helper.set_url("unknown")
        response = api_helper.get_request(url)
        self.assertEqual(response.status_code, 404, "Status code is not 404")
        print(response.status_code)

    def test_create_new_pokemon(self):
        api_helper = ApiHelper(self)
        url = api_helper.set_url("dotto")
        data = {
            "name": "dotto",
            "id": 192,
            "forms": "dotto",
            "stats": {
                "hp": 80,
                "attack": 210,
                "defense": 20,
                "special-attack": 75,
                "special-defense": 45,
                "speed": 50
            },
            "height": 3.0,
            "weight": 45.0,
            "base_experience": 150,
            "abilities": ["sleep", "run", "fly"]
        }
        response = api_helper.post_request(url, data)
        self.assertEqual(response.status_code, 201, "Status code is not 201")
        print(response.status_code)

    def test_delete_pokemon(self):
        api_helper = ApiHelper(self)
        url = api_helper.set_url("132")
        response = api_helper.delete_request(url)
        self.assertEqual(response.status_code, 204, "Status code is not 204")
        print(response.status_code)

    def test_put_pokemon(self):
        api_helper = ApiHelper(self)
        url = api_helper.set_url("ditto")
        data = {
            "name": "ditto",
            "id": 132,
            "forms": "ditto",
            "stats": {
                "hp": 100,
                "attack": 200,
                "defense": 30,
                "special-attack": 80,
                "special-defense": 50,
                "speed": 60
            },
            "height": 4.0,
            "weight": 50.0,
            "base_experience": 200,
            "abilities": ["sleep", "run", "fly"]
        }
        response = api_helper.put_request(url, data)
        self.assertEqual(response.status_code, 200, "Status code is not 200")
        print(response.status_code)

    def test_patch_pokemon(self):
        api_helper = ApiHelper(self)
        url = api_helper.set_url("charmander")
        data = {
            "name": "charmander",
            "id": 132,
            "forms": "charmander",
            "stats": {
                "hp": 100,
                "attack": 200,
                "defense": 30,
                "special-attack": 80,
                "special-defense": 50,
                "speed": 60
            },
            "height": 4.0,
            "weight": 50.0,
            "base_experience": 200,
            "abilities": ["sleep", "run", "fly"]
        }
        response = api_helper.patch_request(url, data)
        self.assertEqual(response.status_code, 200, "Status code is not 200")
        print(response.status_code)