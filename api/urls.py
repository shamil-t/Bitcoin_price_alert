from django.urls import path
from . import views

urlpatterns = [
  path('',views.Index,name='index'),
  path('home/<int:id>/',views.Home,name='home'),
  path('register/',views.UserView.as_view(), name='register'),
  path('login/',views.login,name = 'login'),
  path('home/<int:id>/create', views.CreateAlert, name='create'),
  path('home/<int:id>/alerts',views.GetAlerts,name='getalerts'),

  path('alert/create/',views.createAlert,name='create'),
  path('alert/all/<int:id>/',views.getAlert,name='alerts'),
  path('alert/delete/<int:id>',views.delAlert,name='del'),
  path('get/coins/',views.getCrypto,name='coins'),
]