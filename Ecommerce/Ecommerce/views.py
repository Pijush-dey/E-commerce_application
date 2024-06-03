from django.shortcuts import render

def homepage(request):
    return render(request,"templates/tt1.html")

def contactpage(request):
    return render(request,"templates/contact.html")

def aboutpage(request):
    return render(request,"templates/about.html")

def wishlistpage(request):
    return render(request,"templates/wishlist.html")

def cartpage(request):
    return render(request,"templates/cart.html")

def accountpage(request):
    return render(request,"templates/account.html")