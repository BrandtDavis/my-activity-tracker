import unittest

from .context import timeUtils

class TestTimeUtils(unittest.TestCase):
    
    def test_windows_when_start_and_end_are_equal(self):
        date_windows = timeUtils.get_date_windows('1999-01-01', '1999-01-01')
        self.assertEqual(date_windows, ['1998-12-28'])

    def test_first_time_window(self):
        date_windows = timeUtils.get_date_windows('1999-01-01', '1999-01-10')
        self.assertEqual(date_windows[0], '1998-12-28')

    def test_last_time_window(self):
        date_windows = timeUtils.get_date_windows('1999-01-01', '1999-01-10')
        self.assertEqual(date_windows[-1], '1999-01-04')

if __name__ == '__main__':
    unittest.main()