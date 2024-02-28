# myapp/models.py
from django.db import models
from firebase_admin import firestore

class FirebaseModel(models.Model):
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)

    def save_to_firestore(self):
        db = firestore.client()
        users_ref = db.collection('users')
        users_ref.add({'username': self.username})
        users_ref.add({'password': self.password})

    @classmethod
    def get_data_from_firestore(cls):
        db = firestore.client()
        users_ref = db.collection('users')
        data = []
        for doc in users_ref.stream():
            data.append(doc.to_dict())
        return data
