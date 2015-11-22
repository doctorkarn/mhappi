from django.db import models
from datetime import date
from django.contrib.auth.models import User

# Create your models here.
class Patient(models.Model):
	GENDER_CHOICES = (
		(1, "Male"),
		(2, "Female"),
		(3, "Others"),
	)

	user = models.ForeignKey(User, default = 0)
	hospital_id = models.CharField(max_length = 20)
	national_id = models.CharField(max_length = 20)
	prefix_name = models.CharField(max_length = 200)
	first_name = models.CharField(max_length = 200)
	last_name = models.CharField(max_length = 200)
	gender = models.IntegerField(choices = GENDER_CHOICES)
	birthdate = models.DateField()
	address = models.CharField(max_length = 500)
	phone = models.CharField(max_length = 200)
	email = models.CharField(max_length = 200)
	# created_at = models.DateTimeField(auto_now_add = True)
	# updated_at = models.DateTimeField(auto_now = True)

	def __str__(self):
		return self.hospital_id + " " + self.first_name + " " + self.last_name


class Officer(models.Model):
	GENDER_CHOICES = (
		(1, "Male"),
		(2, "Female"),
		(3, "Others"),
	)
	POSITION_CHOICES = (
		(1, "Staff"),
		(2, "Doctor"),
		(3, "Nurse"),
		(4, "Pharmacist"),
	)

	user = models.ForeignKey(User, default = 0)
	hospital_id = models.CharField(max_length = 20)
	national_id = models.CharField(max_length = 20)
	prefix_name = models.CharField(max_length = 200)
	first_name = models.CharField(max_length = 200)
	last_name = models.CharField(max_length = 200)
	gender = models.IntegerField(choices = GENDER_CHOICES)
	birthdate = models.DateField()
	address = models.CharField(max_length = 500)
	phone = models.CharField(max_length = 200)
	email = models.CharField(max_length = 200)
	specialist = models.ForeignKey('authentication.Department', default = 0)
	position = models.IntegerField(choices = POSITION_CHOICES, default = 1)


	def __str__(self):
		return self.hospital_id + " " + self.first_name + " " + self.last_name


class Department(models.Model):
	name = models.CharField(max_length = 200)