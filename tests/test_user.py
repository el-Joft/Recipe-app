from tests.base import BaseTestCase


class UserAccount(BaseTestCase):

    def test_creating_user(self):
        """Test post user in the database."""
        self.user_data['email'] = 'newemail@gmail.com'
        self.user_data['username'] = 'user001'
        response = self.client.post(
            '/api/v1/create_user/', self.user_data)
        data = response.data["data"]
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data['status'], 'success')
        self.assertEqual(data['email'], 'newemail@gmail.com')

    def test_existing_user(self):
        """ Test if user details exist in the database"""
        self.user_data['email'] = 'newemail@gmail.com'
        response = self.client.post(
            '/api/v1/create_user/', self.user_data)
        data = response.data
        self.assertEqual(response.status_code, 400)
        self.assertEqual(data['status'], 'error')
        self.assertIn(
            'user with this username already exists.', data['data']['username'])

    def test_invalid_password(self):
        """ Test if user details exist in the database"""
        self.user_data['username'] = 'password'
        self.user_data['email'] = 'passwordemail@gmail.com'
        self.user_data['password'] = '1234'
        response = self.client.post(
            '/api/v1/create_user/', self.user_data)
        data = response.data
        self.assertEqual(response.status_code, 400)
        self.assertEqual(data['status'], 'error')
        self.assertIn(
            'Password must contain a Number, a letter and 8 charcters long',
            data['data']['non_field_errors'])
