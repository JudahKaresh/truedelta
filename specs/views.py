from django.shortcuts import render, redirect
from .models import VehicleForm, CarModel, ReportForm
from .forms import IntlCheck, CompareCheck
from django.http import JsonResponse

def index(request):
    if request.method == 'POST':
        reportForm = ReportForm(request.POST)
        intlCheck = IntlCheck(request.POST)
        compareCheck = CompareCheck(request.POST)
        formOne = VehicleForm(request.POST)
        formTwo = VehicleForm(request.POST)
        if formOne.is_valid() and formTwo.is_valid() and reportForm.is_valid() and intlCheck.is_valid() and compareCheck.is_valid():
            # Save the article to the database
            vehicleOne = formOne.save()
            vehicleTwo = formTwo.save()
            checkOne = intlCheck.save()
            checkTwo = compareCheck.save()
            report = reportForm.save()
            return redirect('success')
    else:
        formOne = VehicleForm()
        formTwo = VehicleForm()
        reportForm = ReportForm()
        intlCheck = IntlCheck()
        compareCheck = CompareCheck()
    
    return render(request, 'specs/index.html', {'formOne': formOne, 'formTwo': formTwo, 'reportForm': reportForm, 'intlCheck': intlCheck, 'compareCheck': compareCheck})

def load_models(request):
    brand_id = request.GET.get('brand_id')
    models = CarModel.objects.filter(brand_id = brand_id).values('id','brand_title')
    return JsonResponse(list(models), safe = False)
