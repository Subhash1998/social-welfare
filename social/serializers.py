from rest_framework import models
from rest_framework import serializers
from .models import Question,post_question,answer
from django.contrib.auth.models import User

class StockSerializer1(serializers.ModelSerializer):

      class Meta:
            model = User
            #fields = ('ticker','volume')
            fields = ('first_name','last_name','email','username','password')


class StockSerializer2(serializers.ModelSerializer):

      class Meta:
            model = Question
            #fields = ('ticker','volume')
            fields = '__all__' 


class StockSerializer3(serializers.ModelSerializer):

      class Meta:
            model = post_question
            #fields = ('ticker','volume')
            fields = '__all__' 

class StockSerializer4(serializers.ModelSerializer):

      class Meta:
            model = answer
            #fields = ('ticker','volume')
            fields = '__all__'             