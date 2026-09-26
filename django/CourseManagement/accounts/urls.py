from django.urls import path
from . import views

# app_name creates a namespace for this app's URLs.
# So instead of name='login' you'd reference it as 'accounts:login'
# This prevents name collisions when multiple apps have a URL named 'login'
app_name = 'accounts'

urlpatterns = [
    # Home page — matches exactly '/'
    path('', views.home, name='home'),

    # Register page — matches '/accounts/register/'
    # Wait — the main urls.py includes accounts at '', not 'accounts/'
    # So these URLs will be at /register/, /login/, /logout/
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]
