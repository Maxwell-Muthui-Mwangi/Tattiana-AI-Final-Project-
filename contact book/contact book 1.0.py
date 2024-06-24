import tkinter as tk
from tkinter import messagebox
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

# Tkinter GUI class
class ContactBookApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Contact Book")
        self.geometry("600x400")

        self.contacts = load_contacts()

        self.create_widgets()
        self.display_contacts()

    def create_widgets(self):
        self.name_label = tk.Label(self, text="Name:")
        self.name_label.grid(row=0, column=0, padx=10, pady=5, sticky="e")
        self.name_entry = tk.Entry(self)
        self.name_entry.grid(row=0, column=1, padx=10, pady=5)

        self.phone_label = tk.Label(self, text="Phone:")
        self.phone_label.grid(row=1, column=0, padx=10, pady=5, sticky="e")
        self.phone_entry = tk.Entry(self)
        self.phone_entry.grid(row=1, column=1, padx=10, pady=5)

        self.email_label = tk.Label(self, text="Email:")
        self.email_label.grid(row=2, column=0, padx=10, pady=5, sticky="e")
        self.email_entry = tk.Entry(self)
        self.email_entry.grid(row=2, column=1, padx=10, pady=5)

        self.address_label = tk.Label(self, text="Address:")
        self.address_label.grid(row=3, column=0, padx=10, pady=5, sticky="e")
        self.address_entry = tk.Entry(self)
        self.address_entry.grid(row=3, column=1, padx=10, pady=5)

        self.add_button = tk.Button(self, text="Add Contact", command=self.add_contact)
        self.add_button.grid(row=4, column=0, padx=10, pady=5)

        self.update_button = tk.Button(self, text="Update Contact", command=self.update_contact)
        self.update_button.grid(row=4, column=1, padx=10, pady=5)

        self.delete_button = tk.Button(self, text="Delete Contact", command=self.delete_contact)
        self.delete_button.grid(row=5, column=0, padx=10, pady=5)

        self.search_label = tk.Label(self, text="Search:")
        self.search_label.grid(row=6, column=0, padx=10, pady=5, sticky="e")
        self.search_entry = tk.Entry(self)
        self.search_entry.grid(row=6, column=1, padx=10, pady=5)
        self.search_button = tk.Button(self, text="Search", command=self.search_contact)
        self.search_button.grid(row=6, column=2, padx=10, pady=5)

        self.contacts_listbox = tk.Listbox(self, width=80, height=15)
        self.contacts_listbox.grid(row=7, column=0, columnspan=3, padx=10, pady=5)

    def display_contacts(self):
        self.contacts_listbox.delete(0, tk.END)
        for contact in self.contacts:
            self.contacts_listbox.insert(tk.END, f"Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}, Address: {contact['address']}")

    def add_contact(self):
        name = self.name_entry.get()
        phone = self.phone_entry.get()
        email = self.email_entry.get()
        address = self.address_entry.get()
        if name and phone:
            new_contact = {
                "name": name,
                "phone": phone,
                "email": email,
                "address": address
            }
            self.contacts.append(new_contact)
            save_contacts(self.contacts)
            self.display_contacts()
            self.clear_entries()
        else:
            messagebox.showerror("Error", "Name and phone are required fields.")

    def update_contact(self):
        search_term = self.search_entry.get()
        name = self.name_entry.get()
        phone = self.phone_entry.get()
        email = self.email_entry.get()
        address = self.address_entry.get()
        if search_term:
            update_contact(self.contacts, search_term, name, phone, email, address)
            self.display_contacts()
            self.clear_entries()
        else:
            messagebox.showerror("Error", "Search term is required.")

    def delete_contact(self):
        search_term = self.search_entry.get()
        if search_term:
            delete_contact(self.contacts, search_term)
            self.display_contacts()
            self.clear_entries()
        else:
            messagebox.showerror("Error", "Search term is required.")

    def search_contact(self):
        search_term = self.search_entry.get()
        if search_term:
            results = [contact for contact in self.contacts if search_term.lower() in contact['name'].lower() or search_term in contact['phone']]
            self.contacts_listbox.delete(0, tk.END)
            if results:
                for contact in results:
                    self.contacts_listbox.insert(tk.END, f"Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}, Address: {contact['address']}")
            else:
                self.contacts_listbox.insert(tk.END, "No matching contacts found.")
        else:
            self.display_contacts()

    def clear_entries(self):
        self.name_entry.delete(0, tk.END)
        self.phone_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)
        self.address_entry.delete(0, tk.END)
        self.search_entry.delete(0, tk.END)

if __name__ == "__main__":
    app = ContactBookApp()
    app.mainloop()
