from django.contrib import admin
from django.contrib.auth.admin import UserAdmin  # Django's built-in UserAdmin
from .models import User


# We extend Django's built-in UserAdmin instead of starting from scratch.
# UserAdmin already knows how to handle passwords (hashing, change forms, etc.)
# We just add our custom 'role' field on top of everything it already does.

@admin.register(User)
class CustomUserAdmin(UserAdmin):

    # Columns visible in the user list page
    list_display = ('username', 'email', 'role', 'is_staff', 'is_active')

    # Sidebar filters on the right side of the list page
    list_filter = ('role', 'is_staff', 'is_active')

    # Which fields the search box searches through
    search_fields = ('username', 'email')

    # Default sort order (newest first by id)
    ordering = ('-id',)

    # UserAdmin defines fieldsets — the sections shown on the edit/create form.
    # We add our custom 'role' field to the existing 'Personal info' section.
    fieldsets = UserAdmin.fieldsets + (
        ('Role', {'fields': ('role',)}),
    )

    # This controls which fields appear on the "Add User" form in admin.
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Role', {'fields': ('role',)}),
    )
