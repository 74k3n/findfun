from django.urls import path
from . import views

urlpatterns = [
    path('', views.Index.as_view()),
    path('logout/', views.UserLogout.as_view()),
    path('profile/', views.ProfileView.as_view()),
]

