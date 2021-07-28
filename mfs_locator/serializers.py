from django.contrib.auth.models import User, Group
from rest_framework import serializers
from locator.models import Locator
import logging

logger = logging.getLogger(__name__)

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


class LocatorSerializer(serializers.Serializer):
    points = serializers.CharField(required=True, allow_blank=False)
    # adjuscent = serializers.CharField(required=True, allow_blank=False)

    class Meta:
        model = Locator
        fields = ['id', 'points']

    # id = serializers.IntegerField(read_only=True)
    

    def create(self, validated_data):
        """
        Create and return a new locator instance.
        """
        returned_data = Locator.objects.create(**validated_data)
        logger.info("validated_data=====================>>")
        logger.info(validated_data)
        return returned_data
# post = Post.objects.create(title='First post', text='This is a first post')
# print(PostSerializer(post).data)
    # def update(self, instance, validated_data):
    #     """
    #     Update and return an existing locator instance
    #     """
    #     instance.points = validated_data.get('points', instance.points)
    #     instance.save()

    #     return instance