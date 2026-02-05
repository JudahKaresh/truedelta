from django.db import models
from django.forms import ModelForm

# Create your models here.
class YearNumber(models.Model):
    yearNumber = models.IntegerField()
    def __str__(self):
        return str(self.yearNumber)

class Year(models.Model):
    year = models.ForeignKey(YearNumber, on_delete=models.CASCADE)

class YearForm(ModelForm):
    class Meta:
        model = Year
        fields = ['year']