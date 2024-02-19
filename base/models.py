from django.db import models


# Create your models here.

class Note(models.Model):
    PRIORITY_MODEL = {
        "H": "High",
        "M": "Medium",
        "L": "Low"
    }

    title = models.CharField(max_length=200)
    content = models.TextField()
    version = models.IntegerField(default=0)
    priority = models.CharField(max_length=1, choices=PRIORITY_MODEL)


class VersionHistory(models.Model):
    note_id = models.IntegerField()
    notes = models.ManyToManyField(Note)
