from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.expressions import F

# Create your models here.


class UserModel(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)
    password = models.CharField(max_length=100)

    def __str__(self):
        return "{} - {}".format(self.id, self.name)


class CreateApiModel(models.Model):
    alert_name = models.CharField(max_length=100)
    user = models.ForeignKey(UserModel, on_delete=CASCADE)
    alert_price = models.IntegerField(default=0)
    trigger = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=False)

    # def __str__(self):
    #     return "__all__"
