import unittest
import os
import sys
import requests
sys.path.append(os.getcwd())

from citation import Citation

class TestParseInput(unittest.TestCase):
    def test_null(self):
        input = []
        cite = Citation()

        valid = cite.parseAndValidateInput(input)

        self.assertFalse(valid)
        self.assertEqual(cite.errmsg, "No input found")

    def test_valid_both(self):
        input_string = "-f 9780521825146 -s mla"
        input = input_string.split(" ")
        cite = Citation()

        valid = cite.parseAndValidateInput(input)
        self.assertTrue(valid)
        self.assertEqual(cite.isbn, "9780521825146")
        self.assertEqual(cite.style, Citation.MLA)

    def test_valid_swapped(self):
        input_string = "-s apa -f 9780521825146 "
        input = input_string.split(" ")
        cite = Citation()

        valid = cite.parseAndValidateInput(input)

        self.assertTrue(valid)
        self.assertEqual(cite.isbn, "9780521825146")
        self.assertEqual(cite.style, Citation.APA)

    def test_valid_ISBN_only(self):
        input_string = "-f 9780521825146"
        input = input_string.split(" ")

        cite = Citation()

        valid = cite.parseAndValidateInput(input)

        self.assertTrue(valid)
        self.assertEqual(cite.isbn, "9780521825146")
        self.assertEqual(cite.style, Citation.DEFAULT)

    def test_null_style(self):
        input_string = "-f 9780521825146 -s"
        input = input_string.split(" ")

        cite = Citation()

        valid = cite.parseAndValidateInput(input)

        self.assertFalse(valid)
        self.assertEqual(cite.errmsg, "No Style given: -s must be follow by one of [mla, apa, chicago, default]")

    def test_no_style(self):
        input_string = "-s -f 9780521825146"
        input = input_string.split(" ")

        cite = Citation()

        valid = cite.parseAndValidateInput(input)

        self.assertFalse(valid)
        self.assertEqual(cite.errmsg, "No Style given: -s must be follow by one of [mla, apa, chicago, default]")

    def test_null_ISBN(self):
        input_string = "-f"
        input = input_string.split(" ")
        cite = Citation()

        valid = cite.parseAndValidateInput(input)

        self.assertFalse(valid)
        # check errmsg
        self.assertEqual(cite.errmsg, "No ISBN given: -f must be followed by ISBN number")

    def test_no_ISBN_found(self):
        input_string = "-f -s mla"
        input = input_string.split(" ")

        cite = Citation()

        valid = cite.parseAndValidateInput(input)
        self.assertFalse(valid)
        self.assertEqual(cite.errmsg, "No ISBN found: -f must be followed by ISBN number")

    def test_no_ISBN_given(self):
        input_string = "-s chicago"
        input = input_string.split(" ")

        cite = Citation()

        valid = cite.parseAndValidateInput(input)
        self.assertFalse(valid)
        self.assertEqual(cite.errmsg, "No ISBN given: -f is required")


class TestValidateISBN(unittest.TestCase):
    def test_valid_13_ISBN(self):
        input = "9780521825146"

        cite = Citation()

        cite.isbn = input
        valid = cite.validateISBN()

        self.assertTrue(valid)

    def test_valid_10_ISBN(self):
        input = "0521825148"

        cite = Citation()

        cite.isbn = input

        valid = cite.validateISBN()
        self.assertTrue(valid)

    def test_wrong_length(self):
        input = "97805218251"

        cite = Citation()

        cite.isbn = input
        valid = cite.validateISBN()

        self.assertFalse(valid)
        self.assertEqual(cite.errmsg, "ISBN must have 13 or 10 digits")

    def test_invalid_ISBN(self):
        input = "97805abc25146"

        cite = Citation()

        cite.isbn = input
        valid = cite.validateISBN()

        self.assertFalse(valid)
        self.assertEqual(cite.errmsg, "Invalid characters found. Use digits 0-9 only")

    def test_null_ISBN(self):
        input = ""

        cite = Citation()

        cite.isbn = input
        valid = cite.validateISBN()

        self.assertFalse(valid)
        self.assertEqual(cite.errmsg, "No ISBN found")

class TestSetStyle(unittest.TestCase):
    def test_set_mla(self):
        input = "MLA"
        cite = Citation()

        cite.setStyle(input)

        self.assertEqual(cite.style, Citation.MLA)

    def test_set_apa(self):
        input = "apa"
        cite = Citation()

        cite.setStyle(input)

        self.assertEqual(cite.style, Citation.APA)

    def test_set_chicago(self):
        input = "Chicago"
        cite = Citation()

        cite.setStyle(input)

        self.assertEqual(cite.style, Citation.CHICAGO)

    def test_set_default(self):
        input = "default"
        cite = Citation()

        cite.setStyle(input)

        self.assertEqual(cite.style, Citation.DEFAULT)

    def test_set_null(self):
        input = ""
        cite = Citation()

        cite.setStyle(input)

        self.assertEqual(cite.style, Citation.DEFAULT)

    def test_invalid(self):
        input = "some input"
        cite = Citation()

        cite.setStyle(input)

        self.assertEqual(cite.style, Citation.DEFAULT)

class TestGenerateCitationFromData(unittest.TestCase):
    def test_apa(self):
        pass

    def test_mla(self):
        pass

    def test_default(self):
        pass

    def test_chicago(self):
        pass

    def test_no_style(self):
        pass

class TestParseAPIOutput(unittest.TestCase):
    def test_invalid(self):
        pass