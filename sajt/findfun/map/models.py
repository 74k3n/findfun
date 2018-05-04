from django.contrib.gis.db import models
from django.contrib.gis.geos import Point
from django.contrib import admin
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.conf import settings
from datetime import datetime


class Location(models.Model):

	title 			= models.CharField(max_length = 128)
	description 	= models.TextField(blank = True, null = True)
	address  		= models.CharField(max_length = 256, blank = True, null = True)
	point 			= models.PointField(default='POINT(0 0)', srid = 4326)

	created_at 		= models.DateTimeField(auto_now_add = True)
	updated_at 		= models.DateTimeField(auto_now = True)

	# events 		= models.ForeignKey("Event", blank = True, on_delete = models.DO_NOTHING)
	# ratings 		= models.ForeignKey("Rating", blank = True, on_delete = models.DO_NOTHING)

	def __str__(self):
		return self.title

	@property
	def longitude(self):
		return self.point[0]

	@property
	def lattitude(self):
		return self.point[1]


class Event(models.Model):

	title 			= models.CharField(max_length = 128)
	datetime 		= models.DateTimeField(default = datetime.now(), blank = True)
	description 	= models.TextField(blank = True, null = True)
	location 		= models.ForeignKey(Location, on_delete = models.CASCADE, null = True)

	def __str__(self):
		return self.title

class Rating(models.Model):

	ONE = 1
	TWO = 2
	THREE = 3
	FOUR = 4
	FIVE = 5

	RATINGS = (
		(1, 'ONE'),
		(2, 'TWO'),
		(3, 'THREE'),
		(4, 'FOUR'),
		(5, 'FIVE'),
	)

	title 			= models.CharField(max_length = 128)
	description 	= models.TextField(blank = True, null = True)
	rating 			= models.IntegerField(choices = RATINGS, default = 5)
	location 		= models.ForeignKey(Location, on_delete = models.CASCADE, null = True)

	def __str__(self):
		return self.title