from django.urls import path

from . import views

app_name = "mpg"
urlpatterns = [
    path("",views.index,name = "index"),
    path("ajax/load-models/", views.load_models, name = 'ajax_load_models'),
]