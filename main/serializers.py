from .models import Account
from rest_framework import serializers


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ('no', 'name', 'email', 'password', 'created_at', 'age')
