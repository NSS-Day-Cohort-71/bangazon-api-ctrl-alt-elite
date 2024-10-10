import json
from rest_framework import status
from rest_framework.test import APITestCase



class StoreTests(APITestCase):
    def setUp(self) -> None:
        """
        Create a new account and create sample category
        """
        url = "/register"
        data = {
            "username": "steve",
            "password": "Admin8*",
            "email": "steve@stevebrownlee.com",
            "address": "100 Infinity Way",
            "phone_number": "555-1212",
            "first_name": "Steve",
            "last_name": "Brownlee",
        }
        response = self.client.post(url, data, format="json")
        json_response = json.loads(response.content)
        self.token = json_response["token"]
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_a_store(self):
        """
        Create a store by sending POST to /stores
        """
        url = "/stores"
        data = {"name": "Test Store", "description": "Description of Test Store"}
        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.token)
        response = self.client.post(url, data, format="json")
        json_response = json.loads(response.content)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(json_response["name"], "Test Store")
        self.assertEqual(json_response["description"], "Description of Test Store")

    def test_favorite_a_store(self):
        """
        Favorite a store by sending a POST to /profile/favoritesellers
        """

        url = "/stores"
        data = {"name": "Test Store", "description": "Description of Test Store"}
        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.token)
        response = self.client.post(url, data, format="json")
        json_response = json.loads(response.content)
        store_id = json_response["id"]
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        url = "/profile/favoritesellers"
        data = {"store_id": store_id}
        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.token)
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
