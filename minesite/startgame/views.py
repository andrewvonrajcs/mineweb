from django.shortcuts import render
from django.http import HttpResponse
from . import models

def status(request):
    model = models.MyModelName()
    return HttpResponse(str(model))
