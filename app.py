import tkinter as tk

def main():
    root = tk.Tk()

    root.title("File Search Counter")
    root.geometry("700x400")

    title = tk.Label(
        root,
        text="File Search Counter", 
        font=("Arial", 20, "bold"),
    )

    title.pack(pady=30)

    root.mainloop()

    
if __name__ == "__main__":
    main()