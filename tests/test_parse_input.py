import unittest
import os
import sys
import requests
sys.path.append(os.getcwd())

from book_information import BookRequest

class TestParseInput(unittest.TestCase):
    def test_null(self):
        input = []
        cite = BookRequest()

        valid = cite.parseAndValidateInput(input)

        self.assertFalse(valid)
        self.assertEqual(cite.errmsg, "No input found")

    def test_valid_both(self):
        input_string = "-f 9780521825146 -s mla"
        input = input_string.split(" ")
        cite = BookRequest()

        valid = cite.parseAndValidateInput(input)
        self.assertTrue(valid)
        self.assertEqual(cite.isbn, "9780521825146")
        self.assertEqual(cite.style, BookRequest.MLA)

    def test_valid_swapped(self):
        input_string = "-s apa -f 9780521825146 "
        input = input_string.split(" ")
        cite = BookRequest()

        valid = cite.parseAndValidateInput(input)

        self.assertTrue(valid)
        self.assertEqual(cite.isbn, "9780521825146")
        self.assertEqual(cite.style, BookRequest.APA)

    def test_valid_ISBN_only(self):
        input_string = "-f 9780521825146"
        input = input_string.split(" ")

        cite = BookRequest()

        valid = cite.parseAndValidateInput(input)

        self.assertTrue(valid)
        self.assertEqual(cite.isbn, "9780521825146")
        self.assertEqual(cite.style, BookRequest.DEFAULT)

    def test_null_style(self):
        input_string = "-f 9780521825146 -s"
        input = input_string.split(" ")

        cite = BookRequest()

        valid = cite.parseAndValidateInput(input)

        self.assertFalse(valid)
        self.assertEqual(cite.errmsg, "No Style given: -s must be follow by one of [mla, apa, chicago, default]")

    def test_no_style(self):
        input_string = "-s -f 9780521825146"
        input = input_string.split(" ")

        cite = BookRequest()

        valid = cite.parseAndValidateInput(input)

        self.assertFalse(valid)
        self.assertEqual(cite.errmsg, "No Style given: -s must be follow by one of [mla, apa, chicago, default]")

    def test_null_ISBN(self):
        input_string = "-f"
        input = input_string.split(" ")
        cite = BookRequest()

        valid = cite.parseAndValidateInput(input)

        self.assertFalse(valid)
        # check errmsg
        self.assertEqual(cite.errmsg, "No ISBN given: -f must be followed by ISBN number")

    def test_no_ISBN_found(self):
        input_string = "-f -s mla"
        input = input_string.split(" ")

        cite = BookRequest()

        valid = cite.parseAndValidateInput(input)
        self.assertFalse(valid)
        self.assertEqual(cite.errmsg, "No ISBN found: -f must be followed by ISBN number")

    def test_no_ISBN_given(self):
        input_string = "-s chicago"
        input = input_string.split(" ")

        cite = BookRequest()

        valid = cite.parseAndValidateInput(input)
        self.assertFalse(valid)
        self.assertEqual(cite.errmsg, "No ISBN given: -f is required")


class TestValidateISBN(unittest.TestCase):
    def test_valid_13_ISBN(self):
        input = "-f 9780521825146"

        cite = BookRequest(input)

        valid = cite.validateISBN()

        self.assertTrue(valid)

    def test_valid_10_ISBN(self):
        input = "-f 0521825148"

        cite = BookRequest(input)

        valid = cite.validateISBN()
        self.assertTrue(valid)

    def test_wrong_length(self):
        input = "-f 97805218251"

        cite = BookRequest(input)

        valid = cite.validateISBN()

        self.assertFalse(valid)
        self.assertEqual(cite.errmsg, "ISBN must have 13 or 10 digits")

    def test_invalid_ISBN(self):
        input = "-f 97805abc25146"

        cite = BookRequest(input)

        valid = cite.validateISBN()

        self.assertFalse(valid)
        self.assertEqual(cite.errmsg, "Invalid characters found. Use digits 0-9 only")

    def test_null_ISBN(self):
        input = ""

        cite = BookRequest(input)

        cite.isbn = input
        valid = cite.validateISBN()

        self.assertFalse(valid)
        self.assertEqual(cite.errmsg, "No ISBN found")

class TestSetStyle(unittest.TestCase):
    def test_set_mla(self):
        input = "MLA"
        cite = BookRequest()

        cite.setStyle(input)

        self.assertEqual(cite.style, BookRequest.MLA)

    def test_set_apa(self):
        input = "apa"
        cite = BookRequest()

        cite.setStyle(input)

        self.assertEqual(cite.style, BookRequest.APA)

    def test_set_chicago(self):
        input = "Chicago"
        cite = BookRequest()

        cite.setStyle(input)

        self.assertEqual(cite.style, BookRequest.CHICAGO)

    def test_set_default(self):
        input = "default"
        cite = BookRequest()

        cite.setStyle(input)

        self.assertEqual(cite.style, BookRequest.DEFAULT)

    def test_set_null(self):
        input = ""
        cite = BookRequest()

        cite.setStyle(input)

        self.assertEqual(cite.style, BookRequest.DEFAULT)

    def test_invalid(self):
        input = "some input"
        cite = BookRequest()

        cite.setStyle(input)

        self.assertEqual(cite.style, BookRequest.DEFAULT)