from django.urls import path
from . import views

urlpatterns = [
  path('',views.Index,name='index'),
  path('home/<int:id>/',views.Home,name='home'),
  path('register/',views.UserView.as_view(), name='register'),
  path('login/',views.login,name = 'login'),
  
  path('alert/create/',views.createAlert,name='create'),

  path('get/coins/',views.getCrypto,name='coins')
]