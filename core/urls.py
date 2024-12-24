from django.urls import path
from core import views  # Make sure to adjust the import according to your app structure

urlpatterns = [
    path('', views.index, name='index'),  # Route for the home page
    path('nearest_station/', views.nearest_station, name='nearest_station'),  # Route for finding nearest station
    path('book_station/', views.book_station, name='book_station'),  # Route for booking the station
]
