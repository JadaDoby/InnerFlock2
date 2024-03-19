#from models import GroupChats
from firebase_admin import firestore

# list of GroupChats model objects
'''
groupChatsList = [
    GroupChats(
        name= 'Google Chat',
        description= 'Description of Group Chat 1',
        # image would normally go here, but for testing it should display default
        groupAdmin= 'yPGAWpKMFmNEj0smp8uPGShEQUN2', #admin@email.com
        groupMembers= ['yPGAWpKMFmNEj0smp8uPGShEQUN2', 'aJer8MfPOHOWLFoCP0IBkhK8zRm1'], # admin & john
    ),
    GroupChats(
        name = 'Walmart and Sam Chat',
        description = 'Description of Group Chat 2',
        # image would normally go here, but for testing it should display default
        groupAdmin = 'yPGAWpKMFmNEj0smp8uPGShEQUN2',
        groupMembers = ['yPGAWpKMFmNEj0smp8uPGShEQUN2', 'aJer8MfPOHOWLFoCP0IBkhK8zRm1'], # admin & john
    ),
    GroupChats(
        name = 'Vogue Chat',
        description = 'Description of Group Chat 2',
        # image would normally go here, but for testing it should display default
        groupAdmin = 'yPGAWpKMFmNEj0smp8uPGShEQUN2',
        groupMembers = ['yPGAWpKMFmNEj0smp8uPGShEQUN2', 'aJer8MfPOHOWLFoCP0IBkhK8zRm1'], # admin & john
    ),
    GroupChats(
        name = 'Liberty Mutualt',
        description = 'Description of Group Chat 2',
        # image would normally go here, but for testing it should display default
        groupAdmin = 'yPGAWpKMFmNEj0smp8uPGShEQUN2',
        groupMembers = ['yPGAWpKMFmNEj0smp8uPGShEQUN2', 'aJer8MfPOHOWLFoCP0IBkhK8zRm1'], # admin & john
    ),
    GroupChats(
        name = 'Ramen Headquater',
        description = 'Description of Group Chat 2',
        # image would normally go here, but for testing it should display default
        groupAdmin = 'yPGAWpKMFmNEj0smp8uPGShEQUN2',
        groupMembers = ['yPGAWpKMFmNEj0smp8uPGShEQUN2', 'b0AQpTkExgf4fr9kxCqf4ECIAXJ3'], # admin & jane
    ),
    GroupChats(
        name = "Lindy's Homemade",
        description = 'Description of Group Chat 2',
        # 'image': 'image_url_2.jpg', # image would normally go here, but for testing it should display default
        groupAdmin = 'yPGAWpKMFmNEj0smp8uPGShEQUN2',
        groupMembers = ['yPGAWpKMFmNEj0smp8uPGShEQUN2', 'b0AQpTkExgf4fr9kxCqf4ECIAXJ3'], # admin & jane
    ),
    # Add more group chat data as needed
]
'''

