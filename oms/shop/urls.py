from django.urls import path,include
from .views import HomePageView, hi, Product
app_name = "shop"
urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("Product/", Product, name="Product"),
      path("hi/", hi, name="hi"),
      
 
 
    
]