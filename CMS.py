import tkinter as tk
from tkinter import simpledialog, messagebox

# Class for the linked list
class ContactNode:
    def __init__(self, name, contact_number):
        self.name = name
        self.contact_number = contact_number
        self.prev = None
        self.next = None

# Doubly linked list class
class ContactList:
    def __init__(self):
        self.head = None

    # Insert Contact
    def insert_contact(self, name, contact_number):
        new_node = ContactNode(name, contact_number)

        # Handle empty list
        if self.head is None:
            self.head = new_node
            return

        if name < self.head.name:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
            return

        current = self.head

        # Find the correct place
        while current.next is not None and name > current.next.name:
            current = current.next

        new_node.next = current.next
        if current.next is not None:
            current.next.prev = new_node
        current.next = new_node
        new_node.prev = current

    # Search the contact
    def search_contact(self, name=None, contact_number=None):
        if name is None and contact_number is None:
            return None

        current = self.head

        while current is not None:
            if current.name == name or current.contact_number == contact_number:
                return current
            current = current.next

        return None

    # Delete a Number
    def delete_contact(self, contact_number):
        if self.head is None:
            return

        current = self.head

        # Delete the head node
        if current.contact_number == contact_number:
            self.head = current.next
            if current.next is not None:
                current.next.prev = None
            return

        while current is not None and current.contact_number != contact_number:
            current = current.next

        # Contact didn't exist
        if current is None:
            return

        if current.prev is not None:
            current.prev.next = current.next
        if current.next is not None:
            current.next.prev = current.prev

    # View all the list
    def view_contacts(self):
        contacts = ""
        current = self.head
        count = 1

        while current is not None:
            contacts += f"{count}. Name: {current.name}\n   Contact Number: {current.contact_number}\n\n"
            current = current.next
            count += 1

        return contacts

    # Generate Contact Information Report
    def generate_report(self):
        report = self.view_contacts()
        with open("C:/Users/Methmi Maleeshs/Desktop/contact_information_report.txt", "w") as file:
            file.write(report)

# Create a tkinter window
window = tk.Tk()
window.title("Contact Management System")

# Customize window colors
window.configure(bg="#f0f0f0")

# Create a ContactList object
contact_list = ContactList()

# Function to add a contact
def add_contact():
    name = simpledialog.askstring("Add Contact", "Enter Name: " + " " * 80, initialvalue="" )
    contact_number = simpledialog.askstring("Add Contact", "Enter Contact Number: " + " " * 80, initialvalue="")
    contact_list.insert_contact(name, contact_number)
    update_contacts_display()

# Function to search a contact
def search_contact():
    search_name = simpledialog.askstring("Search Contact", "Enter Name to search: " + " " * 80, initialvalue="")
    contact = contact_list.search_contact(name=search_name)
    if contact:
        messagebox.showinfo("Search Contact", f"Contact found:\nName: {contact.name}\nContact Number: {contact.contact_number}" + " " * 50)
    else:
        messagebox.showinfo("Search Contact", "Contact not found" + " " * 80)

# Function to delete a contact
def delete_contact():
    delete_name = simpledialog.askstring("Delete Contact", "Enter name to delete: " + " " * 80, initialvalue="")
    contact = contact_list.search_contact(name=delete_name)
    if contact:
        contact_list.delete_contact(contact.contact_number)
        messagebox.showinfo("Delete Contact", "Contact deleted successfully!" + " " * 80)
        update_contacts_display()
    else:
        messagebox.showinfo("Delete Contact", "Contact not found" + " " * 80)

# Function to update a contact
def update_contact():
    search_name = simpledialog.askstring("Update Contact", "Enter name to search: " + " " * 80, initialvalue="")
    contact = contact_list.search_contact(name=search_name)
    if contact:
        update_choice = simpledialog.askstring("Update Contact", f"Contact found:\nName: {contact.name}\nContact Number: {contact.contact_number}\n\nEnter 'name' to update name or 'number' to update contact number: " + " " * 50, initialvalue="")
        if update_choice == 'name':
            update_name = simpledialog.askstring("Update Contact", "Enter updated name: " + " " * 80, initialvalue="")
            contact.name = update_name
        elif update_choice == 'number':
            update_number = simpledialog.askstring("Update Contact", "Enter updated contact number: " + " " * 80, initialvalue="")
            contact.contact_number = update_number
        messagebox.showinfo("Update Contact", "Contact updated successfully!" + " " * 80)
        update_contacts_display()
    else:
        messagebox.showinfo("Update Contact", "Contact not found" + " " * 80)

# Function to update the contacts display
def update_contacts_display():
    contacts_text.config(state=tk.NORMAL)
    contacts_text.delete("1.0", tk.END)
    contacts_text.insert(tk.END, contact_list.view_contacts())
    contacts_text.config(state=tk.DISABLED)

# Function to generate the report
def generate_report():
    contact_list.generate_report()
    messagebox.showinfo("Report Generated", "Contact Information Report generated successfully as 'contact_information_report.txt'." + " " * 80)

# Create buttons for each operation
add_button = tk.Button(window, text="Add Contact", command=add_contact, width=15)
add_button.grid(row=0, column=0, padx=10, pady=10)

search_button = tk.Button(window, text="Search Contact", command=search_contact, width=15)
search_button.grid(row=1, column=0, padx=10, pady=10)

update_button = tk.Button(window, text="Update Contact", command=update_contact, width=15)
update_button.grid(row=2, column=0, padx=10, pady=10)

delete_button = tk.Button(window, text="Delete Contact", command=delete_contact, width=15)
delete_button.grid(row=3, column=0, padx=10, pady=10)

generate_report_button = tk.Button(window, text="Generate Report", command=generate_report, width=15)
generate_report_button.grid(row=4, column=0, padx=10, pady=10)


# Create a frame to display contacts
contacts_frame = tk.Frame(window, bg="#ffffff")
contacts_frame.grid(row=0, column=1, rowspan=4, padx=10, pady=10)

# Create a label for contact information title
contacts_title_label = tk.Label(contacts_frame, text="Contact Information", font=("Arial", 12, "bold"), bg="#ffffff")
contacts_title_label.pack()

# Create a text widget to display contacts
contacts_text = tk.Text(contacts_frame, height=20, width=50)
contacts_text.pack()
contacts_text.config(state=tk.DISABLED)

# Update contacts display initially
update_contacts_display()

# Start the GUI
window.mainloop()
