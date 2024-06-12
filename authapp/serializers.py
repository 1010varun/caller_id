from rest_framework import serializers
from .models import *


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'phone_number', 'email', 'is_spam', 'contact_of', 'is_registered')
        extra_kwargs = {'password': {'write_only': True}}

    def mark_registered(self, **kwargs) :
        instance = super().save(**kwargs)
        instance.mark_as_registered() 

    def is_registered(self, **kwargs) :
        instance = super().save(**kwargs)
        if(instance.is_registered) :
            return True
        return False