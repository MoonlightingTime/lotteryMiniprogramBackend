from django.urls import path
from . import views

urlpatterns = [
    path("participate_in", views.participate_in),
    path("check_participated", views.check_participated),
    path("query_participated", views.query_participated)
]