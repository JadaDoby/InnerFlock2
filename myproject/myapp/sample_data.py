from models import GroupChats
from firebase_admin import firestore

groupChatsList = [
    GroupChats(
        name= 'Google Chat',
        description= 'Description of Group Chat 1',
        # image would normally go here, but for testing it should display default
        groupAdmin= 'yPGAWpKMFmNEj0smp8uPGShEQUN2', #admin@email.com
        groupMembers= ['yPGAWpKMFmNEj0smp8uPGShEQUN2', 'aJer8MfPOHOWLFoCP0IBkhK8zRm1'], # admin & john
        isPrivate = True
    ),
    GroupChats(
        name = 'Walmart and Sam Chat',
        description = 'Description of Group Chat 2',
        # image would normally go here, but for testing it should display default
        groupAdmin = 'yPGAWpKMFmNEj0smp8uPGShEQUN2',
        groupMembers = ['yPGAWpKMFmNEj0smp8uPGShEQUN2', 'aJer8MfPOHOWLFoCP0IBkhK8zRm1'], # admin & john
        isPrivate = False
    ),
    GroupChats(
        name = 'Vogue Chat',
        description = 'Description of Group Chat 2',
        # image would normally go here, but for testing it should display default
        groupAdmin = 'yPGAWpKMFmNEj0smp8uPGShEQUN2',
        groupMembers = ['yPGAWpKMFmNEj0smp8uPGShEQUN2', 'aJer8MfPOHOWLFoCP0IBkhK8zRm1'], # admin & john
        isPrivate = False
    ),
    GroupChats(
        name = 'Liberty Mutualt',
        description = 'Description of Group Chat 2',
        # image would normally go here, but for testing it should display default
        groupAdmin = 'yPGAWpKMFmNEj0smp8uPGShEQUN2',
        groupMembers = ['yPGAWpKMFmNEj0smp8uPGShEQUN2', 'aJer8MfPOHOWLFoCP0IBkhK8zRm1'], # admin & john
        isPrivate = False
    ),
    GroupChats(
        name = 'Ramen Headquater',
        description = 'Description of Group Chat 2',
        # image would normally go here, but for testing it should display default
        groupAdmin = 'yPGAWpKMFmNEj0smp8uPGShEQUN2',
        groupMembers = ['yPGAWpKMFmNEj0smp8uPGShEQUN2', 'b0AQpTkExgf4fr9kxCqf4ECIAXJ3'], # admin & jane
        isPrivate = False
    ),
    GroupChats(
        name = "Lindy's Homemade",
        description = 'Description of Group Chat 2',
        # 'image': 'image_url_2.jpg', # image would normally go here, but for testing it should display default
        groupAdmin = 'yPGAWpKMFmNEj0smp8uPGShEQUN2',
        groupMembers = ['yPGAWpKMFmNEj0smp8uPGShEQUN2', 'b0AQpTkExgf4fr9kxCqf4ECIAXJ3'], # admin & jane
        isPrivate = False
    ),
    # Add more group chat data as needed
]

def save_group_chats_to_firestore(groupChatsList):
    db = firestore.client()
    group_chats_ref = db.collection('group_chats')

    # Loop through each group chat instance
    for group_chat in groupChatsList:
        # Convert the group chat instance to a dictionary
        chat_data = group_chat.__dict__

        # Save the group chat data to Firebase
        group_chats_ref.add(chat_data)

save_group_chats_to_firestore(groupChatsList)