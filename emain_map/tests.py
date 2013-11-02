"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase

from emain_map.models import *

class SimpleTest(TestCase):
    def test_basic_addition(self):
        """
        Tests that 1 + 1 always equals 2.
        """
        self.assertEqual(1 + 1, 2)

class UpdateFromAppTestCase(TestCase):
    def testSimple(self):
        self.assertEqual(Location.objects.all().count(), 0)  # none at start
        resp = self.client.post("/api/v1/update_from_app/", )
        self.assertEqual(resp.status_code, 200)
