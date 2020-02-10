from django.test import TestCase,SimpleTestCase, Client
from .models import *
from .views import *
from django.urls import reverse,resolve

# Create your tests here.

class Test(TestCase): #Model testing     
    def test_dESC(self):
        desc = Software.objects.create(title="chartpaper", name="Namaste",
                                      stw = "i am the one"
                                      )
        use=Software.objects.get(title="chartpaper")
        self.assertEquals(use.title,"chartpaper")
    
    def test_User(self):
        user = User.objects.create(user_fname="test1",user_lname="test2",user_email="test@gmail.com",password="12345678")

        self.assertEqual(user.user_email,"test@gmail.com")
        self.assertEqual(user.password,"12345678")
    
    def test_Device(self):
        device = Device.objects.create(device_name="Android",device_model="10.1")

        self.assertEqual(device.device_model,"10.1")

    def test_User(self):
        user = User.objects.create(user_fname="test1",user_lname="test2",user_email="test@gmail.com",password="12345678")

        self.assertEqual(user.user_email,"test@gmail.com")
        self.assertEqual(user.password,"12345678")