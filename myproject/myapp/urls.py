from django.urls import path
from myapp import views  # Import views from the same directory

urlpatterns = [
    path('', views.home, name='home'),  # URL pattern for the home view
    # Add other app-specific URL patterns
]
