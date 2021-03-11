from rest_framework import serializers
from stringsapp.models import phonenum
from stringsapp.models import inputstring
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = phonenum
        fields = ["number"]

class StringSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = inputstring
        fields = ["source"]
