from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
from .choices import USER_TYPE_CHOICES

# Create your models here.

class User(AbstractUser):
    # user_type = models.CharField(max_length=1, choices=USER_TYPE_CHOICES)
    is_student = models.BooleanField('student status', default=False)
    is_mentor = models.BooleanField('mentor status', default=False)


class CalendarEvents(models.Model):
    date = models.DateField('Date',help_text='Day of the event')
    start_time = models.TimeField('Start Time',help_text='Start time')
    end_time = models.TimeField('End Time',help_text='End time')
    reason = models.TextField('Reason',help_text='Reason for the call')
    user = models.ManyToManyField(User)


    class Meta:
        verbose_name_plural = 'Calendar Events'

    def clean(self):
        if self.end_time<= self.start_time:
            raise ValidationError('End time must be after start time')

