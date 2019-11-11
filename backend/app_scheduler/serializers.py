from rest_framework import serializers
from app_scheduler.models import User, Schedule, Organization

from app_scheduler.scraping import get_user_schedule


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('user_name', 'user_pswd', 'student_id', 'student_pswd')

class ScheduleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Schedule
        field = ('student_id', 'schedule')

class OrganizationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Organization
        fields = ('organization_id', 'team_schedule')
