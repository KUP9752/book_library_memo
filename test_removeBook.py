import unittest
from unittest.mock import patch

from solution import Book, Library


class TestRemoveBook(unittest.TestCase):
  book1args = {"title": "book1", "author": "author1", "publish_date": "15", "isbn": 25}
  book1 = Book(**book1args)
  
  def test_removesBookIfPresent(self):
    lib = Library(test = True)
    self.assertEqual(len(lib.books), 0)
    lib.add_book(**self.book1args)
    self.assertEqual(len(lib.books), 1)
    lib.remove_book(self.book1.isbn)
    self.assertEqual(len(lib.books), 0)
    
  def test_returnsFalseIfTheBookCouldntBeFound(self):
    lib = Library(test = True)
    self.assertEqual(len(lib.books), 0)
    res = lib.remove_book(self.book1.isbn)
    self.assertEqual(len(lib.books), 0) # Check if the length is unchanged
    self.assertFalse(res)
  
  def test_returnsBookTitleIfBookPresent(self):
    lib = Library(test = True)
    lib.add_book(**self.book1args)
    res = lib.remove_book(self.book1.isbn)
    self.assertEqual(res, self.book1.title)
    
    
  def test_checkDataIsSavedToJSONWhenRemoveIsSuccessful(self):
    lib = Library(test = True)
    lib.add_book(**self.book1args)
    with patch.object(lib, "_save_data") as mockLib:
      lib.remove_book(self.book1.isbn)
      
      mockLib.assert_called_once()
      
  def test_checkDataIsNotSavedToJSONWhenRemoveIsAFailure(self):
    lib = Library(test = True)
    
    with patch.object(lib, "_save_data") as mockLib:
      lib.remove_book(self.book1.isbn)
      
      mockLib.assert_not_called()
      
if __name__ == "__main__":
  unittest.main()