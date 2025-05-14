import unittest
from data.helper import ApiHelper

class Tests(unittest.TestCase):

    def test_get_pokemon(self):
        api_helper = ApiHelper(self)
        url = api_helper.set_url("ditto")
        response = api_helper.get_request(url)
        self.assertEqual(response.status_code, 200, "Status code is not 200")
        