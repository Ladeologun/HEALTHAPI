from django.db import models
from authentication.models import User
import uuid


class MenstrualCycle(models.Model):
    id = models.UUIDField(unique=True, primary_key=True,default=uuid.uuid4, editable=False)
    Last_period_date = models.DateField()
    Cycle_average = models.PositiveIntegerField()
    Period_average = models.PositiveIntegerField()
    Start_date = models.DateField()
    End_date = models.DateField()
    cycle_event_date = models.DateField(blank=True,null=True)
    owner = models.OneToOneField(User, on_delete = models.CASCADE)
   


