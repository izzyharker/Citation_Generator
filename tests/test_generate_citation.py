import unittest
import os
import sys
import requests
sys.path.append(os.getcwd())

from book_information import BookRequest
from citation import Citation

class TestReadBookInformation(unittest.TestCase):
    def read_book_information(self):
        input = "-f 9780521825146"

        book = BookRequest(input)
        book.requestAndWriteBookInformation()

        citation = Citation(book.style, book.data_filename)
        self.assertEqual(citation.authors[0], "Jane Austen")
        self.assertEqual(citation.publisher, "Cambridge University Press")
        self.assertEqual(citation.published_year, "2006")

class TestGenerateCitation(unittest.TestCase):
    def test_cite_APA(self):
        input = "-f 9780521825146 -s APA"

        book = BookRequest(input)
        book.requestAndWriteBookInformation()

        citation = Citation(book.style, book.data_filename)
        cited = citation.citeAPA()
        self.assertEqual(cited, "Austen, J. (2006). \x1B[3mPride and Prejudice\x1B[0m. Cambridge University Press.")

    def test_cite_MLA(self):
        input = "-f 9780521825146 -s MLA"

        book = BookRequest(input)
        book.requestAndWriteBookInformation()

        citation = Citation(book.style, book.data_filename)
        cited = citation.citeMLA()
        self.assertEqual(cited, "Austen, Jane. \x1B[3mPride and Prejudice\x1B[0m. Cambridge University Press, 2006.")

    def test_cite_Chicago(self):
        input = "-f 9780521825146 -s Chicago"

        book = BookRequest(input)
        book.requestAndWriteBookInformation()

        citation = Citation(book.style, book.data_filename)
        cited = citation.citeChicago()
        self.assertEqual(cited, "Austen, Jane. \x1B[3mPride and Prejudice\x1B[0m. Cambridge University Press, 2006.")

    def test_cite_Default(self):
        input = "-f 9780521825146"

        book = BookRequest(input)
        book.requestAndWriteBookInformation()

        citation = Citation(book.style, book.data_filename)
        cited = citation.citeDefault()
        self.assertEqual(cited, "Austen, Jane. \x1B[3mPride and Prejudice\x1B[0m. Cambridge University Press, 2006.")

    def test_generate_author_list(self):
        authors = ["Jane Austen", "Nikola Tesla"]

        self.assertEqual(Citation.generateAuthorString(authors), "Jane Austen and Nikola Tesla")

    def test_generate_null_author_list(self):
        authors = []

        self.assertIsNone(Citation.generateAuthorString(authors))

    def test_generate_title(self):
        title = "Hello"
        subtitle = "World"

        combined = Citation.generateTitleString(title, subtitle)
        self.assertEqual(combined, "Hello: World")