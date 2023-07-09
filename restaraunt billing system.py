import tkinter as tk
menu = {
    "Burger": 120.00,
    "Pizza": 240.00,
    "Fries": 80.00,
    "Soda": 15.00,
    "Noodles":60.00,
    "Manchuria":40.00,
    "Panipuri":20.00,
    "Soft Drink":20.00
}
quantities = {item: 0 for item in menu.keys()}
def calculate_total():
    subtotal = sum(menu[item] * quantities[item] for item in menu)
    tax = 0.1 * subtotal  
    total = subtotal + tax
    return subtotal, tax, total
def update_quantity(*args):
    item = args[0]
    quantity_str = entry_vars[item].get()
    if quantity_str == "":
        quantity = 0
    else:
        quantity = int(quantity_str)
    quantities[item] = quantity
def clear_quantities():
    for item in quantities:
        quantities[item] = 0
        entry_vars[item].set("")
def show_result():
    subtotal, tax, total = calculate_total()
    subtotal_label.config(text=f"Subtotal: ${subtotal:.2f}")
    tax_label.config(text=f"Tax: ${tax:.2f}")
    total_label.config(text=f"Total: ${total:.2f}")

root = tk.Tk()
root.title("Restaurant Billing System")
entry_vars = {}
row = 0
for item, cost in menu.items():
    item_label = tk.Label(root, text=item)
    item_label.grid(row=row, column=0)

    cost_label = tk.Label(root, text=f"${cost:.2f}")
    cost_label.grid(row=row, column=1)

    entry_var = tk.StringVar(value="")
    entry_vars[item] = entry_var
    quantity_entry = tk.Entry(root, textvariable=entry_var, width=5)
    quantity_entry.grid(row=row, column=2)

    entry_var.trace_add("write", lambda *args, item=item: update_quantity(item, *args))

    row += 1

calculate_button = tk.Button(root, text="Calculate", command=show_result)
calculate_button.grid(row=row, column=0, pady=10)

clear_button = tk.Button(root, text="Clear", command=clear_quantities)
clear_button.grid(row=row, column=1, pady=10)

subtotal_label = tk.Label(root, text="Subtotal: $0.00")
subtotal_label.grid(row=row+1, column=0, columnspan=2, pady=5)

tax_label = tk.Label(root, text="Tax: $0.00")
tax_label.grid(row=row+2, column=0, columnspan=2, pady=5)

total_label = tk.Label(root, text="Total: $0.00")
total_label.grid(row=row+3, column=0, columnspan=2, pady=5)

root.mainloop()
