# myapp/models.py
from django.db import models
from django.contrib.auth.hashers import make_password 
from firebase_admin import firestore
from django.contrib.auth.hashers import check_password

class FirebaseModel(models.Model):
    email = models.EmailField(max_length=255)
    username = models.CharField(max_length=255)
    school = models.CharField(max_length=255, blank=True)  # Assuming school can be optional
    password = models.CharField(max_length=255)


    def save_to_firestore(self):
        
        hashed_password = make_password(self.password)
        db = firestore.client()
        users_ref = db.collection('users')
        users_ref.add({
            'email': self.email,
            'username': self.username,
            'school': self.school,
            'password': hashed_password,  # Store hashed password
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


def authenticate_with_firestore(username, password):
    db = firestore.client()
    users_ref = db.collection('users')
    query = users_ref.where(field_path='username', op_string='==', value=username)
    results = list(query.stream())

    if not results:
        return None  # User not found

    user_data = results[0].to_dict()
    if check_password(password, user_data['password']):
        return user_data  # Password matches, return user data
    else:
        return None  # Password does not match