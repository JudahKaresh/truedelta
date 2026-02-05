from django.shortcuts import render, redirect
from .models import YearForm;
from django.http import JsonResponse

#from .models import Category
# Create your views here.

def index(request):
    if request.method == 'POST':
        yearForm = YearForm(request.POST)
        if yearForm.is_valid():
            # Save the article to the database
            year = yearForm.save()
            return redirect('success', {'yearForm': yearForm})
    else:
        yearForm = YearForm()

    return render(request, 'search/index.html',{'yearForm': yearForm})

