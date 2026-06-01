from django.urls import path 
from .views import CustomLoginView,  RegisterView, CustomPasswordResetView, CustomPasswordResetConfirmView; 
from django.contrib.auth import views as auth_views


app_name = "userauth"

urlpatterns = [
   path("", CustomLoginView.as_view(), name="login"),
   path("register/", RegisterView.as_view(), name = "register"),
     path('password-reset/', CustomPasswordResetView.as_view(), name='password_reset'),
    path('password-reset/done/',
         auth_views.PasswordResetDoneView.as_view(
             template_name='auth/password_reset_done.html'
         ), 
         name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',
         CustomPasswordResetConfirmView.as_view(),
         name='password_reset_confirm'),
    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(
             template_name='auth/password_reset_complete.html'
         ),
         name='password_reset_complete'),
]