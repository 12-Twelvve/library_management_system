from allFunction import  add_book, retrieve_books, update_book, delete_book, add_user, retrieve_users, delete_user, update_user, lend_book, return_book, get_user_lent_books, retrieve_lend_table, fetch_lend_record
from prettytable import PrettyTable
from utils import red_colored_print, green_colored_print, print_menu, colored_print


def libFunc(conn):
    while True:
        print_menu()
        with conn:
            try:
                choice = int(input("Enter your choice: "))
                if choice == 0: 
                    colored_print("Exiting.....  [Thanks For Visiting]", "YELLOW")
                    break
                elif choice == 1:
                    title = input("Enter book title: ")
                    author = input("Enter book author: ")
                    quantity = int(input("Enter quantity: "))
                    add_book(conn, title, author, quantity)
                    green_colored_print("Book Added Successfully !")

                elif choice == 2:
                    keyword = input("Enter search keyword (Leave blank to retrieve all books): ")
                    books = retrieve_books(conn, keyword)
                    print("\nBooks:")
                    table = PrettyTable()
                    table.field_names = ["ID", "Title", "Author", "Quantity"]
                    for book in books:
                        table.add_row([book[0], book[1], book[2], book[3]])
                    print("\033[1;33;40m" + str(table) + "\033[0m")

                elif choice == 3:
                    book_id = int(input("Enter book ID to update: "))
                    title = input("Enter new title: ")
                    author = input("Enter new author: ")
                    quantity = int(input("Enter new quantity: "))
                    update_book(conn, book_id, title, author, quantity)
                    green_colored_print("Book updated Successfully !")
                    
                elif choice == 4:
                    book_id = int(input("Enter book ID to delete: "))
                    delete_book(conn, book_id)
                    red_colored_print("Book deleted successfully!")

                elif choice == 5:
                    name = input("Enter Student name: ")
                    add_user(conn, name)
                    green_colored_print("Student Added successfully!")

                elif choice == 6:
                    users = retrieve_users(conn)
                    print("\nStudents:")
                    table = PrettyTable()
                    table.field_names = ["ID", "Name"]
                    for user in users:
                        table.add_row([user[0], user[1]])
                    print("\033[1;33;40m" + str(table) + "\033[0m")
                
                elif choice == 7:
                    student_id = int(input("Enter Student ID to update: "))
                    name = input("Enter new name: ")
                    update_user(conn, student_id, name)
                    green_colored_print("Student updated Successfully !")
                    
                elif choice == 8:
                    student_id = int(input("Enter Student ID to delete: "))
                    delete_user(conn, student_id)
                    red_colored_print("Student deleted successfully!")
                
                elif choice == 9:
                    book_id = int(input("Enter book ID to lend: "))
                    user_id = int(input("Enter Student ID: "))
                    lend_book(conn, book_id, user_id)

                elif choice == 10:
                    lend_id = int(input("Enter lend record ID to update (return): "))
                    return_book(conn, lend_id)
                
                elif choice == 11:
                    retrieve_lend_table(conn)

                elif choice == 12:
                    user_id = int(input("Enter Student ID: "))
                    get_user_lent_books(conn, user_id)

                elif choice == 13:
                    data = fetch_lend_record(conn)
                    print(data)
                else:
                    red_colored_print("Invalid choice. Please try again.")

            except:
                red_colored_print("Invalid choice. Please try again.")