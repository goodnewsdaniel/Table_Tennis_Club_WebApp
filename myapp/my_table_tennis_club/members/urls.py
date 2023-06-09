from django.urls import path
from . import views


# This is where you create all paths for all view functions
urlpatterns = [
    path('members/', views.members, name='members'),
]
 