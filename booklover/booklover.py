import pandas as pd

class BookLover:
    def __init__(self, name, email, fav_genre, num_books=0, book_list=None):
        self.name = name
        self.email = email
        self.fav_genre = fav_genre
        self.num_books = num_books
        
        if book_list is None:
            self.book_list = pd.DataFrame({'book_name': [], 'book_rating': []})
        else:
            self.book_list = book_list
    
    def add_book(self, book_name, book_rating):
        if book_name in self.book_list['book_name'].values:
            print(f"{book_name} is already in our book list.")
        else:
            new_book = pd.DataFrame({'book_name': [book_name], 'book_rating': [book_rating]})
            self.book_list = pd.concat([self.book_list, new_book], ignore_index=True)
            self.num_books += 1
    
    def has_read(self, book_name):
        return book_name in self.book_list['book_name'].values
    
    def num_books_read(self):
        return len(self.book_list)
    
    def fav_books(self):
        return self.book_list[self.book_list['book_rating'] > 3]
    
# Example usage for testing
if __name__ == '__main__':
    test_object = BookLover("Han Solo", "hsolo@millenniumfalcon.com", "scifi")
    test_object.add_book("Jane Eyre", 4)
    test_object.add_book("Fight Club", 5)
    test_object.add_book("The Divine Comedy", 4)
    print(test_object.book_list)
