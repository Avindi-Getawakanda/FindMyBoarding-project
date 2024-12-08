from conn import create_connection
from Authentication import register_owner, owner_login
from Add_listing import add_listing
from view_listing import view_listings
from rent_cal import rent_calculator

current_owner = None 


def main():
    global current_owner
    while True:
        print("\nFindMyBoarding")
        print("1. Register as Owner")
        print("2. Login as Owner")
        print("3. Add Listing (Owner)")
        print("4. View Listings (Student)")
        print("5. Rent Calculator")
        print("6. Logout")
        print("7. Exit")

        choice = int(input("Choose an option: "))

        if choice == 1:
            email = input("Enter email: ")
            password = input("Enter password: ")
            register_owner(email, password)

        elif choice == 2:
            email = input("Enter email: ")
            password = input("Enter password: ")
            owner = owner_login(email, password)
            if owner:
                print("Login successful!")
                current_owner = owner  # Set the logged-in owner
            else:
                print("Invalid credentials.")

        elif choice == 3:
            if current_owner:
                print("Current owner details:", current_owner)  # Debugging
                owner_id = current_owner['id']  # Use the logged-in owner's ID
                title = input("Enter title: ")
                image_path = input("Enter image path: ")
                address = input("Enter address: ")
                distance = float(input("Enter distance from campus (km): "))
                price = float(input("Enter price (Rs.): "))
                facilities = input("Enter facilities: ")

                while True:
                    contact = input("Enter contact info: ")
                    if len(contact) == 10 and contact.isdigit():
                        break
                    print("Invalid contact number. It must have exactly 10 digits. Please try again.")

                description = input("Enter description: ")
                add_listing(owner_id, title, image_path, address, distance, price, facilities, contact, description)
            else:
                print("You need to log in as an owner to add listings.")

        elif choice == 4:
            view_listings()

        elif choice == 5:
            income = float(input("Enter your monthly income (Rs.): "))
            other_expenses = float(input("Enter other monthly expenses (Rs.): "))
            rent_calculator(income, other_expenses)

        elif choice == 6:
            if current_owner:
                print(f"Logged out from {current_owner['email']}")
                current_owner = None
            else:
                print("You are not logged in.")

        elif choice == 7:
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
