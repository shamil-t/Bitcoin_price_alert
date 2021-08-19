import json
from api.serializers import *
from django.http.response import HttpResponse
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view

from django.views.decorators.csrf import csrf_exempt
from .models import *

import schedule
from schedule import Scheduler
import time
import threading

from .scrapper import crypto

# Create your views here.


def Index(request):
    Scheduler.run_continuously = run_continuously
    return render(request, 'index.html')


def Home(request, id):
    user = UserModel.objects.get(id=id)

    name = user.name
    email = user.email

    context = {
        "name": name,
        "email": email,
        "id": id,
    }

    return render(request, 'home.html', context=context)


def CreateAlert(request, id):
    user = UserModel.objects.get(id=id)

    name = user.name
    email = user.email

    context = {
        "name": name,
        "email": email,
        "id": id,
    }

    return render(request, 'create_alert.html', context=context)


def GetAlerts(request, id):
    user = UserModel.objects.get(id=id)
    alerts = CreateApiModel.objects.filter(user=id)
    name = user.name
    email = user.email

    context = {
        "name": name,
        "email": email,
        "id": id,
        "alerts": alerts
    }

    return render(request, 'alerts.html', context=context)




class UserView(APIView):
    serializer_class = UserSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': True, 'id': serializer.data['id']})

        return Response(serializer.errors)

# end point
# /login/


@api_view(['POST'])
def login(request):
    users = UserModel.objects.all()
    user = users.filter(email=request.data['email'])

    if user.exists():
        user = user.get(email=request.data['email'])
        if user.password == request.data['pwd']:
            return Response({"u_id": user.id})

    return Response({"res": False})

# end point
# /alert/create


@api_view(['POST'])
def createAlert(request):
    serialaizer_class = CreateSerializers

    serializer = serialaizer_class(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)

    return Response(serializer.errors)

# end point
# /alert/all/


@api_view(['GET'])
def getAlert(request, id):
    Alerts = CreateApiModel.objects.filter(user=id)
    alerts = [CreateSerializers(alert).data for alert in Alerts]
    return Response(alerts)

@csrf_exempt
@api_view(['POST'])
def delAlert(request,id):
    CreateApiModel.objects.get(id=id).delete()
    return Response({"res": True})


# end point
# /get/coins


@api_view(['GET'])
def getCrypto(request):
    coins = crypto.getCoinPrice()
    return Response(coins)


## Scheduler

def run_continuously(self, interval=1):
    """Continuously run, while executing pending jobs at each elapsed
    time interval.
    @return cease_continuous_run: threading.Event which can be set to
    cease continuous run.
    Please note that it is *intended behavior that run_continuously()
    does not run missed jobs*. For example, if you've registered a job
    that should run every minute and you set a continuous run interval
    of one hour then your job won't be run 60 times at each interval but
    only once.
    """

    print('in class scheduler')

    cease_continuous_run = threading.Event()

    class ScheduleThread(threading.Thread):

        @classmethod
        def run(cls):
            while not cease_continuous_run.is_set():
                self.run_pending()
                time.sleep(interval)
        
        def foo(self):
            # if some_condition():
            print('in fooo')
            return schedule.CancelJob  # a job can dequeue it

        # can be put in __enter__ or __init__
        # self._job_stop = self.scheduler.run_continuously()

        # logger.debug("doing foo"...)
        self.foo() # call foo
        self.scheduler.every(5).seconds.do(self.foo) # schedule foo for running every 5 seconds


        # later on foo is not needed any more:
        self._job_stop.set()

        def __exit__(self, exec_type, exc_value, traceback):
            # if the jobs are not stop, you can stop them
            self._job_stop.set()

    continuous_thread = ScheduleThread()
    continuous_thread.setDaemon(True)
    continuous_thread.start()

    return cease_continuous_run