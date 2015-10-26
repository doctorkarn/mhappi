from django.db import models
from datetime import date

# Create your models here.
class Patient(models.Model):
	GENDER_CHOICES = (
		(1, "Male"),
		(2, "Female"),
		(3, "Others"),
	)

	hospital_id = models.CharField(max_length = 20)
	national_id = models.CharField(max_length = 20)
	prefix_name = models.CharField(max_length = 200)
	first_name = models.CharField(max_length = 200)
	last_name = models.CharField(max_length = 200)
	gender = models.IntegerField(choices = GENDER_CHOICES)
	birthdate = models.DateTimeField()
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
	specialist = models.CharField(max_length = 200)
	position = models.CharField(max_length = 100, default = "")


	def __str__(self):
		return self.hospital_id + " " + self.first_name + " " + self.last_name