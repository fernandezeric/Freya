import tempfile

from unittest import TestCase
from Freya_alerce.core.base import Base


class TestCreateApi(TestCase):
    
    def setUp(self):
        self.temp_FreyaApi = tempfile.TemporaryDirectory()

    def test(self):
        Base(path=self.temp_FreyaApi.name).create_new_api()

    def tearDown(self):
        self.temp_FreyaApi.cleanup()

if __name__ == '__main__':
    unittest.main() 