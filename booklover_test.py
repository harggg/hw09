import unittest
from booklover import BookLover

class BookLoverTestSuite(unittest.TestCase):
    
    def test_1_add_book(self): 
        test_obj = BookLover("User 1", "user@gmail.com", "justice")
        test_obj.add_book("Pride and Prejudice", 5)
        self.assertTrue("Pride and Prejudice" in test_obj.book_list['book_name'].values)

    def test_2_add_book(self):
        test_obj = BookLover("User 1", "user@gmail.com", "adventure")
        test_obj.add_book("Huck Finn", 4)
        test_obj.add_book("Huck Finn", 4)
        self.assertEqual(len(test_obj.book_list[test_obj.book_list['book_name'] == "Huck Finn"]), 1)
                
    def test_3_has_read(self): 
        test_obj = BookLover("User 1", "user@gmail.com", "food")
        test_obj.add_book("Jimmy Johns The Book", 5)
        self.assertTrue(test_obj.has_read("Jimmy Johns The Book"))
        
    def test_4_has_read(self): 
        test_obj = BookLover("User 1", "user@gmail.com", "fiction")
        self.assertFalse(test_obj.has_read("Art of War"))
        
    def test_5_num_books_read(self): 
        test_obj = BookLover("User 1", "user@gmail.com", "fiction")
        test_obj.add_book("Star Wars", 5)
        test_obj.add_book("Beyblade", 4)
        test_obj.add_book("Farenheit 451", 5)
        self.assertEqual(test_obj.num_books_read(), 3)

    def test_6_fav_books(self):
        test_obj = BookLover("User 1", "user@gmail.com", "scary stuff")
        test_obj.add_book("The Odyssey", 5)
        test_obj.add_book("Dracula", 2)
        test_obj.add_book("Thomas the Train", 4)
        test_obj.add_book("Winnie the Pooh", 3)
        fav_books_df = test_obj.fav_books()
        self.assertTrue(all(fav_books_df['book_rating'] > 3))
                
if __name__ == '__main__':
    unittest.main(verbosity=3)
