import unittest
import os
import sys
sys.path.append(os.getcwd())

import request_information as req

class TestConfigureRequest(unittest.TestCase):
    def test_configure_url(self):
        input = "9780521825146"
        output_url = req.configureBookUrl(input)

        self.assertEqual(output_url, "https://www.googleapis.com/books/v1/volumes?q=isbn:9780521825146&key=" + req.getAPIKey())