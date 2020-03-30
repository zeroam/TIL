import unittest
from my_calendar import get_holidays
from requests.exceptions import Timeout
from unittest.mock import patch


class TestCalendar(unittest.TestCase):
    def test_get_holidays_timeout(self):
        with patch('my_calendar.requests') as mock_reqeusts:
            mock_reqeusts.get.side_effect = Timeout
            with self.assertRaises(Timeout):
                get_holidays()
                mock_reqeusts.get.assert_called_once()


if __name__ == '__main__':
    unittest.main()
