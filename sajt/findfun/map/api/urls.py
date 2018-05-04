from .views import LocationRView, LocationLView, EventLView, EventRView
from django.urls import path, include

urlpatterns = [
	path('locations/', LocationLView.as_view(), name = 'loc-l'),
	path('locations/<int:pk>/', LocationRView.as_view(), name = 'loc-r'),
	path('events/<int:location>/', EventLView.as_view(), name = 'event-l'),
	path('events/<int:location>/<int:pk>/', EventRView.as_view(), name = 'event-r')
]