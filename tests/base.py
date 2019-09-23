from django.test import Client, TestCase
from recipe_app.models.app import User, Ingredient, Recipe, Step


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
        self.recipe_data = {
            "name": "Recipe test"
        }
        
        self.ingred_data = {
            "ingd_text": "Assorted beef"
        }
        
        self.step_data = {
            "text_step": "Step 1"
        }
        
        self.recipe_data2 = {
            "name": "Recipe test1"
        }
        
        self.recipe = Recipe(**self.recipe_data)
        
        self.recipe2 = Recipe(**self.recipe_data2)
        self.recipe2.save()

        self.new_user = User(**self.user_data)

        self.new_user_2 = User(**self.user_data_2)

        self.new_user.save()
        self.ingredient = self.create_ingredient()
        self.step = self.create_step()

    def create_ingredient(self):
        """Create an ingredient """
        return Ingredient.objects.create(ingd_text='ingredient')

    def create_step(self):
        """Create an Step """
        return Step.objects.create(text_step='step')
