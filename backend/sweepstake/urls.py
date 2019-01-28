from django.urls import path
from . import views

urlpatterns = [
    path('query_swpstk/', views.query_swpstk)
]