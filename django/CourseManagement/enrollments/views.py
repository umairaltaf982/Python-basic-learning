from django.http import HttpResponse


# Placeholder views — will be replaced with real logic in Phase 8.

def enrollment_list(request):
    return HttpResponse("My Enrollments Page")

def enroll(request, course_pk):
    return HttpResponse(f"Enroll in Course ID: {course_pk}")

def leave(request, course_pk):
    return HttpResponse(f"Leave Course ID: {course_pk}")
