from django.db import models

class User(models.Model):
    # Referencing a foreign key from the Organization class
    organization  = models.ForeignKey("Organization", to_field='team_id', on_delete=models.SET_NULL, null=True)
    display_name  = models.CharField(max_length=256, null=True)
    student_id    = models.CharField(max_length=256, primary_key=True)
    user_schedule = models.CharField(max_length=256)

    """
    def get_absolute_url(self):
        return reverse('member-detail', args=[str(self.student_id)])

    def __str__(self):
        return self.org
    """

class Organization(models.Model):
    team_id = models.CharField(max_length=256, primary_key=True)
    team_schedule = models.CharField(max_length=256)
    """
    def get_absolute_url(self):
        return reverse('team-detail', args=[str(self.id_team)])

    def __str__(self):
        return self.team_id
    """
