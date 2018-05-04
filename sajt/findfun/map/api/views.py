from rest_framework import generics
from map.models import Location, Event, Rating
from .serializers import LocationSerializer, EventSerializer, RatingSerializer

class LocationRView(generics.RetrieveAPIView):
	lookup_field 			= 'pk'

	serializer_class 		= LocationSerializer

	def get_queryset(self):
		return Location.objects.all()


class LocationLView(generics.ListAPIView):

	lookup_field			= 'pk'
	serializer_class		= LocationSerializer

	def get_queryset(self):
		return Location.objects.all()

class EventLView(generics.ListAPIView):

	serializer_class		= EventSerializer

	def get_queryset(self):
		location = self.kwargs['location']
		return Event.objects.filter(location = location)

class EventRView(generics.RetrieveAPIView):

	serializer_class		= EventSerializer

	def get_queryset(self):
		location = self.kwargs['location']
		pk = self.kwargs['pk']
		return Event.objects.filter(location = location, id = pk)

class RatingLView(generics.ListAPIView):

	serializer_class		= RatingSerializer

	def get_queryset(self):
		location = self.kwargs['location']
		return Rating.objects.filter(location = location)

