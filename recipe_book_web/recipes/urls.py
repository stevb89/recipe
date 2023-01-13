from django.urls import path
from recipes import views


urlpatterns=[
    path("hello/<name>", views.hello, name="hello"),
    path("", views.home, name="home")
]