import sys
contacts = []

def show_contacts():
    if not contacts:
        print("No contacts available.")
    else:
        for i, contact in enumerate(contacts, 1):
            print(f"{i}. {contact['name']} - {contact['phone']} - {contact['email']} - {contact['address']}")

def add_contact(name, phone, email, address):
    contact = {"name": name, "phone": phone, "email": email, "address": address}
    contacts.append(contact)
    print(f"Contact '{name}' added.")

def validate_phone(phone):
    if len(phone) != 10 or not phone.isdigit():
        return False
    return True

def validate_email(email):
    if not email.endswith("@gmail.com"):
        return False
    return True

def search_contact(search_term):
    results = [contact for contact in contacts if search_term.lower() in contact['name'].lower() or search_term in contact['phone']]
    if not results:
        print("No matching contacts found.")
    else:
        for i, contact in enumerate(results, 1):
            print(f"{i}. {contact['name']} - {contact['phone']} - {contact['email']} - {contact['address']}")

def update_contact(contact_number, name=None, phone=None, email=None, address=None):
    while True:
        try:
            contact = contacts[contact_number - 1]
            if name:
                contact['name'] = name
            if phone:
                if validate_phone(phone):
                    contact['phone'] = phone
                else:
                    phone = input("Invalid phone number. Please enter a 10-digit phone number: ")
                    continue
            if email:
                if validate_email(email):
                    contact['email'] = email
                else:
                    email = input("Invalid email. Please enter a valid Gmail address ending with @gmail.com: ")
                    continue
            if address:
                contact['address'] = address
            print(f"Contact {contact_number} updated.")
            break
        except IndexError:
            contact_number = int(input("Invalid contact number. Please enter a valid contact number: "))

def delete_contact(contact_number):
    while True:
        try:
            contact = contacts.pop(contact_number - 1)
            print(f"Contact '{contact['name']}' removed.")
            break
        except IndexError:
            contact_number = int(input("Invalid contact number. Please enter a valid contact number: "))

def main():
    while True:
        print("\nContact Manager")
        print("1. Show contact list")
        print("2. Add contact")
        print("3. Search contact")
        print("4. Update contact")
        print("5. Delete contact")
        print("6. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == '1':
            show_contacts()
        elif choice == '2':
            name = input("Enter name: ")
            phone = input("Enter phone number (10 digits): ")
            while not validate_phone(phone):
                phone = input("Invalid phone number. Please enter a 10-digit phone number: ")
            email = input("Enter email (must end with @gmail.com): ")
            while not validate_email(email):
                email = input("Invalid email. Please enter a valid Gmail address ending with @gmail.com: ")
            address = input("Enter address: ")
            add_contact(name, phone, email, address)
        elif choice == '3':
            search_term = input("Enter name or phone number to search: ")
            search_contact(search_term)
        elif choice == '4':
            show_contacts()
            try:
                contact_number = int(input("Enter contact number to update: "))
                name = input("Enter new name (or press Enter to skip): ")
                phone = input("Enter new phone number (or press Enter to skip): ")
                if phone:
                    while not validate_phone(phone):
                        phone = input("Invalid phone number. Please enter a 10-digit phone number: ")
                email = input("Enter new email (or press Enter to skip, must end with @gmail.com): ")
                if email:
                    while not validate_email(email):
                        email = input("Invalid email. Please enter a valid Gmail address ending with @gmail.com: ")
                address = input("Enter new address (or press Enter to skip): ")
                update_contact(contact_number, name, phone, email, address)
            except ValueError:
                print("Invalid input. Please enter a number.")
        elif choice == '5':
            show_contacts()
            try:
                contact_number = int(input("Enter contact number to delete: "))
                delete_contact(contact_number)
            except ValueError:
                print("Invalid input. Please enter a number.")
        elif choice == '6':
            print("Exiting...")
            sys.exit()
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

       
