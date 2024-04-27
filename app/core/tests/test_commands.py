from unittest.mock import patch
from django.test import SimpleTestCase
from django.core.management import call_command
from django.db.utils import OperationalError
from psycopg2 import OperationalError as Psycopg2OpError


@patch('core.management.commands.wait_for_db.Command.check')
class TestCommands(SimpleTestCase):

    def test_wait_for_db_called(self,check_patched):
        check_patched.return_value = True
        call_command('wait_for_db')
        check_patched.assert_called_once_with(databases=['default'])

    @patch('time.sleep')
    def test_wait_for_db_delay(self,check_sleep,check_patched):
        check_patched.side_effect = [OperationalError]*2 + [Psycopg2OpError]*3 + [True]
        call_command('wait_for_db')
        self.assertEqual(check_patched.call_count,6)
        check_patched.assert_called_with(databases=['default'])



