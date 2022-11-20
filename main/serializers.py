from .models import Account, Example
from rest_framework import serializers


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ('no', 'name', 'email', 'password',
                  'created_at', 'age', 'point')


class ExampleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Example
        fields = ('id', 'title', 'content', 'exam_question',
                  'answer', 'example', 'point', 'level')
