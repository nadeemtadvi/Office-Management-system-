from django.shortcuts import render,HttpResponse
from django.db.models import Q
from .models import *
from datetime import datetime

def index(request):
    return render(request,'index.html')

def all_emp(request):
    emp=Employee.objects.all()
    return render(request,'all_emp.html',{'emp':emp})

def add_emp(request):
    if request.method=="POST":
        dept=int(request.POST['dept'])
        role=int(request.POST['role'])
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        salary=int(request.POST['salary'])
        bonus=int(request.POST['bonus'])
        phone=int(request.POST['phone'])
        new_emp=Employee(
            dept_id=dept,
            role_id=role,
            first_name=first_name,
            last_name=last_name,
            salary=salary,
            bonus=bonus,
            phone=phone,
            hire_date=datetime.now()
        )
        new_emp.save()
        return HttpResponse('Employe Added Successfully')
    elif request.method=="GET": 
        return render(request,'add_emp.html')
    else:
        return HttpResponse("Exception Occured : Employee not added ")

def remove_emp(request,emp_id=0):
    if emp_id:
        try:
           emp_remove=Employee.objects.get(id=emp_id)
           emp_remove.delete()
           return HttpResponse("Emp Remove")
        except:
           return HttpResponse("Invalid emp Id")
    emp=Employee.objects.all()        
           
    return render(request,'remove_emp.html',{'emp':emp})

def filter_emp(request):
    if request.method=="POST":
        name=request.POST['name']
        dept=request.POST['dept']
        role=request.POST['role']
        emp=Employee.objects.all()
        if name:
            emp=emp.filter(Q(first_name__icontains=name) | Q(last_name__icontains=name))
        if dept:
            emp=emp.filter(dept__name__icontains=dept)    
        if role:
            emp=emp.filter(role__name__icontains=role)    
        context={
            'emp':emp
        }
        return render(request,'all_emp.html',context)
    elif request.method=="GET":
        return render(request,'filter_emp.html')
    else:  
        return HttpResponse('invalid search')



# Create your views here.
