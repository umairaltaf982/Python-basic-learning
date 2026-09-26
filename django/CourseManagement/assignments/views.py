from django.http import HttpResponse


# Placeholder views — will be replaced with real logic in Phase 8.

def assignment_list(request):
    return HttpResponse("Assignment List Page")

def assignment_detail(request, pk):
    return HttpResponse(f"Assignment Detail Page — Assignment ID: {pk}")

def assignment_submit(request, pk):
    return HttpResponse(f"Submit Assignment ID: {pk}")

def assignment_grade(request, pk):
    return HttpResponse(f"Grade Assignment ID: {pk}")
