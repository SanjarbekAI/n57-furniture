from django.db import models

from common.models import BaseModel


class ContactModel(BaseModel):
    full_name = models.CharField(max_length=128)
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = 'contact'
        verbose_name_plural = 'contacts'
