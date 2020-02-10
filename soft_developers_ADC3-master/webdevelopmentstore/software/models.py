from django.db import models

# Create your models here.

class App(models.Model):
	soft_name = models.CharField(max_length = 200)
	developer = models.CharField(max_length = 200)
	version = models.IntegerField()
	date = models.DateTimeField("uploaded date")


class Position(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class User(models.Model):
	user_fname = models.CharField(max_length = 100)
	user_lname = models.CharField(max_length = 100)
	username = models.CharField(max_length = 100)
	user_email = models.EmailField()
	password = models.CharField(max_length=32, null = True )


class Device(models.Model):
	device_name = models.CharField(max_length = 100)
	device_model = models.CharField(max_length = 100)

class Software(models.Model):
	title = models.CharField(max_length=100)
	name = models.CharField(max_length=20)
	stw = models.FileField(upload_to="software_upload/stw")
