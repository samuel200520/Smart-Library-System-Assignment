# demo.py
from operations import *

print(add_book("101", "Python Basics", "John Doe", "Education", 3))
print(add_book("102", "Future World", "Jane Ray", "Sci-Fi", 2))
print(add_member("M01", "Samuel Siaka", "samuel@example.com"))

print(search_book("python"))

print(borrow_book("M01", "101"))
print(return_book("M01", "101"))
print(delete_book("101"))
