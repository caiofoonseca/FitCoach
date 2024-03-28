from django.db import models
import datetime
from pytz import timezone

# Create your models here.
class Question(models.Model):
    title = models.CharField(max_length=200, null=False)
    details = models.TextField(null=False)
    have_tried = models.TextField()
    created_date = models.DateTimeField("Created on")

    def __str__(self):
        return "[" + str(self.id) + "] " + self.title
    
    def was_published_recently(self):
        return self.created_date >= timezone.now() - datetime.timedelta(days=1)

    def __str__(self):
        return "[" + str(self.id) + "] " + self.title

    def was_published_recently(self):
        return self.created_date >= timezone.now() - datetime.timedelta(days=1)