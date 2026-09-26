from django.db import models

# for database configuration 
class Student(models.Model):
    name = models.CharField(
        max_length=30,
    )

    email = models.EmailField()

    description = models.TextField()

    class genderChoices(models.TextChoices):
        MALE = 'M', 'Male'
        FEMALE = 'F', 'Female'
        OTHER = 'O', 'Other'
        PREFER_NOT_TO_SAY = 'NX', 'Prefer not to say'

    gender = models.CharField(
        max_length=2,
        choices=genderChoices.choices,
        default=genderChoices.PREFER_NOT_TO_SAY,
    )

# added owner new field for the authentication and permissions
    owner = models.ForeignKey(
        "auth.User", related_name="students", on_delete=models.CASCADE
    )

    # for model configuration, we write the class Meta to make the database's data to look like the way we want
    class Meta:
        ordering = ["-id"]              # '-' is used for decending



    def __str__(self):
        return self.name



# Other way is to make tuple, instead of creating the class
"""
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]

    gender = models.CharField(
        max_length=1,
        choices=GENDER_CHOICES,
        default='O',
    )
"""