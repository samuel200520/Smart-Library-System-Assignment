

# --- Data Structures ---
books = {}  # ISBN -> {title, author, genre, total_copies, available_copies}
members = []  # list of dicts {id, name, email, borrowed_books}
genres = ("Fiction", "Non-Fiction", "Sci-Fi", "Biography", "Education")

# --- Core Functions ---

def add_book(isbn, title, author, genre, total_copies):
    """Add a new book if ISBN is unique and genre is valid."""
    if isbn in books:
        return "Book already exists."
    if genre not in genres:
        return "Invalid genre."
    books[isbn] = {
        "title": title,
        "author": author,
        "genre": genre,
        "total_copies": total_copies,
        "available_copies": total_copies
    }
    return f"Book '{title}' added successfully."


def search_book(keyword):
    """Search for books by title or author."""
    result = []
    for isbn, info in books.items():
        if keyword.lower() in info["title"].lower() or keyword.lower() in info["author"].lower():
            result.append((isbn, info))
    return result


def add_member(member_id, name, email):
    """Add a new library member."""
    for m in members:
        if m["id"] == member_id:
            return "Member ID already exists."
    members.append({"id": member_id, "name": name, "email": email, "borrowed_books": []})
    return f"Member '{name}' added successfully."


def delete_member(member_id):
    """Delete a member if they have no borrowed books."""
    for m in members:
        if m["id"] == member_id:
            if m["borrowed_books"]:
                return "Cannot delete member. Borrowed books not returned."
            members.remove(m)
            return "Member deleted."
    return "Member not found."


def borrow_book(member_id, isbn):
    """Allow member to borrow a book if available."""
    if isbn not in books:
        return "Book not found."
    if books[isbn]["available_copies"] <= 0:
        return "No copies available."

    for m in members:
        if m["id"] == member_id:
            m["borrowed_books"].append(isbn)
            books[isbn]["available_copies"] -= 1
            return f"{m['name']} borrowed '{books[isbn]['title']}'."
    return "Member not found."


def return_book(member_id, isbn):
    """Return a borrowed book."""
    for m in members:
        if m["id"] == member_id:
            if isbn in m["borrowed_books"]:
                m["borrowed_books"].remove(isbn)
                books[isbn]["available_copies"] += 1
                return f"{m['name']} returned '{books[isbn]['title']}'."
            return "Book not borrowed by this member."
    return "Member not found."


def delete_book(isbn):
    """Delete a book from library if no copies are borrowed."""
    if isbn not in books:
        return "Book not found."
    if books[isbn]["available_copies"] != books[isbn]["total_copies"]:
        return "Cannot delete. Some copies are borrowed."
    del books[isbn]
    return "Book deleted."
