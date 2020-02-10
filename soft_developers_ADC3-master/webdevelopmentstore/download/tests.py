from django.test import TestCase

# Create your tests here.
from main.models import Tutorial
from datetime import datetime

# Create your tests here.

class Coders(TestCase):
	def setUp(self):
		Device.objects.Create(device_name="hello", device_model="We are at risk")


def Device_ORM(self):
	d = Device.objects.get(device_name="hello")
	self.assertEqual(d.Device_name, "hello")
