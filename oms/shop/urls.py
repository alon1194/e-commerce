from django.urls import path,include
from .views import HomePageView, ProductDetailView
from django.urls import path
from .views import ProfileView




app_name = "shop"
urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("Product/<int:pk>/", ProductDetailView.as_view(), name="Product"),
    path('profile/<int:pk>/', ProfileView.as_view(), name='profile'),
      
 
 
    
]
