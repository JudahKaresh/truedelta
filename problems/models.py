from django.db import models
from django.forms import ModelForm

# Create your models here.
class Year(models.Model):
    year = models.IntegerField()
    def __str__(self):
        return str(self.year)

class CategoryTitle(models.Model):
    category_title = models.CharField(max_length=100)
    def __str__(self):
        return self.category_title

class Make(models.Model):
    make_title = models.CharField(max_length = 50)
    year = models.ForeignKey(Year, on_delete=models.CASCADE)
    def __str__(self):
        return self.make_title

class Problem(models.Model):
    problem_title = models.CharField(max_length=100)
    year = models.ForeignKey(Year, on_delete=models.CASCADE)
    category_title = models.ForeignKey(CategoryTitle, on_delete=models.CASCADE)
    make = models.ForeignKey(Make,on_delete=models.CASCADE)
    def __str__(self):
        return self.problem_title

class Category(models.Model):
    year = models.ForeignKey(Year, on_delete=models.CASCADE)
    category_title = models.ForeignKey(CategoryTitle, on_delete=models.CASCADE)
    make = models.ForeignKey('Make',on_delete=models.CASCADE)

class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = ['category_title','year','make']
    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)
        self.fields['make'].queryset = Make.objects.none()

        # If editing an existing instance, populate makes for that year
        if self.instance.pk:
            self.fields['make'].queryset = Make.objects.filter(
                year=self.instance.year
            )
        # If form data exists (submission), filter makes by selected year
        elif 'year' in self.data:
            try:
                year_id = int(self.data.get('year'))
                self.fields['make'].queryset = Make.objects.filter(
                    year_id=year_id
                )
            except (ValueError, TypeError):
                pass
