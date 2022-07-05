from django.test import TestCase
from tolsys.models import Patient, Survey
#from tolsys.views import MainPage

class HomePageTest(TestCase):
	def test_mainpage_as_seen_client(self):
		response=self.client.get('/')
		self.assertTemplateUsed(response,'mainpage.html')

class CreateListTest(TestCase):
	def test_responsing_post_request(self):
		response = self.client.post('/tolsys/newlist_url', data={ 
			'firstname':'Angela Frances', 
			'middlename':'Columna',
			'surname':'Velasco',
			'birthday':'10 / 04 / 2000',
			'age':'21',
			'sex':'Female',
			'address':'Amuntay Road Zone 3 Dasma City, Cavite',
			'email':'angelafrances.velasco@gsfe.tupcavite.edu.ph',
			'mobile':'09514948724'})
		self.assertEqual(Patient.objects.count(), 1)
		newEntry = Patient.objects.first()
		self.assertEqual(newEntry.fname, 'Angela Frances')

	def test_redirect_POST(self):
		response = self.client.post('/tolsys/newlist_url', data={ 
			'firstname':'Angela Frances', 
			'middlename':'Columna',
			'surname':'Velasco',
			'birthday':'10 / 04 / 2000',
			'age':'21',
			'sex':'Female',
			'address':'Amuntay Road Zone 3 Dasma City, Cavite',
			'email':'angelafrances.velasco@gsfe.tupcavite.edu.ph',
			'mobile':'09514948724'})
		self.assertEqual (Patient.objects.count(), 1)
		newPatient = Patient.objects.first()
		self.assertRedirects(response,f'/tolsys/{newPatient.id}/')

class ViewTest(TestCase):
	def test_displays_for_each_patient(self):
		mpatientid1= Patient.objects.create(fname="Angela Frances",mname="Columna",sname="Velasco")
		Survey.objects.create(patientid=mpatientid1,dttoday="06 / 27 / 2022",sncwhen="2019",md="Afraid",cs="Seasonal",dcd="Want to do it so")
		Survey.objects.create(patientid=mpatientid1,dttoday="07 / 16 / 2022",sncwhen="01 / 02 / 2022",md="Sad",cs="Self",dcd="I dont know")
		mpatientid2= Patient.objects.create(fname="Rose Angeline",mname="Columna",sname="Velasco")
		Survey.objects.create(patientid=mpatientid2,dttoday="06 / 25 / 2022",sncwhen="2021",md="Not good",cs="Loneliness",dcd="I really need this.")
		Survey.objects.create(patientid=mpatientid2,dttoday="07 / 10 / 2022",sncwhen="01 / 10 / 2022",md="Moody",cs="Others",dcd="I am not well for so long")
		response = self.client.get(f'/tolsys/{mpatientid1.id}/')
		self.assertContains(response,'06 / 27 / 2022')
		self.assertContains(response,'07 / 16 / 2022')
		self.assertNotContains(response,'06 / 25 / 2022')
		self.assertNotContains(response,'07 / 10 / 2022')
		response = self.client.get(f'/tolsys/{mpatientid2.id}/')
		self.assertNotContains(response,'06 / 27 / 2022')
		self.assertNotContains(response,'07 / 16 / 2022')
		self.assertContains(response,'06 / 25 / 2022')
		self.assertContains(response,'07 / 10 / 2022')

	def test_survey_uses_surveypage(self):
		newPatient = Patient.objects.create()
		response = self.client.get(f'/tolsys/{newPatient.id}/')
		self.assertTemplateUsed(response, 'surveypage.html')

	def test_pass_surveyans_to_template(self):
		patient1 = Patient.objects.create()
		passAnswer = Patient.objects.create()
		response = self.client.get(f'/tolsys/{passAnswer.id}/')
		patient2 = Patient.objects.create()
		self.assertEqual(response.context['patientId'],passAnswer)

class AddSurveyAnswerTest(TestCase):
	def test_add_POST_request_to_existing_Patient(self):
		Patient1 = Patient.objects.create()
		Patient0 = Patient.objects.create()
		Patient2 = Patient.objects.create()
		self.client.post(f'/tolsys/{Patient0.id}/addans',data={
			'datetoday':'06 / 27 / 2022',
			'sincewhen':'2020',
			'mood':'Sad',
			'cause':'Seasonal',
			'decide':'Want to do it so'})
		self.assertEqual(Survey.objects.count(), 1)
		newEntry = Survey.objects.first()
		self.assertEqual(newEntry.dttoday, '06 / 27 / 2022')
		self.assertEqual(newEntry.patientid, Patient0)

	def test_redirects_to_list_view(self):
		Patient1 = Patient.objects.create()
		Patient0 = Patient.objects.create()
		Patient2 = Patient.objects.create()
		Patient3 = Patient.objects.create()
		response = self.client.post(f'/tolsys/{Patient0.id}/addans',data={
			'datetoday':'06 / 27 / 2022',
			'sincewhen':'2020',
			'mood':'Sad',
			'cause':'Seasonal',
			'decide':'Want to do it so'})
		self.assertRedirects(response, f'/tolsys/{Patient0.id}/')

class ORMTest(TestCase):
	def test_saving_retrieving_list(self):
		newEntry = Patient()
		newEntry.fname = 'Angela Frances'
		newEntry.mname = 'Columna'
		newEntry.sname = 'Velasco'
		newEntry.bday = '10 / 04 / 2000'
		newEntry.age = '21'
		newEntry.sex = 'Female'
		newEntry.add = 'Amuntay Road Zone 3 Dasma City, Cavite'
		newEntry.eml = 'angelafrances.velasco@gsfe.tupcavite.edu.ph'
		newEntry.mbl =  '09514948724'
		newEntry.save()
		surveyItem1 = Survey()
		surveyItem1.patientid = newEntry
		surveyItem1.dttoday = '06 / 27 / 2022'
		surveyItem1.sncwhen = '2020'
		surveyItem1.md = 'Frustrated'
		surveyItem1.cs = 'Too many roles in life.'
		surveyItem1.dcd = 'Too much stress.'
		surveyItem1.save()
		surveyItem2 = Survey()
		surveyItem2.patientid = newEntry
		surveyItem2.dttoday = '07 / 16 / 2022'
		surveyItem2.sncwhen = '01 / 02 / 2022'
		surveyItem2.md = 'Disappointed'
		surveyItem2.cs = 'Procrastination'
		surveyItem2.dcd = 'I am not well for so long.'
		surveyItem2.save()
		savedEntry = Patient.objects.first()
		self.assertEqual(savedEntry, newEntry)
		savedSurveyAns = Survey.objects.all()
		self.assertEqual(savedSurveyAns.count(), 2)
		savedSurveyAns1 = savedSurveyAns[0]
		savedSurveyAns2 = savedSurveyAns[1]
		self.assertEqual(savedSurveyAns1.dttoday, '06 / 27 / 2022')
		self.assertEqual(savedSurveyAns2.dttoday, '07 / 16 / 2022')
		self.assertEqual(savedSurveyAns1.sncwhen, '2020')
		self.assertEqual(savedSurveyAns2.sncwhen, '01 / 02 / 2022')
		self.assertEqual(savedSurveyAns1.md, 'Frustrated')
		self.assertEqual(savedSurveyAns2.md, 'Disappointed')
		self.assertEqual(savedSurveyAns1.cs, 'Too many roles in life.')
		self.assertEqual(savedSurveyAns2.cs, 'Procrastination')
		self.assertEqual(savedSurveyAns1.dcd, 'Too much stress.')
		self.assertEqual(savedSurveyAns2.dcd, 'I am not well for so long.')
		self.assertEqual(savedSurveyAns1.patientid, newEntry)
		self.assertEqual(savedSurveyAns2.patientid, newEntry)
		
	# def test_saving_retrieving_list(self):
	# 	entry1 = Patient()
	# 	entry1.fname = 'Angela Frances'
	# 	entry1.mname = 'Columna'
	# 	entry1.sname = 'Velasco'
	# 	entry1.bday = '10 / 04 / 2000'
	# 	entry1.age = '21'
	# 	entry1.sex = 'Female'
	# 	entry1.add = 'Amuntay Road Zone 3 Dasma City, Cavite'
	# 	entry1.eml = 'angelafrances.velasco@gsfe.tupcavite.edu.ph'
	# 	entry1.mbl =  '09514948724'
	# 	entry1.save()
	# 	entry2 = Patient()
	# 	entry2.fname = 'Ana'
	# 	entry2.mname = 'Juan'
	# 	entry2.sname = 'Cruz'
	# 	entry1.bday = '06 / 27 / 1998'
	# 	entry1.age = '23'
	# 	entry1.sex = 'Female'
	# 	entry1.add = 'Adlas Silang, Cavite'
	# 	entry2.eml = 'ana.cruz@gsfe.tupcavite.edu.ph'
	# 	entry2.mbl =  '09098159410'
	# 	entry2.save()
	# 	items = Patient.objects.all()
	# 	self.assertEqual(items.count(), 2)
	# 	items1 = items[0]
	# 	items2 = items[1]
	# 	self.assertEqual(items1.fname, 'Angela Frances')
	# 	self.assertEqual(items2.fname, 'Ana')