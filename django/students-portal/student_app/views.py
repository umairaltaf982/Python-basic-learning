from student_app.models import Student
from student_app.serializers import StudentSerializer
from rest_framework import generics
from rest_framework import mixins
from django.contrib.auth.models import User
from student_app.serializers import UserSerializer
# for authentication and permissions only
from rest_framework import permissions
from rest_framework.permissions import BasePermission, SAFE_METHODS, IsAuthenticated
# For downloading CSV 
import csv
from django.http import HttpResponse
from rest_framework.views import APIView


class IsOwnerOrReadOnly(BasePermission):
    """
    Only the owner of the student record can edit or delete it.
    Everyone else gets read-only access.
    """
    def has_object_permission(self, request, view, obj):
        # GET, HEAD, OPTIONS are allowed for anyone
        if request.method in SAFE_METHODS:
            return True
        # Write permissions only for the owner
        return obj.owner == request.user


"""
List all students, or create a new student.
"""
class StudentList(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    generics.GenericAPIView
):

    queryset = Student.objects.all()
    serializer_class = StudentSerializer


    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

# for authentication and permissions
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

"""
    Retrieve, update or delete a student instance.
"""
class StudentDetail(
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    generics.GenericAPIView
):

    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
        
# for authentication and permissions
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]


# added for the authentication and permissions
class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


# For downloading CSV
class StudentCSVDownload(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        students = Student.objects.filter(owner=request.user)

        response = HttpResponse(content_type="text/csv")
        response["Content-Disposition"] = 'attachment; filename="my_students.csv"'

        writer = csv.writer(response)
        # header row
        writer.writerow(["ID", "Name", "Email", "Gender", "Description"])

        # data rows
        for student in students:
            writer.writerow([
                student.id,
                student.name,
                student.email,
                student.get_gender_display(),
                student.description,
            ])

        return response
