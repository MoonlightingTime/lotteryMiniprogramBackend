from django.urls import path
from . import views

urlpatterns = [
    path('query_rules', views.query_rules),
]