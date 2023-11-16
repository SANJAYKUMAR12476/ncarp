from django.db import models
from .user_details import Login_User_Details


class Project_User_Mapping(models.Model):
    user_detail = models.ForeignKey(Login_User_Details,on_delete=models.CASCADE)
    project_name = models.CharField(max_length=155)
    project_description = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    logo = models.TextField()
    created_on = models.DateTimeField(auto_now=True)
    modified_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.project_name +'-->' +self.user_detail.user_name
    