import tkinter as tk
from tkinter import messagebox

def continue_to_blank_page():
    messagebox.showinfo("Continue", "Continuing to blank page...")
    # Code to navigate to a blank page goes here

def main():
    root = tk.Tk()
    root.title("Checkbox UI")
    root.configure(background="#001F3F")  # Navy color background

    # Custom font
    custom_font = ("Helvetica", 12)

    # Set column and row weights to make widgets scale
    root.columnconfigure(0, weight=1)
    root.rowconfigure(1, weight=1)

    # Create frame for checkboxes
    checkboxes_frame = tk.Frame(root, background="#001F3F")
    checkboxes_frame.grid(row=1, column=0, sticky="nsew")

    # Define column titles
    column_titles = ["Column 1", "Column 2", "Column 3"]

    # Create columns
    for i, title in enumerate(column_titles):
        column_frame = tk.Frame(checkboxes_frame, background="#001F3F")
        column_frame.grid(row=0, column=i, padx=5, pady=5, sticky="nsew")

        # Add column title
        tk.Label(column_frame, text=title, font=custom_font, fg="white", bg="#001F3F").pack()

        # Add checkboxes
        for j in range(5):
            tk.Checkbutton(column_frame, text=f"Checkbox {j+1}", font=custom_font, fg="white", bg="#001F3F",
                           selectcolor="#001F3F").pack(anchor=tk.W)

        # Set column weights
        checkboxes_frame.columnconfigure(i, weight=1)

    # Continue button
    continue_button = tk.Button(root, text="Continue", font=custom_font, command=continue_to_blank_page, bg="#0074D9", fg="white")
    continue_button.grid(row=2, column=0, pady=10, sticky="ew")

    root.mainloop()

if __name__ == "__main__":
    main()
