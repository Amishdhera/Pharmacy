from django.shortcuts import render
from.models import Medicines
# Create your views here.
def home(request):
     med = Medicines.objects.all()
     context ={'med':med}
     


     return render(request,'index.html',context)


