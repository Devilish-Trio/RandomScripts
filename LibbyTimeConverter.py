def option_1():
    # User inputs for the first part
    how_long_left = float(input("Enter how long is left of the book in hours (e.g., 11.35): "))
    desired_length_book_hours = float(input("Enter your desired length for the book in hours (e.g., 5): "))

    # Calculating the speed multiplier
    total1 = how_long_left / desired_length_book_hours
    print(f"{total1:.2f} ~ xSpeed", "to listen at to finish by the desired time.")


def option_2():
    # User inputs for the second part
    current_book_length_hours = float(input("Enter the current length of the book in hours (e.g., 11.2): "))
    percentage_of_speed = float(input("Enter the playback speed multiplier (e.g., 1.35): "))

    # Converting hours to minutes and calculating the time left
    hours_to_mins = current_book_length_hours * 60
    total2 = (hours_to_mins / percentage_of_speed) / 60
    print(f"{total2:.2f} hours roughly left", "at the current playback speed.")


def main_menu():
    while True:
        print("\nSelect an option:")
        print("1. Calculate speed multiplier to finish the book in desired time.")
        print("2. Calculate time left to finish the book at a certain playback speed.")
        print("3. Exit")

        user_choice = input("Enter your choice (1, 2, or 3): ")

        if user_choice == '1':
            option_1()
        elif user_choice == '2':
            option_2()
        elif user_choice == '3':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid option selected. Please try again.")


# Calling the main menu function to start the program
main_menu()
