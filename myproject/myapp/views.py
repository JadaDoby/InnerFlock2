from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from .forms import SignUpForm
from .models import FirebaseModel

# def home(request):
#     return render(request, 'myapp/home.html', {})

def home(request):
    # Handle user input or other view-related logic
    if request.method == 'POST':
        username = request.POST.get('username')
        FirebaseModel.objects.create(username=username).save_to_firestore()
        password = request.POST.get('password')
        FirebaseModel.objects.create(password=password).save_to_firestore()

    # Retrieve data from Firestore using the model method
    firebase_data = FirebaseModel.get_data_from_firestore()

    # Pass data to the template
    context = {'firebase_data': firebase_data}
    return render(request, 'myapp/home.html', context)
        
def signup(request):
    if request.method == 'POST':
        # Directly retrieve data from the request
        email = request.POST.get('email')
        username = request.POST.get('username')
        school = request.POST.get('school')  # Assuming you have a school input in your form
        password = request.POST.get('password')

        # Attempt to create a new FirebaseModel instance and save to Firestore
        try:
            firebase_user = FirebaseModel(email=email, username=username, school=school, password=password)
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