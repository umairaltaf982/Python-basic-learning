from django.contrib import admin
from .models import Assignment, Submission


@admin.register(Assignment)
class AssignmentAdmin(admin.ModelAdmin):

    # Columns in the assignment list
    list_display = ('title', 'course', 'due_date', 'created_at')

    # Filter assignments by course
    list_filter = ('course',)

    # Search by title or the course title it belongs to
    search_fields = ('title', 'course__title')

    # Upcoming deadlines first
    ordering = ('due_date',)


@admin.register(Submission)
class SubmissionAdmin(admin.ModelAdmin):

    # Columns in the submission list
    list_display = ('student', 'assignment', 'marks', 'submitted_at')

    # Filter by assignment so you can see all submissions for one assignment
    list_filter = ('assignment',)

    # Search by student username or assignment title
    search_fields = ('student__username', 'assignment__title')

    # Most recent submissions first
    ordering = ('-submitted_at',)
