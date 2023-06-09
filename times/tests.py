from unittest.mock import patch
from django.test import TestCase
from django.utils import timezone
from datetime import datetime

class TimeApiTestCase(TestCase):
    """Test cases for the time api"""

    def test_time_url_is_status_okay(self):
        """A test case for the response status - 200"""

        response = self.client.get('/api/time/')
        self.assertEqual(200, response.status_code)

    def test_time_api_should_return_json(self):
        """Test case for JSONResponse from /api/time/"""

        response = self.client.get('/api/time/')
        self.assertEqual('application/json', response['Content-Type'])

    def test_time_api_should_include_current_time_key(self):
        """Test case for current time key in HTTPResonse"""

        response = self.client.get('/api/time/')
        self.assertTrue('current_time' in response.json())

    def test_time_api_should_return_valid_iso861_format(self):
        """Test if the response returns iso861 format"""

        response = self.client.get('/api/time/')
        current_time = response.json()['current_time']
        dt = datetime.strptime(current_time, '%Y-%m-%dT%H:%M:%SZ')
        self.assertTrue(isinstance(dt, datetime))

    def test_time_api_should_return_current_utc_time(self):
        """Test current if it response returns current utc time"""

        with patch('django.utils.timezone.now') as mock_tz_now:
            expected_datetime = datetime.now().replace(microsecond=0)
            mock_tz_now.return_value = expected_datetime

            response = self.client.get('/api/time/')
            current_time = response.json()['current_time']
            parsed_time = datetime.strptime(current_time, '%Y-%m-%dT%H:%M:%SZ')

            self.assertEqual(parsed_time, expected_datetime)