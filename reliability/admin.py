from django.contrib import admin
from .models import Brand,CarModel,Report,Vehicle

# Register your models here.
admin.site.register(Brand)
admin.site.register(CarModel)
admin.site.register(Report)
admin.site.register(Vehicle)