import tkinter as tk
from tkinter import filedialog

selected_file = ""

def select_file():
    global selected_file

    selected_file = filedialog.askopenfilename()

    if selected_file:
        file_label.config(text=selected_file)


def search():
    search_text = search_entry.get().strip()

    if not selected_file:
        result_label.config(
            text="Please select a file first."
            )
        return

    if not search_text:
        result_label.config(
            text=f'Search: "{search_text}"   Count: {count}'
            )
        return

    try:
        with open(
            selected_file, 
            "r", 
            encoding="utf-8", 
            errors="ignore"
        ) as file:
            content = file.read()

        count = content.lower().count(
            search_text.lower()
        )

        result_label.config(
            text=f"Count: {count}"
            )

    except Exception as error:
        result_label.config(
            text=f"Could not read file: {error}"
            )

# main
def main():
    global result_label
    global file_label
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
        text="Select File",
        command=select_file,    
    )

    select_button.pack(pady=10)

    file_label = tk.Label(
        root,
        text="No file selected",
        wraplength=600,
    )

    file_label.pack(pady=10)

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

    result_label = tk.Label(
        root,
        text="Result:",
    )

    result_label.pack(pady=10)

    root.mainloop()

    
if __name__ == "__main__":
    main()