
from datetime import datetime
from django.shortcuts import render, HttpResponse
from . models import Employee, Role, Department
# Create your views here.

def login(request):
    return render(request, 'login.html')

def signup(request):
    return render(request, 'signup.html')


def index(request):
    return render(request, 'index.html')

def all(request):
    emps = Employee.objects.all()
    context = {
        'emps': emps
    }
    return render(request, 'view.html', context)

def add(request):
    if request.method== "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        salary = int(request.POST['salary'])
        bonus = int(request.POST['bonus'])
        phone = int(request.POST['phone'])
        dept = int(request.POST['dept'])
        role = int(request.POST['role'])
        new_emp = Employee(first_name=first_name,last_name=last_name,salary=salary,bonus=bonus,dept_id=dept,role_id=role,phone=phone,hire_date = datetime.now())
        new_emp.save()

        return HttpResponse('Employee Added successfully')
    elif request.method == "GET":
        return render(request, "add.html")
    else:
        return HttpResponse("An exception occured! Employee has not been added!")

    

def remove(request, emp_id = 0):
    if emp_id:
        try:
            emp_delete = Employee.objects.get(id = emp_id)
            emp_delete.delete()
            return HttpResponse("Delete successful!")
        except:
            return HttpResponse("Oops! Something gone wrong.")
    emps = Employee.objects.all()
    context = {
        'emps' : emps
    }
    return render(request, 'remove.html', context)

def filter(request):
    return render(request, 'filter.html')