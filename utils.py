COLORS = {
    'RESET': '\033[0m',
    'BOLD': '\033[1m',
    'RED': '\033[91m',
    'GREEN': '\033[92m',
    'YELLOW': '\033[93m',
    'BLUE': '\033[94m',
    'MAGENTA': '\033[95m',
    'CYAN': '\033[96m',
    'WHITE': '\033[97m'
}

def green_colored_print(text):
    print(f"{COLORS['GREEN']}{text}\033[0m")

def red_colored_print(text):
    print(f"{COLORS['RED']}{text}\033[0m")

def colored_print(text, color):
    print(f"{COLORS[color.upper()]}{text}\033[0m")

def print_menu():
    menu = """
    \033[1;32;40m
    +----------------------------------+
    |    Menu   [-Librarian-]          |
    +----------------------------------+
    | 0. Exit                          |
    | 1. Add Book                      |
    | 2. Retrieve Books                |
    | 3. Update Book                   |
    | 4. Delete Book                   |
    | 5. Add Student                   |
    | 6. Retrieve Student              |
    | 7. Update Student                |
    | 8. Delete Student                |
    | 9. Lend Book                     |
    | 10.Return Book                   |
    | 11.Retrive Lend Table            |
    | 12.User's Lend History           |
    +----------------------------------+
     \033[0m
    """
    print(menu)

def print_menu_student():
    menu = """
    \033[1;32;40m
    +----------------------------------+
    |    Menu   [-Student-]            |
    +----------------------------------+
    | 0. Exit                          |
    | 1. Retrieve Books                |
    +----------------------------------+
     \033[0m
    """
    print(menu)
