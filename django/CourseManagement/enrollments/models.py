from django.db import models
from django.conf import settings

class Enrollment(models.Model):
    student = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )

    course = models.ForeignKey(
        'courses.Course',
        on_delete=models.CASCADE,
    )

    enrolled_at = models.DateTimeField(auto_now_add=True)

# In Python data models (most notably in frameworks like Django ORM),
# a class Meta is an inner class used to provide metadata options to your model.
# It defines configuration settings that do not represent database fields themselves,
# but rather modify how the model behaves, how its database table is structured, or how it is queried

    class Meta:
        unique_together = ('student', 'course')     # Django enforces that each (student, course) pair is unique.

    def __str__(self):
        return f'{self.student.username} -> {self.course.title}'
