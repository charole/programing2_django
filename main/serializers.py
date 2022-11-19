from .models import Account, Example
from rest_framework import serializers


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ('no', 'name', 'email', 'password', 'created_at', 'age')

class ExampleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Example
        fields = ('index', 'title', 'content', 'answer', 'example', 'point')
