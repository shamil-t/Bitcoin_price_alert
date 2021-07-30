from django.db import models

# Create your models here.

class CreateApiModel(models.Model):
  name = models.CharField(max_length=100)
  email = models.EmailField(max_length=100)
  price = models.IntegerField(default=0)

  def __str__(self):
      return "{} - {}".format(self.name, self.email)