from django.contrib import admin
from . models import *
# Register your models here.

class MedAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price',)

admin.site.register(Medicines, MedAdmin)
admin.site.register(Order)
admin.site.register(OrderItem)
