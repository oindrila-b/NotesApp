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
    version = models.AutoField()
    priority = models.CharField(max_length=1, choices=PRIORITY_MODEL)
