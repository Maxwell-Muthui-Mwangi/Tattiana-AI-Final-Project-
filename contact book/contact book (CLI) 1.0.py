import json
import os

# File to store contacts
CONTACTS_FILE = "contacts.json"

# Load contacts from file
def load_contacts():
    if os.path.exists(CONTACTS_FILE):
        with open(CONTACTS_FILE, 'r') as file:
            return json.load(file)
    return []

# Save contacts to file
def save_contacts(contacts):
    with open(CONTACTS_FILE, 'w') as file:
        json.dump(contacts, file, indent=4)

# Add a new contact
def add_contact(contacts, name, phone, email, address):
    contacts.append({"name": name, "phone": phone, "email": email, "address": address})
    save_contacts(contacts)

# View all contacts
def view_contacts(contacts):
    if not contacts:
        print("No contacts found.")
    else:
        for contact in contacts:
            print(f"Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}, Address: {contact['address']}")

# Search for a contact
def search_contacts(contacts, search_term):
    results = [contact for contact in contacts if search_term.lower() in contact['name'].lower() or search_term in contact['phone']]
    if results:
        for contact in results:
            print(f"Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}, Address: {contact['address']}")
    else:
        print("No matching contacts found.")

# Update a contact
def update_contact(contacts, search_term, name, phone, email, address):
    updated = False
    for contact in contacts:
        if search_term.lower() in contact['name'].lower() or search_term in contact['phone']:
            contact['name'] = name
            contact['phone'] = phone
            contact['email'] = email
            contact['address'] = address
            save_contacts(contacts)
            updated = True
            print("Contact updated.")
            break
    if not updated:
        print("No matching contacts found.")

# Delete a contact
def delete_contact(contacts, search_term):
    deleted = False
    for contact in contacts:
        if search_term.lower() in contact['name'].lower() or search_term in contact['phone']:
            contacts.remove(contact)
            save_contacts(contacts)
            deleted = True
            print("Contact deleted.")
            break
    if not deleted:
        print("No matching contacts found.")

def command_line_contact_book():
    contacts = load_contacts()

    while True:
        print("\nContact Book")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice: ")
        if choice == '1':
            name = input("Enter name: ")
            phone = input("Enter phone number: ")
            email = input("Enter email: ")
            address = input("Enter address: ")
            add_contact(contacts, name, phone, email, address)
        elif choice == '2':
            view_contacts(contacts)
        elif choice == '3':
            search_term = input("Enter name or phone number to search: ")
            search_contacts(contacts, search_term)
        elif choice == '4':
            search_term = input("Enter name or phone number to update: ")
            name = input("Enter new name: ")
            phone = input("Enter new phone number: ")
            email = input("Enter new email: ")
            address = input("Enter new address: ")
            update_contact(contacts, search_term, name, phone, email, address)
        elif choice == '5':
            search_term = input("Enter name or phone number to delete: ")
            delete_contact(contacts, search_term)
        elif choice == '6':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    command_line_contact_book()
