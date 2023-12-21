
from django.http import HttpResponse
import datetime

from django.shortcuts import render
# 1:08:25

def home(request):
    isActive=True
    if request.method=='POST':

        check=request.POST.get('check')
        print(check)
        

    date=datetime.datetime.now()
    
    name="Shivam"
    list_of_programs=[
        'wap to check even or odd',
        'wap to check prime number',
        'wap to print all prime numbers from 1 to 100',
        'wap to print pascals triangle'

    ]
    student={
        "student_name":"Shivam",
        "student_college":"XYZ",
        "student_city":"Hyderabad"

    }
    data={
        "date":date,
        "isActive":isActive,
        "name":name,
        "list_of_programs":list_of_programs,
        "student_data":student


    }

    print("test function")
    return render(request,"home.html",data)
def about(request):
    return render(request,"about.html",{})
def services(request):
    return render(request,"services.html",{})
