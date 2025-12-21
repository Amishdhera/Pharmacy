from django.shortcuts import render, redirect
from.models import Medicines
# Create your views here.
def home(request):
     med = Medicines.objects.all()
     context ={'med':med}
     


     return render(request,'index.html',context)

def about(request):
     return render(request,'about.html')

def contact(request):
     return render(request,'contact.html')
def addtocart(request):
     return render(request,'addtocart.html')

def product(request):

     if request.method=='POST':
          name=request.POST.get('med_name')
          price=request.POST.get('med_price')
          # img=request.POST.get('med_name')

          Medicines.objects.create(
               name=name,
               price=price,
               image = request.FILES.get('med_img')
          )

          return redirect('home')


     return render(request,'add_product.html')

