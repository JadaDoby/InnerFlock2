from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from .models import FirebaseModel
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import get_user_model, login, logout as auth_logout
from firebase_admin import auth as firebase_auth
from django.contrib.auth.decorators import login_required
from .models import UserProfile
from firebase_admin import firestore
from .models import GroupChats  
from django.urls import reverse
from django.views.decorators.cache import never_cache
from django.http import HttpResponse
from .decorators import firebase_login_required  # Import your custom decorator
import time

# Assuming you have access to the Firebase UID and the Django user instance
def save_user_profile(user, firebase_uid):
    UserProfile.objects.create(user=user, firebase_uid=firebase_uid)

def add_user_to_group_chat(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        group_chat_id = data.get('groupChatId')
        user_id = data.get('userId')

        try:
            # Retrieve the group chat object from the database
            group_chat = GroupChats.objects.get(id=group_chat_id)
            
            # Add the user ID to the group chat's members list
            group_chat.groupMembers.add(user_id)
            
            # Save the updated group chat object
            group_chat.save()

            return JsonResponse({'success': True})
        except GroupChats.DoesNotExist:
            return JsonResponse({'error': 'Group chat not found'}, status=404)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=405)

def homepage(request):
    # Retrieve group chat data from Firestore
    db = firestore.client()
    group_chats_ref = db.collection('group_chats').stream()

    # Parse Firestore data and create GroupChats objects
    group_chats = []
    for doc in group_chats_ref:
        data = doc.to_dict()
        data['id'] = doc.id
        #data['data'] = doc._data
        '''
        chat = GroupChats(
            name=data['name'],
            description=data['description'],
            groupAdmin=data['groupAdmin'],
            isPrivate=data['isPrivate']
            # Add other fields as needed
        )
        '''
        #chat.id = doc.id
        #group_chats.append(chat)
        group_chats.append(data)
        
    return render(request, 'myapp/homepage.html', {'group_chats': group_chats})

@never_cache
def signin(request):
    return render(request, 'myapp/signin.html', {}) 


def signup(request):
    return render(request, 'myapp/signup.html')
  
@csrf_exempt
def verify_token(request):
    """ 
    Verify the token passed in the request.
    If the token is valid, authenticate the user.
    """
    data = json.loads(request.body)
    id_token = data.get('token')
    
    max_attempts = 3
    for attempt in range(max_attempts):
        try:
            decoded_token = firebase_auth.verify_id_token(id_token)
            uid = decoded_token['uid']
            
            # Extract user information
            email = decoded_token.get('email')
            username = decoded_token.get('name', 'default_username')
            school = 'default_school'  
            
            # Authenticate the user using your custom backend
            user = authenticate(request, uid=uid)
            if user:
                login(request, user)
                return JsonResponse({'success': True})
            else:
                return JsonResponse({'success': False, 'message': 'User does not exist or is inactive'})
        except Exception as e:
            # Log the error for debugging
            print(f"Attempt {attempt + 1}: {e}")
            if "Token used too early" in str(e) and attempt < max_attempts - 1:
                time.sleep(1)
            else:
                print(e)
                return JsonResponse({'success': False, 'message': 'Failed to authenticate'})

def search(request):
    return render(request, 'myapp/search.html', {})


def groupchatPage(request):
    return redirect('groupchat_view')


def groupchat_view(request):
    return render(request, 'myapp/groupchatPage.html', {})


def privatechat(request):
    return render(request, 'myapp/private.html', {})

def chatroom(request, groupid):
    return render(request, 'myapp/chatroom.html', {})

def profile(request):
    # print("Current user:", request.user)
    # print(f"Email for Firestore Query: '{request.user.email}'")
    try:
        firebase_uid = str(request.user.username)
        print(f"Firebase UID: {firebase_uid}")
        firestore_data = UserProfile.get_data_from_firestore(firebase_uid)
        
        if firestore_data:
            # Print the email, school, and username
            print(f"Email: {firestore_data['email']}, School: {firestore_data['school']}, Username: {firestore_data['username']}")
        else:
            print("No data found for the current user in Firestore.")
            
    except Exception as e:
        print(f"Failed to fetch data from Firestore: {e}")
        firestore_data = {}
                                                          
    return render(request, 'myapp/profile.html', {'user_profile_data': firestore_data})

def privatechat(request):
    return render(request, 'myapp/privatechat.html', {})

def privatechat(request):
    return render(request, 'myapp/privatechat.html', {})

def privatechat(request):
    return render(request, 'myapp/privatechat.html', {})
 