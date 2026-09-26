from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # Django's built-in admin panel
    path('admin/', admin.site.urls),

    # accounts app handles everything at /accounts/
    # EXCEPT the home page, which also lives in accounts but at the root /
    path('', include('accounts.urls')),

    # courses app handles everything at /courses/
    path('courses/', include('courses.urls')),

    # enrollments app handles everything at /enrollments/
    path('enrollments/', include('enrollments.urls')),

    # assignments app handles everything at /assignments/
    path('assignments/', include('assignments.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# The static() line tells Django to serve uploaded files (PDFs, images)
# during development. In production a real web server (nginx) handles this.
