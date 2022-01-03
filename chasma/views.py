from django.core import paginator
from django.db.models.deletion import PROTECT
from django.http import request
from django.http.response import JsonResponse
from django.shortcuts import render, redirect
from .models import Cart, Order, Product
from django.conf import settings
from django.core.mail import send_mail
from django.db.models import Q
from django.template.loader import render_to_string
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

# Create your views here.

# home page
def index(request):
    try:
        cart_total = Cart.objects.filter(user=request.user).count()
        sunglass = Product.objects.filter(catagory='Sunglass')[0:4]
        frame = Product.objects.filter(catagory='Frame')
        lens = Product.objects.filter(catagory='Eyelens')
        male = Product.objects.filter(catagory='Male')
        female = Product.objects.filter(catagory='Female')
        discount_percent = Product.discount_precentage
        context = {
            'sunglass':sunglass, 'frame':frame, 'lens':lens, 'male':male,'female':female, 'discount_percent':discount_percent,'carttotal':cart_total
        }
        return render(request, 'index.html',context)
    except:
        sunglass = Product.objects.filter(catagory='Sunglass')[0:4]
        frame = Product.objects.filter(catagory='Frame')
        lens = Product.objects.filter(catagory='Eyelens')
        male = Product.objects.filter(catagory='Male')
        female = Product.objects.filter(catagory='Female')
        discount_percent = Product.discount_precentage
        context = {
            'sunglass':sunglass, 'frame':frame, 'lens':lens, 'male':male,'female':female, 'discount_percent':discount_percent
        }
        return render(request, 'index.html',context)

# product detail
def detail(request, id):
    try:
        cart_total = Cart.objects.filter(user=request.user).count()
        product = Product.objects.get(id=id)
        sunglass = Product.objects.filter(catagory='Sunglass')
        frame = Product.objects.filter(catagory='Frame')
        lens = Product.objects.filter(catagory='Eyelens')
        male = Product.objects.filter(catagory='Male')
        female = Product.objects.filter(catagory='Female')
        # 
        item_in_cart = False
        item_in_cart = Cart.objects.filter(Q(product = product.id) & Q(user=request.user)).exists()
        context = {'prod':product,'sunglass':sunglass, 'frame':frame, 'lens':lens, 'male':male,'female':female,'carttotal':cart_total,'item_in_cart':item_in_cart}
        return render(request, 'detail.html', context)
    except:
        product = Product.objects.get(id=id)
        sunglass = Product.objects.filter(catagory='Sunglass')
        frame = Product.objects.filter(catagory='Frame')
        lens = Product.objects.filter(catagory='Eyelens')
        male = Product.objects.filter(catagory='Male')
        female = Product.objects.filter(catagory='Female')
        context = {'prod':product,'sunglass':sunglass, 'frame':frame, 'lens':lens, 'male':male,'female':female}
        return render(request, 'detail.html', context)

# contact us page 
def contact(request):
    try:
        user = request.user
        cart_total = Cart.objects.filter(user=user).count()
        if request.method == "POST":
            name = request.POST['name']
            phone = request.POST['phone']
            email = request.POST['email']
            message = request.POST['message']
            # contact = ContactFOrm(name=name,phone=phone,email=email,message=message)
            # contact.save()
            send_mail(name,message,settings.EMAIL_HOST_USER,[email],fail_silently=False)
        return render(request,'contact.html',{'carttotal':cart_total})
    except:
        user = request.user
        if request.method == "POST":
            name = request.POST['name']
            phone = request.POST['phone']
            email = request.POST['email']
            message = request.POST['message']
            # contact = ContactFOrm(name=name,phone=phone,email=email,message=message)
            # contact.save()
            send_mail(name,message,settings.EMAIL_HOST_USER,[email],fail_silently=False)
        return render(request,'contact.html')

# search the product
def searchProduct(request):
    try:
        cart_total = Cart.objects.filter(user=request.user).count()
        if request.method =='POST':
            search = request.POST.get('search')
            product = Product.objects.filter(name__icontains=search)
            context = {
                'search':search,
                'product':product,
                'carttotal':cart_total
            }
            return render(request,'search.html',context)
    except:
        if request.method =='POST':
            search = request.POST.get('search')
            product = Product.objects.filter(name__icontains=search)
        context = {
            'search':search,
            'product':product,
        }
        return render(request,'search.html',context)

# add the product to the cart
def addtocart(request):
    user = request.user
    prod_id = request.GET.get('product_id')
    product = Product.objects.get(id=prod_id)
    Cart.objects.create(user=user, product=product)
    return redirect('/detail/'+str(product.id)+'/')

# update the cart 
def updateCart(request):
    if request.method =='GET':
        prod_id= request.GET.get('product_id')
        is_cart = Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
        # increase the quantity of the cart 
        if is_cart:
            is_cart.quantity +=1 
            is_cart.save()

        # total cost of the cart 
        total_cost = 0.0
        cart_product = [p for p in Cart.objects.all() if p.user == request.user]
        if cart_product:
            for p in cart_product:
                sum = ( p.quantity * p.product.price )
                total_cost += sum

        data = {'totalcost':total_cost , 'quantity':is_cart.quantity}
        return JsonResponse(data)

# decrease the cart 
def decreaseCart(request):
    if request.method =='GET':
        prod_id = request.GET.get('product_id')
        product_in_cart = Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
        if product_in_cart:
            product_in_cart.quantity -= 1 
            product_in_cart.save()
            if product_in_cart.quantity < 1:
                product_in_cart.delete()

        total_cost = 0.0
        cart_product = [p for p in Cart.objects.all() if p.user == request.user]
        if cart_product:
            for p in cart_product:
                sum  = (p.quantity* p.product.price)
                total_cost += sum
        data = {'totalcost':total_cost , 'quantity':product_in_cart.quantity}
        return JsonResponse(data)

def reomveCart(request):
    if request.method =='GET':
        prod_id = request.GET.get('product_id')
        a = Cart.objects.get(product=prod_id)
        product_in_cart = Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
        product_in_cart.delete()
        # remove price 
        total_cost = 0.0
        cart_product = [p for p in Cart.objects.all() if p.user == request.user]
        if cart_product:
            for p in cart_product:
                sum  = (p.quantity* p.product.price)
                total_cost += sum
        data = {'totalcost':total_cost,'cart':a}
        # html  = render_to_string('deletecart.html',data)
        return JsonResponse({'success':data})

        
# show the products in cart
def cart(request):
    cart_total = Cart.objects.filter(user=request.user).count()
    cart = Cart.objects.filter(user=request.user)
    # total cost of the cart 
    total_cost = 0.0
    cart_product = [p for p in Cart.objects.all() if p.user == request.user]

    if cart_product:
        for p in cart_product:
            sum = ( p.quantity * p.product.price )
            total_cost += sum
    data = {
        'cart':cart,
        'totalcost':total_cost,
        'carttotal':cart_total
    }
    return render(request,'cart.html',data)

def order(request):
    cart_total = Cart.objects.filter(user=request.user).count()
    cart = Cart.objects.filter(user=request.user)
    total_cost = 0.0
    cart_product = [p for p in Cart.objects.all() if p.user == request.user]
    if cart_product:
        for p in cart_product:
            sum = ( p.quantity * p.product.price )
            total_cost += sum
    return render(request, 'payment.html',{'cart':cart,'carttotal':cart_total,'totalcost':total_cost})

def payment(request):
    cart = Cart.objects.filter(user=request.user)
    if request.method=='POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        address = request.POST.get('address')
        for c in cart:
            Order.objects.create(user=request.user, product = c.product, quantity= c.quantity,name=name, address=address,phone=phone,email=email).save()
            c.delete()
            send_mail("hello",'Your order has been placed and will be delevered within 7 days',settings.EMAIL_HOST_USER,[email],fail_silently=False)
        return JsonResponse({'success':'success'})

def sunglass(request):
    sunglass = Product.objects.filter(catagory='Sunglass')
    p = Paginator(Product.objects.all(),15)
    page = request.GET.get('page')
    pagination = p.get_page(page)
    numofpage = 'a'* pagination.paginator.num_pages
    return render(request, 'sunglass.html',{'sunglass':sunglass,'pagination':pagination,'numofpage':numofpage})
    
def frame(request):
    return render(request, 'sunglass.html')
def lens(request):
    return render(request, 'sunglass.htmsl')
