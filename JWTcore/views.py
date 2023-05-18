from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes

from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
# Create your views here.


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def api_home_page(request):
    return Response("This is the home page")


