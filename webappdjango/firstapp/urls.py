from django.urls import path
from . import views

urlpatterns = [
    path("function", views.function, name='function'),
    path("<str:name>", views.greet, name="greet"),
    path("index", views.index, name="index")
]
