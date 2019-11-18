from rest_framework import serializers
from app_scheduler.models import User, Organization
from django.contrib.auth.hashers import make_password

from app_scheduler.scraping import get_user_schedule


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('user_name', 'user_pswd', 'student_id', 'student_pswd', 'user_schedule')

    def create(self, validated_data):
        user_pswd = validated_data.get('user_pswd')
        student_id = validated_data.get('student_id')
        student_pswd = validated_data.get('student_pswd')
        user_schedule = get_user_schedule(student_id, student_pswd)
        validated_data['user_pswd'] = make_password(user_pswd)
        validated_data['student_pswd'] = make_password(student_pswd)
        validated_data['user_schedule'] = user_schedule
        return User.objects.create(**validated_data)

class OrganizationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Organization
        fields = ('organization_id', 'team_schedule')
