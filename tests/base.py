from django.test import Client, TestCase
from recipe_app.models.app import User


class BaseTestCase(TestCase):
    """
    Base configuration file for all tests.
    """

    @classmethod
    def setUpClass(cls):

        super(BaseTestCase, cls).setUpClass()

        cls.client = Client()

    def setUp(self):
        """
        Configurations to be made available before each
        individual test case inheriting from this class.
        """
        self.user_data = {
            "first_name": "Firstname",
            "password": "123456ABC",
            "last_name": "lastname",
            "username": "test1",
            "email": "test1@gmail.com",
        }
        self.user_data_2 = {
            "first_name": "Firstname",
            "password": "123456ABC",
            "last_name": "lastname",
            "username": "test2",
            "email": "test2@gmail.com"
        }

        self.new_user = User(**self.user_data)

        self.new_user_2 = User(**self.user_data_2)

        self.new_user.save()

