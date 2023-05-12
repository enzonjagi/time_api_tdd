from django.test import TestCase

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

        response = self.client.get('/api/time')
        self.assertTrue('current_time' in response.json())