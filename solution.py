############ Do not change the assignment code value ############
assignment_code = 140110202
name = "omer"
surname = "tatlici"
student_id = "1903"
### Do not change the variable names above, just fill them in ###

import json

class Book:
    def __init__(self, title: str, author: str, publish_date: str, isbn: int, is_borrow: bool = False, borrower: int = None):
        self.title = title
        self.author = author
        self.publish_date = publish_date
        self.isbn = isbn
        self.is_borrowed = is_borrow
        self.borrower = borrower
    def __eq__(self, other: object) -> bool:
      return isinstance(other, Book) and other.isbn == self.student_id
        
class User:
    def __init__(self, first_name: str, last_name: str, student_id: int):
        self.first_name: str = first_name
        self.last_name: str = last_name
        self.student_id: int = student_id
    def __eq__(self, other: object) -> bool:
      ## other must also be a User
      return isinstance(other, User) and other.isbn == self.isbn

class Library:
    def __init__(self):
        self.books: list[Book] = []
        self.users: list[User] = []
        self.data_file = "library_data.json"
        # self._load_data()

    def _save_data(self):
        books_data = []
        for book in self.books:
            book_data = {
                'title': book.title,
                'author': book.author,
                'publish_date': book.publish_date,
                'isbn': book.isbn,
                'is_borrowed': book.is_borrowed,
                'borrower': book.borrower,
            }
            books_data.append(book_data)

        users_data = []
        for user in self.users:
            user_data = {
                'first_name': user.first_name,
                'last_name': user.last_name,
                'student_id': user.student_id
            }
            users_data.append(user_data)

        with open(self.data_file, 'w', encoding="utf-8") as file:
            json.dump({
                'books': books_data,
                'users': users_data,
            }, file, indent=2, ensure_ascii=False)

    def _load_data(self):
        try:
            with open(self.data_file, 'r') as file:
                data = json.load(file)
                for book_data in data.get('books', []):
                    title = book_data['title']
                    author = book_data['author']
                    publish_date = book_data['publish_date']
                    isbn = book_data['isbn']
                    is_borrowed = book_data.get('is_borrowed', False)
                    borrower = book_data.get('borrower', None)

                    book_obj = Book(title, author, publish_date, isbn, is_borrowed, borrower)
                    self.books.append(book_obj)

                for user_data in data.get('users', []):
                    first_name = user_data['first_name']
                    last_name = user_data['last_name']
                    student_id = user_data['student_id']
                    user_obj = User(first_name, last_name, student_id)
                    self.users.append(user_obj)

        except FileNotFoundError:
            self._save_data()
            
    def add_book(self, title: str, author: str, publish_date, isbn: int):
      newBook = Book(title, author, publish_date, isbn)
      ## i took isbn to be uniquely defining, reference check makes no sense here
      if newBook in self.books: 
        return False
      self.books.append(newBook)
      self._save_data()
      return newBook.title
        
    def add_user(self, first_name: str, last_name: str, student_id: int):
      newUser = User(first_name, last_name, student_id)
      if newUser in self.users:
        return False
      self.users.append(newUser)
      self._save_data()
      return newUser.student_id
        
    def check_book_by_isbn(self, isbn) -> bool:
      ## yavas olabilir (olmayadabilir, test etmedim) ama siktiret 1 satir
      return any(map(lambda book: book.isbn == isbn, self.books))

    def find_book_by_isbn(self, isbn) :
      ## yavas olabilir (olmayadabilir, test etmedim) ama siktiret 1 satir
      for book in self.books:
        if book.isbn == isbn:
          return book
      return False
    
    def remove_book(self, isbn: int) -> bool:
      res: str | False = False
      for book in self.books:
        if book.isbn == isbn:
          self.books.remove(book)
          res = book.title
      self._save_data()
      return res
      
    def delete_user(self, student_id: int):
      fakeUser = User("fake", "fake", student_id)
      if fakeUser in self.users:
        if not list(filter(lambda book: book.borrower == student_id, self.books)):
          self.users.remove(fakeUser)
          return student_id
      return False
      
        
    def list_books(self) -> list[int]:
        return [book.isbn for book in self.books]
        
    def borrow_book(self, isbn: int, student_id: int):
      ## list has any items, then user is registered
      isUserReg: list[User] = [user for user in self.users if user.student_id == student_id] 
      foundBook: False | Book = self.find_book_by_isbn(isbn)
      if foundBook and isUserReg:
        if not foundBook.is_borrowed:
          foundBook.is_borrowed = True
          foundBook.borrower = student_id
          self._save_data()
          return True
      return False
          
    def return_book(self, isbn: int):
      foundBook = self.find_book_by_isbn(isbn)
      if foundBook:
        foundBook.is_borrowed = False
        foundBook.borrower = -1 ## just to be safe, don't leave stale data active
        return True
      return False




