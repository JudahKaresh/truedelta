from django.contrib import admin
from .models import Year,Category,CategoryTitle,Make, Problem

# Register your models here.
admin.site.register(Category)
admin.site.register(CategoryTitle)
admin.site.register(Year)
admin.site.register(Make)
admin.site.register(Problem)