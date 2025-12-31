from django.db import models 
from django.contrib.auth.models import User

# Create your models here.
class Medicines(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    image = models.ImageField(upload_to='images/', null=True)

    def __str__(self):
        return self.name


class Order(models.Model):
    customer = models.ForeignKey(User,on_delete=models.SET_NULL,null=True,blank=True)
    data =models.DateTimeField(auto_now_add=True)
    status= models.BooleanField(default=False)
    transaction_id =models.CharField(max_length=100)

    def __str__(self):
        return str(self.id)
    @property
    def get_cart_total(self):
        orderItems= self.orderitem_set.all()
        total=sum([item.get_total for item in orderItems])
        return total
    @property
    def get_cart_item(self):
        orderItems= self.orderitem_set.all()
        total=sum([item.quantityn for item in orderItems])
        return total
    


class OrderItem(models.Model):
    order = models.ForeignKey(Order,on_delete=models.SET_NULL,null=True,blank=True)
    product = models.ForeignKey(Medicines, on_delete=models.SET_NULL,null=True,blank=True)
    quantity= models.IntegerField(default=0) 
    date= models.DateTimeField(auto_now_add=True)

    @property
    def get_total(self):
        total = self.quantity = self.product.price
        return total     

            
