from io import StringIO
from unittest.mock import Mock, call, patch

from django.test import TestCase

from mocks.core.management.commands.congresspeople import Command
from mocks.core.models import Congressperson


class TestCommand(TestCase):

    @patch('mocks.core.management.commands.congresspeople.os.path.exists')
    @patch('mocks.core.management.commands.congresspeople.open')
    @patch('mocks.core.management.commands.congresspeople.print')
    @patch('mocks.core.management.commands.congresspeople.DictReader')
    @patch.object(Congressperson.objects, 'create')
    def test_existing_file(self, create, reader, print, open, exists):
        exists.return_value = True
        open.return_value = StringIO()
        reader.return_value = ({'ahoy': 42} for number in range(3))

        command = Command()
        command.handle(source='data.csv')
        print.assert_has_calls((
            call('Reading dataset…'),
            call('1 congresspeople imported…', end='\r'),
            call('2 congresspeople imported…', end='\r'),
            call('3 congresspeople imported…', end='\r'),
            call(),
            call('Done!')
        ))
        self.assertEqual(3, len(create.call_args_list))
        self.assertEqual(3, command.count)

    @patch('mocks.core.management.commands.congresspeople.os.path.exists')
    def test_non_existing_file(self, exists):
        exists.return_value = False
        with self.assertRaises(FileNotFoundError):
            Command().handle(source='data.csv')

    def test_add_arguments(self):
        parser = Mock()
        Command().add_arguments(parser)
        parser.add_argument.assert_called_once_with(
            'source', help='Path to the .csv dataset'
        )
