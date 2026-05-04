from django.views.generic import View
from django.shortcuts import render
from django.views.generic import DetailView
from django.contrib.auth.models import User
class HomePageView(View):
    def get(self, request):
        return render(request, 'shop/home.html')
class ProfileView(DetailView):
    model = User
    template_name = "shop/profile.html"
    context_object_name = "user_profile" 
def Product(request):
     return render(request, "shop/Product.html") 