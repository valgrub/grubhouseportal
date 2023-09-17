import tkinter as tk
from tkinter import ttk
import random

class CommonPage:
    def __init__(self, root, title_text):
        self.root = root
        self.root.title("Log Gen - v.BETA")

        # Create a frame for the page components
        self.page_frame = ttk.Frame(root)
        self.page_frame.pack()

        # Create a label for the common title
        self.title_label = ttk.Label(self.page_frame, text=title_text, font=("Helvetica", 16, "bold"))
        self.title_label.pack(pady=10)

        # Create a label for the version
        self.version_label = ttk.Label(self.page_frame, text="v.BETA", font=("Helvetica", 12))
        self.version_label.pack()

        # Create a button for the log list
        self.log_list_button = ttk.Button(self.page_frame, text="Log List", command=self.show_log_list)
        self.log_list_button.pack(pady=10)

        # Create a back button (initially hidden)
        self.back_button = ttk.Button(root, text="Back", command=self.show_main_menu)
        self.back_button.pack(pady=10)
        self.back_button.pack_forget()

        # Initialize a variable to store the "Coming Soon" label
        self.coming_soon_label = None

    def show_coming_soon(self):
        # Clear the page frame
        for widget in self.page_frame.winfo_children():
            widget.destroy()

        # Create a label to display "Coming Soon"
        self.coming_soon_label = ttk.Label(self.root, text="Coming Soon", font=("Helvetica", 14))
        self.coming_soon_label.pack(pady=30)

        # Show the back button
        self.back_button.pack()

    def show_main_menu(self):
        # Clear the "Coming Soon" label if it exists
        if self.coming_soon_label:
            self.coming_soon_label.destroy()
            self.coming_soon_label = None

        # Clear all widgets in the page frame
        for widget in self.page_frame.winfo_children():
            widget.destroy()

        # Recreate the page components
        self.title_label = ttk.Label(self.page_frame, text="Log Gen", font=("Oswald", 16, "bold"))
        self.title_label.pack(pady=10)

        self.version_label = ttk.Label(self.page_frame, text="v.BETA", font=("Helvetica", 12))
        self.version_label.pack()

        self.log_list_button = ttk.Button(self.page_frame, text="Log List", command=self.show_log_list)
        self.log_list_button.pack(pady=10)

        # Hide the back button
        self.back_button.pack_forget()

    def show_log_list(self):
        # Clear the page frame
        for widget in self.page_frame.winfo_children():
            widget.destroy()

        # Create a label for the title
        log_list_label = ttk.Label(self.page_frame, text="Log List", font=("Helvetica", 16, "bold"))
        log_list_label.pack(pady=10)

        # Create a list of text entries with "Generate Log" buttons
        self.log_entries = []
        log_text = "Wendys Log"
        log_frame = ttk.Frame(self.page_frame)
        log_frame.pack()

        log_label = ttk.Label(log_frame, text=f"{log_text} —>", font=("Helvetica", 14))
        log_label.pack(side=tk.LEFT)

        # Create a "Generate" button for each log entry (initially)
        generate_button = ttk.Button(log_frame, text="Generate", command=lambda text=log_text: self.generate_log(text))
        generate_button.pack(side=tk.LEFT)

        self.log_entries.append({"log_frame": log_frame, "log_text": log_text, "generate_button": generate_button})

        # Create a text widget to display log entries (3 lines)
        self.log_display_text = tk.Text(self.page_frame, height=3, width=40)
        self.log_display_text.pack()

        # Show the back button
        self.back_button.pack()

    def generate_log(self, log_text):
        # Clear the last log entry
        self.log_display_text.config(state=tk.NORMAL)
        self.log_display_text.delete("1.0", tk.END)

        # For demonstration purposes, let's generate a random log entry
        log_entries = {
            "Wendys Log": [
                "Baileydeanna98@icloud.com:Soithought1  Points: [349]",
                "felicia.bailey1987@yahoo.com:Cocoaloco1!  Points: [349]",
                "Jeck_UG@nec.edu:Slark329  Points: [348]",
                "Jcoffman520@yahoo.com:Anakin1121   Points: [328]"
            ],
            "McDonald's Log": ["LOGIN - 12M", "ORDER - 34D", "DELIVERY - 9T"],
            "Burger King Log": ["LOGIN - 78B", "ORDER - 22K", "DELIVERY - 16R"],
            "Taco Bell Log": ["LOGIN - 55T", "ORDER - 29F", "DELIVERY - 11E"],
            "KFC Log": ["LOGIN - 43K", "ORDER - 18C", "DELIVERY - 7L"]
        }

        if log_text in log_entries:
            random_log_entry = random.choice(log_entries[log_text])
            self.log_display_text.insert(tk.END, random_log_entry)
            self.log_display_text.config(state=tk.DISABLED)

def main():
    root = tk.Tk()
    app = CommonPage(root, "Home Page")
    root.mainloop()

if __name__ == "__main__":
    main()
import tkinter as tk
from tkinter import ttk
import random

class CommonPage:
    def __init__(self, root, title_text):
        self.root = root
        self.root.title("Log Gen - v.BETA")

        # Create a frame for the page components
        self.page_frame = ttk.Frame(root)
        self.page_frame.pack()

        # Create a label for the common title
        self.title_label = ttk.Label(self.page_frame, text=title_text, font=("Helvetica", 16, "bold"))
        self.title_label.pack(pady=10)

        # Create a label for the version
        self.version_label = ttk.Label(self.page_frame, text="v.BETA", font=("Helvetica", 12))
        self.version_label.pack()

        # Create a button for the log list
        self.log_list_button = ttk.Button(self.page_frame, text="Log List", command=self.show_log_list)
        self.log_list_button.pack(pady=10)

        # Create a back button (initially hidden)
        self.back_button = ttk.Button(root, text="Back", command=self.show_main_menu)
        self.back_button.pack(pady=10)
        self.back_button.pack_forget()

        # Initialize a variable to store the "Coming Soon" label
        self.coming_soon_label = None

    def show_coming_soon(self):
        # Clear the page frame
        for widget in self.page_frame.winfo_children():
            widget.destroy()

        # Create a label to display "Coming Soon"
        self.coming_soon_label = ttk.Label(self.root, text="Coming Soon", font=("Helvetica", 14))
        self.coming_soon_label.pack(pady=30)

        # Show the back button
        self.back_button.pack()

    def show_main_menu(self):
        # Clear the "Coming Soon" label if it exists
        if self.coming_soon_label:
            self.coming_soon_label.destroy()
            self.coming_soon_label = None

        # Clear all widgets in the page frame
        for widget in self.page_frame.winfo_children():
            widget.destroy()

        # Recreate the page components
        self.title_label = ttk.Label(self.page_frame, text="HOME PAGE", font=("Helvetica", 16, "bold"))
        self.title_label.pack(pady=10)

        self.version_label = ttk.Label(self.page_frame, text="v.BETA", font=("Helvetica", 12))
        self.version_label.pack()

        self.log_list_button = ttk.Button(self.page_frame, text="Log List", command=self.show_log_list)
        self.log_list_button.pack(pady=10)

        # Hide the back button
        self.back_button.pack_forget()

    def show_log_list(self):
        # Clear the page frame
        for widget in self.page_frame.winfo_children():
            widget.destroy()

        # Create a label for the title
        log_list_label = ttk.Label(self.page_frame, text="Log List", font=("Helvetica", 16, "bold"))
        log_list_label.pack(pady=10)

        # Create a list of text entries with "Generate Log" buttons
        self.log_entries = []
        log_text = "Wendys Log"
        log_frame = ttk.Frame(self.page_frame)
        log_frame.pack()

        log_label = ttk.Label(log_frame, text=f"{log_text} —>", font=("Helvetica", 14))
        log_label.pack(side=tk.LEFT)

        # Create a "Generate" button for each log entry (initially)
        generate_button = ttk.Button(log_frame, text="Generate", command=lambda text=log_text: self.generate_log(text))
        generate_button.pack(side=tk.LEFT)

        self.log_entries.append({"log_frame": log_frame, "log_text": log_text, "generate_button": generate_button})

        # Create a text widget to display log entries (3 lines)
        self.log_display_text = tk.Text(self.page_frame, height=3, width=40)
        self.log_display_text.pack()

        # Show the back button
        self.back_button.pack()

    def generate_log(self, log_text):
        # Clear the last log entry
        self.log_display_text.config(state=tk.NORMAL)
        self.log_display_text.delete("1.0", tk.END)

        # For demonstration purposes, let's generate a random log entry
        log_entries = {
            "Wendys Log": [
                "Baileydeanna98@icloud.com:Soithought1 Points: [349]",
                "felicia.bailey1987@yahoo.com:Cocoaloco1! Points: [349]",
                "Jeck_UG@nec.edu:Slark329 Points: [348]",
                "Jcoffman520@yahoo.com:Anakin1121 Points: [328]",
                "scoobyjoss69@aol.com:Everette01 | Points: [409]",
                "dahltristin@outlook.com:Hope53fist | Points: [409]",
                "pams1962@comcast.net:Sweetpea1 | Points = 1266",
                "Matthew_verville@hotmail.com:34Maddie! | Points = 968",
                "jasmin.torres25@yahoo.com:Laredo21 | Points = 962",
                "jaleecia2007@gmail.com:030488Em | Points = 990"
            ],
            "McDonald's Log": ["LOGIN - 12M", "ORDER - 34D", "DELIVERY - 9T"],
            "Burger King Log": ["LOGIN - 78B", "ORDER - 22K", "DELIVERY - 16R"],
            "Taco Bell Log": ["LOGIN - 55T", "ORDER - 29F", "DELIVERY - 11E"],
            "KFC Log": ["LOGIN - 43K", "ORDER - 18C", "DELIVERY - 7L"]
        }

        if log_text in log_entries:
            random_log_entry = random.choice(log_entries[log_text])
            self.log_display_text.insert(tk.END, random_log_entry)
            self.log_display_text.config(state=tk.DISABLED)

def main():
    root = tk.Tk()
    app = CommonPage(root, "Home Page")
    root.mainloop()

if __name__ == "__main__":
    main()
