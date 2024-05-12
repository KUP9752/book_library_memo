import unittest
from unittest.mock import patch

import sys
sys.path.append("../")

from src.solution import Book, User, Library


class TestBorrowBook(unittest.TestCase):
  book1args = {"title": "book1", "author": "author1", "publish_date": "15", "isbn": 25}
  book1 = Book(**book1args)
  
  user1args = {"first_name": "NAME", "last_name": "LASTNAME", "student_id": 1}
  user1 = User(**user1args)
  
  def test_bookNotRegisteredShouldReturnFalse(self):
    lib = Library(test = True)
    res = lib.borrow_book(self.book1.isbn, self.user1.student_id)
    self.assertFalse(res)

  def test_userNotRegisteredShouldReturnFalse(self):
    lib = Library(test = True)
    res = lib.borrow_book(self.book1.isbn, self.user1.student_id)
    self.assertFalse(res)
    
  def test_bookRegisteredButUserIsntIsFalse(self):
    lib = Library(test = True)
    lib.add_book(**self.book1args)
    res = lib.borrow_book(self.book1.isbn, self.user1.student_id)
    self.assertFalse(res)
    
  def test_userRegisteredButBookIsntIsFalse(self):
    lib = Library(test = True)
    lib.add_user(**self.user1args)
    res = lib.borrow_book(self.book1.isbn, self.user1.student_id)
    self.assertFalse(res)
  
  def test_bothRegisteredAndBookIsntBorrowedShouldUpdateTheObjects(self):
    lib = Library(test = True)
    lib.add_book(**self.book1args) # reg book
    lib.add_user(**self.user1args) # reg user
    res = lib.borrow_book(self.book1.isbn, self.user1.student_id)
    self.assertEqual(res, True)
    
  def test_bothRegisteredAndBookIsntBorrowedUserCanOnlyBorrowOnce(self):
    lib = Library(test = True)
    lib.add_book(**self.book1args) # reg book
    lib.add_user(**self.user1args) # reg user
    res = lib.borrow_book(self.book1.isbn, self.user1.student_id)
    self.assertEqual(res, True)
    
    res = lib.borrow_book(self.book1.isbn, self.user1.student_id)
    self.assertFalse(res)
    
    res = lib.borrow_book(self.book1.isbn, self.user1.student_id)
    self.assertFalse(res)
    
    
  def test_bothRegisteredButBookIsBorrowedShouldReturnFalse(self):
    lib = Library(test = True)
    lib.add_book(**self.book1args) # reg book
    lib.add_user(**self.user1args) # reg user
    
    ## force book to be borrowed
    lib.books[0].is_borrowed = True
    lib.books[0].borrower = 90 # someone
    
    res = lib.borrow_book(self.book1.isbn, self.user1.student_id)
    self.assertFalse(res)
    
  def test_checkDataIsSavedToJSONWhenBorrowIsSuccessful(self):
    lib = Library(test = True)
    lib.add_book(**self.book1args) # reg book
    lib.add_user(**self.user1args) # reg user
    
    with patch.object(lib, "_save_data") as mockLib:
      lib.borrow_book(self.book1.isbn, self.user1.student_id)
      
      mockLib.assert_called_once()
  
  def test_checkDataIsntSavedToJSONWhenBorrowFailsBookNotReg(self):
    lib = Library(test = True)
    lib.add_user(**self.user1args) # reg user
    
    with patch.object(lib, "_save_data") as mockLib:
      lib.borrow_book(self.book1.isbn, self.user1.student_id)
      
      mockLib.assert_not_called()
      
  def test_checkDataIsntSavedToJSONWhenBorrowFailsUserNotReg(self):
    lib = Library(test = True)
    lib.add_book(**self.book1args) # reg book
    
    with patch.object(lib, "_save_data") as mockLib:
      lib.borrow_book(self.book1.isbn, self.user1.student_id)
      
      mockLib.assert_not_called()
      
  def test_checkDataIsntSavedToJSONWhenBorrowFailsNeitherReg(self):
    lib = Library(test = True)
    
    with patch.object(lib, "_save_data") as mockLib:
      lib.borrow_book(self.book1.isbn, self.user1.student_id)
      
      mockLib.assert_not_called()
      
    
if __name__ == "__main__":
  unittest.main()