from django.contrib import admin
from . models import Medicines
# Register your models here.

class MedAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price',)

admin.site.register(Medicines, MedAdmin)