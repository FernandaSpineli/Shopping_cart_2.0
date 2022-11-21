import json

from rest_framework.test import APITestCase

from users.models import User
# Create your tests here.

class TestUsersList(APITestCase):
    def test_user_created(self):
        user_request_data = {
            "name": "Carolina Santos",
            "CPF": "12456789121",
            "birth_date": "2001-3-01",
            "email": "carolina32@gmail.com",
            "password": "Aa@123548",
            "phone_number": "37045674"
        }
        
        response = self.client.post('/api/usuarios/', user_request_data, format='json')
        
        self.assertEqual(response.status_code, 201)
        
class TestUserDetail(APITestCase):
    def test_get_user_by_id(self):
        ...
    def test_update_user(self):
        ...   
    def test_delete_user(self):
        ...
    