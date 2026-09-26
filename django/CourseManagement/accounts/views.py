from django.http import HttpResponse


# These are placeholder views for Phase 7 (URL routing verification).
# We will replace every one of these with real logic in Phase 8.

def home(request):
    return HttpResponse("Home Page — accounts app")

def register(request):
    return HttpResponse("Register Page")

def login_view(request):
    return HttpResponse("Login Page")

def logout_view(request):
    return HttpResponse("Logout")
