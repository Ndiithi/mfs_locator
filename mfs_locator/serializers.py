from django.contrib.auth.models import User, Group
from rest_framework import serializers
from locator.models import Locator
from locator.service import Locator as Locator_Service
from ast import literal_eval as make_tuple

import logging

logger = logging.getLogger('django')


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
    adjuscent = serializers.CharField(required=False, read_only=True)

    class Meta:
        model = Locator
        fields = ['id', 'points']

    # id = serializers.IntegerField(read_only=True)

    def create(self, validated_data):
        """
        Create and return a new locator instance.
        """

        validated_data['points'] = validated_data['points'].replace(" ", "")
        delimeter = "),"
        # strip req string
        params = [
            e+')' for e in validated_data['points'].strip().split(delimeter) if e]
        params[len(params)-1] = params[len(params)-1].replace("))", ")")

        params_tuple = list(set([make_tuple(e) for e in params if e]))

        # points  = validated_data['points'].split(")")

        loc_service = Locator_Service(params_tuple)

        validated_data['adjuscent'] = "%s,%s" % (str(loc_service.get_adjuscent_points()[
                                                 0]), str(loc_service.get_adjuscent_points()[1]))
        logger.info("validated_data")
        logger.info(str(validated_data['adjuscent'][0]))
        returned_data = Locator.objects.create(**validated_data)
        return returned_data
