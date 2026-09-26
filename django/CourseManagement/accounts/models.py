from django.contrib.auth.models import AbstractUser
# as we have inherited from AbstractUser, it means we automatically get the access of
# username, first_name, last_name, email, password, last_login etc
# we only need to add the 'role' i.e. whether teacher or student
from django.db import models

# Create your models here.
class User(AbstractUser):
    STUDENT = 'student'
    TEACHER = 'teacher'

    ROLE_CHOICES = [
        (STUDENT, 'Student'),
        (TEACHER, 'Teacher'),
    ]

    role = models.CharField(
        max_length=10,
        choices=ROLE_CHOICES,
        default=STUDENT
    )

    def __str__(self):
        return self.username