
# Main menu for application
def main():
        print("-- Horse Stable Management App --")
        print("1. Add a horse")
        print("2. Remove a horse")
        print("3. Update horse details")
        print("4. View horse details")
        print("5. Add race results")
        print("6. View race logs")
        print("7. Exit app")

        choice = input("Enter your choice: ")

        if choice == '1':
                horse_manager.add_horse()
        elif choice == '2':
                horse_manager.remove_horse()
        elif choice == '3':
                horse_manager.update_horse_details()
        elif choice == '4':
                horse_manager.view_all_horses()
        elif choice == '5':
                race_manager.add_race_results()
        elif choice == '6':
                race_manager.view_race_logs()
        elif choice == '7':
                print("Goodbye!")
                exit()
        else:
                print("Invalid choice, please try again!")

main()