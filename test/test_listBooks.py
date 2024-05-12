import unittest
from unittest.mock import patch

import sys
sys.path.append("../")

from src.solution import Book, Library


class TestListBooks(unittest.TestCase):
  
  def generateNBooks(self, n: int) -> list[Book]:
    return [{"title": f"book{i}", "author": f"author{i}","publish_date": f"date{i}", "isbn": i} for i in range(n)]
  
  def test_returnsAListLengthEqualToAdded(self):
    lib = Library(test = True)
    bookArgs = self.generateNBooks(15)
    for bookArg in bookArgs:
      lib.add_book(**bookArg)
    self.assertEqual(len(lib.list_books()), 15)
    
  def test_doubleAdditionListShouldResultInHalf(self):
    lib = Library(test = True)
    bookArgs = self.generateNBooks(15)
    bookArgs += self.generateNBooks(15)
    self.assertEqual(len(bookArgs), 30)
    for bookArg in bookArgs:
      lib.add_book(**bookArg)
    self.assertEqual(len(lib.list_books()), 15)

  def test_checkDataIsNeverSavedOnThisMethod(self):
    lib = Library(test = True)
    
    with patch.object(lib, "_save_data") as mockLib:
      lib.list_books()
      
      mockLib.assert_not_called()
if __name__ == "__main__":
  unittest.main()