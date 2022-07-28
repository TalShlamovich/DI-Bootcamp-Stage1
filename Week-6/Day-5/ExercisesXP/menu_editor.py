import psycopg2

HOSTNAME = 'localhost'
USERNAME = 'postgres'
PASSWORD = 'first'
DATABASE = 'W6D5'

from exerciseXP import MenuItem

def show_user_menu():
    """Display the program menu to the user,
    ask to choose an option,
    call the next funtion according to the choice"""
    the_choice = ''
    while the_choice != 'a' or the_choice != 'd' or the_choice != 'v' or the_choice != 'x':
        the_choice = input("Welcome to Menu_manager_v0.09b!\nPlease choose an option\n(a) Add an item to the menu\n(d) Delete an item\n(v) View the menu\n(x) Exit\n:  ")
        return the_choice
    if the_choice == 'a':
        add_item()
    
    elif the_choice == 'd':
        delete_item()

    elif the_choice == 'v':
        show_menu()
    
    elif the_choice == 'x':
        print("See you later")
        quit()
        

    
# show_user_menu()