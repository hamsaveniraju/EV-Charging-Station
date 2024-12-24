from django import forms
from .models import EVChargingLocation

class EVChargingLocationForm(forms.ModelForm):
    class Meta:
        model = EVChargingLocation
        fields = ['station_name', 'latitude', 'longitude']
        widgets = {
            'station_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Station Name'}),
            'latitude': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter Latitude'}),
            'longitude': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter Longitude'}),
        }

class BookingForm(forms.Form):
    user_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Name'}))
    user_email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Your Email'}))
    booking_time = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'class': 'form-control', 'placeholder': 'Booking Time (YYYY-MM-DD HH:MM)'}))
