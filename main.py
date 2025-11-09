import os
import django
import tkinter as tk
from tkinter import messagebox

# Configure Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")
django.setup()

from db.models import Product

# Populate DB (we have used the same data as we had in assignment2)
def populate_products():
    products = [
            {"upc": "12345", "name": "Hot Chocolate", "price": 3.49},
            {"upc": "67890", "name": "Timbits", "price": 2.50},
            {"upc": "54321", "name": "Wrap", "price": 6.75},
            {"upc": "98765", "name": "Bagel", "price": 3.00},
            {"upc": "38929", "name": "Pizza", "price": 6.00},
            {"upc": "11223", "name": "Latte", "price": 4.25},
            {"upc": "33445", "name": "Croissant", "price": 2.75},
            {"upc": "55667", "name": "Sandwich", "price": 5.50},
            {"upc": "77889", "name": "Muffin", "price": 2.50},
            {"upc": "99001", "name": "Tea", "price": 1.99},
            {"upc": "10101", "name": "Cappuccino", "price": 4.50},
            {"upc": "20202", "name": "Donut", "price": 1.25},
            {"upc": "30303", "name": "Chocolate Bar", "price": 1.75},
            {"upc": "40404", "name": "Granola Bar", "price": 2.00},
            {"upc": "50505", "name": "Apple Juice", "price": 2.99},
            {"upc": "20221", "name": "Chocolate Milk", "price": 2.75},
            {"upc": "21212", "name": "Smoothie", "price": 4.99},
            {"upc": "22222", "name": "Brownie", "price": 3.25},
            {"upc": "23232", "name": "Macaron", "price": 1.99},
    ]
    for p in products:
        Product.objects.get_or_create(upc=p["upc"], defaults={"name": p["name"], "price": p["price"]})
    print("✅ Database populated with products.\n")

# Tkinter Functions
scanned_products = []  # list to hold scanned items
subtotal = 0.0         # running total

# Handles product scanning by UPC and updates UI elements.
def scan_product():
    global subtotal
    upc = entry.get().strip()

    if not upc:
        messagebox.showwarning("Input Error", "Please enter a UPC code.")
        return
    
    try:
        # product lookup in DB
        product = Product.objects.get(upc=upc)  

        # Add product to listbox
        listbox.insert(tk.END, f"{product.name} - ${product.price:.2f}")
        scanned_products.append(product)

        # Update subtotal
        subtotal += float(product.price)
        subtotal_label.config(text=f"Subtotal: ${subtotal:.2f}")

        # Clear the entry field for next scan
        entry.delete(0, tk.END)

    except Product.DoesNotExist:
        messagebox.showerror("Not Found", "❌ Product not found. Please try again.")

# Clears the scanned list and resets subtotal.
def clear_list():
    global subtotal, scanned_products
    scanned_products.clear()
    listbox.delete(0, tk.END)
    subtotal = 0.0
    subtotal_label.config(text="Subtotal: $0.00")
    
# GUI Setup
root = tk.Tk()
root.title("Cash Register - Product Scanner")

# Setting modal dimensions
window_width = 1000
window_height = 1000

# Set desired window size
window_width = 500
window_height = 450

# Get screen width and height
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Calculate x and y coordinates for centering modal
x = int((screen_width / 2) - (window_width / 2))
y = int((screen_height / 2) - (window_height / 2))

# Applying geometry dynamically so it opens centered
root.geometry(f"{window_width}x{window_height}+{x}+{y}")
root.configure(bg="#f5f5f5")

# UPC Input section
tk.Label(root, text="Enter UPC Code:", font=("Arial", 12, "bold"), bg="#f5f5f5").pack(pady=10)
entry = tk.Entry(root, font=("Arial", 12), width=25)
entry.pack(pady=5)

# Scan and CLear Buttons
btn_frame = tk.Frame(root, bg="#f5f5f5")
btn_frame.pack(pady=5)
tk.Button(btn_frame, text="Scan", command=scan_product, font=("Arial", 11), width=10, bg="#4CAF50", activebackground="#33a539" ).grid(row=0, column=0, padx=5)
tk.Button(btn_frame, text="Clear", command=clear_list, font=("Arial", 11), width=10, bg="#CB1E0A",fg="white", activebackground="#900F01").grid(row=0, column=1, padx=5)

# Listbox for scanned products
tk.Label(root, text="Scanned Products:", font=("Arial", 12, "bold"), bg="#f5f5f5").pack(pady=10)

# Frame to hold listbox + scrollbar
list_frame = tk.Frame(root, bg="#f5f5f5")
list_frame.pack(pady=5)

# Create a scrollbar
scrollbar = tk.Scrollbar(list_frame, orient="vertical")

# Create listbox and attach scrollbar to it
listbox = tk.Listbox(list_frame,width=45,height=10,font=("Arial", 12),yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)
listbox.pack(side="left", fill="both", expand=True)
scrollbar.pack(side="right", fill="y")

# Subtotal display
subtotal_label = tk.Label(root, text="Subtotal: $0.00", font=("Arial", 13, "bold"), bg="#f5f5f5", fg="#000000")
subtotal_label.pack(pady=10)

# Run Setuup
populate_products()
root.mainloop()
