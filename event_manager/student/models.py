from django.db import models
from user.models import CustomUser
from organizer.models import Event


class Participation(models.Model):
    student = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        limit_choices_to={'role': 'student'}
    )

    event = models.ForeignKey(Event, on_delete=models.CASCADE)

    joined_at = models.DateTimeField(auto_now_add=True)

    status = models.CharField(
        max_length=20,
        default='registered'
    )

    def __str__(self):
        return f"{self.student.username} -> {self.event.title}"
    
    class Meta:
        unique_together = ('student', 'event')