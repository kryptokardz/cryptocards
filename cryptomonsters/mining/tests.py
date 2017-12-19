from django.test import TestCase
from django.urls import reverse_lazy

# Create your tests here.


class MainRoutingTests(TestCase):
    """Tests for the routes in imagersite."""

    def test_mining_route_has_200_response(self):
        """Test that mining route has a 200 response code."""
        response = self.client.get(reverse_lazy('mining'))
        self.assertEqual(response.status_code, 200)

    def test_mining_route_has_content(self):
        """Test that mining route has a contenton the page."""
        response = self.client.get(reverse_lazy('mining'))
        self.assertIn(b'Cryptomonsters', response.content)
