from django.test import TestCase, Client
from django.urls import reverse


class TestViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.index_url = "mercury:index"
        self.dashboard_url = "mercury:dashboard"
        self.simulator_url = "mercury:simulator"

    def test_HomePageView_GET_fail(self):
        response = self.client.get(reverse(self.index_url))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "login.html")

    def test_DashboardView_GET_fail(self):
        response = self.client.get(reverse(self.dashboard_url))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "login.html")

    def test_SimulatorView_GET_fail(self):
        response = self.client.get(reverse(self.simulator_url))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "login.html")
