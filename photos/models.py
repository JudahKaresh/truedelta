from django.db import models
from django.forms import ModelForm

# Create your models here.
class FilterTitle(models.Model):
    CHOICES = [
        ('recent','Most Recent Photos'),
        ('popular', 'Most Popular Photos'),
        ('review', 'TrueDelta Review Photos'),
        ('filter','Filter car searches by'),
    ]
    filter_title = models.CharField(max_length=100,choices=CHOICES)
    def __str__(self):
        return self.filter_title

class Filter(models.Model):
    filter = models.ForeignKey(FilterTitle, on_delete=models.CASCADE)

class FilterForm(ModelForm):
    class Meta:
        model = Filter
        fields = ['filter']
