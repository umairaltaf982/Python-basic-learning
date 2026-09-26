from rest_framework import serializers
from .models import Student
# added for the authentication and permissions
from django.contrib.auth.models import User

class StudentSerializer(serializers.ModelSerializer):

    # serializer's Meta configures how the model is converted to and from JSON.
    class Meta:
        model = Student
        fields = "__all__"
        read_only_fields = ["id"]

    def validate_name(self, value):
        if len(value.strip()) < 3:
            raise serializers.ValidationError(
                "Name must contain atleast 3 characters!!!"
            )
        return value

# for authentication and permissions only
    owner = serializers.ReadOnlyField(source="owner.username")


# added for the authentication and permissions
class UserSerializer(serializers.ModelSerializer):
    students = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Student.objects.all()
    )

    class Meta:
        model = User
        fields = "__all__"