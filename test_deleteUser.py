import unittest
from unittest.mock import patch

from solution import User, Book, Library


class TestDeleteUSer(unittest.TestCase):
  user1args = {"first_name": "NAME", "last_name": "LASTNAME", "student_id": 1}
  user1 = User(**user1args)
  
  book1args = {"title": "book1", "author": "author1", "publish_date": "15", "isbn": 25}
  book1 = Book(**book1args)
  
  def test_returnsFalseIfTheUSerDoesntExist(self):
    lib = Library(test = True)
    res = lib.delete_user(self.user1.student_id)
    self.assertFalse(res)
    
  def test_returnsStudentIdIfTheStudentIsRegistered(self):
    lib = Library(test = True)
    lib.add_user(**self.user1args)
    res = lib.delete_user(self.user1.student_id)
    self.assertEqual(res, self.user1.student_id)
    
  def test_decrementsTheUserListUponRemove(self):
    lib = Library(test = True)
    lib.add_user(**self.user1args)
    self.assertEqual(len(lib.users), 1)
    lib.delete_user(self.user1.student_id)
    self.assertEqual(len(lib.users), 0)
    
  def test_userCannotBeRemovedIfTheyHaveBorrowedABook(self):
    lib = Library(test = True)
    lib.add_book(**self.book1args)
    lib.add_user(**self.user1args)
    
    lib.books[0].is_borrowed = True
    lib.books[0].borrower = self.user1.student_id 
    
    self.assertEqual(len(lib.users), 1)
    res = lib.delete_user(self.user1.student_id)
    self.assertEqual(len(lib.users), 1)
    self.assertFalse(res)
    
  
  def test_checkDataIsSavedToJSONWhenDeleteIsSuccessful(self):
    lib = Library(test = True)
    lib.add_user(**self.user1args)
    with patch.object(lib, "_save_data") as mockLib:
      lib.delete_user(self.user1.student_id)
      
      mockLib.assert_called_once()
      
  def test_checkDataIsNotSavedToJSONWhenDeleteIsAFailure(self):
    lib = Library(test = True)
    
    with patch.object(lib, "_save_data") as mockLib:
      lib.delete_user(self.user1.student_id)
      
      mockLib.assert_not_called()
      
  def test_checkDataIsNotSavedToJSONWhenDeleteFailsBevauseOfBorrowedBook(self):
    lib = Library(test = True)
    lib.add_book(**self.book1args)
    lib.add_user(**self.user1args)
    
    lib.books[0].is_borrowed = True
    lib.books[0].borrower = self.user1.student_id 
    
    with patch.object(lib, "_save_data") as mockLib:
      lib.delete_user(self.user1.student_id)
      
      mockLib.assert_not_called()
      
  
if __name__ == "__main__":
  unittest.main()