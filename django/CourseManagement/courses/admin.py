from django.contrib import admin
from .models import Course


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):

    # Columns visible in the course list page
    list_display = ('title', 'teacher', 'created_at', 'updated_at')

    # Sidebar filter — lets you filter courses by which teacher created them
    list_filter = ('teacher',)

    # Search box searches through title and teacher's username
    search_fields = ('title', 'teacher__username')

    # Default sort: newest course first
    ordering = ('-created_at',)

    # Makes the created_at field clickable (it links to the detail page)
    list_display_links = ('title',)
