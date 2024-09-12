from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponseForbidden

# Home page - requires login
@login_required(login_url='login')
def HomePage(request):
    return render(request, 'home.html')

# Signup page
def SignupPage(request):
    if request.method == 'POST':
        username = request.POST.get('user')
        email = request.POST.get('email')
        pass1 = request.POST.get('pass1')
        pass2 = request.POST.get('pass2')

        # Check if passwords match
        if pass1 != pass2:
            return HttpResponse("Your password and confirm password do not match!")
       
        if len(pass1) < 8:
            return HttpResponse("Password is too short. It must be at least 8 characters.")

        if not any(char.isupper() for char in pass1):
            return HttpResponse(("Password must contain at least one uppercase letter.")   
            )
        if not any(char.islower() for char in pass1):
            return HttpResponse(("Password must contain at least one lowercase letter.")     
             )
         # Check for at least one digit
        if not any(char.isdigit() for char in pass1):
           return HttpResponse(("Password must contain at least one digit.")
                   )
        #   Check for at least one special character
        special_characters = "!@#$%^&*()-+"
        if not any(char in special_characters for char in pass1):
                 return HttpResponse(("Password must contain at least one special character: " + special_characters),
                            )
    
        # Check if the username already exists
        if User.objects.filter(username=username).exists():
            return HttpResponse("Username already taken! Please choose another.")

        # Check if the email is already in use
        if User.objects.filter(email=email).exists():
            return HttpResponse("Email is already registered!")

        # Create the new user
        User.objects.create_user(username=username, email=email, password=pass1)
        return redirect('login')  # Redirect to login after successful signup

    return render(request, 'Signup.html')

# Login page
def LoginPage(request):
    if request.method == 'POST':
        email_input = request.POST.get('email')
        pass1 = request.POST.get('pass')

        # Get the user by email
        try:
            user = User.objects.get(email=email_input)
        except User.DoesNotExist:
            return HttpResponse("Invalid email or password!")

        # Authenticate using the username and password
        user = authenticate(request, username=user.username, password=pass1)
        if user is not None:
            login(request, user)
            return redirect('home')  # Redirect to the home page on successful login
        else:
            return HttpResponse("Invalid email or password!")
    return render(request, 'Login.html')

# Logout page
def LogoutPage(request):
    logout(request)
    return redirect('login')

