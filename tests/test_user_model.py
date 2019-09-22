from recipe_app.models.app import User
from tests.base import BaseTestCase


class UserTestCase(BaseTestCase):
    """User Model test case."""

    def test_models_can_create_user(self):
        """Test creation of activity."""
        old_count = User.objects.count()
        self.new_user_2.save()
        new_count = User.objects.count()
        self.assertEqual(new_count, old_count + 1)

    def test_models_return_user_string_representation(self):
        """ Test activity string representation """
        user = self.new_user
        self.assertEqual(str(user), self.user_data['username'])

