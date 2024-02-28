from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import SignUpForm
from .models import FirebaseModel

def home(request):
    return render(request, 'myapp/home.html', {})

def my_view(request):
    # Handle user input or other view-related logic
    if request.method == 'POST':
        name = request.POST.get('name')
        FirebaseModel.objects.create(name=name).save_to_firestore()

    # Retrieve data from Firestore using the model method
    firebase_data = FirebaseModel.get_data_from_firestore()

    # Pass data to the template
    context = {'firebase_data': firebase_data}
    return render(request, 'home.html', context)
        
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('groupchat')  # Redirect to the group chat page upon successful signup and login
    else:
        form = SignUpForm()

    return render(request, 'myapp/signup.html', {'form': form})

def search(request):
    return render(request, 'myapp/search.html', {})

def groupchat(request):
    return redirect('groupchat_view')  # Assuming 'groupchat_view' is the name of your view function

def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('groupchat')  # Redirect to the group chat page upon successful login
        else:
            # Handle invalid login (display error message, etc.)
            pass

    return render(request, 'myapp/signin.html', {})

def groupchat_view(request):
    return render(request, 'myapp/groupchat.html', {})

def privatechat(request):
    return render(request,'myapp/private.html',{})