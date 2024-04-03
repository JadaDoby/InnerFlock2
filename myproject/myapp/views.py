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
from django.shortcuts import render, redirect
from .forms import PostForm
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import PostForm
from firebase_admin import firestore
from django.contrib.auth.decorators import login_required
from datetime import datetime
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_protect



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
    print("Current user:", request.user)
    print(f"Email for Firestore Query: '{request.user.email}'")
    try:
        firebase_uid = str(request.user.username)
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
    # return HttpResponse("This is the protected profile page.")


def privatechat(request):
    return render(request, 'myapp/privatechat.html', {})


##
def post_message_to_firestore(content, sender):
    db = firestore.client()
    timestamp = datetime.now()  # Get current timestamp
    message_data = {
        'content': content,
        'sender': sender,
        'timestamp': timestamp
    }
    db.collection('Messages').add(message_data)  # Updated collection name to 'Messages'

# Function to retrieve messages from Firestore
def get_messages_from_firestore(groupChatId):
    db = firestore.client()
    # Assuming 'Messages' collection contains a 'groupChatId' field to filter by
    messages_ref = db.collection('Messages').where('groupChatId', '==', groupChatId).order_by('timestamp', direction=firestore.Query.DESCENDING).limit(10).stream()
    messages = [doc.to_dict() for doc in messages_ref]
    return messages

@csrf_protect
def my_view(request):
    # Your view logic here to retrieve sender, post_context, and timestamp
    sender = 'Example Sender'  # Replace with actual sender data
    post_context = 'Example Post Content'  # Replace with actual post content data
    timestamp = datetime.now()  # Replace with actual timestamp data

    # Create context dictionary with the retrieved data
    context = {
        'sender': sender,
        'post_context': post_context,
        'timestamp': timestamp,
    }

    # Render the template with the provided context
    return render(request, 'chatroom.html', context)

# now trying to fetch the message in my view from firestore
def chatroom_view(request, groupid):
    messages = get_messages_from_firestore()  # Fetch messages
    return render(request, 'myapp/chatroom.html', {'messages': messages})


from django.shortcuts import redirect
from django.urls import reverse
from .forms import PostMessageForm

# Example of a view function to handle message posting
def post_message(request):
    if request.method == 'POST':
        form = PostMessageForm(request.POST)
        if form.is_valid():
            # Extract necessary data from the form
            group_chat_id = form.cleaned_data['groupChatId']
            content = form.cleaned_data['content']
            sender = request.user  # Assuming you're using Django's authentication
            

            # Process the message (save to the database, send to Firebase, etc.)

            # Redirect to the group chat view after posting
            return redirect('groupchat_view', groupChatId=group_chat_id)
    else:
        form = PostMessageForm()
    # If not POST or form is not valid, redirect to a default view or render an error
    return redirect('default_view')

def save_message_to_firestore(content, sender, groupChatId):
    db = firestore.client()
    doc_ref = db.collection('Messages').document()
    doc_ref.set({
        'content': content,
        'sender': sender,
        'groupChatId': groupChatId,
        'timestamp': firestore.SERVER_TIMESTAMP
    })
    print(f"Message saved: {content}")


@login_required
def chatroom_view(request, groupChatId):
    try:
        # Your logic to fetch messages goes here
        messages = get_messages_from_firestore(groupChatId)  # Make sure this function is prepared to receive a groupChatId

        # Debug print statement to ensure groupChatId is correctly passed
        print("Rendering form with groupChatId:", groupChatId)

        # Render the chatroom template with messages and groupChatId included in the context
        return render(request, 'myapp/chatroom.html', {'messages': messages, 'groupChatId': groupChatId})
    except Exception as e:
        print(f"Error retrieving messages: {e}")
        # Consider redirecting to a specific error handling page or back to a safe page
        return redirect('homepage')
    
@csrf_exempt
@login_required
def post_message_view(request):
    if request.method == 'POST':
        print(request.POST)  # Debug print to inspect all received POST data
        form = PostForm(request.POST)
        if form.is_valid():
            content = form.cleaned_data['post_content']
            groupChatId = form.cleaned_data['groupChatId']  # Correctly access groupChatId
            sender = request.user.username
            
            print(f"Content: {content}, GroupChatId: {groupChatId}, Sender: {sender}")
            save_message_to_firestore(content, sender, groupChatId)
            return redirect('chatroom_view', groupChatId=groupChatId)
        else:
            print("Form is not valid:", form.errors)
            return JsonResponse({'error': 'Invalid form data', 'details': form.errors.as_json()}, status=400)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=405)
