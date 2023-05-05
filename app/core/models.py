import datetime
import uuid
from typing import List

from django.db import models
from django.db.models import Sum


class AbstractModel(models.Model):
    """
    Abstract model class to use UUID as primary keys for in all heirs
    """
    primary_id = models.UUIDField(editable=False, primary_key=True, default=uuid.uuid4)
    created_at = models.DateTimeField(editable=False, auto_now_add=True)

    class Meta:
        abstract = True


class UploadedFile(AbstractModel):
    """
    Uploaded file model for history
    """
    file_name = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.file_name} (uploaded {self.created_at.strftime("%d.%m.%Y %H:%M")})'

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'uploaded file'
        verbose_name_plural = 'uploaded files'


class StatDataItem(AbstractModel):
    """
    Model for saving raw data from the Excel files
    """
    id = models.IntegerField()
    date = models.DateField()
    company = models.CharField(max_length=255)
    fact_qliq_data1 = models.FloatField()
    fact_qliq_data2 = models.FloatField()
    fact_qoil_data1 = models.FloatField()
    fact_qoil_data2 = models.FloatField()
    forecast_qliq_data1 = models.FloatField()
    forecast_qliq_data2 = models.FloatField()
    forecast_qoil_data1 = models.FloatField()
    forecast_qoil_data2 = models.FloatField()
    file = models.ForeignKey(UploadedFile, related_name='items', on_delete=models.CASCADE)

    class Meta:
        ordering = ['file', 'id']
