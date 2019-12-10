from rest_framework import serializers
from app_scheduler.models import User, Group
from django.contrib.auth.hashers import make_password
from app_scheduler.scraping import get_user_schedule


class UserSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = User
        fields = ['username', 'student_id', 'password', 'groupname']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user_schedule = get_user_schedule(validated_data['student_id'], validated_data['password'])
        user = User(
            username=validated_data['username'],
            student_id=validated_data['student_id'],
            schedule=user_schedule,
        )
        user.set_password(validated_data['password'])
        user.save()

        # Add student lecture data to group
        group = Group.objects.get(groupname=validated_data.get('groupname'))
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
        fields = ['groupname']

    def create(self, validated_data):
        group = Group(
            groupname=validated_data['groupname'],
        )

        group.save()

        return group
