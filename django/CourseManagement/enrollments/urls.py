from django.urls import path
from . import views

app_name = 'enrollments'

urlpatterns = [
    # /enrollments/  → list courses the logged-in student is enrolled in
    path('', views.enrollment_list, name='enrollment_list'),

    # /enrollments/5/enroll/  → enroll in course with id=5
    path('<int:course_pk>/enroll/', views.enroll, name='enroll'),

    # /enrollments/5/leave/  → leave course with id=5
    path('<int:course_pk>/leave/', views.leave, name='leave'),
]
