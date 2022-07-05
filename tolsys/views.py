from django.shortcuts import render, redirect
from django.http import HttpResponse
from tolsys.models import Patient,Survey,Appointment

def MainPage(request):
	patientlist = Patient.objects.all()
	return render(request,'mainpage.html')

def ViewList(request,patientId):
	newPatient = Patient.objects.get(id=patientId)
	#patientlist = Survey.objects.filter(patientid=patientId)
	#return render(request,'surveypage.html',{'patientid':patientId,'patientList':patientlist})
	return render(request,'surveypage.html',{'newPatient':newPatient})

def NewList(request):
	vfname = request.POST['firstname']
	vmname = request.POST['middlename']
	vsname = request.POST['surname']
	vbday = request.POST['birthday']
	vage = request.POST['age']
	vsex = request.POST['sex']
	vadd = request.POST['address']
	veml = request.POST['email']
	vmbl = request.POST['mobile']
	newPatient =  Patient.objects.create(fname=vfname,mname=vmname,sname=vsname,
		bday=vbday,age=vage,sex=vsex,
		add=vadd,eml=veml,mbl=vmbl)
	# return redirect(f'/tolsys/viewlist_url')
	return redirect(f'/tolsys/{newPatient.id}/')

def AddAns(request, patientId):
	newPatient = Patient.objects.get(id=patientId)
	vdttoday = request.POST['dttoday']
	vsncwhen = request.POST['sncwhen']
	vmd = request.POST['md']
	vcs = request.POST['cs']
	vdcd = request.POST['dcd']
	Survey.objects.create(patientid=newPatient,dttoday=vdttoday,sncwhen=vsncwhen,md=vmd,cs=vcs,dcd=vdcd)
	return redirect(f'/tolsys/{newPatient.id}/')
	# return redirect(f'/tolsys/{vpatientid.id}/')

def delete(request, patientId):
	newPatient =  Patient.objects.get(id=patientId)
	newPatient.delete()
	return redirect(f'/tolsys/{None}/Addans2/')

def Addans2(request):
	return render(request, 'surveypage.html')

def edit(request, patientId):
	newPatient = Patient.objects.get(id=patientId)
	survey = Survey.objects.filter(id=patientId)
	print (survey)
	# vdttoday = request.POST['datetoday']
	# vsncwhen = request.POST['sincewhen']
	# vmd = request.POST['mood']
	# vcs = request.POST['cause']
	# vdcd = request.POST['decide']
	# Survey.objects.create(patientid=newPatient,dttoday=vdttoday,sncwhen=vsncwhen,md=vmd,cs=vcs,dcd=vdcd)
	return render(request,'edit.html', {'survey':survey,'newPatient':newPatient})

def update(request, patientId):
	newPatient = Patient.objects.get(id=patientId)
	survey = Survey.objects.get(id=patientId)
	survey.dttoday = request.POST['dttoday']
	survey.sncwhen = request.POST['sncwhen']
	survey.md = request.POST['md']
	survey.cs = request.POST['cs']
	survey.dcd = request.POST['dcd']
	survey.save()
	return redirect(f'/tolsys/{survey.id}/addans/')
	# return render(request,'surveypage.html',{'newPatient':newPatient})

# def edit(request, rId):
# 	cuiReg = Registration.objects.get(id=rId)
# 	cuisineClass = CookingClass.objects.filter(regid=rId)
# 	print (cuisineClass)
# 	schedClass = Schedule.objects.filter(regid=rId)
# 	print (schedClass)
# 	checkoutMod = CheckoutInfo.objects.filter(regid=rId)
# 	print (schedClass)
# 	return render(request,'edit.html', {'cuiReg':cuiReg, 'cuisineClass':cuisineClass, 
# 		'schedClass':schedClass, 'checkoutMod':checkoutMod})


def AddAppointment(request, patientId):
	newPatient =  Patient.objects.get(id=patientId)
	return render(request, 'appointment.html', {'appointment': newPatient})

# def App(request):
# 	vkdsession = request.POST['kind']
# 	vtpsession = request.POST['type']
# 	vadate = request.POST['adate']
# 	vatime = request.POST['atime']
# 	Appointment.objects.create(kdsession=vkdsession,tpsession=vtpsession,adate=vadate,atime=vatime)
# 	return render(request, 'appsummary.html')

# def Delete(request, patientId):
# 	newPatient = Patient.objects.get(id=patientId)
# 	newPatient.delete()
# 	return redirect(f'/tolsys/{newPatient.id}/')

def App(request, patientIdd):
	pPatient = Patient.objects.get(id=patientIdd)
	patientid = request.POST.get('patientIdd','')
	vkdsession = request.POST['kind']
	vtpsession = request.POST['type']
	vadate = request.POST['adate']
	vatime = request.POST['atime']
	Appointment.objects.create(patientid=pPatient,kdsession=vkdsession,tpsession=vtpsession,adate=vadate,atime=vatime)
	# return render(request, 'appsummary.html', {'appointment': newPatient})
	return redirect(f'/tolsys/{pPatient.id}/')

# def App(request, patientId):
# 	newPatient = Patient.objects.get(id=patientId)
# 	newPatient = patientId()
# 	if request.method=='POST':
# 		Appointment.objects.create(patientid=newPatient,kdsession = request.POST['kind'],
# 			tpsession = request.POST['type'],adate = request.POST['adate'],atime = request.POST['atime'])
# 		return redirect(f'/tolsys/{newPatient.id}/')
# 	else:
# 		return render(request, 'appsummary.html', {'newPatient': newPatient})

# def Summary(request):
# 	patientdisplay=Patient.objects.all()
# 	appointmentdisplay=Appointment.all()
# 	return render(request,'appsummary.html',{'Patient':patientdisplay,'Appointment':appointmentdisplay})

# def AddAppointment(request, patientId):
# 	newPatient =  Patient.objects.get(id=patientId)
# 	apppointment = Appointment.objects.all()
# 	return render(request, 'appointment/apppointment.html',
# 		{'appointment': apppointment}, {'appointment': newPatient})

# def Summary(request):
# 	# newPatient = Patient.objects.get(id=patientId)
# 	vkdsession = request.POST['kind']
# 	vtpsession = request.POST['type']
# 	vadate = request.POST['adate']
# 	vatime = request.POST['atime']
# 	Appointment.objects.create(kdsession=vkdsession,tpsession=vtpsession,adate=vadate,atime=vatime)
# 	return redirect(f'/tolsys/{newPatient.id}/')




# def Appointment(request, patientId):
# 	newPatient = Patient.objects.get(id=patientId)
# 	if request.method=='POST':
# 		Appointment.objects.create(patientid=newPatient,
# 	kdsession = request.POST['kind'],
# 	tpsession = request.POST['type'],
# 	adate = request.POST['adate'],
# 	atime = request.POST['atime'],)
# 	# return redirect(f'/tolsys/viewlist_url')
# 	return render(request, 'appsummary.html', {'appointment': newPatient})



#From WebDev 1
def TopicPage(request):
	return render(request,'Topics.html')

def Newsroom(request):
	return render(request,'Newsroom.html')

def Findhelp(request):
	return render(request,'FindHelp.html')

def Aboutus(request):
	return render(request,'AboutUs.html')

	