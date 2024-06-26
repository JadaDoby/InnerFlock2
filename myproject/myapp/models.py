# myapp/models.py
from django.db import models
from django.contrib.auth.hashers import make_password 
from firebase_admin import firestore
from django.contrib.auth.hashers import check_password
from django.contrib.auth.models import User

class FirebaseModel(models.Model):
    email = models.EmailField(max_length=255)
    username = models.CharField(max_length=255)
    school = models.CharField(max_length=255, blank=True)  
    password = models.CharField(max_length=255)

    def save_to_firestore(self):
        db = firestore.client()
        users_ref = db.collection('users')
        users_ref.add({
            'email': self.email,
            'username': self.username,
            'school': self.school,
            'password': self.password,
            
        })
    
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    firebase_uid = models.CharField(max_length=128, unique=True)
    email = models.EmailField(default='example@example.com')
    username = models.CharField(max_length=100)
    school = models.CharField(max_length=100)
    role = models.CharField(max_length=50, blank=True)

    @classmethod
    def get_data_from_firestore(cls, firebase_uid):
        print(f"Attempting to fetch Firestore data for UID: {firebase_uid}")
        db = firestore.client()
        users_ref = db.collection('users')
        user_data = None

        # Try to get the document with the matching Firebase UID
        try:
            doc_ref = users_ref.document(firebase_uid)
            doc = doc_ref.get()
            if doc.exists:
                doc_data = doc.to_dict()
                print(f"Document data found for UID {firebase_uid}: {doc_data}")
                user_data = {
                    'email': doc_data.get('email'),
                    'username': doc_data.get('username'),
                    'school': doc_data.get('school'),
                    'role': doc_data.get('role')
                }
                print(f"User data extracted: {user_data}")
            else:
                print(f"No document found for UID {firebase_uid}")
        except Exception as e:
            print(f"Exception occurred while fetching data from Firestore for UID {firebase_uid}: {e}")

        return user_data

    
class GroupChats(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=350)
    image = models.ImageField()
    groupAdmin = models.ForeignKey(User, related_name = 'admin_of_groupchat', on_delete=models.SET_NULL, null=True)  # group chats remain if admin is deleted
    groupMembers = models.ManyToManyField(User, related_name='groupchat_participants')  
    isPrivate = models.BooleanField() 