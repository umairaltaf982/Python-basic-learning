from django.contrib import admin
from .models import Enrollment


@admin.register(Enrollment)
class EnrollmentAdmin(admin.ModelAdmin):

    # Show these columns in the enrollment list
    list_display = ('student', 'course', 'enrolled_at')

    # Filter by course on the sidebar
    list_filter = ('course',)

    # Search by student username or course title
    # The double underscore (__) means: go into the related model and search that field
    # student__username means: follow the ForeignKey to User, then search the username field
    search_fields = ('student__username', 'course__title')

    # Most recent enrollments first
    ordering = ('-enrolled_at',)
