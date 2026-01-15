from django.urls import path

from . import views

app_name = "problems"
urlpatterns = [
    path("",views.index,name = "index"),
    path("ajax/load-makes/", views.load_makes, name = 'ajax_load_makes'),
]