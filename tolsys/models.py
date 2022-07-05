from django.db import models

class Patient(models.Model):
	fname = models.CharField(max_length=200)
	mname = models.CharField(max_length=200)
	sname = models.CharField(max_length=200)
	bday = models.CharField(max_length=200)
	age = models.IntegerField(default=None, blank=False)
	sex = models.CharField(max_length=200)
	add = models.CharField(max_length=200)
	eml = models.CharField(max_length=200)
	mbl = models.IntegerField(default=None, blank=False)

class Survey(models.Model):
	patientid = models.ForeignKey(Patient,default=None, on_delete=models.CASCADE)
	dttoday = models.DateField(default=None, blank=False)
	sncwhen = models.TextField(default=None, blank=False)
	md = models.TextField(default=None, blank=False)
	cs = models.TextField(default=None, blank=False)
	dcd = models.TextField(default=None, blank=False)

	class meta:
		db_table = 'survey'
		verbose_name = 'survey'

class Appointment(models.Model):
	patientid = models.ForeignKey(Patient,default="None", on_delete=models.CASCADE)
	kdsession = models.TextField(default=None, blank=False)
	tpsession = models.TextField(default=None, blank=False)
	adate = models.TextField(default=None, blank=False)
	atime = models.TextField(default=None, blank=False)
	class meta:
		db_table = 'appointment'
		verbose_name = 'appointment'




