from django.shortcuts import render, redirect
from .models import CategoryForm, Make
from django.http import JsonResponse

#from .models import Category
# Create your views here.

#def index(request):
#    form = MyForm()
#    return render(request, "problems/index.html",{'form': form})

def index(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            # Save the article to the database
            category = form.save()
            return redirect('success')
    else:
        form = CategoryForm()
    
    return render(request, 'problems/index.html', {'form': form})

def load_makes(request):
    year_id = request.GET.get('year_id')
    makes = Make.objects.filter(year_id = year_id).values('id','make_title')
    return JsonResponse(list(makes), safe = False)
