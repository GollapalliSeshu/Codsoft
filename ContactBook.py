import os
import json

CONTACTS_FILE = "contacts.json"

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def load_contacts():
    try:
        with open(CONTACTS_FILE, 'r') as file:
            contacts = json.load(file)
    except FileNotFoundError:
        contacts = []
    return contacts

def save_contacts(contacts):
    with open(CONTACTS_FILE, 'w') as file:
        json.dump(contacts, file)

def add_contact(contacts, name, phone, email, address):
    new_contact = {
        "name": name,
        "phone": phone,
        "email": email,
        "address": address
    }
    contacts.append(new_contact)
    save_contacts(contacts)

def view_contacts(contacts):
    clear_screen()
    if not contacts:
        print("No contacts found.")
    else:
        print("Contact List:")
        for i, contact in enumerate(contacts, start=1):
            print(f"{i}. {contact['name']} - {contact['phone']}")

def search_contact(contacts, search_term):
    results = []
    for contact in contacts:
        if (
            search_term.lower() in contact['name'].lower() or
            search_term in contact['phone']
        ):
            results.append(contact)
    return results

def update_contact(contacts, index, name, phone, email, address):
    contacts[index]["name"] = name
    contacts[index]["phone"] = phone
    contacts[index]["email"] = email
    contacts[index]["address"] = address
    save_contacts(contacts)

def delete_contact(contacts, index):
    del contacts[index]
    save_contacts(contacts)

def main():
    contacts = load_contacts()

    while True:
        clear_screen()
        print("Contact Management System")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            name = input("Enter the name: ")
            phone = input("Enter the phone number: ")
            email = input("Enter the email: ")
            address = input("Enter the address: ")
            add_contact(contacts, name, phone, email, address)

        elif choice == '2':
            view_contacts(contacts)
            input("Press Enter to continue...")

        elif choice == '3':
            search_term = input("Enter the name or phone number to search: ")
            search_results = search_contact(contacts, search_term)
            view_contacts(search_results)
            input("Press Enter to continue...")

        elif choice == '4':
            view_contacts(contacts)
            try:
                index = int(input("Enter the index of the contact to update: ")) - 1
                contact = contacts[index]
                name = input(f"Enter the new name for {contact['name']}: ")
                phone = input(f"Enter the new phone number for {contact['name']}: ")
                email = input(f"Enter the new email for {contact['name']}: ")
                address = input(f"Enter the new address for {contact['name']}: ")
                update_contact(contacts, index, name, phone, email, address)
            except (ValueError, IndexError):
                print("Invalid input. Please enter a valid index.")
            input("Press Enter to continue...")

        elif choice == '5':
            view_contacts(contacts)
            try:
                index = int(input("Enter the index of the contact to delete: ")) - 1
                delete_contact(contacts, index)
            except (ValueError, IndexError):
                print("Invalid input. Please enter a valid index.")
            input("Press Enter to continue...")

        elif choice == '6':
            print("Exiting program. Goodbye!")
            break

        else:
            input("Invalid choice. Press Enter to continue...")

if __name__ == "__main__":
    main()
