from django.db import models
from user.models import CustomUser


class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateField()
    location = models.CharField(max_length=200)

    created_by = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        limit_choices_to={'role': 'organizer'}
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    # ⭐ PARTICIPATION TRACKING SHORTCUT
    @property
    def total_participants(self):
        return self.participation_set.count()