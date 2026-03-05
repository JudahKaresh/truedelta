from django.shortcuts import render, redirect
from django.http import JsonResponse

#from .models import Category
# Create your views here.

def index(request):

    return render(request, 'reviews/index.html')

