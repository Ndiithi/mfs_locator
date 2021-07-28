import json
import logging
from django.urls import reverse
from locator.models import Locator
from django.test import Client, TestCase
from django.contrib.auth.models import User
# from requests.auth import HTTPBasicAuth

from rest_framework.test import APITestCase
from rest_framework.views import status
from rest_framework.test import APIClient


class PostPointsCreateAPIView(APITestCase):
    def setUp(self) -> None:
        self.url = 'http://localhost:8000/locator/'
        self.content_type = "application/json"
        self.superuser = User.objects.create_superuser(
            'mfsuser', 'mfsuser@gmail.com', 'I@mtowers26')
        self.client.login(username='mfsuser', password='I@mtowers26')

    def test_record_created(self):
        self.assertEquals(
            Locator.objects.count(),
            0
        )
        data = {
            'points': '(2,3),(1,1),(5,4),(2,3),(1,1),(5,4)'
        }
        response = self.client.post(
            self.url, data=data, CONTENT_TYPE=self.content_type)
        # data = json.loads(response.content)
        self.assertEquals(response.status_code, status.HTTP_201_CREATED)

    def test_create_post(self):

        data = {
            'points': '(2,3),(1,1),(5,4),(2,3),(1,1),(5,4)'
        }
        response = self.client.post(
            self.url, data=data, CONTENT_TYPE=self.content_type)

        self.assertEquals(
            Locator.objects.count(),
            1
        )

    def test_accurate_adjuscent_point(self):

        data = {
            'points': '(2,3),(1,1),(5,4),(2,3),(1,1),(5,4)'
        }
        response = self.client.post(
            self.url, data=data, CONTENT_TYPE=self.content_type)

        locator = Locator.objects.first()
        self.assertEquals(
            locator.adjuscent,
            "[2 3],[1 1]"
        )
