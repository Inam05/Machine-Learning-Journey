from tkinter import *
from tkinter import ttk
from myDB import DataBase
from tkinter import messagebox
from myapi import API

class NLPApp:
    def __init__(self):
        """Initialize the NLP App GUI."""
        self.dbo = DataBase()  # Database Object
        self.myapi = API()  # API Object
        self.root = Tk()
        self.root.title('NLP APP | Inam Ul Hassan')

        # Slightly increased height for better UI spacing
        self.root.geometry('370x580')
        self.root.configure(bg='#2C3E50')

        # Safe icon loading
        try:
            self.root.iconbitmap('Resource/favicon.ico')
        except:
            print("Icon not found, continuing without it.")

        self.loginGUI()
        self.root.mainloop()

    def clear_window(self):
        """Clears all widgets from the window."""
        for widget in self.root.winfo_children():
            widget.destroy()

    def loginGUI(self):
        """Creates the Login GUI."""
        self.clear_window()

        Label(self.root, text="NLP APP", font=("Verdana", 22, "bold"), bg="#2C3E50", fg="white").pack(pady=15)
        Label(self.root, text="Login Here", font=("Verdana", 16, "bold"), bg="#2C3E50", fg="white").pack(pady=10)

        # Username
        Label(self.root, text="Email:", font=("Verdana", 12), bg="#2C3E50", fg="white").pack(pady=5)
        self.username_entry = Entry(self.root, font=("Verdana", 12), width=28, bg="#ECF0F1", fg="#2C3E50", bd=2, relief=FLAT)
        self.username_entry.pack(pady=5, ipady=5)

        # Password
        Label(self.root, text="Password:", font=("Verdana", 12), bg="#2C3E50", fg="white").pack(pady=5)
        self.password_entry = Entry(self.root, font=("Verdana", 12), width=28, show="*", bg="#ECF0F1", fg="#2C3E50", bd=2, relief=FLAT)
        self.password_entry.pack(pady=5, ipady=5)

        # Login Button
        Button(self.root, text="Login", font=("Verdana", 12, "bold"), bg="#27AE60", fg="white",
               bd=0, relief=FLAT, cursor="hand2", command=self.login).pack(pady=20, ipadx=40, ipady=7)

        # Sign Up Section
        Label(self.root, text="Not a member?", font=("Verdana", 10), bg="#2C3E50", fg="white").pack(pady=5)
        Button(self.root, text="Sign Up", font=("Verdana", 10, "bold"), fg="white", bg="#2980B9",
               bd=0, relief=FLAT, cursor="hand2", command=self.signupGUI).pack(pady=5, ipadx=20, ipady=3)

    def signupGUI(self):
        """Creates the Sign-Up GUI."""
        self.clear_window()

        Label(self.root, text="NLP APP", font=("Verdana", 22, "bold"), bg="#2C3E50", fg="white").pack(pady=15)
        Label(self.root, text="Sign Up Here", font=("Verdana", 16, "bold"), bg="#2C3E50", fg="white").pack(pady=10)

        # Name
        Label(self.root, text="Full Name:", font=("Verdana", 12), bg="#2C3E50", fg="white").pack(pady=5)
        self.name_entry = Entry(self.root, font=("Verdana", 12), width=28, bg="#ECF0F1", fg="#2C3E50", bd=2, relief=FLAT)
        self.name_entry.pack(pady=5, ipady=5)

        # Email
        Label(self.root, text="Email:", font=("Verdana", 12), bg="#2C3E50", fg="white").pack(pady=5)
        self.email_entry = Entry(self.root, font=("Verdana", 12), width=28, bg="#ECF0F1", fg="#2C3E50", bd=2, relief=FLAT)
        self.email_entry.pack(pady=5, ipady=5)

        # Password
        Label(self.root, text="Password:", font=("Verdana", 12), bg="#2C3E50", fg="white").pack(pady=5)
        self.signup_password_entry = Entry(self.root, font=("Verdana", 12), width=28, show="*", bg="#ECF0F1", fg="#2C3E50", bd=2, relief=FLAT)
        self.signup_password_entry.pack(pady=5, ipady=5)

        # Sign Up Button
        Button(self.root, text="Sign Up", font=("Verdana", 12, "bold"), bg="#27AE60", fg="white",
               bd=0, relief=FLAT, cursor="hand2", command=self.signup).pack(pady=20, ipadx=40, ipady=7)

        # Back to Login Section
        Label(self.root, text="Already have an account?", font=("Verdana", 10), bg="#2C3E50", fg="white").pack(pady=5)
        Button(self.root, text="Login", font=("Verdana", 10, "bold"), fg="white", bg="#2980B9",
               bd=0, relief=FLAT, cursor="hand2", command=self.loginGUI).pack(pady=5, ipadx=20, ipady=3)

    def homeGUI(self):
        """Creates the Home Page GUI."""
        self.clear_window()

        Label(self.root, text="NLP APP", font=("Verdana", 22, "bold"), bg="#2C3E50", fg="white").pack(pady=15)

        # Button Frame for Vertical Alignment
        button_frame = Frame(self.root, bg="#2C3E50")
        button_frame.pack(pady=20)

        # Common button style
        button_style = {
            "font": ("Verdana", 12, "bold"),
            "bg": "#27AE60",
            "fg": "white",
            "bd": 0,
            "relief": FLAT,
            "cursor": "hand2",
            "width": 20,
            "height": 2
        }

        # Buttons - Using pack() for vertical alignment
        Button(button_frame, text="Sentiment Analytics", **button_style, command=self.sentimentGUI).pack(pady=10)
        Button(button_frame, text="NER", **button_style, command=self.nerGUI).pack(pady=10)
        Button(button_frame, text="Emotion Detection", **button_style, command=self.edGUI).pack(pady=10)

        # Logout Button at the Bottom
        Button(self.root, text="Logout", font=("Verdana", 12, "bold"), bg="#E74C3C", fg="white",
               bd=0, relief=FLAT, cursor="hand2", width=20, height=2, command=self.logout).pack(pady=30)

    def login(self):
        """Handles login process using the database."""
        email = self.username_entry.get()
        password = self.password_entry.get()

        if not email or not password:
            messagebox.showerror("Login Failed", "All fields are required!")
            return

        response = self.dbo.search(email, password)

        if response == 1:
            messagebox.showinfo("Login Successful", "Welcome to the NLP App!")
            self.homeGUI()
        else:
            messagebox.showerror("Login Failed", "Invalid email or password")

    def signup(self):
        """Handles user signup."""
        name = self.name_entry.get()
        email = self.email_entry.get()
        password = self.signup_password_entry.get()


        if name and email and password:
            response = self.dbo.add_data(name, email, password)
            if response == 1:
                messagebox.showinfo("Sign Up Successful", "Account created successfully!")
                self.loginGUI()
            else:
                messagebox.showerror("Sign Up Failed", "Email already registered!")
        else:
            messagebox.showerror("Sign Up Failed", "All fields are required!")

    def sentimentGUI(self):
        """Creates the Sentiment Analysis GUI with Table Output, Target Input, Go Back, and Logout."""
        self.clear_window()

        frame = Frame(self.root, bg="#2C3E50", padx=20, pady=20)
        frame.pack(expand=True)

        Label(frame, text="NLP APP", font=("Verdana", 24, "bold"), bg="#2C3E50", fg="white").pack(pady=(10, 5))
        Label(frame, text="Sentiment Analysis", font=("Verdana", 18, "bold"), bg="#2C3E50", fg="white").pack(
            pady=(5, 20))

        Label(frame, text="Enter your text:", font=("Verdana", 12), bg="#2C3E50", fg="white").pack(pady=(5, 5))

        self.sentiment_input = Text(frame, font=("Verdana", 12), width=50, height=5, bg="#ECF0F1", fg="#2C3E50", bd=2,
                                    relief=FLAT)
        self.sentiment_input.pack(pady=(5, 15))

        Label(frame, text="Target (optional, for specific entity sentiment):", font=("Verdana", 12), bg="#2C3E50",
              fg="white").pack(pady=(5, 5))

        self.target_input = Entry(frame, font=("Verdana", 12), width=45, bg="#ECF0F1", fg="#2C3E50", bd=2, relief=FLAT)
        self.target_input.pack(pady=(5, 15), ipady=6)

        Button(frame, text="Analyze Sentiment", font=("Verdana", 12, "bold"), bg="#27AE60", fg="white",
               bd=0, relief=FLAT, cursor="hand2", width=25, height=2, command=self.do_sentiment_analysis).pack(
            pady=(5, 15))

        # Table for results
        columns = ("Sentiment", "Score")
        self.sentiment_table = ttk.Treeview(frame, columns=columns, show="headings", height=3)
        self.sentiment_table.heading("Sentiment", text="Sentiment")
        self.sentiment_table.heading("Score", text="Score")
        self.sentiment_table.pack(pady=(10, 20))

        # Navigation Buttons
        button_frame = Frame(frame, bg="#2C3E50")
        button_frame.pack(pady=(10, 5))

        Button(button_frame, text="⬅ Go Back", font=("Verdana", 12, "bold"), bg="#E74C3C", fg="white",
               bd=0, relief=FLAT, cursor="hand2", width=15, height=2, command=self.homeGUI).grid(row=0, column=0,
                                                                                                 padx=10)

        Button(button_frame, text="🚪 Logout", font=("Verdana", 12, "bold"), bg="#C0392B", fg="white",
               bd=0, relief=FLAT, cursor="hand2", width=15, height=2, command=self.logoutGUI).grid(row=0, column=1,
                                                                                                   padx=10)

    def do_sentiment_analysis(self):
        """Performs sentiment analysis and updates the table."""

        # Get input values
        text = self.sentiment_input.get("1.0", END).strip()
        target = self.target_input.get().strip() or None

        # Check if input text is empty
        if not text:
            return  # Don't proceed if there's no input text

        try:
            # Call the API
            result = self.myapi.sentiment_analysis(text, target)

            # Ensure API response is valid
            if "sentiment" not in result:
                return  # No valid sentiment data

            # Clear previous table data
            for item in self.sentiment_table.get_children():
                self.sentiment_table.delete(item)

            # Insert new data into the table
            for sentiment, score in result["sentiment"].items():
                self.sentiment_table.insert("", "end", values=(sentiment, score))

        except Exception as e:
            print("Error in sentiment analysis:", str(e))  # Debugging output

    def nerGUI(self):
        messagebox.showinfo("NER", "Named Entity Recognition Module Coming Soon!")

    def edGUI(self):
        messagebox.showinfo("Emotion Detection", "Emotion Detection Module Coming Soon!")

    def logout(self):
        """Handles user logout and redirects to the login screen."""
        response = messagebox.askyesno("Logout", "Are you sure you want to logout?")
        if response:
            self.loginGUI()

# Run App
if __name__ == "__main__":
    NLPApp()
