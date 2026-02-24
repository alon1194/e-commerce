from django.views.generic import View
from django.shortcuts import render
class HomePageView(View):
    def get(self, request):
        return render(request, 'shop/home.html')
def hi(request):
     return render(request, "shop/hi.html") 
def Product(request):
     return render(request, "shop/Product.html") 