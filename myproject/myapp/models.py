# myapp/models.py
from django.db import models
from firebase_admin import firestore

class FirebaseModel(models.Model):
    name = models.CharField(max_length=255)

    def save_to_firestore(self):
        db = firestore.client()
        users_ref = db.collection('users')
        users_ref.add({'name': self.name})

    @classmethod
    def get_data_from_firestore(cls):
        db = firestore.client()
        users_ref = db.collection('users')
        data = []
        for doc in users_ref.stream():
            data.append(doc.to_dict())
        return data
