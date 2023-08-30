from django.urls import path
from .views import list_receipt_view

urlpatterns = [
    path("", list_receipt_view, name="home")
]
