from django.test import TestCase
from django.urls import reverse_lazy

# Create your tests here.


class MainRoutingTests(TestCase):
    """Tests for the routes in imagersite."""

    def test_home_route_has_200_response(self):
        """Test that home route has a 200 response code."""
        response = self.client.get(reverse_lazy('home'))
        self.assertEqual(response.status_code, 200)

    def test_home_route_has_content(self):
        """Test that home route has a contenton the page."""
        response = self.client.get(reverse_lazy('home'))
        self.assertIn(b'Cryptomonsters', response.content)

