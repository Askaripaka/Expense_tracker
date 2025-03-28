class UserUi:
    def __init__(self) -> None:
        pass

    def menu(self) -> None:
        """User menu"""
        print(
            "\nEnter '1' to add expense\nEnter '2' to View expenses\nEnter '3' to delete an expense\nEnter '4' to view total expenditure\nEnter '5' to exit the program\n"
        )

    def user_entry_to_file(self) -> list:
        """
        This function returns a list of the users input : amount , category , description
        """
        try:
            amount = float(input("Amount -> "))
            category = input("Category -> ")
            description = input("Description -> ")

            return [amount, category, description]
            # TODO: Provide a better more detailed error message
        except:
            print(f"You have provided wrong input : '{amount}' in the 'amount' field\n")
            return []
