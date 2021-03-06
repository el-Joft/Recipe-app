import uuid

from django.contrib.auth.models import AbstractBaseUser
from django.db import models
from recipe_app.models.base import CommonFieldsMixin
from recipe_app.models.user_manager import UsersManager


class User(AbstractBaseUser, CommonFieldsMixin):
    """Users Model."""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(unique=True, null=False)
    username = models.CharField(unique=True, max_length=100,)
    first_name = models.CharField(max_length=30, null=True)
    last_name = models.CharField(max_length=30, null=True)
    password = models.CharField(max_length=128, blank=False)
    objects = UsersManager()
    
    USERNAME_FIELD = 'email'
    
    def __str__(self):
        return self.username

    
class Recipe(CommonFieldsMixin):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=200, null=False, blank=False)
    user =  models.OneToOneField(User, on_delete=models.CASCADE, null=True,)
        
    def __str__(self):
        return self.name


class Ingredient(CommonFieldsMixin):
    """ Ingredient Model """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    ingd_text = models.CharField(max_length=200,null=False, blank=False)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, null=True)
    
    def __str__(self):
        return self.ingd_text


class Step(CommonFieldsMixin):
    """ Recipe step Model """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    text_step = models.CharField(max_length=200,null=False, blank=False)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, null=True)
    
    def __str__(self):
        return self.text_step
