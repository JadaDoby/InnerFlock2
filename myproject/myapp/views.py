from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from .models import FirebaseModel
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import get_user_model, login
from firebase_admin import auth as firebase_auth
from django.contrib.auth.decorators import login_required
from .models import UserProfile
from .forms import UserProfileForm

@login_required
def view_profile(request):
    user_profile = UserProfile.objects.get_or_create(user=request.user)[0]
    return render(request, 'profile/view_profile.html', {'user_profile': user_profile})

@login_required
def edit_profile(request):
    user_profile = UserProfile.objects.get_or_create(user=request.user)[0]

    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=user_profile)
        if form.is_valid():
            form.save()
            return redirect('view_profile')
    else:
        form = UserProfileForm(instance=user_profile)

    return render(request, 'profile/edit_profile.html', {'form': form})


def homepage(request):
    return render(request, 'myapp/homepage.html')


def home(request):
    # if request.method == 'POST':
    #     username = request.POST['username']
    #     password = request.POST['password']
    #     user = authenticate(request, username=username, password=password)
    #     print("User:", user)  # Debugging statement

    #     if user is not None:
    #         login(request, user)
    #         return redirect('homepage')  # Redirect to the homepage upon successful login
    #     else:
    #         return render(request, 'myapp/signup.html', {'error_message': 'Invalid username or password'})
    # else: 
    return render(request, 'myapp/home.html', {}) 


def signup(request):
    # if request.method == 'POST':
    #     email = request.POST.get('email')
    #     username = request.POST.get('username')
    #     school = request.POST.get('school')
    #     password = request.POST.get('password')

    #     try:
    #         firebase_user = FirebaseModel(email=email, username=username, school=school, password=password)
    #         firebase_user.save_to_firestore()
    #         return redirect('homepage')  # Redirect to the homepage upon successful signup
    #     except Exception as e:
    #         return render(request, 'myapp/signup.html', {'error_message': str(e)})

    return render(request, 'myapp/signup.html')


@csrf_exempt
def verify_token(request):
    data = json.loads(request.body)
    id_token = data.get('token')
    try:
        decoded_token = firebase_auth.verify_id_token(id_token)
        # UID from the decoded token
        uid = decoded_token['uid']
        
        # Authenticate the user using your custom backend
        user = authenticate(request, uid=uid)
        if user:
            login(request, user)
            return JsonResponse({'success': True})
        else:
            return JsonResponse({'success': False, 'message': 'User does not exist or is inactive'})
    except Exception as e:
        # Log the error for debugging
        print(e)
        return JsonResponse({'success': False, 'message': 'Failed to authenticate'})
    
    
@login_required
def view_profile(request):
    user_profile = UserProfile.objects.get_or_create(user=request.user)[0]
    return render(request, 'profile/view_profile.html', {'user_profile': user_profile})

    
def search(request):
    return render(request, 'myapp/search.html', {})


def groupchatPage(request):
    return redirect('groupchat_view')


def groupchat_view(request):
    return render(request, 'myapp/groupchatPage.html', {})


def privatechat(request):
    return render(request, 'myapp/private.html', {})

def chatroom(request):
    return render(request, 'myapp/chatroom.html', {})

def profile(request):
    return render(request, 'myapp/profile.html', {})

def privatechat(request):
    return render(request, 'myapp/privatechat.html', {})

