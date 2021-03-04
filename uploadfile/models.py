from django.db import models


# Create your models here.
from partial_date import PartialDateField


class BoardPaper(models.Model):
    description = models.CharField(max_length=255, blank=True)
    document = models.FileField(upload_to='BoardPapers/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.description



