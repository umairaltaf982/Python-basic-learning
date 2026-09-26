from django.http import HttpResponse


# Placeholder views — will be replaced with real logic in Phase 8.

def course_list(request):
    return HttpResponse("Course List Page")

def course_create(request):
    return HttpResponse("Create Course Page")

def course_detail(request, pk):
    # pk comes from the URL pattern <int:pk>
    # Django captures the number in the URL and passes it here as the argument 'pk'
    return HttpResponse(f"Course Detail Page — Course ID: {pk}")

def course_update(request, pk):
    return HttpResponse(f"Update Course Page — Course ID: {pk}")

def course_delete(request, pk):
    return HttpResponse(f"Delete Course Page — Course ID: {pk}")
