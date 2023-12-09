import tkinter as tk

def search():
    query = entry_search.get()
    result_label.config(text="Search result for: " + query)

# Create the main window
root = tk.Tk()
root.title("Search Bar")

# Create and place widgets
label_search = tk.Label(root, text="Enter search query:")
label_search.pack(pady=10)

entry_search = tk.Entry(root, width=30)
entry_search.pack(pady=10)

btn_search = tk.Button(root, text="Search", command=search)
btn_search.pack(pady=10)

result_label = tk.Label(root, text="")
result_label.pack(pady=10)

# Run the Tkinter event loop
root.mainloop()
