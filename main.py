import sys

from Expenses_lib import Expeses
from user_cli_ui import UserUi

# TODO: Remeber to provide detailed documentation of the entire program

ui = UserUi()
util = Expeses()


def main():
    """the main program"""

    print("\n HELLO AND WELCOME TO YOUR TRUSTY EXPENSE TRACKER \n")
    while True:
        ui.menu()
        while True:
            try:
                user_menu_input = int(input("--> "))
                break
            except:
                print("please provide an option within the range of the menu aboove\n")

        match user_menu_input:
            case 1:
                while True:
                    info_list = ui.user_entry_to_file()
                        
                    try:
                        next_index = util.get_next_index()
                    except:
                        next_index = 0
                        
                    util.add_entry(info_list=info_list, counter=next_index)

                    user_quit_option = input("enter 'y' to quit( 'N' to proceed)")

                    if user_quit_option == "y":
                        break

            case 2:
                util.view_expenses()

            case 3:
                util.view_expenses()
                while True:
                    try:
                        user_del_entry = int(input("Enter the entry to delete --> "))
                        util.delete_entry(user_del_entry)
                        break
                    except ValueError:
                        print("Please provide a valid number")
                    except KeyError:
                        print("Provided entry number not in scope")

            case 4:
                print(
                    f"Your current total spenditure is : {float(util.total_expenditure())} Shs"
                )

            case 5:
                print("Thank you for using Expense Tracker. Goodbye!")
                sys.exit(0)
            
            case _:
                print("Invalid option. Please select a number between 1 and 5.")


if __name__ == "__main__":
    main()
