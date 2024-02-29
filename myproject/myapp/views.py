from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password
from .forms import SignUpForm
from .models import FirebaseModel
from .models import authenticate_with_firestore

# def home(request):
#     return render(request, 'myapp/home.html', {})
@login_required
def homepage(request):
    return render(request, 'myapp/homepage.html')

def home(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('homepage')  # Redirect to a "homepage" view upon success
        else:
            # Invalid login - handle as needed
            return render(request, 'myapp/home.html', {'error': 'Invalid username or password.'})
    return render(request, 'myapp/home.html')
        
def signup(request):
    if request.method == 'POST':
        # Directly retrieve data from the request
        email = request.POST.get('email')
        username = request.POST.get('username')
        school = request.POST.get('school')  # Assuming you have a school input in your form
        password = request.POST.get('password')

        hashed_password = make_password(password)
        
        # Attempt to create a new FirebaseModel instance and save to Firestore
        try:
            firebase_user = FirebaseModel(email=email, username=username, school=school, password=hashed_password)
            firebase_user.save_to_firestore()
            return HttpResponse("User registered successfully.")
        except Exception as e:
            return HttpResponse(f"Failed to register user: {e}")

    # If not a POST request, or if there was an error, display the signup form again
    return render(request, 'myapp/signup.html')

def search(request):
    return render(request, 'myapp/search.html', {})

def groupchat(request):
    return redirect('groupchat_view')  # Assuming 'groupchat_view' is the name of your view function

def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user_data = authenticate_with_firestore(username, password)
        if user_data:
            # User authenticated successfully
            # Implement your session handling or redirect logic here
            return redirect('homepage')
        else:
            # Authentication failed
            return render(request, 'myapp/signin.html', {'error': 'Invalid username or password.'})

def groupchat_view(request):
    return render(request, 'myapp/groupchat.html', {})

def privatechat(request):
    return render(request,'myapp/private.html',{})