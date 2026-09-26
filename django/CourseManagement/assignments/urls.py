from django.urls import path
from . import views

app_name = 'assignments'

urlpatterns = [
    # /assignments/  → list all assignments (filtered by enrolled courses)
    path('', views.assignment_list, name='assignment_list'),

    # /assignments/3/  → detail + submission form for assignment with id=3
    path('<int:pk>/', views.assignment_detail, name='assignment_detail'),

    # /assignments/3/submit/  → handle the file upload submission
    path('<int:pk>/submit/', views.assignment_submit, name='assignment_submit'),

    # /assignments/3/grade/  → teacher grades a submission
    path('<int:pk>/grade/', views.assignment_grade, name='assignment_grade'),
]
