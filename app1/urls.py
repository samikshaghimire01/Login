from django.urls import path
from . import views  # Import views from the current app

urlpatterns = [
    path('', views.SignupPage, name='SignupPage'),  # Signup page
    path('login/', views.LoginPage, name='login'),   # Login page
    path('home/', views.HomePage, name='home'),      # Home page
    path('logout/', views.LogoutPage, name='logout') # Logout page
]
