import json
from api.serializers import *
from django.http.response import HttpResponse
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view

from django.conf import settings
from django.core.mail import send_mail
from .models import *

from .scrapper import crypto
# Create your views here.

# admin : btc123

def Index(request):
    return render(request, 'index.html')

def Home(request,id):
    user = UserModel.objects.get(id = id)

    name = user.name
    email = user.email

    context = {
        "name" : name,
        "email":email,
    }

    return render(request,'home.html',context=context)



def sendEmail():
    Users = CreateApiModel.objects.all()
    for user in Users:
        subject = 'Bitcoin $ Price Alert'
        message = 'Hi {user.name}, \n The Bitcoin price is higher than your alert price({user.price})'
        email_from = settings.EMAIL_HOST_USER
        send_mail(subject, message, email_from, user.email)
    return HttpResponse('Email send')


class UserView(APIView):
    serializer_class = UserSerializer

    def post(self, request, format=None):

        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response({'status':True, 'id': serializer.data['id']})

        return Response(serializer.errors)

@api_view(['POST'])
def login(request):
	users = UserModel.objects.all()
	user = users.filter(email = request.data['email'])

	if user.exists():
		user = user.get(email = request.data['email'])
		if user.password == request.data['pwd']:
			return Response({"u_id": user.id})
	else:
		return Response('false')

@api_view(['POST'])
def createAlert(request):

    return Response('Heloo')

@api_view(['GET'])
def getCrypto(request):
    coins = crypto.getCoinPrice()
    # print(coins)
    return Response(coins)