from rest_framework import models
from rest_framework import serializers
from .models import Question
from django.contrib.auth.models import User

class StockSerializer(serializers.ModelSerializer):

      class Meta:
            model = User
            #fields = ('ticker','volume')
            fields = '__all__' 


class StockSerializer(serializers.ModelSerializer):

      class Meta:
            model = Question
            #fields = ('ticker','volume')
            fields = '__all__' 