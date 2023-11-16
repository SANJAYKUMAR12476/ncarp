from django.db import models

class Mode_Details(models.Model):
    mode_name = models.CharField(max_length=155)
    mode_description = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.mode_name
