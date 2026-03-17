from django.db import models
from django.forms import ModelForm

# Create your models here.
class YearNumber(models.Model):
    yearNumber = models.IntegerField()
    def __str__(self):
        return str(self.yearNumber)

class BodyStyle(models.Model):
    bodyStyle = models.CharField()
    def __str__(self):
        return str(self.bodyStyle)
    
class DoorNumber(models.Model):
    doorNumber = models.IntegerField()
    def __str__(self):
        return str(self.doorNumber)

class FuelType(models.Model):
    fuelType = models.CharField()
    def __str__(self):
        return str(self.fuelType)

class Year(models.Model):
    year = models.ForeignKey(YearNumber, on_delete=models.CASCADE)

class Body(models.Model):
    body = models.ForeignKey(BodyStyle, on_delete=models.CASCADE)

class Doors(models.Model):
    doors = models.ForeignKey(DoorNumber, on_delete=models.CASCADE)

class Fuel(models.Model):
    fuel = models.ForeignKey(FuelType, on_delete=models.CASCADE)

class YearForm(ModelForm):
    class Meta:
        model = Year
        fields = ['year']

class BodyForm(ModelForm):
    class Meta:
        model = Body
        fields = ['body']

class DoorForm(ModelForm):
    class Meta:
        model = Doors
        fields = ['doors']

class FuelForm(ModelForm):
    class Meta:
        model = Fuel
        fields = ['fuel']