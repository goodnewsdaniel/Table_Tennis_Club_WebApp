from django.urls import path
from . import views

urlpatterns = [
    path("", views.blog, name='blog'),
    path('blog/details/<slug:slug>', views.details, name='details'),

]
