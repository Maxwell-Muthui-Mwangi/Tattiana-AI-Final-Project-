import tkinter as tk
from tkinter import messagebox
import json
import os
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build

# File to store contacts
CONTACTS_FILE = "contacts.json"

# Google API credentials file
GOOGLE_TOKEN_FILE = "google_token.json"

# Google OAuth scopes
SCOPES = ['https://www.googleapis.com/auth/contacts']

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

# Save Google credentials to file
def save_google_token(token):
    with open(GOOGLE_TOKEN_FILE, 'w') as file:
        json.dump(token, file)

# Load Google credentials from file
def load_google_token():
    if os.path.exists(GOOGLE_TOKEN_FILE):
        with open(GOOGLE_TOKEN_FILE, 'r') as file:
            return json.load(file)
    return None

# Tkinter GUI class
class ContactBookApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Contact Book")
        self.geometry("600x400")

        self.contacts = load_contacts()

        self.create_widgets()
        self.display_contacts()

        self.google_service = None
        self.google_authenticated = False
        self.google_token = load_google_token()
        if self.google_token:
            self.setup_google_service()

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

        self.save_google_button = tk.Button(self, text="Save to Google", command=self.save_to_google)
        self.save_google_button.grid(row=4, column=1, padx=10, pady=5)

        self.update_button = tk.Button(self, text="Update Contact", command=self.update_contact)
        self.update_button.grid(row=5, column=0, padx=10, pady=5)

        self.delete_button = tk.Button(self, text="Delete Contact", command=self.delete_contact)
        self.delete_button.grid(row=5, column=1, padx=10, pady=5)

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
            # Check if any contact matches the search term
            found = False
            for contact in self.contacts:
                if search_term.lower() in contact['name'].lower() or search_term in contact['phone']:
                    contact['name'] = name if name else contact['name']
                    contact['phone'] = phone if phone else contact['phone']
                    contact['email'] = email if email else contact['email']
                    contact['address'] = address if address else contact['address']
                    found = True
                    break

            if found:
                # Save updated contacts to file
                save_contacts(self.contacts)
                self.display_contacts()
                self.clear_entries()
            else:
                messagebox.showerror("Error", "No matching contact found.")
        else:
            messagebox.showerror("Error", "Search term is required.")

    def delete_contact(self):
        search_term = self.search_entry.get()
        if search_term:
            # Check if any contact matches the search term
            matching_contacts = [contact for contact in self.contacts
                                if search_term.lower() in contact['name'].lower()
                                or search_term in contact['phone']]
            
            if matching_contacts:
                # Display a confirmation dialog
                confirmed = messagebox.askyesno("Confirm Deletion", "Are you sure you want to delete this contact?")
                if confirmed:
                    # Remove all matching contacts from self.contacts
                    self.contacts = [contact for contact in self.contacts
                                    if search_term.lower() not in contact['name'].lower()
                                    and search_term not in contact['phone']]
                    
                    # Save updated contacts to file
                    save_contacts(self.contacts)
                    self.display_contacts()
                    self.clear_entries()
            else:
                messagebox.showerror("Error", "No matching contacts found.")
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

    def save_to_google(self):
        if not self.google_authenticated:
            self.authenticate_google()
        if self.google_authenticated:
            new_contacts = []
            for contact in self.contacts:
                new_contact = {
                    'names': [{'displayName': contact['name']}],
                    'phoneNumbers': [{'value': contact['phone']}]
                }
                if contact['email']:
                    new_contact['emailAddresses'] = [{'value': contact['email']}]
                if contact['address']:
                    new_contact['addresses'] = [{'formattedValue': contact['address']}]
                new_contacts.append(new_contact)
            response = self.google_service.people().createContact(body=new_contacts).execute()
            if response.get('createdContact'):
                messagebox.showinfo("Success", "Contacts saved to Google successfully.")
            else:
                messagebox.showerror("Error", "Failed to save contacts to Google.")

    def authenticate_google(self):
        flow = InstalledAppFlow.from_client_secrets_file(
            'credentials.json', SCOPES)
        self.google_token = flow.run_local_server(port=0)
        self.google_authenticated = True
        save_google_token(self.google_token)
        self.setup_google_service()

    def setup_google_service(self):
        if self.google_token:
            credentials = Credentials(
                token=self.google_token['token'],
                refresh_token=self.google_token.get('refresh_token', None),
                token_uri=self.google_token['token_uri'],
                client_id=self.google_token['client_id'],
                client_secret=self.google_token['client_secret'],
                scopes=SCOPES
            )
            self.google_service = build('people', 'v1', credentials=credentials)

if __name__ == "__main__":
    app = ContactBookApp()
    app.mainloop()
