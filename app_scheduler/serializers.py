from rest_framework import serializers
from app_scheduler.models import User, Organization
from django.contrib.auth.hashers import make_password

from app_scheduler.scraping import get_user_schedule


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        # touple of fields you want to output
        fields = ('user_name', 'student_id', 'passwd')

    def create(self, validated_data):
        user_name = validated_data.get('user_name')
        student_id = validated_data.get('student_id')
        passwd = validated_data.get('passwd')
        schedule = get_user_schedule(student_id, passwd)
        validated_data['passwd'] = make_password(passwd)
        validated_data['schedule'] = schedule
        return User.objects.create(**validated_data)

class OrganizationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Organization
        # touple of fields you want to output
        fields = ('organization_id', 'schedule')
