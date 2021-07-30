from api.models import CreateApiModel
from rest_framework  import serializers


class CreateSerializers(serializers.ModelSerializer):

  class Meta:
    model = CreateApiModel
    fields = [
      'name', 'email', 'price'
    ]