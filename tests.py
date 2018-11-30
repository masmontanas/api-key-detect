import os
import unittest
from api_key_detect import scan_for_keys

basedir = os.path.abspath(os.path.dirname(__file__))

class TestCase(unittest.TestCase):

    def test_api_key_detection(self):
        key_count = scan_for_keys(basedir)
        assert key_count >= 2


if __name__ == '__main__':
    try:
        unittest.main()
    except:
        pass