from django.urls import path
from myapp import views  # Import views from the same directory
from .views import verify_token

urlpatterns = [
    path('', views.home, name='home'),
    path('homepage/', views.homepage, name='homepage'),
    path('signup/' , views.signup, name='signup'),
    path('search' , views.search, name='search'),
    path('groupchatPage/' , views.groupchat_view, name='groupchatPage'),   
    path('groupchat_view/', views.groupchatPage, name='groupchat_view'),
    path('privatechat/', views.privatechat, name='privatechat'),
    path('verify-token/', verify_token, name='verify_token'),
]
