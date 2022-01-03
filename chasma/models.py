from functools import partialmethod
from django.db import models
from django.contrib.auth.models import User
from django.db.models.expressions import F

# Create your models here.
CATAGORY = (
    ('Sunglass' ,'Sunglass') , ('Frame',"Frame") , ('Eyelens','Eyelens') , ('Male','Male'),('Female','Female')
)
class Product(models.Model):
    name = models.CharField(max_length= 100)
    detail = models.CharField(max_length=500)
    price = models.PositiveIntegerField()
    discount_price = models.PositiveIntegerField()
    image = models.ImageField(upload_to='static/uploads')
    image2 = models.ImageField(upload_to='static/uploads')
    image3 = models.ImageField(upload_to='static/uploads')
    catagory = models.CharField(choices=CATAGORY, max_length=12)

    @property
    def discount_precentage(self):
        discount_precent = (self.price - self.discount_price)/(self.price)*(100)
        return discount_precent

class Cart(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    @property
    def total_cost(self):
        return self.quantity * self.product.price

STATUS_CHOOISE = (('p','pending'),('a','accepted'),('c','cancle'),('d','delevered'),('e','remove_status'))
class Order(models.Model):
    user =models.ForeignKey(User , on_delete=models.CASCADE)
    product = models.ForeignKey(Product , on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    order_at  =models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    email = models.EmailField(max_length=50)
    phone = models.IntegerField()
    status = models.CharField(max_length=5 , choices=STATUS_CHOOISE , default='p')

Like_Chooise = (('Like',"Like"),('Unlike','Unlike'))
