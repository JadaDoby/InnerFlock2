from django.urls import path
from myapp import views  # Import views from the same directory

urlpatterns = [
    path('', views.home, name='home'),
    path('homepage/', views.homepage, name='homepage'),
    path('signup/' , views.signup, name='signup'),
    path('search' , views.search, name='search'),
    path('groupchat/' , views.groupchat_view, name='groupchat'),   
    path('signin/', views.signin, name='signin'),
    path('groupchat_view/', views.groupchat, name='groupchat_view'),
    path('privatechat/', views.privatechat, name='privatechat'),
]
