from django.urls import path, include
from myapp import views
from .views import verify_token
from django.contrib import admin
from .views import chatroom_view, post_message_view

urlpatterns = [
    path('signin/', views.signin, name='signin'),
    path('', views.signin, name='signin'),
    path('homepage/', views.homepage, name='homepage'),
    path('signup/', views.signup, name='signup'),
    path('search/', views.search, name='search'),
    path('groupchatPage/', views.groupchat_view, name='groupchatPage'),   
    path('groupchat_view/', views.groupchatPage, name='groupchat_view'),
    path('privatechat/', views.privatechat, name='privatechat'),
    path('verify-token/', verify_token, name='verify_token'),
    path('homepage/chatroom/<str:groupid>/', views.chatroom, name='chatroom'),
    path('profile/', views.profile, name='profile'),
    path('homepage/privatechat.html', views.privatechat, name='privatechat'),
    path('post_message/', views.post_message_view, name='post_message'),
    path('chatroom/<str:groupChatId>/', views.chatroom_view, name='chatroom_view'),
    path('post_message/', post_message_view, name='post_message'),
]
