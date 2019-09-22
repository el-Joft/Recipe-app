from django.conf.urls import include
from rest_framework.routers import DefaultRouter
from recipe_app.views.user import UserViewSet
from django.urls import path


app_name = 'recipe_app'
urlpatterns = [
    path('create_user/',
         UserViewSet.as_view({'post': 'create'}), name='create_user'),
]
