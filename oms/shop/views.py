from django.views.generic import View
from django.shortcuts import render
from django.views.generic import TemplateView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Custumer, Product
from django.contrib.auth.models import User
from django.http import HttpResponseForbidden
from django.shortcuts import redirect





class HomePageView(TemplateView):
    template_name = "shop/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["featured_products"] = Product.objects.filter(featured=True)[:8]
        context["new_arrivals"] = Product.objects.order_by("-created_at")[:8]

        return context


    

class ProductDetailView(DetailView):
     model = Product
     template_name = "shop/Product.html"
    
     def get_context_data(self, **kwargs):
         context = super().get_context_data(**kwargs)
         return context



class ProfileView(LoginRequiredMixin, TemplateView):

    template_name = "shop/profile.html"

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        if self.request.user.is_staff or self.request.user.is_superuser:
            raise HttpResponseForbidden("Admins cannot access this page")

        profile, created = Custumer.objects.get_or_create(
            user=self.request.user
        )

        context["profile"] = profile

        return context
    


    def post(self, request, *args, **kwargs):

        profile, created = Custumer.objects.get_or_create(
            user=request.user
        )

        if request.FILES.get("image"):
            profile.Image = request.FILES["image"]
            profile.save()
        
    # username update
        username = request.POST.get("username")
        if username:
            request.user.username = username
            request.user.save()
    #user phone number
        phone_number = request.POST.get("phone_number")
        if phone_number: 
            profile.phone_number = phone_number
            profile.save()
        return redirect("shop:profile", pk=self.request.user.id)
