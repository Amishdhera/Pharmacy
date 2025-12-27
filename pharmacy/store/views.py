from django.shortcuts import render,  redirect, get_object_or_404
from.models import Medicines 
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
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


def update(request, pk):
     med = get_object_or_404(Medicines, pk=pk)  

     if request.method=='POST':
          name=request.POST.get('m_name')
          price=request.POST.get('m_price')
          image=request.POST.get('m_img')

          if image:
               if med.image:
                    if os.path.join(med.image.path):
                         os.remove(med.image.path)

               med.image=image
          med.name=name
          med.price=price
          med.save()
          return redirect('home')
     
     context={'med':med}
     return render(request,'update.html',context)

              



def delete(request, pk):  
    
    med = get_object_or_404(Medicines, pk=pk)  
   
    med.delete()

    
    return redirect('home')

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
        else:
            print(form.errors)  # Print form errors for debugging
    else:
        form = UserCreationForm()

    return render(request, 'registration/signup.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})