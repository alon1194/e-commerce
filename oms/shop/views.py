from django.views.generic import View
from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Custumer
from django.contrib.auth.models import User
from django.http import HttpResponseForbidden
from django.shortcuts import redirect



class HomePageView(View):
    def get(self, request):
        return render(request, 'shop/home.html')
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
def Product(request):
     return render(request, "shop/profile.html") 