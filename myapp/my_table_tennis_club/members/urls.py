from django.urls import path
from . import views


# This is where you create all paths for all view functions
urlpatterns = [
    path('', views.main, name='main'),
    path('members/', views.member, name='members'),
    path('members/details/<int:id>', views.details, name='details'),
]
