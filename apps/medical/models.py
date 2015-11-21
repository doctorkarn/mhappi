from django.db import models

# Create your models here.
class MedicalRecord(models.Model):
	patient = models.ForeignKey('authentication.Patient')
	officer = models.ForeignKey('authentication.Officer')
	symptom = models.TextField()
	diagnosis = models.TextField()
	drg_code = models.ForeignKey('medical.DrgCode')
	created_at = models.DateTimeField(auto_now_add = True)
	# updated_at = models.DateTimeField(auto_now = True)

	def __str__(self):
		return self.id + " " + self.patient_id + ":" + self.officer + " " + self.symptom + " -> " + self.diagnosis


class PatientInfo(models.Model):
	patient = models.ForeignKey('authentication.Patient')
	officer = models.ForeignKey('authentication.Officer')
	information = models.TextField()
	created_at = models.DateTimeField(auto_now_add = True)
	# updated_at = models.DateTimeField(auto_now = True)

	def __str__(self):
		return self.id + " " + self.patient_id + ":" + self.officer + " " + self.information


class Prescritpion(models.Model):
	patient = models.ForeignKey('authentication.Patient')
	officer = models.ForeignKey('authentication.Officer')
	drug_list = models.TextField()
	created_at = models.DateTimeField(auto_now_add = True)
	# updated_at = models.DateTimeField(auto_now = True)

	def __str__(self):
		return self.id + " " + self.patient_id + ":" + self.officer + " " + self.drug_list


class DrgCode(models.Model):
	description = models.CharField(max_length = 200)


class DrugList(models.Model):
	description = models.CharField(max_length = 200)