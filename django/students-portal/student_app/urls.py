from django.urls import path
from student_app import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path("students/", views.StudentList.as_view()),
    path("students/<int:pk>/", views.StudentDetail.as_view()),

# added for the authentication and permissions
    path("users/", views.UserList.as_view()),
    path("users/<int:pk>/", views.UserDetail.as_view()),
# for downloading CSV
    path("students/download/", views.StudentCSVDownload.as_view()),

]

urlpatterns = format_suffix_patterns(urlpatterns)

# it is used when the user wants to change the request type. 
# for example: instead of json he want to use html request
# to apply this we also need to change our view methods to:
# def snippet_list(request, format=None): 
#     and 
# def snippet_detail(request, pk, format=None):