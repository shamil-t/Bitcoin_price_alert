from django.db.models import fields
from api.models import *
from rest_framework  import serializers


class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model = UserModel
    fields = '__all__'

class CreateSerializers(serializers.ModelSerializer):
  class Meta:
    model = CreateApiModel
    fields =  '__all__'
