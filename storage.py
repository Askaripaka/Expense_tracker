import csv
import os

FIELDNAMES = ["index", "amount", "category", "description"]


def file_operations(info_list: list, counter: int):
    """
    This defined function takes a list and a counter arguments. The list should contain user entries and the counter is just but an index for each user provided entry
    """

    file_exists = os.path.isfile("expenses.csv")

    with open("expenses.csv", "a") as file:
        writer = csv.DictWriter(file, fieldnames=FIELDNAMES)

        if not file_exists:
            writer.writeheader()

        try:

            writer.writerow(
                {
                    "index": counter,
                    "amount": info_list[0],
                    "category": info_list[1],
                    "description": info_list[2],
                }
            )
        except:
            print("\nU may have provided wrong input. Try again later")
