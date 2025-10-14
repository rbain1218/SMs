from django.db import models
from teachers.models import Teacher  # Optional: to assign a class teacher

class ClassModel(models.Model):
    class_name = models.CharField(max_length=50, unique=True)
    section = models.CharField(max_length=10, blank=True)
    class_teacher = models.ForeignKey(
        Teacher,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='class_groups'
    )

    def __str__(self):
        section = f" - {self.section}" if self.section else ""
        return f"{self.class_name}{section}"
