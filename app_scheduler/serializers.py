from rest_framework import serializers
from app_scheduler.models import User, Group
from django.contrib.auth.hashers import make_password

from app_scheduler.scraping import get_user_schedule


class UserSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = User
        fields = ['username', 'student_id', 'password', 'group_id']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        #student_id = validated_data.get('student_id')
        #password = validated_data.get('password')
        user_schedule = get_user_schedule(validated_data['student_id'], validated_data['password'])
        #validated_data['password'] = make_password(password)
        #validated_data['schedule'] = user_schedule

        user = User(
            username=validated_data['username'],
            student_id=validated_data['student_id'],
            schedule=user_schedule,
        )
        user.set_password(validated_data['password'])
        user.save()

        # Add student lecture data to group
        group = Group.objects.get(group_id=validated_data.get('group_id'))
        group_schedule = group.schedule
        data = ""
        for i,j in zip(user_schedule, group_schedule):
            data += str(int(i) + int(j))
        group.schedule = data
        group.save()
        # print(organization_schedule)

        return user

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        # touple of fields you want to output
        fields = ['group_id']

    def create(self, validated_data):
        group = Group(
            group_id=validated_data['group_id'],
        )

        group.save()

        return group
