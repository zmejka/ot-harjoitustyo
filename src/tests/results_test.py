import os
import unittest
from results import Results

dirname = os.path.dirname(__file__)

class TestResults(unittest.TestCase):
    def setUp(self):
        self.test_results = Results("test_results.txt")
        self.test_file = os.path.join(dirname, "..","test_results.txt")

    def test_data_save_to_file(self):
        test_setup = ("TestUser", "48")
        self.test_results.write_results(test_setup)
        results = self.test_results.load_results()
        self.assertEqual(results[0], "TestUser,48\n")
        os.remove(self.test_file)
