import csv

from storage import FIELDNAMES, file_operations


class Expeses:
    """
    This class provides the utility functions needed to operate the Expeses Tracker
    """

    def __init__(self) -> None:
        pass

    def total_expenditure(self) -> float:
        """
        This method returns the total expenditure of the user
        """
        total_expenditure = 0
        try:
            with open("./expenses.csv", "r") as file:
                contents = csv.DictReader(file)
                for row in contents:
                    try:
                        total_expenditure += float(row["amount"])
                    except (ValueError, TypeError):
                        print(f"Warning: Could not process amount: {row['amount']}")
                        continue
            return total_expenditure
        except FileNotFoundError:
            print("No expenses recorded yet.")
            return 0

    def view_expenses(self):
        """
        This method prints out the entries within the storage site(CSV File)
        """
        try:
            with open("./expenses.csv", "r") as file:
                reader = csv.DictReader(file)
                entries = list(reader)
                
                if not entries:
                    print("No expenses found.")
                    return
                    
                print("\n--- Your Expenses ---")
                for i in entries:
                    print(
                        f"{i["index"]}) Amount: {i["amount"]} | Category: {i["category"]} | Description: {i["description"]}"
                    )
                print("--------------------\n")
        except FileNotFoundError:
            print("No expenses recorded yet.")

    def delete_entry(self, entry_number: int):
        """
        This method takes a user defined int 'entry' and delete the entry in the source file
        """
        try:
            with open("./expenses.csv", "r") as file:
                reader = csv.DictReader(file)
                all_entries = list(reader)
                
                entry_exists = any(int(row["index"]) == entry_number for row in all_entries)
                if not entry_exists:
                    print(f"Error: Entry with index {entry_number} not found.")
                    raise KeyError(f"Entry with index {entry_number} not found")
                
                entries = [row for row in all_entries if int(row["index"]) != entry_number]
            
            for i, entry in enumerate(entries):
                entry["index"] = i
            
            with open("./expenses.csv", "w", newline='') as file:
                writer = csv.DictWriter(file, fieldnames=FIELDNAMES)
                writer.writeheader()
                writer.writerows(entries)
            
            print(f"Entry {entry_number} deleted successfully.")
            
        except FileNotFoundError:
            print("No expenses recorded yet")
            raise KeyError("No expenses file found")

    def add_entry(self, info_list: list, counter: int):
        """
        This method calls from a storage module which contains the logic for the entry of user provided records
        """
        file_operations(info_list=info_list, counter=counter)

    def get_next_index(self) -> int:
        """
        This method returns the next available index for a new expense entry
        """
        try:
            with open("./expenses.csv", "r") as file:
                reader = csv.DictReader(file)
                indexes = [int(row["index"]) for row in reader]
                if indexes:
                    return max(indexes) + 1
                else:
                    return 0
        except FileNotFoundError:
            return 0
        except (ValueError, KeyError) as e:
            print(f"Warning: Issue with index values: {e}")
            return 0
