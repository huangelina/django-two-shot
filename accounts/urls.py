from django.urls import path
from . import views

app_NAME = 'accounts'

urlpatterns = [
    path("login/", views.login_view, name="login"),
]
