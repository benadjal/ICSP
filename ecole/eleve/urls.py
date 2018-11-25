from django.urls import path
from . import views

urlpatterns = [
	path('home', views.home),
    path('inscription', views.inscription),
    path('addition/<int:x>/<int:y>/', views.addition)
]

