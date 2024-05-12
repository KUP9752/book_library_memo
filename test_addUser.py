import unittest
from unittest.mock import patch

from solution import User, Library


class TestAddUser(unittest.TestCase):
  user1args = {"first_name": "NAME", "last_name": "LASTNAME", "student_id": 1}
  user1 = User(**user1args)
  
  def test_addingOneReturnsStudentId(self):
    lib = Library(test = True)
    self.assertEqual(lib.add_user(**self.user1args), self.user1.student_id)
    
  def test_addingOneIncreasesLibrarySize(self):
    lib = Library(test = True)
    self.assertEqual(len(lib.users), 0) # no users yet
    lib.add_user(**self.user1args)
    self.assertEqual(len(lib.users), 1) # 1 book after addition

  def test_addingSameReturnsFalse(self):
    lib = Library(test = True)
    first = lib.add_user(**self.user1args)
    second = lib.add_user(**self.user1args)
    self.assertEqual(first, self.user1.student_id) # Check we can succesfully add the first one
    self.assertFalse(second) # check the second one doesn't get added at all

  def test_checkDataIsSavedToJSONWhenAddIsSuccessful(self):
    lib = Library(test = True)
    
    with patch.object(lib, "_save_data") as mockLib:
      lib.add_user(**self.user1args)
      
      mockLib.assert_called_once()
      
  def test_checkDataIsNotSavedToJSONWhenAddIsAFailure(self):
    lib = Library(test = True)
    lib.add_user(**self.user1args)
    
    with patch.object(lib, "_save_data") as mockLib:
      lib.add_user(**self.user1args)
      
      mockLib.assert_not_called()

if __name__ == "__main__":
  unittest.main()