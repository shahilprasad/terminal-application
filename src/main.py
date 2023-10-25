import os
import horse_manager
import race_logs_manager

# Main menu for application
def main_menu():
     os.system('clear')  # Clears console when called
     while True:
        print("-- Horse Stable Management App --")
        print("1. Add horse")
        print("2. Remove horse")
        print("3. Update horse details")
        print("4. View horse details")
        print("5. Add race results")
        print("6. View race logs")
        print("7. Exit app")

        choice = input("Choose an option: ")
        
        if choice == '1':
            horse_manager.add_horse()
        elif choice == '2':
            horse_manager.remove_horse()
        elif choice == '3':
            horse_manager.update_horse_details()
        elif choice == '4':
            horse_manager.view_all_horses()
        elif choice == '5':
            race_logs_manager.add_race_log()
        elif choice == '6':
            race_logs_manager.view_race_logs()
        elif choice.lower() == '7':
            print("Goodbye!")
            exit()
        else:
            print("Invalid choice, please try again!")

main_menu()