from django.urls import path
from . import views  # Import views from the current app

urlpatterns = [  
    path('', views.HomePage, name='home'),  
    path('signup/', views.SignupPage, name='signup'),  # Signup page
    path('login/', views.LoginPage, name='login'),   # Login page
    path('logout/', views.LogoutPage, name='logout') # Logout page
]
