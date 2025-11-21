from django.shortcuts import render, redirect
from .models import Medicine

def home(request):
    if request.method == "POST":
        # Form se data lena
        name = request.POST.get('name')
        price = request.POST.get('price')
        qty = request.POST.get('qty')
        
        # Database mein save karna
        Medicine.objects.create(name=name, price=price, quantity=qty)
        return redirect('home')

    # Data dikhane ke liye fetch karna
    medicines = Medicine.objects.all()
    return render(request, 'index.html', {'medicines': medicines})