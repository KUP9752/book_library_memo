import unittest
from unittest.mock import patch

from solution import Book, Library

class TestAddBook(unittest.TestCase):
  book1args = {"title": "book1", "author": "author1", "publish_date": "15", "isbn": 25}
  book1 = Book(**book1args)
  
  def test_addingOneReturnsTitle(self):
    lib = Library(test = True)
    self.assertEqual(lib.add_book(**self.book1args), self.book1.title)
    
  def test_addingOneIncreasesLibrarySize(self):
    lib = Library(test = True)
    self.assertEqual(len(lib.books), 0) # no books yet
    lib.add_book(**self.book1args)
    self.assertEqual(len(lib.books), 1) # 1 book after addition

  def test_addingSameReturnsFalse(self):
    lib = Library(test = True)
    first = lib.add_book(**self.book1args)
    second = lib.add_book(**self.book1args)
    self.assertEqual(first, self.book1.title) # Check we can succesfully add the first one
    self.assertFalse(second) # check the second one doesn't get added at all

  def test_checkDataIsSavedToJSONWhenAddIsSuccessful(self):
    lib = Library(test = True)
    
    with patch.object(lib, "_save_data") as mockLib:
      lib.add_book(**self.book1args)
      
      mockLib.assert_called_once()
      
  def test_checkDataIsNotSavedToJSONWhenAddIsAFailure(self):
    lib = Library(test = True)
    lib.add_book(**self.book1args)
    
    with patch.object(lib, "_save_data") as mockLib:
      lib.add_book(**self.book1args)
      
      mockLib.assert_not_called()
      
      
    

if __name__ == "__main__":
  unittest.main()