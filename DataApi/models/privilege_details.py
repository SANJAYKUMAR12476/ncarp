from django.db import models
from .mode_details import Mode_Details

class Previlege_Details(models.Model):
    mode_detail = models.ForeignKey(Mode_Details,on_delete=models.CASCADE)
    name = models.CharField(max_length=155)
    description = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    visibility = models.BooleanField(default=True)    
    
    def __str__(self):
        return self.name
    