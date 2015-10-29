from django.db import models
from datetime import date

# Create your models here.
class ClinicTime(models.Model):
	officer = models.ForeignKey('authenication.Officer')
	clinic_datetime = models.DateTimeField()
	clinic_status = models.SmallIntegerField()

	def __str__(self):
		return self.id + " " + self.officer_id + " " + self.clinic_datetime + " " + self.clinic_status


class Appointment(models.Model):
	patient = models.ForeignKey('authenication.Patient')
	clinic_time = models.ForeignKey('appointment.ClinicTime')
	appointment_status = models.SmallIntegerField()

	def __str__(self):
		return self.id + " " + self.patient_id + " " + self.clinic_time_id + " " + self.appointment_status



