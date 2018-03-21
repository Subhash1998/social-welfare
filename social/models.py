from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

class Question(models.Model):
	RATING_CHOICES = (
	('HEALTH', 'HEALTH'),
	('AGRICULTURE', 'AGRICULTURE'),
	('UNEMPLOYMENT', 'UNEMPLOYMENT'),
	('CORRUPTION', 'CORRUPTION'),
	('EDUCATION', 'EDUCATION'),
	)
	user_name=models.CharField(max_length=100,blank=True)
	question=models.CharField(max_length=10000,null=True,blank=True)
	topic=models.CharField(max_length=20,choices=RATING_CHOICES,null=True,blank=True)
	def __str__(self):
          return self.topic 


class post_question(models.Model):
	name=models.CharField(max_length=200)
	ask = models.CharField(max_length=20000)
	def __unicode__(self):
		return self.name


class answer(models.Model):
	ques = models.ForeignKey(post_question)
	pub_date = models.DateTimeField('date published')
	user_name = models.CharField(max_length=100)
	comment = models.CharField(max_length=200)
	def __str__(self):
          return self.user_name