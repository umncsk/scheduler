from django.db import models

class User(models.Model):
    # Referencing a foreign key from the Organization class
    organization  = models.ForeignKey("Organization", to_field='team_id', on_delete=models.SET_NULL, null=True)
    user_name     = models.CharField(max_length=256, null=False)
    user_pswd     = models.CharField(max_length=256, null=False)
    student_id    = models.CharField(max_length=20, null=False)
    student_pswd  = models.CharField(max_length=256, null=False)

    def __str__(self):
        return self.student_id


class Schedule(models.Model):
    student_id = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    schedule = models.CharField(max_length=256)

    def __str__(self):
        return self.schedule


class Organization(models.Model):
    team_id = models.CharField(max_length=256, primary_key=True)
    team_schedule = models.CharField(max_length=256)

    def __str__(self):
        return self.team_schedule

