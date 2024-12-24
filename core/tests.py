from django.test import TestCase
from .models import EVChargingLocation
from .forms import EVChargingLocationForm, BookingForm

class EVChargingLocationModelTest(TestCase):

    def setUp(self):
        self.station = EVChargingLocation.objects.create(
            station_name='Test Station',
            latitude=34.0522,
            longitude=-118.2437
        )

    def test_station_creation(self):
        self.assertEqual(self.station.station_name, 'Test Station')
        self.assertEqual(self.station.latitude, 34.0522)
        self.assertEqual(self.station.longitude, -118.2437)

class EVChargingLocationFormTest(TestCase):

    def test_valid_form(self):
        form_data = {
            'station_name': 'New Station',
            'latitude': 40.7128,
            'longitude': -74.0060
        }
        form = EVChargingLocationForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        form_data = {
            'station_name': '',
            'latitude': '',
            'longitude': ''
        }
        form = EVChargingLocationForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 3)  # All fields are required

class BookingFormTest(TestCase):

    def test_valid_booking_form(self):
        form_data = {
            'user_name': 'John Doe',
            'user_email': 'john@example.com',
            'booking_time': '2024-10-23 15:30'
        }
        form = BookingForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_invalid_booking_form(self):
        form_data = {
            'user_name': '',
            'user_email': 'invalid-email',
            'booking_time': ''
        }
        form = BookingForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 3)  # All fields are required
