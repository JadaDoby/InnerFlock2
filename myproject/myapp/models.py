# myapp/models.py
from django.db import models
from django.contrib.auth.hashers import make_password 
from firebase_admin import firestore
from django.contrib.auth.hashers import check_password

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

    @classmethod
    def get_data_from_firestore(cls):
        db = firestore.client()
        users_ref = db.collection('users')
        data = []
        for doc in users_ref.stream():
            doc_data = doc.to_dict()
            # Note: Passwords stored are hashed, never send them back to the client or display them
            # Consider excluding 'password' from the returned data if it's not needed for a specific operation
            data.append({
                'email': doc_data.get('email'),
                'username': doc_data.get('username'),
                'school': doc_data.get('school'),
                # 'password': doc_data.get('password'),  # Generally, you shouldn't retrieve or send the password
            })
        return data
