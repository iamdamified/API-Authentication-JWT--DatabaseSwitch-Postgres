from django.db import models

# Create your models here.

COURSE_CHOICES = (
    ("B", "Backend"),
    ("F", "Frontend"),
    ("D", "Data Science"),
)

class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    class_code = models.CharField(max_length=12)
    course = models.CharField(choices=COURSE_CHOICES, max_length=13)
    date_joined = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name
