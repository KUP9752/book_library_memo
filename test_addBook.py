import unittest
from unittest.mock import MagicMock
from unittest.mock import Mock

from solution import Book, Library


class TestAddBook(unittest.TestCase):
  
  
  def test_addingOneReturnsTitle(self):
    lib = Library()
    self.assertEqual(lib.add_book("book1", "author1", "15", 25), "book1")
    
  def test_addingOneIncreasesLibrarySize(self):
    lib = Library()
    lib.add_book("book1", "author1", "15", 25)
    self.assertEqual(len(lib.books), 1)

  def test_addingOneIncreasesLibrarySize(self):
    lib = Library()
    lib.add_book("book1", "author1", "15", 25)
    self.assertEqual(len(lib.books), 1)


if __name__ == "__main__":
  unittest.main()