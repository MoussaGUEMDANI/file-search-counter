import tkinter as tk
from tkinter import filedialog

selected_directory = ""

def select_directory():
    global selected_directory

    selected_directory = filedialog.askdirectory()

    if selected_directory:
        directory_label.config(text=selected_directory)

def search():
    search_text = search_entry.get()

    print(f"You searched for: {search_text}")

# main
def main():
    global directory_label
    global search_entry

    root = tk.Tk()

    root.title("File Search Counter")
    root.geometry("700x500")

    title = tk.Label(
        root,
        text="File Search Counter", 
        font=("Arial", 20, "bold"),
    )

    title.pack(pady=30)

    select_button = tk.Button(
        root,
        text="Select Directory",
        command=select_directory,    
    )

    select_button.pack(pady=10)

    directory_label = tk.Label(
        root,
        text="No directory selected",
        wraplength=600,
    )

    directory_label.pack(pady=10)

    search_label = tk.Label(
        root,
        text="Enter a word or sentence:",
    )

    search_label.pack(pady=(20, 5))

    search_entry = tk.Entry(
        root,
        width=60,
    )

    search_entry.pack(pady=5)

    search_button = tk.Button(
        root,
        text="Search",
        command=search,
    )

    search_button.pack(pady=15)

    root.mainloop()

    
if __name__ == "__main__":
    main()