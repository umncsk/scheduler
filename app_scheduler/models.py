from django.db import models

class User(models.Model):
    # Referencing a foreign key from the Organization class
    organization  = models.ForeignKey("Organization", to_field='team_id', on_delete=models.SET_NULL, null=True)
    user_name     = models.CharField(max_length=256, null=False)
    user_pswd     = models.CharField(max_length=256, null=False)
    user_schedule = models.CharField(max_length=256)

class Organization(models.Model):
    team_id = models.CharField(max_length=256, primary_key=True)
    team_schedule = models.CharField(max_length=256)
