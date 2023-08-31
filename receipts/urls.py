from django.urls import path
from .views import account_list, category_list, create_account, create_category, create_receipt, list_receipt_view


urlpatterns = [
    path("", list_receipt_view, name="home"),
    path("create/", create_receipt, name="create_receipt"),
    path("categories/", category_list, name="category_list"),
    path("accounts/", account_list, name="account_list"),
    path("categories/create/", create_category, name="create_category"),
    path("accounts/create/", create_account, name="create_account"),
]
