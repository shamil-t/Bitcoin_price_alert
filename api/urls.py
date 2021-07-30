from django.urls import path
from . import views

urlpatterns = [
  path('',views.Home,name='home'),
  path('alert/create',views.CreateApi.as_view())
]