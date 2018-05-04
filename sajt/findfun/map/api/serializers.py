from rest_framework import serializers

from map.models import Location, Rating, Event

class LocationSerializer(serializers.ModelSerializer):
	class Meta:
		model = Location
		fields = [
			'pk',
			'title',
			'description',
			'address',
			'point',
			'created_at',
			'updated_at',
		]

class EventSerializer(serializers.ModelSerializer):
	class Meta:
		model = Event
		fields = [
			'pk',
			'title',
			'datetime',
			'description',
			'location',
		]


class RatingSerializer(serializers.ModelSerializer):
	class Meta:
		model = Rating
		fields = [
			'pk',
			'title',
			'description',
			'rating',
			'location',
		]
