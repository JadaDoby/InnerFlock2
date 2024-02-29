# myapp/firebase.py
import os
import firebase_admin
from firebase_admin import credentials

def initialize_firebase():
    cred_path = os.environ.get('FIREBASE_CREDENTIALS_PATH', './serviceAccountKey.json')
    cred = credentials.Certificate(cred_path)
    firebase_admin.initialize_app(cred)
