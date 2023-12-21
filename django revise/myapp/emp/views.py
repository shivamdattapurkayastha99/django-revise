from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import *

# Create your views here.
def emp_home(request):
    emps=Emp.objects.all()
    
    return render(request,"emp/home.html",{
        'emps':emps
    })
def add_emp(request):
    if request.method=="POST":
        emp_name=request.POST.get("name")
        emp_id=request.POST.get("id")
        emp_phone=request.POST.get("phone")
        emp_address=request.POST.get("address")
        emp_working=request.POST.get("working")
        emp_department=request.POST.get("department")
        e=Emp()
        e.name=emp_name
        e.emp_id=emp_id
        e.phone=emp_phone
        e.address=emp_address
        # e.working=emp_working
        e.department=emp_department
        if emp_working is None:
            e.working=False
        else:
            e.working=True
        e.save()



        return redirect("/emp/home/")
    return render(request,"emp/add_emp.html",{})

