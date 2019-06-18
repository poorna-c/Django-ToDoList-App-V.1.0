from django.db import models
import datetime

# Create your models here.
class ToDoList(models.Model):
    text = models.CharField(max_length=300)
    complete = models.BooleanField(default=False)
    created_date = models.DateTimeField(default = datetime.datetime.now)
    completed_date = models.DateTimeField(blank = True, null=True)
    def __str__(self):
        return str(self.id)