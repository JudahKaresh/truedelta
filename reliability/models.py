from django.db import models
from django.forms import ModelForm

# Create your models here.

class Brand(models.Model):
    brand_name = models.CharField(max_length=50)
    def __str__(self):
        return self.brand_name
    
class CarModel(models.Model):
    model_title = models.CharField(max_length = 50)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    def __str__(self):
        return self.model_title
    
class ReportTitle(models.Model):
    report_title = models.CharField(max_length=100)
    def __str__(self):
        return self.report_title

class Report(models.Model):
    report = models.ForeignKey(ReportTitle, on_delete=models.CASCADE)

class Vehicle(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    model = models.ForeignKey('CarModel', on_delete=models.CASCADE)

class ReportForm(ModelForm):
    class Meta:
        model = Report
        fields = ['report']

class VehicleForm(ModelForm):
    class Meta:
        model = Vehicle
        fields = ['brand','model']
    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)
        self.fields['model'].queryset = CarModel.objects.none()

        # If editing an existing instance, populate models for that brand
        if self.instance.pk:
            self.fields['model'].queryset = CarModel.objects.filter(
                brand=self.instance.brand
            )
        # If form data exists (submission), filter models by selected brand
        elif 'brand' in self.data:
            try:
                brand_id = int(self.data.get('brand'))
                self.fields['model'].queryset = CarModel.objects.filter(
                    brand_id=brand_id
                )
            except (ValueError, TypeError):
                pass