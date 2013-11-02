"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase

from django.contrib.auth.models import User
from emain_map.models import *
from datetime import date

class SimpleTest(TestCase):
    def test_basic_addition(self):
        """
        Tests that 1 + 1 always equals 2.
        """
        self.assertEqual(1 + 1, 2)

class UpdateFromAppTestCase(TestCase):
    def setUp(self):
        Location.objects.all().delete()
        self.user, _ = User.objects.get_or_create(username="test@example.com")
        self.user.set_password("password")
        self.user.save()
        self.client.login(username="test@example.com", password="password")

    def testSimple(self):
        """
        Simple post to ajax
        """
        self.assertEqual(Location.objects.all().count(), 0)  # none at start
        resp = self.client.post("/api/v1/update_from_app/", {'lat': 53.34146, 'lon':-6.26876})
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(Location.objects.all().count(), 1)  # now there is one
        location = Location.objects.all()[0]
        self.assertEqual(location.when.date(), date.today())
        self.assertEqual(location.user, self.user)
        self.assertEqual(location.lat, 53.34146)
        self.assertEqual(location.lon, -6.26876)

    def testCanUseOldTime(self):
        """
        Check you can include a time
        """
        resp = self.client.post("/api/v1/update_from_app/", {'lat': 53.34146, 'lon':-6.26876, 'when': '2013-01-01 12:00:00'})
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(Location.objects.all().count(), 1)  # now there is one
        location = Location.objects.all()[0]
        # if off by serveral hours, check your timezone
        self.assertEqual(location.when.isoformat(), '2013-01-01T12:00:00+00:00')
