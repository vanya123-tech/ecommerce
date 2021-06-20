from django.shortcuts import render
from django.http import HttpResponse
from math import ceil
#from .models import Product
from . models import Product
# Create your views here.
def index(request):
    # products= Product.objects.all()
    # print(products)
    # n= len(products)
    # nSlides= n//4 + ceil((n/4) + (n//4))
    # allProds=[[products,range(1,nSlides),nSlides],
    # [products,range(1,nSlides),nSlides]]
    allProds=[]
    catprods=Product.objects.values('category')
    cats={item['category']for item in catprods}
    for cat in cats:
        prod=Product.objects.filter(category=cat)
        n= len(prod)
        nSlides= n//4 + ceil((n/4) + (n//4))
        allProds.append([prod,range(1,nSlides),nSlides])
    params={'allProds':allProds}
    #params={'no_of_slides':nSlides, 'range':range(1,nSlides), 'product': products}
    return render(request,"shop/index.html", params)
    #return render(request,"shop/about.html")
def about(request):
    return render(request,"shop/about.html")
def contact(request):
    return render(request,"shop/contact.html")
def tracker(request):
    return render(request,"shop/tracker.html")
def search(request):
    return HttpResponse("we are at search")
def products(request,myid):
    product=Product.objects.filter(id=myid)
    return render(request,"shop/prodview.html",{'product':product[0]})
def checkout(request):
    return HttpResponse("we are at checkout")

