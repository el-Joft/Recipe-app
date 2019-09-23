from tests.base import BaseTestCase


class RecipeTest(BaseTestCase):

    def test_creating_ingredient(self):
        """Test post ingredient in the database."""
        response = self.client.post(
            '/api/v1/ingredients/', self.ingred_data)
        data = response.data
        self.assertEqual(response.status_code, 201)
        self.assertEqual(data['ingd_text'], self.ingred_data['ingd_text'])
        
    def test_error_creating_ingredient(self):
        """Test post ingredient in the database."""
        response = self.client.post(
            '/api/v1/ingredients/')
        data = response.data
        self.assertEqual(response.status_code, 400)
        self.assertIn(
            'This field is required.', data['ingd_text'])

    def test_creating_step(self):
        """Test post step in the database."""
        response = self.client.post(
            '/api/v1/steps/', self.step_data)
        data = response.data
        self.assertEqual(response.status_code, 201)
        self.assertEqual(data['text_step'], self.step_data['text_step'])

    def test_error_creating_step(self):
        """Test error creating step."""
        response = self.client.post(
            '/api/v1/steps/')
        data = response.data
        self.assertEqual(response.status_code, 400)
        self.assertIn(
            'This field is required.', data['text_step'])
        
    def test_creating_recipe(self):
        """Test post recipe in the database."""
        self.recipe_data['user'] = self.new_user.id
        self.recipe_data['ingredient'] = [self.ingredient.id]
        self.recipe_data['step'] = [self.step.id]
        response = self.client.post(
            '/api/v1/recipe/', self.recipe_data)
        data = response.data
        self.assertEqual(response.status_code, 201)
        self.assertEqual(data['data']['name'], self.recipe_data['name'])

    def test_all_recipe(self):
        """Test get recipe in the database."""
        response = self.client.get('/api/v1/recipe/')
        data = response.data
        self.assertEqual(response.status_code, 200)

    def test_single_recipe(self):
        self.recipe.save()
        """Test get single recipe in the database."""
        response = self.client.get(
            f'/api/v1/recipe/{self.recipe.pk}/')
        data = response.data
        self.assertEqual(response.status_code, 200)

    def test_user_recipe(self):
        self.recipe.user = self.new_user
        self.recipe.save()
        """Test get single recipe in the database."""
        response = self.client.get(
            f'/api/v1/recipe/user/{self.new_user.pk}/')
        data = response.data
        self.assertEqual(response.status_code, 200)


    def test_delete_recipe(self):
        """Test delete single recipe in the database."""
        response = self.client.delete(
            f'/api/v1/recipe/{self.recipe2.pk}/')
        data = response.data
        self.assertEqual(response.status_code, 200)
