from django.db import models

# Create your models here.
class MedicalRecord(models.Model):
	patient = models.ForeignKey('authenication.Patient')
	officer = models.ForeignKey('authenication.Officer')
	symptom = models.TextField()
	diagnosis = models.TextField()
	drg_code = models.CharField(max_length = 20)

	def __str__(self):
		return self.id + " " + self.patient_id + ":" + self.officer + " " + self.symptom + " -> " + self.diagnosis


class PatientInfo(models.Model):
	patient = models.ForeignKey('authenication.Patient')
	officer = models.ForeignKey('authenication.Officer')
	information = models.TextField()

	def __str__(self):
		return self.id + " " + self.patient_id + ":" + self.officer + " " + self.information


class Prescritpion(models.Model):
	patient = models.ForeignKey('authenication.Patient')
	officer = models.ForeignKey('authenication.Officer')
	drug_list = models.TextField()

	def __str__(self):
		return self.id + " " + self.patient_id + ":" + self.officer + " " + self.drug_list

