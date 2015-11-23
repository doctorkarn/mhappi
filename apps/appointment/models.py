from django.db import models
from django.utils import timezone

# Create your models here.
class ClinicTime(models.Model):
	officer = models.ForeignKey('authentication.Officer')
	clinic_datetime = models.DateTimeField()
	clinic_status = models.SmallIntegerField()
	# clinic_count = models.IntegerField()
	created_at = models.DateTimeField(auto_now_add = True)

	def __str__(self):
		return self.id + " " + self.officer_id + " " + self.clinic_datetime + " " + self.clinic_status


class Appointment(models.Model):
	patient = models.ForeignKey('authentication.Patient')
	clinic_time = models.ForeignKey('appointment.ClinicTime')
	appointment_status = models.SmallIntegerField()
	created_at = models.DateTimeField(auto_now_add = True)

	def __str__(self):
		return self.id + " " + self.patient_id + " " + self.clinic_time_id + " " + self.appointment_status



