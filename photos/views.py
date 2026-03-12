from django.shortcuts import render, redirect
from .models import FilterForm
from django.http import JsonResponse

#from .models import Category
# Create your views here.

def index(request):
    if request.method == 'POST':
        filterForm = FilterForm(request.POST)
        if filterForm.is_valid():
            # Save the article to the database
            filter = filterForm.save()
            return redirect('success')
    else:
        filterForm = FilterForm()
    
    return render(request, 'photos/index.html', {'filterForm': filterForm})

