import tkinter as tk
from tkinter import messagebox

class AccountCreationApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Account Creation")
        self.root.geometry("400x400")
        self.root.configure(bg="#f0f0f0")
        
        # Styling
        label_font = ("Arial", 12, "bold")
        entry_font = ("Arial", 12)
        button_font = ("Arial", 12, "bold")
        
        # Labels
        tk.Label(root, text="Name:", font=label_font, bg="#f0f0f0").grid(row=0, column=0, padx=10, pady=10, sticky="e")
        tk.Label(root, text="Email:", font=label_font, bg="#f0f0f0").grid(row=1, column=0, padx=10, pady=10, sticky="e")
        tk.Label(root, text="Age:", font=label_font, bg="#f0f0f0").grid(row=2, column=0, padx=10, pady=10, sticky="e")
        tk.Label(root, text="Password:", font=label_font, bg="#f0f0f0").grid(row=3, column=0, padx=10, pady=10, sticky="e")
        tk.Label(root, text="Confirm Password:", font=label_font, bg="#f0f0f0").grid(row=4, column=0, padx=10, pady=10, sticky="e")
        
        # Entry fields
        self.name_entry = tk.Entry(root, font=entry_font, width=25)
        self.email_entry = tk.Entry(root, font=entry_font, width=25)
        self.age_entry = tk.Entry(root, font=entry_font, width=25)
        self.password_entry = tk.Entry(root, font=entry_font, width=25, show="*")
        self.confirm_password_entry = tk.Entry(root, font=entry_font, width=25, show="*")
        
        self.name_entry.grid(row=0, column=1, padx=10, pady=10)
        self.email_entry.grid(row=1, column=1, padx=10, pady=10)
        self.age_entry.grid(row=2, column=1, padx=10, pady=10)
        self.password_entry.grid(row=3, column=1, padx=10, pady=10)
        self.confirm_password_entry.grid(row=4, column=1, padx=10, pady=10)
        
        # Submit button
        tk.Button(root, text="Create Account", font=button_font, bg="#4CAF50", fg="white", command=self.create_account).grid(row=5, column=0, columnspan=2, pady=20)

    def create_account(self):
        name = self.name_entry.get()
        email = self.email_entry.get()
        age = self.age_entry.get()
        password = self.password_entry.get()
        confirm_password = self.confirm_password_entry.get()
        
        if not name or not email or not age or not password or not confirm_password:
            messagebox.showerror("Error", "All fields are required!")
            return
        
        if password != confirm_password:
            messagebox.showerror("Error", "Passwords do not match!")
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
