import os
import firebase_admin
from firebase_admin import credentials, firestore, initialize_app
from decouple import config

def initialize_firebase():
    cred_path = os.environ.get('FIREBASE_CREDENTIALS_PATH', './serviceAccountKey.json')
    cred = credentials.Certificate(cred_path)
    
    try:
        firebase_app = firebase_admin.get_app()
    except ValueError:
        firebase_app = initialize_app(cred)
    
    return firestore.client(app=firebase_app)

def post_message_to_firestore(content, sender):
    db = initialize_firebase()

    # Define message data
    message_data = {
        'content': content,
        'sender': sender,
        'timestamp': firestore.SERVER_TIMESTAMP
    }

    # Add the message document to the 'Messages' collection
    db.collection('Messages').add(message_data)

def get_messages_from_firestore():
    db = initialize_firebase()

    # Retrieve messages from the 'Messages' collection
    messages_ref = db.collection('Messages').order_by('timestamp', direction=firestore.Query.DESCENDING).limit(10).get()
    messages = []
    for doc in messages_ref:
        messages.append(doc.to_dict())
    return messages
