from django.db import models
from .project_user_mapping_details import Project_User_Mapping

class Page_User_Mapping(models.Model):
    project_user_mapping = models.ForeignKey(Project_User_Mapping,on_delete=models.ForeignKey)
    page_name = models.CharField(max_length=155)
    page_description = models.CharField(max_length=255)
    access_to = models.CharField(max_length=155)
    background = models.CharField(max_length=155)
    layout = models.CharField(max_length=155)
    data = models.JSONField(default=None)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.page_name
