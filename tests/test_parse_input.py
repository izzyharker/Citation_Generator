import unittest
import os
import sys
sys.path.append(os.getcwd())

import parse_input as parse

class TestParseInput(unittest.TestCase):
    def test_null(self):
        input = []

        valid, _, errmsg = parse.parseInput(input)
        self.assertFalse(valid)
        self.assertEqual(errmsg, "No input found")

    def test_valid_both(self):
        input_string = "-f 9780521825146 -s mla"
        input = input_string.split(" ")

        valid, search_parameters, _ = parse.parseInput(input)
        self.assertTrue(valid)
        self.assertEqual(search_parameters["ISBN"], "9780521825146")
        self.assertEqual(search_parameters["Style"], parse.MLA)

    def test_valid_swapped(self):
        input_string = "-s apa -f 9780521825146 "
        input = input_string.split(" ")

        valid, search_parameters, _ = parse.parseInput(input)
        self.assertTrue(valid)
        self.assertEqual(search_parameters["ISBN"], "9780521825146")
        self.assertEqual(search_parameters["Style"], parse.APA)

    def test_valid_ISBN_only(self):
        input_string = "-f 9780521825146"
        input = input_string.split(" ")

        valid, search_parameters, _ = parse.parseInput(input)
        self.assertTrue(valid)
        self.assertEqual(search_parameters["ISBN"], "9780521825146")
        self.assertEqual(search_parameters["Style"], parse.DEFAULT)

    def test_null_style(self):
        input_string = "-f 9780521825146 -s"
        input = input_string.split(" ")

        valid, _, errmsg = parse.parseInput(input)
        self.assertFalse(valid)
        self.assertEqual(errmsg, "No Style given: -s must be follow by one of [mla, apa, chicago, default]")

    def test_no_style(self):
        input_string = "-s -f 9780521825146"
        input = input_string.split(" ")

        valid, _, errmsg = parse.parseInput(input)
        self.assertFalse(valid)
        self.assertEqual(errmsg, "No Style given: -s must be follow by one of [mla, apa, chicago, default]")

    def test_null_ISBN(self):
        input_string = "-f"
        input = input_string.split(" ")

        valid, _, errmsg = parse.parseInput(input)
        self.assertFalse(valid)
        # check errmsg
        self.assertEqual(errmsg, "No ISBN given: -f must be followed by ISBN number")

    def test_no_ISBN_found(self):
        input_string = "-f -s mla"
        input = input_string.split(" ")

        valid, _, errmsg = parse.parseInput(input)
        self.assertFalse(valid)
        self.assertEqual(errmsg, "No ISBN found: -f must be followed by ISBN number")

    def test_no_ISBN_given(self):
        input_string = "-s chicago"
        input = input_string.split(" ")

        valid, _, errmsg = parse.parseInput(input)
        self.assertFalse(valid)
        self.assertEqual(errmsg, "No ISBN given: -f is required")


class TestValidateISBN(unittest.TestCase):
    def test_valid_13_ISBN(self):
        input = "9780521825146"

        valid, _ = parse.validateISBN(input)
        self.assertTrue(valid)

    def test_valid_10_ISBN(self):
        input = "0521825148"

        valid, _ = parse.validateISBN(input)
        self.assertTrue(valid)

    def test_wrong_length(self):
        input = "97805218251"

        valid, errmsg = parse.validateISBN(input)
        self.assertFalse(valid)
        self.assertEqual(errmsg, "ISBN must have 13 or 10 digits")

    def test_invalid_ISBN(self):
        input = "97805abc25146"

        valid, errmsg = parse.validateISBN(input)
        self.assertFalse(valid)
        self.assertEqual(errmsg, "Invalid characters found. Use digits 0-9 only")

    def test_null_ISBN(self):
        input = ""

        valid, errmsg = parse.validateISBN(input)
        self.assertFalse(valid)
        self.assertEqual(errmsg, "No ISBN found")

class TestSetStyle(unittest.TestCase):
    def test_set_mla(self):
        input = "MLA"
        style = parse.setStyle(input)

        self.assertEqual(style, parse.MLA)

    def test_set_apa(self):
        input = "apa"
        style = parse.setStyle(input)

        self.assertEqual(style, parse.APA)

    def test_set_chicago(self):
        input = "Chicago"
        style = parse.setStyle(input)

        self.assertEqual(style, parse.CHICAGO)

    def test_set_default(self):
        input = "default"
        style = parse.setStyle(input)

        self.assertEqual(style, parse.DEFAULT)

    def test_set_null(self):
        input = ""
        style = parse.setStyle(input)

        self.assertEqual(style, parse.DEFAULT)

    def test_invalid(self):
        input = "some input"
        style = parse.setStyle(input)

        self.assertEqual(style, parse.DEFAULT)