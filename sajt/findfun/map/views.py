from django.shortcuts import render
from .models import Location
from django.conf import settings
from django.views import View
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.core.validators import validate_email
from django.core.exceptions import ValidationError

class ProfileView(View):
	def get(self, request, *args, **kwargs):
		return render(request, 'map/profile.html')

class UserLogout(View):
	def get(self, request, *args, **kwargs):
		logout(request)
		return HttpResponseRedirect("/")

class Index(View):
	def get(self, request, *args, **kwargs):
		return render(request, 'map/index.html', {'Locations':Location.objects.all(), 'GOOGLE_MAPS_API':settings.GOOGLE_MAPS_KEY})

	def post(self, request, *args, **kwargs):
		username = password = ''
		response_data = {}
		if request.is_ajax:

			if request.POST.get('classifier') == 'login':

				username = request.POST.get('username')
				password = request.POST.get('password')

				try:
					User.objects.get(username = username)
					user = authenticate(request,username = username, password = password)
					if user is not None:
						if user.is_active:
							login(request, user)
							response_data = {'login' : "Success"}
						else:
							response_data['user'] = "not active"
					else:
						response_data = {'user' : "password wrong"}
				except User.DoesNotExist:
					response_data = {'user' : "nouser"}

			elif request.POST.get('classifier') == 'register':

				username = request.POST.get('username')
				email = request.POST.get('email')
				password = request.POST.get('password')
				password_c = request.POST.get('password_c')

				try:
					user = User.objects.get(username = username)
					response_data['username'] = 'taken'
				except User.DoesNotExist:
					try:
						userE = User.objects.get(email = email)
						response_data['email'] = 'taken'
					except User.DoesNotExist:

						try:
							validate_email(email)
							if len(password) < 8:
								response_data['password'] = 'short'
							elif password != password_c:
								response_data['password_c'] = 'nomatch'
							else:
								User.objects.create_user(username = username, password = password, email = email)
								response_data = {'register' : 'Success'}
								user = authenticate(request, username = username, password = password)
								login(request, user)
						except ValidationError:
							response_data['email'] = 'invalid'

						

		else:
			username = password = ''
			response_data = {'error': "True"}
		return HttpResponse(JsonResponse(response_data))
		
