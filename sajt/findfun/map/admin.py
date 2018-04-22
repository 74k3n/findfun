from django.contrib import admin
from django.contrib.gis.db import models
from .models import Location, Event, Rating
from mapwidgets.widgets import GooglePointFieldWidget
# Register your models here.

class locationAdmin(admin.ModelAdmin):
	formfield_overrides = {
        models.PointField: {"widget": GooglePointFieldWidget}
    }

admin.site.register(Location, locationAdmin)

class eventAdmin(admin.ModelAdmin):
	pass

admin.site.register(Event, eventAdmin)

class ratingAdmin(admin.ModelAdmin):
	pass

admin.site.register(Rating, ratingAdmin)