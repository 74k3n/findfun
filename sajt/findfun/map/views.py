from django.shortcuts import render
from .models import Location
from django.conf import settings
import json



def index(request):
	return render(request, 'map/index.html', {'Locations':Location.objects.all(), 'GOOGLE_MAPS_API':settings.GOOGLE_MAPS_KEY})
