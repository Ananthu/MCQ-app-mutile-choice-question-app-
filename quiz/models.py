from __future__ import unicode_literals
from django.core.urlresolvers import reverse
from django.db import models

# Create your models here.


class Question(models.Model):
	question_no=models.IntegerField(default=0)
	question_text=models.TextField(max_length=1000)
	option1=models.CharField(max_length=100)
	option2=models.CharField(max_length=100)
	option3=models.CharField(max_length=100)
	option4=models.CharField(max_length=100)
	option5=models.CharField(max_length=100)
	answer1=models.CharField(max_length=100)

	def get_absolute_url(self):
		return reverse('quiz:detail',kwargs={'pk':self.pk})

	def __str__(self):
		return self.question_text

class Result(models.Model):
	username=models.CharField(max_length=100)
	email=models.CharField(max_length=100)
	score=models.IntegerField(default=0)

	def __str__(self):
		return self.username
		