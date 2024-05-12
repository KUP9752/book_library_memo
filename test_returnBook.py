import unittest
from unittest.mock import patch

from solution import Book, User, Library


class TestReturnBook(unittest.TestCase):
  book1args = {"title": "book1", "author": "author1", "publish_date": "15", "isbn": 25}
  book1 = Book(**book1args)
  
  def test_bookDoesntExistReturnsFalse(self):
    lib = Library(test = True)
    res = lib.return_book(self.book1.isbn)  
    self.assertFalse(res)
    
  def test_bookExistButNotBorrwed(self):
    lib = Library(test = True)
    lib.add_book(**self.book1args)
    res = lib.return_book(self.book1.isbn)  
    self.assertFalse(res)
    
  def test_bookExistAndBorrwedReturnsTrue(self):
    lib = Library(test = True)
    lib.add_book(**self.book1args)
    
    lib.books[0].is_borrowed = True
    lib.books[0].borrower = 18 # someone
    
    res = lib.return_book(self.book1.isbn)  
    self.assertEqual(res, True)
    
  def test_bookExistAndBorrwedShouldUpdateTheBookToBeUnborrowedAgain(self):
    lib = Library(test = True)
    lib.add_book(**self.book1args)
    
    lib.books[0].is_borrowed = True
    lib.books[0].borrower = 18 # someone
    
    res = lib.return_book(self.book1.isbn)  
    self.assertEqual(res, True)
    
    self.assertEqual(lib.books[0].is_borrowed, False)
    self.assertEqual(lib.books[0].borrower, None)
    
  def test_checkDataIsSavedToJSONWhenBookIsFoundAndItIsBorrowed(self):
    lib = Library(test = True)
    lib.add_book(**self.book1args) # reg book
    lib.books[0].is_borrowed = True
    lib.books[0].borrower = 18 # someone
    
    with patch.object(lib, "_save_data") as mockLib:
      lib.return_book(self.book1.isbn) 
      
      mockLib.assert_called_once()
      
  def test_checkDataIsntSavedWhenBookIsntBorrowed(self):
    lib = Library(test = True)
    lib.add_book(**self.book1args) # reg book
    lib.books[0].is_borrowed = False
    lib.books[0].borrower = 18 # someone
    
    with patch.object(lib, "_save_data") as mockLib:
      lib.return_book(self.book1.isbn) 
      
      mockLib.assert_not_called()
      
  def test_checkDataIsntSavedWhenBookIsntRegistered(self):
    lib = Library(test = True)
    
    with patch.object(lib, "_save_data") as mockLib:
      lib.return_book(self.book1.isbn) 
      
      mockLib.assert_not_called()
    
if __name__ == "__main__":
  unittest.main()