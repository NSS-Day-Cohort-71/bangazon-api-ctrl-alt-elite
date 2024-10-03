import datetime
import json
from rest_framework import status
from rest_framework.test import APITestCase


class PaymentTests(APITestCase):
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

    def test_create_payment_type(self):
        """
        Ensure we can add a payment type for a customer.
        """
        # Add product to order
        url = "/payment-types"
        data = {
            "merchant": "American Express",
            "acctNumber": "111-1111-1111",
            "expirationDate": "2024-12-31",
            # "create_date": datetime.date.today(),
        }
        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.token)
        response = self.client.post(url, data, format="json")
        json_response = json.loads(response.content)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(json_response["merchant_name"], "American Express")
        self.assertEqual(json_response["account_number"], "111-1111-1111")
        self.assertEqual(json_response["expiration_date"], "2024-12-31")
        # self.assertEqual(json_response["create_date"], str(datetime.date.today()))

    # TODO: Delete payment type

    def test_delete_payment_type(self):

        #Create
        url = "/payment-types"
        data = {
        "merchant": "Visa",
        "acctNumber": 1234567890,
        "expirationDate": "2027-02-01",
        }
        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.token)
        response = self.client.post(url, data, format="json")
        json_response = json.loads(response.content)
        payment_id = json_response["id"]

        #Verify create
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        #Delete
        url = f"/payment-types/{payment_id}"
        response = self.client.delete(url)
    

        #Verify delete
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        #Retrieve delete
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_500_INTERNAL_SERVER_ERROR)