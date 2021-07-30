from api.serializers import CreateSerializers
from django.http.response import HttpResponse
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

from django.conf import settings
from django.core.mail import send_mail
from .models import CreateApiModel

# Create your views here.

def Home(request):
  return HttpResponse('Home page ')

def sendEmail():
  Users = CreateApiModel.objects.all()
  for user in Users:
    subject = 'Bitcoin $ Price Alert'
    message = 'Hi {user.name}, \n The Bitcoin price is higher than your alert price({user.price})'
    email_from = settings.EMAIL_HOST_USER
    send_mail(subject, message, email_from, user.email)
  return HttpResponse('Email send')


class CreateApi(APIView):
  serializer_class = CreateSerializers

  def get(self, request):
    return Response('get fun')

  def post(self, request):
    serializer = CreateSerializers(data = request.data)
    if serializer.is_valid():
      serializer.save()
    return Response('post fun')