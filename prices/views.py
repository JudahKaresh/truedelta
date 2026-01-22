from django.shortcuts import render, redirect
from .models import VehicleForm, CarModel
from django.http import JsonResponse

#from .models import Category
# Create your views here.

#def index(request):
#    form = MyForm()
#    return render(request, "problems/index.html",{'form': form})

def index(request):
    if request.method == 'POST':
        formOne = VehicleForm(request.POST)
        formTwo = VehicleForm(request.POST)
        if formOne.is_valid() and formTwo.is_valid():
            # Save the article to the database
            vehicleOne = formOne.save()
            vehicleTwo = formTwo.save()
            return redirect('success')
    else:
        formOne = VehicleForm()
        formTwo = VehicleForm()
    
    return render(request, 'prices/index.html', {'formOne': formOne, 'formTwo': formTwo})

def load_models(request):
    brand_id = request.GET.get('brand_id')
    models = CarModel.objects.filter(brand_id = brand_id).values('id','brand_title')
    return JsonResponse(list(models), safe = False)
