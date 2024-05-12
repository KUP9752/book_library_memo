import unittest
from unittest.mock import patch

import sys
sys.path.append("../")

from src.solution import Book, Library


class TestCheckBookByISBN(unittest.TestCase):
  book1args = {"title": "book1", "author": "author1", "publish_date": "15", "isbn": 25}
  book1 = Book(**book1args)
  
  
  def test_bookNotInReturnsFalse(self):
    lib = Library(test = True)
    res = lib.check_book_by_isbn(self.book1.isbn)
    self.assertFalse(res)
  
  def test_bookInReturnsTrue(self):
    lib = Library(test = True)
    lib.add_book(**self.book1args) # add book 1
    res = lib.check_book_by_isbn(self.book1.isbn) # check book 1
    self.assertEqual(res, True )
    
  def test_checkDataIsNeverSavedTOJSONOnThisMethod(self):
    lib = Library(test = True)
    
    with patch.object(lib, "_save_data") as mockLib:
      lib.check_book_by_isbn(self.book1.isbn)
      
      mockLib.assert_not_called()
    
if __name__ == "__main__":
  unittest.main()