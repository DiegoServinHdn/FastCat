from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics

from .models import Workspace
from .serialazers import WorkspaceSerializer

# Create your views here.
def main(request):
    return HttpResponse('Hello')

class WorkspaceView(generics.ListAPIView):
    queryset = Workspace.objects.all()
    serializer_class = WorkspaceSerializer