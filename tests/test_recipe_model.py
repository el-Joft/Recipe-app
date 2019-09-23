from recipe_app.models.app import Recipe, Ingredient, Step
from tests.base import BaseTestCase


class RecipeTestCase(BaseTestCase):
    """ Recipe model test case"""
    
    def test_models_can_create_recipe(self):
        """Test creation of recipe """
        old_count = Recipe.objects.count()
        self.recipe.save()
        new_count = Recipe.objects.count()
        self.assertEqual(new_count, old_count + 1)
        
    def test_models_return_string_representation(self):
        """ Test recipe string representation """
        recipe = self.recipe
        self.assertEqual(str(recipe), self.recipe_data['name'])

    def test_ingredient_model(self):
        """Test Ingredient model """
        old_count = Ingredient.objects.count()
        ing = Ingredient.objects.create(ingd_text='ingredients')
        new_count = Ingredient.objects.count()
        self.assertEqual(new_count, old_count + 1)
        self.assertEqual(str(ing), 'ingredients')


    def test_step_model(self):
        """Test step model """
        old_count = Step.objects.count()
        step = Step.objects.create(text_step='step1')
        new_count = Step.objects.count()
        self.assertEqual(new_count, old_count + 1)
        self.assertEqual(str(step), 'step1')
