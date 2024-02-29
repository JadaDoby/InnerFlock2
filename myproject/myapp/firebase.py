# myapp/firebase.py
import os
import firebase_admin
from firebase_admin import credentials
from decouple import config

def initialize_firebase():
    cred_path = os.environ.get('FIREBASE_CREDENTIALS_PATH', './serviceAccountKey.json')
    cred = credentials.Certificate(cred_path)
    firebase_admin.initialize_app(cred)

FIREBASE_CONFIG = {
    'apiKey': config('FIREBASE_API_KEY'),
    'authDomain': config('FIREBASE_AUTH_DOMAIN'),
    'projectId': config('FIREBASE_PROJECT_ID'),
    'storageBucket': config('FIREBASE_STORAGE_BUCKET'),
    'messagingSenderId': config('FIREBASE_MESSAGING_SENDER_ID'),
    'appId': config('FIREBASE_APP_ID'),
    'measurementId': config('FIREBASE_MEASUREMENT_ID'),
}