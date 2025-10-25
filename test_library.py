from operations import *

add_book("201", "AI Revolution", "Elon Mars", "Non-Fiction", 2)
add_member("M02", "Mr. Amandus", "Amandus@example.com")

# Test adding and borrowing
assert borrow_book("M02", "201") == "Mr. Amandus borrowed 'AI Revolution'."
assert return_book("M02", "201") == "Mr. Amandus returned 'AI Revolution'."
assert delete_book("201") == "Book deleted."

print("✅ All tests passed successfully!")