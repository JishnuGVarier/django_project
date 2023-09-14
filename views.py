from django.shortcuts import render,redirect
from hospitalapp.models import Doctor
# Create your views here.
def loginPageView(request):
    return render(request,'login.html',{})

def logincheckView(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        if username=='admin' and password=='123':
            print(username)
            print(password)
            return redirect('admin')
        else:
            return redirect('login')
        
def adminPageView(request):
    return render(request,'admin.html',{})

def docPageView(request):
    return render(request,'adddoc.html',{})

def savedocView(request):
    if request.method == 'POST':
        #Retrieve form data and adding doctor details
        name=request.POST['doctorName']
        spec=request.POST['doctorSpecialization']
        number=request.POST['doctorNumber']

        print("Name: ",name)
        print("Spec: ",spec)
        print("number: ",number)

        doctor=Doctor(name=name,spec=spec,number=number)
        doctor.save()
        return redirect('adddoc')
    
def patPageView(request):
    return render(request,'addpat.html',{})

def savepatView(request):
    if request.method == 'POST':
        #Retrieve form data and adding doctor details
        name=request.POST['patientName']
        address=request.POST['patientAddress']
        number=request.POST['patientNumber']
        patid=request.POST['patientid']


        print("Name: ",name)
        print("Spec: ",spec)
        print("number: ",number)

        doctor=Doctor(name=name,spec=spec,number=number)
        doctor.save()
        return redirect('adddoc')