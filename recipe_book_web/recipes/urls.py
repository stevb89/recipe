from django.urls import path
from recipes import views
from recipes.models import Recipe


home_list_view = views.HomeListView.as_view(
    queryset = Recipe.objects.all()[:5], # :5 limits the results to the five most recent
    context_object_name="recipe_list",
    template_name="recipes/home.html",
)

urlpatterns=[
    path("hello/<name>", views.hello, name="hello"),
    path("", home_list_view, name="home"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
    path("enter_ingredient/", views.enter_ingredient, name="enter_ingredient")
]