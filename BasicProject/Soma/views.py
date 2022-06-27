from django.shortcuts import render

from django.http import HttpResponse

def soma(request):
    return HttpResponse("Soma!")

