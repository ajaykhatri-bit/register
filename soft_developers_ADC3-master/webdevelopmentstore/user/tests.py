from django.test import TestCase
from main.models import Tutorial
from datetime import datetime

# Create your tests here.

class AppTest(TestCase):
	def setUp(self):
		App.objects.Create(soft_name="hey", developer="hahhahah", date=datetime.now())


def test_ORM(self):
	a = App.objects.get(soft_name="hey")
	self.assertEqual(a.soft_name, "hey")