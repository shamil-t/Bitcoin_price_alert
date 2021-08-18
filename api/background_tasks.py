from schedule import Scheduler
import threading
import time
from .models import *
from .scrapper.crypto import getCoinPrice

from django.conf import settings
from django.core.mail import send_mail


def checkStatus():
    coin = getCoinPrice()
    btc_price = coin[0]['price'].replace("$", "").strip()

    Alerts = CreateApiModel.objects.filter(trigger=True)

    for alert in Alerts:
        if alert.alert_price <= int(float(btc_price.replace(',', ""))):
            sendEmail(alert)

    # print(Alerts)


def start_scheduler():
    scheduler = Scheduler()
    scheduler.every().second.do(checkStatus)
    scheduler.run_continuously()


def sendEmail(alert):
    subject = 'Bitcoin Price Alert ()'
    message = f'Hi {alert.user.name}, \n The Bitcoin price is higher than your alert price ${alert.alert_price}'
    email_from = settings.EMAIL_HOST_USER

    send_mail(subject, message, email_from, [alert.user.email])

    a = CreateApiModel.objects.get(id = alert.id)
    a.trigger = False
    a.status = True
    a.save()

    print('Email send')


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

    cease_continuous_run = threading.Event()

    class ScheduleThread(threading.Thread):

        @classmethod
        def run(cls):
            while not cease_continuous_run.is_set():
                self.run_pending()
                time.sleep(interval)

    continuous_thread = ScheduleThread()
    continuous_thread.setDaemon(True)
    continuous_thread.start()
    return cease_continuous_run


Scheduler.run_continuously = run_continuously
