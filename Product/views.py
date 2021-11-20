from django.shortcuts import render


from .models import Product

# Create your views here.

def product(request):
    product=Product.objects.all()
    context={
        'product': product
    }
    return render(request,"Post/products.html",context)
