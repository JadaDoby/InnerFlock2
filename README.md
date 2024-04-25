# InnerFlock2
 # Description:  We developed a chat application that enables hiring managers to create a large group chat to help create better relationships with potential students who are considering joining the workforce soon. This will make it easier for them to share their updates, invite them to events, and share humorous memes or longer videos with everyone in the group. Sharing things with others through group messages is only sometimes feasible due to space constraints or low-quality media. Our desktop app aims to provide a platform for people to share their interests in the professional realm without any limitations. 

#Details regarding user interface:
 In the admin interface, you can edit the group chats and create and edit them.
In the hiring manager interface, you can only create and delete group chats and join existing chats.
In the student interface, you can only join chats.
#List of Libraries used for our project- We used Django for the backend and html for the frontend

asgiref==3.7.2
blinker==1.7.0
CacheControl==0.14.0
cachetools==5.3.3
certifi==2023.11.17
cffi==1.16.0
charset-normalizer==3.3.2
click==8.1.7
cryptography==42.0.5
distlib==0.3.8
Django==5.0.2
et-xmlfile==1.1.0
filelock==3.13.1
firebase-admin==6.4.0
Flask==3.0.2
google-api-core==2.17.1
google-api-python-client==2.120.0
google-auth==2.28.1
google-auth-httplib2==0.2.0
google-cloud-core==2.4.1
google-cloud-firestore==2.15.0
google-cloud-storage==2.14.0
google-crc32c==1.5.0
google-resumable-media==2.7.0
googleapis-common-protos==1.62.0
grpcio==1.62.0
grpcio-status==1.62.0
gunicorn==22.0.0
httplib2==0.22.0
idna==3.6
install==1.3.5
itsdangerous==2.1.2
Jinja2==3.1.3
MarkupSafe==2.1.5
msgpack==1.0.7
numpy==1.26.3
openpyxl==3.1.2
packaging==24.0
pandas==2.1.4
pillow==10.2.0
platformdirs==4.2.0
proto-plus==1.23.0
protobuf==4.25.3
pyasn1==0.5.1
pyasn1-modules==0.3.0
pycparser==2.21
PyJWT==2.8.0
pyparsing==3.1.1
python-dateutil==2.8.2
python-decouple==3.8
pytz==2023.3.post1
requests==2.31.0
rsa==4.9
six==1.16.0
sqlparse==0.4.4
tzdata==2023.4
uritemplate==4.1.1
urllib3==2.2.1
virtualenv==20.25.0
Werkzeug==3.0.1

#List of other resources
We used Cloud  Firestore as our database
# The separation of the work
Jada: Did the basic setup of the initial of all the HTML templates, Created the chats application, Did the database that nested the group chat to the message in the chats, Did the signup page, and Did the set-up of the environment with Jasmine.  Helped with models, forms, and URLs, py, and views.
Sabrina: I set up Firebase, role-based access for students, hiring managers, and admin. I added the buttons Student and Hiring manager to the signup page. I created the buttons and functionalities Create Chat and Delete Chat, which only Hiring managers and admin can access. I then created an Edit button for Admin.
Raul: Created the groupchat.html, Created the page that shows what the users chats are , added navigation bar to the group chats, worked on the homepage as well, created the initial group chats database 
Jasmine: Did the Firebase authentication, logout functionality, and registration, firestore database,search bar, base.html, helped with the routing, added the Profile Page, viewed database info on the profile screen, and helped with initial set-up.

  ## To run 
  cd myproject
  python manage.py runserver

