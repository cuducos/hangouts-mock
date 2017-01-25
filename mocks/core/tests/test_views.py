from unittest.mock import patch

from django.test import TestCase
from requests.exceptions import ConnectionError

from mocks.core.models import Congressperson
from mocks.core.views import _is_chamber_of_deputies_on


class TestGet(TestCase):

    @patch.object(Congressperson.objects, 'all')
    @patch('mocks.core.views._is_chamber_of_deputies_on')
    def test_server_is_on_but_not_data(self, server, people):
        server.return_value = True
        people.return_value = None
        resp = self.client.get('/')
        html = resp.content.decode('utf-8')
        self.assertIn('text-success', html)
        self.assertIn('Sorry', html)

    @patch.object(Congressperson.objects, 'all')
    @patch('mocks.core.views._is_chamber_of_deputies_on')
    def test_server_is_off_but_not_data(self, server, people):
        server.return_value = False
        people.return_value = None
        resp = self.client.get('/')
        html = resp.content.decode('utf-8')
        self.assertIn('text-danger', html)
        self.assertIn('Sorry', html)

    @patch.object(Congressperson.objects, 'all')
    @patch('mocks.core.views._is_chamber_of_deputies_on')
    def test_server_is_on_and_we_have_data(self, server, people):
        server.return_value = True
        people.return_value = (
            { 'applicant_id': 42, 'name': 'Fulano'},
            { 'applicant_id': 24, 'name': 'Ciclano'},
        )
        resp = self.client.get('/')
        html = resp.content.decode('utf-8')
        self.assertIn('text-success', html)
        self.assertIn('<table class="table">', html)

    @patch.object(Congressperson.objects, 'all')
    @patch('mocks.core.views._is_chamber_of_deputies_on')
    def test_server_is_off_and_we_have_data(self, server, people):
        server.return_value = False
        people.return_value = (
            { 'applicant_id': 42, 'name': 'Fulano'},
            { 'applicant_id': 24, 'name': 'Ciclano'},
        )
        resp = self.client.get('/')
        html = resp.content.decode('utf-8')
        self.assertIn('text-danger', html)
        self.assertIn('<table class="table">', html)


class TestIsTheServerOn(TestCase):

    @patch('mocks.core.views.head')
    def test_on(self, mocked_head):
        mocked_head.return_value.status_code = 200
        self.assertTrue(_is_chamber_of_deputies_on())

    @patch('mocks.core.views.head')
    def test_off(self, mocked_head):
        mocked_head.return_value.status_code = 500
        self.assertFalse(_is_chamber_of_deputies_on())

    @patch('mocks.core.views.head')
    def test_error(self, mocked_head):
        mocked_head.side_effect = ConnectionError
        self.assertFalse(_is_chamber_of_deputies_on())
