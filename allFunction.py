# All the database functionality to perform task
from utils import red_colored_print, green_colored_print
from prettytable import PrettyTable


def add_book(conn, title, author, quantity):
    # """ Add Book to the book table"""
    cursor = conn.cursor()
    cursor.execute('INSERT INTO books (title, author, quantity) VALUES (?, ?, ?)', (title, author, quantity))
    conn.commit()

def retrieve_books(conn, keyword=None):
    """ Search Book from book table """
    cursor = conn.cursor()
    if keyword:
        cursor.execute('SELECT * FROM books WHERE title LIKE ? OR author LIKE ?', ('%'+keyword+'%', '%'+keyword+'%'))
    else:
        cursor.execute('SELECT * FROM books')
    return cursor.fetchall()

def update_book(conn, book_id, title, author, quantity):
    cursor = conn.cursor()
    cursor.execute('UPDATE books SET title=?, author=?, quantity=? WHERE id=?', (title, author, quantity, book_id))
    conn.commit()

def delete_book(conn, book_id):
    cursor = conn.cursor()
    cursor.execute('DELETE FROM books WHERE id=?', (book_id,))
    conn.commit()

def add_user(conn, name):
    cursor = conn.cursor()
    cursor.execute('INSERT INTO users (name) VALUES (?)', (name,))
    conn.commit()

def retrieve_users(conn):
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users')
    return cursor.fetchall()


def update_user(conn, user_id, name):
    cursor = conn.cursor()
    cursor.execute('UPDATE users SET name=? WHERE id=?', (name, user_id))
    conn.commit()

def delete_user(conn, user_id):
    cursor = conn.cursor()
    cursor.execute('DELETE FROM users WHERE id=?', (user_id,))
    conn.commit()

def retrieve_lend_table(conn):
    cursor = conn.cursor()
    cursor.execute(
        '''
        SELECT  
        lend_records.id as lend_id,
        books.title, 
        books.author, 
        users.name,
        lend_records.return_status
        from lend_records
        INNER JOIN books ON lend_records.book_id = books.id
        INNER JOIN users ON lend_records.user_id = users.id
    '''
    )
    lent_books = cursor.fetchall()
    if lent_books:
        print("\nLent Book History:")
        table = PrettyTable()
        table.field_names = ["Lend ID", "Book Title", "Author", "Student Name", "Status"]
        for book in lent_books:
            lend_status = "Returned" if book[4] else "Not Returned"
            table.add_row([book[0], book[1], book[2], book[3], lend_status ])
        print("\033[1;33;40m" + str(table) + "\033[0m")
    else:
        red_colored_print("No lent books found.")


def lend_book(conn, book_id, user_id):
    cursor = conn.cursor()
    # Check if the book is available (quantity > 0)
    cursor.execute('SELECT quantity FROM books WHERE id=?', (book_id,))
    quantity = cursor.fetchone()
    if quantity and quantity[0] > 0:
        # Book is available, lend the book
        cursor.execute('INSERT INTO lend_records (book_id, user_id) VALUES (?, ?)', (book_id, user_id))
        # Decrement the book quantity in the library
        cursor.execute('UPDATE books SET quantity = quantity - 1 WHERE id=?', (book_id,))
        conn.commit()
        green_colored_print("Book lent successfully!")
    else:
        red_colored_print("Book not available for lending.")

def return_book(conn, lend_id):
    cursor = conn.cursor()
    # Get book_id for the given lend_id
    cursor.execute('SELECT book_id FROM lend_records WHERE id=?', (lend_id,))
    book_id = cursor.fetchone()
    if book_id:
        # Increment the book quantity in the library
        cursor.execute('UPDATE books SET quantity = quantity + 1 WHERE id=?', (book_id[0],))
        # Update lend record to mark the book as returned
        cursor.execute('UPDATE lend_records SET return_status=1 WHERE id=?', (lend_id,))
        conn.commit()
        green_colored_print("Book returned successfully!")
    else:
        red_colored_print("Invalid lend ID.")

def get_user_lent_books(conn, user_id):
    cursor = conn.cursor()
    # Select relevant columns from lend_records, books, and users tables
    cursor.execute('''
        SELECT
        lend_records.id AS lend_id,
        books.id AS book_id,
        books.title,
        books.author,
        lend_records.return_status
        from lend_records
        INNER JOIN books ON lend_records.book_id = books.id
        INNER JOIN users ON lend_records.user_id = users.id
        where lend_records.user_id = ?;
    ''', (user_id,))

    lent_books = cursor.fetchall()
    if lent_books:
        print("\nUser's Lent Book History:")
        table = PrettyTable()
        table.field_names = ["Lend ID", "Book ID", "Book Title", "Author", "Status"]
        for book in lent_books:
            lend_status = "Returned" if book[4] else "Not Returned"
            table.add_row([book[0], book[1], book[2], book[3], lend_status ])
        print("\033[1;33;40m" + str(table) + "\033[0m")

    else:
        red_colored_print("No lent books found for the user.")


def fetch_lend_record(conn):
    cursor = conn.cursor()
    cursor.execute("select * from lend_records")
    return cursor.fetchall()
