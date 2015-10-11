from django.db import models
import datetime

# Create your models here
class Person(models.Model):
	name = models.CharField(max_length=20)
	tfidf_score = models.FloatField()
	num_followers = models.IntegerField()

class Word_Count_Table(models.Model):
	person = models.OneToOneField(Person)
	word = models.CharField(max_length=100)
	count = models.IntegerField()

class Tweet_Table(models.Model):
	person = models.OneToOneField(Person)
	tweet_time = models.DateTimeField()
	tweet_place = models.CharField(max_length=500)
