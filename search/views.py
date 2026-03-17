from django.shortcuts import render, redirect
from .models import YearForm, BodyForm, FuelForm, DoorForm;
from django.http import JsonResponse

def index(request):
    if request.method == 'POST':
        yearForm = YearForm(request.POST)
        fuelForm = FuelForm(request.POST)
        doorForm = DoorForm(request.POST)
        bodyForm = BodyForm(request.POST)
        if yearForm.is_valid() and bodyForm.is_valid() and doorForm.is_valid() and fuelForm.is_valid():
            # Save the article to the database
            year = yearForm.save()
            body = bodyForm.save()
            fuel = fuelForm.save()
            door = doorForm.save()
            return redirect('success', {'yearForm': yearForm, 'bodyForm': bodyForm, 'fuelForm': fuelForm, 'doorForm': doorForm})
    else:
        yearForm = YearForm()
        bodyForm = BodyForm()
        doorForm = DoorForm()
        fuelForm = FuelForm()

    return render(request, 'search/index.html',{'yearForm': yearForm, 'bodyForm': bodyForm, 'fuelForm': fuelForm, 'doorForm': doorForm})

