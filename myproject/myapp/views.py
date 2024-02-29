from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .models import FirebaseModel


def homepage(request):
    return render(request, 'myapp/homepage.html')


def home(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        print("User:", user)  # Debugging statement

        if user is not None:
            login(request, user)
            return redirect('homepage')  # Redirect to the homepage upon successful login
        else:
            return render(request, 'myapp/signup.html', {'error_message': 'Invalid username or password'})

    return render(request, 'myapp/home.html', {})


def signup(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        username = request.POST.get('username')
        school = request.POST.get('school')
        password = request.POST.get('password')

        try:
            firebase_user = FirebaseModel(email=email, username=username, school=school, password=password)
            firebase_user.save_to_firestore()
            return redirect('homepage')  # Redirect to the homepage upon successful signup
        except Exception as e:
            return render(request, 'myapp/signup.html', {'error_message': str(e)})

    return render(request, 'myapp/signup.html')


def search(request):
    return render(request, 'myapp/search.html', {})


def groupchat(request):
    return redirect('groupchat_view')


def groupchat_view(request):
    return render(request, 'myapp/groupchat.html', {})


def privatechat(request):
    return render(request, 'myapp/private.html', {})
