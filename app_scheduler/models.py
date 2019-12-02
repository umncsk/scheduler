from django.db import models

class User(models.Model):
    # Referencing a foreign key from the Organization class
    organization  = models.ForeignKey("Organization", to_field='team_id', on_delete=models.SET_NULL, null=True)
    student_id    = models.CharField(max_length=14, null=False, primary_key=True)
    user_name     = models.CharField(max_length=256, null=False)
    passwd        = models.CharField(max_length=256, null=False)
    schedule      = models.CharField(max_length=256, null=True)

    def __str__(self):
        return self.student_id

class Organization(models.Model):
    team_id       = models.CharField(max_length=256, primary_key=True)
    schedule      = models.CharField(max_length=256, null=True)

    def __str__(self):
        return self.team_id

