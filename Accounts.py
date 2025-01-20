import tkinter as tk
from tkinter import messagebox

class AccountCreationApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Account Creation")
        
        # Labels
        tk.Label(root, text="Name:").grid(row=0, column=0, padx=10, pady=10)
        tk.Label(root, text="Email:").grid(row=1, column=0, padx=10, pady=10)
        tk.Label(root, text="Age:").grid(row=2, column=0, padx=10, pady=10)
        
        # Entry fields
        self.name_entry = tk.Entry(root)
        self.email_entry = tk.Entry(root)
        self.age_entry = tk.Entry(root)
        
        self.name_entry.grid(row=0, column=1, padx=10, pady=10)
        self.email_entry.grid(row=1, column=1, padx=10, pady=10)
        self.age_entry.grid(row=2, column=1, padx=10, pady=10)
        
        # Submit button
        tk.Button(root, text="Create Account", command=self.create_account).grid(row=3, column=0, columnspan=2, pady=20)

    def create_account(self):
        name = self.name_entry.get()
        email = self.email_entry.get()
        age = self.age_entry.get()
        
        if not name or not email or not age:
            messagebox.showerror("Error", "All fields are required!")
            return
        
        try:
            age = int(age)
            if age < 0:
                raise ValueError
        except ValueError:
            messagebox.showerror("Error", "Age must be a valid positive number!")
            return
        
        messagebox.showinfo("Success", f"Account created for {name} ({email}), Age: {age}")

if __name__ == "__main__":
    root = tk.Tk()
    app = AccountCreationApp(root)
    root.mainloop()
