from django.forms import EmailField
from django.shortcuts import render
from django.http import HttpResponseRedirect
import requests
import json
# Create your views here.
def home(request):
    #pull data from third party rest api
    response = requests.get('http://127.0.0.1:8000/api/employeeapi',verify=False)
    #convert reponse data into json
    users = response.json()
    #print(users)
    return render(request, "home.html", {'users': users})
    pass

def add(request):
    if request.method=="POST":
        Name = request.POST.get("name")
        Email = request.POST.get("email")
        Designation = request.POST.get("dsg")
        Salary = request.POST.get("salary")
        City = request.POST.get("city")
        State = request.POST.get("state")
        data={
            "name": Name,
            "email": Email,
            "designation": Designation,
            "salary": Salary,
            "city": City,
            "state": State
        }
        r = requests.post("http://127.0.0.1:8000/api/employeeapi/", json=data, verify=True)
        return HttpResponseRedirect("/")
    return render(request, "add.html")


def update(request,email):
    data1={
        "email":email
    }
    response = requests.get("http://127.0.0.1:8000/api/employeeapi/", json=data1, verify=True)
    users = response.json()
    # print(users)
    if request.method=="POST":
        Name = request.POST.get("name")
        # Email = request.POST.get(email)
        Designation = request.POST.get("dsg")
        Salary = request.POST.get("salary")
        City = request.POST.get("city")
        State = request.POST.get("state")
        data={
            "name": Name,
            "email": email,
            "designation": Designation,
            "salary": Salary,
            "city": City,
            "state": State
        }

        r = requests.put("http://127.0.0.1:8000/api/employeeapi/", json=data, verify=True)
        return HttpResponseRedirect("/")
    return render(request, "update.html",{'users': users})


def delete(request,email):
    data1={
        "email":email
    }
    response = requests.delete("http://127.0.0.1:8000/api/employeeapi/", json=data1, verify=True)
    return HttpResponseRedirect("/")






