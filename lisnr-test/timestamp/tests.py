from django.test import TestCase

from rest_framework.test import APIRequestFactory
from datetime import datetime

from .views import timestamp


factory = APIRequestFactory()

class TimestampTest(TestCase):
    def test_timestamp(self):
        request = factory.get('/')
        first_timestamp = datetime.utcnow().isoformat()
        test_timestamp = timestamp(request).data['timestamp']
        third_timestamp = datetime.utcnow().isoformat()
        assert (first_timestamp <= test_timestamp <= third_timestamp)
