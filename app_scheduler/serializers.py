from rest_framework import serializers
from app_scheduler.models import User, Organization

from app_scheduler.scraping import get_user_schedule


class UserSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.IntegerField(read_only=True)
    organization = serializers.CharField(required=True, allow_blank=True)
    user_schedule = serializers.CharField(required=False, allow_blank=True, max_length=128)
    user_name = serializers.CharField(required=False, allow_blank=False, max_length=64)
    user_pswd = serializers.CharField(required=True, allow_blank=False, max_length=64)
    student_id = serializers.CharField(required=True, allow_blank=False)
    student_pswd = serializers.CharField(required=True, allow_blank=False)

    def create(self, validated_data):
        """
        Create and return a new `User` instance, given the validated data.
        """
        return User.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `User` instance, given the validated data.
        """
        instance.organization = validated_data.get('organization', instance.organization)
        instance.user_name = validated_data.get('user_name', instance.user_name)
        instance.user_pswd = validated_data.get('user_pswd', instance.user_pswd)
        instance.student_id = validated_data.get('student_id', instance.student_id)
        instance.studnet_pswd = validated_data.get('student_pswd', instance.student_pswd)
        instance.user_schedule = get_user_schedule(instance.student_id, instance.student_pswd)
        instance.save()
        return instance

    class Meta:
        model = User
        fields = ['id', 'organization', 'user_name', 'user_pswd', 'student_id', 'student_pswd', 'user_schedule']


class OrganizationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Organization
        fields = ['url', 'name']
