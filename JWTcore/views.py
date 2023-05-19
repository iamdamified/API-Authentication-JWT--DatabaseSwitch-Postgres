from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes

from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

from .forms import StudentForm
from django.http import HttpResponse
from .models import Student
# Create your views here.

# This first view is used to define the content of page which is to be displayed in API testing apps(JSON and POSTMAN) and using JWT Authentication
@api_view(["GET"])
@permission_classes([IsAuthenticated])
def api_home_page(request):
    return Response("This is the home page")

# This would be used if class or generic method is used in the views.py to display the view
# class api_home_page(APIView)
#      permission_classes = [IsAuthenticated]


def create_student(request):
    if request.method == "GET":
        form = StudentForm()
        context = {
            'form': form
        }
        return render(request, 'JWTcore/create_student.html', context)
    

    elif request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("your data has been saved")
    return render(request, 'JWTcore/create_student.html')


def all_student(request):
        students = Student.objects.all()
        context = {
            'student': students
        }
        return render(request, 'JWTcore/all_student.html', context)

def new_registration(request):
     if request.method == "POST":
          name = request.POST["name"]
          email = request.POST["email"]
          class_code = request.POST["class_code"]
          course = request.POST["course"]

          Student.objects.create(name=name, email=email, class_code=class_code, course=course)

          return HttpResponse("Nice one")
     
     elif request.method == "GET":
          return render(request, "JWTcore/frontendform.html")

          
    
    






