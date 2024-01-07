from connectDb import connect, create_table
from student import stdFunc
from librarian import libFunc
from utils import colored_print

if __name__ == "__main__":
    conn = connect()
    with conn:
        create_table(conn)
    choice = input("Who are you Student or Librarian? [S/any]:")
    if choice.upper() == 'S':
        colored_print("Hello Student :)", 'magenta')
        stdFunc(conn)
    else:
        colored_print("Hello Librarian :)",'magenta')
        libFunc(conn)