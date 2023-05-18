from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes

from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

from .forms import StudentForm
from django.http import HttpResponse
# Create your views here.


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def api_home_page(request):
    return Response("This is the home page")


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
    






