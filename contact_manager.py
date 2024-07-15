import tkinter as tk
from tkinter import messagebox, simpledialog
import json
import os

class ContactManagerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("PRODIGY INFOTECH - Contact Management System")
        
        self.contacts = self.load_contacts()

        self.title_label = tk.Label(root, text="Contact Management System", font=("Helvetica", 16, "bold"))
        self.title_label.pack(pady=10)

        self.add_button = tk.Button(root, text="Add Contact", command=self.add_contact)
        self.add_button.pack(pady=5)

        self.view_button = tk.Button(root, text="View Contacts", command=self.view_contacts)
        self.view_button.pack(pady=5)

        self.edit_button = tk.Button(root, text="Edit Contact", command=self.edit_contact)
        self.edit_button.pack(pady=5)

        self.delete_button = tk.Button(root, text="Delete Contact", command=self.delete_contact)
        self.delete_button.pack(pady=5)

    def load_contacts(self):
        if os.path.exists("contacts.json"):
            with open("contacts.json", "r") as file:
                return json.load(file)
        return {}

    def save_contacts(self):
        with open("contacts.json", "w") as file:
            json.dump(self.contacts, file, indent=4)

    def add_contact(self):
        name = simpledialog.askstring("Input", "Enter name:")
        if not name:
            return
        phone = simpledialog.askstring("Input", "Enter phone number:")
        if not phone:
            return
        email = simpledialog.askstring("Input", "Enter email address:")
        if not email:
            return

        self.contacts[name] = {"phone": phone, "email": email}
        self.save_contacts()
        messagebox.showinfo("Success", "Contact added successfully!")

    def view_contacts(self):
        contact_list = ""
        for name, info in self.contacts.items():
            contact_list += f"Name: {name}\nPhone: {info['phone']}\nEmail: {info['email']}\n\n"
        
        if contact_list:
            messagebox.showinfo("Contact List", contact_list)
        else:
            messagebox.showinfo("Contact List", "No contacts found.")

    def edit_contact(self):
        name = simpledialog.askstring("Input", "Enter the name of the contact to edit:")
        if name not in self.contacts:
            messagebox.showerror("Error", "Contact not found.")
            return

        phone = simpledialog.askstring("Input", "Enter new phone number:", initialvalue=self.contacts[name]["phone"])
        if not phone:
            return
        email = simpledialog.askstring("Input", "Enter new email address:", initialvalue=self.contacts[name]["email"])
        if not email:
            return

        self.contacts[name] = {"phone": phone, "email": email}
        self.save_contacts()
        messagebox.showinfo("Success", "Contact updated successfully!")

    def delete_contact(self):
        name = simpledialog.askstring("Input", "Enter the name of the contact to delete:")
        if name not in self.contacts:
            messagebox.showerror("Error", "Contact not found.")
            return

        del self.contacts[name]
        self.save_contacts()
        messagebox.showinfo("Success", "Contact deleted successfully!")

if __name__ == "__main__":
    root = tk.Tk()
    app = ContactManagerApp(root)
    root.mainloop()
