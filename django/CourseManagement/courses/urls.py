from django.urls import path
from . import views

app_name = 'courses'

urlpatterns = [
    # /courses/  → list all courses
    path('', views.course_list, name='course_list'),

    # /courses/create/  → form to create a new course
    # IMPORTANT: 'create/' must come BEFORE '<int:pk>/'
    # Django matches URLs top to bottom. If <int:pk>/ came first,
    # Django would try to interpret 'create' as an integer and fail.
    path('create/', views.course_create, name='course_create'),

    # /courses/1/  → detail page for course with id=1
    # <int:pk> is a URL parameter — Django captures the number and
    # passes it as the argument 'pk' to the view function
    path('<int:pk>/', views.course_detail, name='course_detail'),

    # /courses/1/update/  → form to edit course with id=1
    path('<int:pk>/update/', views.course_update, name='course_update'),

    # /courses/1/delete/  → confirm and delete course with id=1
    path('<int:pk>/delete/', views.course_delete, name='course_delete'),
]
