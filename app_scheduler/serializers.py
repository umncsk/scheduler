from rest_framework import serializers
from app_scheduler.models import User, Organization
from django.contrib.auth.hashers import make_password

from app_scheduler.scraping import get_user_schedule


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'student_id', 'password', 'organization']
        write_only_fields = ['password']

    def create(self, validated_data):
        student_id = validated_data.get('student_id')
        password = validated_data.get('password')
        user_schedule = get_user_schedule(student_id, password)
        validated_data['password'] = make_password(password)
        validated_data['schedule'] = user_schedule

        # Add student lecture data to group
        organization = Organization.objects.get(organization_id=validated_data.get('organization'))
        organization_schedule = organization.schedule
        data = ""
        for i,j in zip(user_schedule, organization_schedule):
            data += str(int(i) + int(j))
        organization.schedule = data
        organization.save()
        # print(organization_schedule)

        return User.objects.create(**validated_data)


class OrganizationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Organization
        # touple of fields you want to output
        fields = ['organization_id']

    def create(self, validated_data):
        user = User.objects.get(organization_id=validated_data['organization_id'])
        print(user.organization_id)
