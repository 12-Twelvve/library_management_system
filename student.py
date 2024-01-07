from allFunction import retrieve_books
from prettytable import PrettyTable
from utils import red_colored_print, colored_print, print_menu_student

def stdFunc(conn):
    while True:
        print_menu_student()
        try:
            choice = int(input("Enter your choice: "))
            if choice == 0:
                colored_print("Exiting..... [Thanks For Visiting]", "yellow")
                break
            elif choice == 1:
                keyword = input("Enter search keyword (Leave blank to retrieve all books): ")
                books = retrieve_books(conn, keyword)
                print("\nBooks:")
                table = PrettyTable()
                table.field_names = ["ID", "Title", "Author", "Quantity"]
                for book in books:
                    table.add_row([book[0], book[1], book[2], book[3] ])
                print("\033[1;33;40m" + str(table) + "\033[0m")
            else:
                red_colored_print("Invalid choice. Please try again.")

        except:
            red_colored_print("Invalid Choice. Please try Again.")