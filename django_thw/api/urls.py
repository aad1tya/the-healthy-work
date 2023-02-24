from django.urls import path
from . import views

urlpatterns = [
	path('', views.getRoutes, name="routes"),
	path('cards/', views.getCards, name="cards"),
	path('cards/<str:pk>', views.getCard, name="card")
]
