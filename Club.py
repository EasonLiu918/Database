import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import mysql.connector
from datetime import datetime
from openpyxl import Workbook
from ttkthemes import ThemedTk

class RecreationClubApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Recreation Club Activity Registration System")
        self.master.geometry("1200x700")
        self.master.configure(bg="#f0f0f0")

        # Set styles
        self.style = ttk.Style()
        self.style.theme_use("clam")
        self.style.configure("TNotebook", background="#f0f0f0", borderwidth=0)
        self.style.configure("TNotebook.Tab", background="#e0e0e0", padding=[10, 5], font=('Helvetica', 10))
        self.style.map("TNotebook.Tab", background=[("selected", "#ffffff")])
        self.style.configure("Treeview", rowheight=25, font=('Helvetica', 9))
        self.style.configure("Treeview.Heading", font=('Helvetica', 10, 'bold'))
        self.style.configure("TButton", padding=10, font=('Helvetica', 10))

        # Database connection
        try:
            self.db = mysql.connector.connect(
                host="localhost",
                user="root",
                password="123456",
                database="club",
                port=3306
            )
            self.cursor = self.db.cursor()
        except mysql.connector.Error as err:
            messagebox.showerror("Database Connection Error", f"Unable to connect to database: {err}")
            self.master.destroy()
            return

        # Create main frame
        self.main_frame = ttk.Notebook(self.master)
        self.main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Create function pages
        self.create_member_page()
        self.create_activity_page()
        self.create_location_page()
        self.create_signup_page()
        self.create_feedback_page()
        self.create_report_page()

    def create_member_page(self):
        member_frame = ttk.Frame(self.main_frame, padding=20)
        self.main_frame.add(member_frame, text="Member Management")

        # Member list
        self.member_tree = ttk.Treeview(member_frame, columns=("ID", "Name", "Birthday", "Phone", "Gender", "Email", "Preferences", "Membership Type"), show="headings")
        for col in self.member_tree["columns"]:
            self.member_tree.heading(col, text=col)
            self.member_tree.column(col, width=100)
        self.member_tree.pack(fill=tk.BOTH, expand=True)

        # Scrollbar
        scrollbar = ttk.Scrollbar(member_frame, orient="vertical", command=self.member_tree.yview)
        scrollbar.pack(side="right", fill="y")
        self.member_tree.configure(yscrollcommand=scrollbar.set)

        # Button frame
        btn_frame = ttk.Frame(member_frame)
        btn_frame.pack(fill=tk.X, pady=(10, 0))

        # Add member button
        add_member_btn = ttk.Button(btn_frame, text="Add Member", command=self.add_member_window)
        add_member_btn.pack(side=tk.LEFT, padx=(0, 5))

        # Edit member button
        edit_member_btn = ttk.Button(btn_frame, text="Edit Member", command=self.edit_member_window)
        edit_member_btn.pack(side=tk.LEFT, padx=5)

        # Delete member button
        delete_member_btn = ttk.Button(btn_frame, text="Delete Member", command=self.delete_member)
        delete_member_btn.pack(side=tk.LEFT, padx=5)

        # Load member data
        self.load_members()

    def create_activity_page(self):
        activity_frame = ttk.Frame(self.main_frame, padding=20)
        self.main_frame.add(activity_frame, text="Activity Management")

        # Activity list
        self.activity_tree = ttk.Treeview(activity_frame, columns=("ID", "Name", "Description", "Status", "Quota", "Location"), show="headings")
        for col in self.activity_tree["columns"]:
            self.activity_tree.heading(col, text=col)
            self.activity_tree.column(col, width=100)
        self.activity_tree.pack(fill=tk.BOTH, expand=True)

        # Scrollbar
        scrollbar = ttk.Scrollbar(activity_frame, orient="vertical", command=self.activity_tree.yview)
        scrollbar.pack(side="right", fill="y")
        self.activity_tree.configure(yscrollcommand=scrollbar.set)

        # Button frame
        btn_frame = ttk.Frame(activity_frame)
        btn_frame.pack(fill=tk.X, pady=(10, 0))

        # Add activity button
        add_activity_btn = ttk.Button(btn_frame, text="Add Activity", command=self.add_activity_window)
        add_activity_btn.pack(side=tk.LEFT, padx=(0, 5))

        # Edit activity button
        edit_activity_btn = ttk.Button(btn_frame, text="Edit Activity", command=self.edit_activity_window)
        edit_activity_btn.pack(side=tk.LEFT, padx=5)

        # Delete activity button
        delete_activity_btn = ttk.Button(btn_frame, text="Delete Activity", command=self.delete_activity)
        delete_activity_btn.pack(side=tk.LEFT, padx=5)

        # Load activity data
        self.load_activities()

    def create_location_page(self):
        location_frame = ttk.Frame(self.main_frame, padding=20)
        self.main_frame.add(location_frame, text="Location Management")

        # Location list
        self.location_tree = ttk.Treeview(location_frame, columns=("ID", "Capacity", "Type", "Availability"), show="headings")
        for col in self.location_tree["columns"]:
            self.location_tree.heading(col, text=col)
            self.location_tree.column(col, width=100)
        self.location_tree.pack(fill=tk.BOTH, expand=True)

        # Scrollbar
        scrollbar = ttk.Scrollbar(location_frame, orient="vertical", command=self.location_tree.yview)
        scrollbar.pack(side="right", fill="y")
        self.location_tree.configure(yscrollcommand=scrollbar.set)

        # Button frame
        btn_frame = ttk.Frame(location_frame)
        btn_frame.pack(fill=tk.X, pady=(10, 0))

        # Add location button
        add_location_btn = ttk.Button(btn_frame, text="Add Location", command=self.add_location_window)
        add_location_btn.pack(side=tk.LEFT, padx=(0, 5))

        # Edit location button
        edit_location_btn = ttk.Button(btn_frame, text="Edit Location", command=self.edit_location_window)
        edit_location_btn.pack(side=tk.LEFT, padx=5)

        # Delete location button
        delete_location_btn = ttk.Button(btn_frame, text="Delete Location", command=self.delete_location)
        delete_location_btn.pack(side=tk.LEFT, padx=5)

        # Load location data
        self.load_locations()

    def create_signup_page(self):
        signup_frame = ttk.Frame(self.main_frame, padding=20)
        self.main_frame.add(signup_frame, text="Activity Registration")

        # Registration list
        self.signup_tree = ttk.Treeview(signup_frame, columns=("ID", "Member", "Activity", "Date", "Time"), show="headings")
        for col in self.signup_tree["columns"]:
            self.signup_tree.heading(col, text=col)
            self.signup_tree.column(col, width=100)
        self.signup_tree.pack(fill=tk.BOTH, expand=True)

        # Scrollbar
        scrollbar = ttk.Scrollbar(signup_frame, orient="vertical", command=self.signup_tree.yview)
        scrollbar.pack(side="right", fill="y")
        self.signup_tree.configure(yscrollcommand=scrollbar.set)

        # Registration operation frame
        signup_op_frame = ttk.Frame(signup_frame)
        signup_op_frame.pack(fill=tk.X, pady=(10, 0))

        # Member selection
        ttk.Label(signup_op_frame, text="Select Member:").pack(side=tk.LEFT, padx=(0, 5))
        self.member_var = tk.StringVar()
        self.member_combobox = ttk.Combobox(signup_op_frame, textvariable=self.member_var)
        self.member_combobox.pack(side=tk.LEFT, padx=(0, 10))

        # Activity selection
        ttk.Label(signup_op_frame, text="Select Activity:").pack(side=tk.LEFT, padx=(0, 5))
        self.activity_var = tk.StringVar()
        self.activity_combobox = ttk.Combobox(signup_op_frame, textvariable=self.activity_var)
        self.activity_combobox.pack(side=tk.LEFT, padx=(0, 10))

        # Register button
        signup_btn = ttk.Button(signup_op_frame, text="Register", command=self.signup_activity)
        signup_btn.pack(side=tk.LEFT, padx=(0, 5))

        # Cancel registration button
        cancel_signup_btn = ttk.Button(signup_op_frame, text="Cancel Registration", command=self.cancel_signup)
        cancel_signup_btn.pack(side=tk.LEFT)

        # Load member and activity data
        self.load_member_names()
        self.load_activity_names()
        self.load_signups()

    def create_feedback_page(self):
        feedback_frame = ttk.Frame(self.main_frame, padding=20)
        self.main_frame.add(feedback_frame, text="Feedback Management")

        # Feedback list
        self.feedback_tree = ttk.Treeview(feedback_frame, columns=("ID", "Activity", "Member", "Rating", "Comments", "Date"), show="headings")
        for col in self.feedback_tree["columns"]:
            self.feedback_tree.heading(col, text=col)
            self.feedback_tree.column(col, width=100)
        self.feedback_tree.pack(fill=tk.BOTH, expand=True)

        # Scrollbar
        scrollbar = ttk.Scrollbar(feedback_frame, orient="vertical", command=self.feedback_tree.yview)
        scrollbar.pack(side="right", fill="y")
        self.feedback_tree.configure(yscrollcommand=scrollbar.set)

        # Button frame
        btn_frame = ttk.Frame(feedback_frame)
        btn_frame.pack(fill=tk.X, pady=(10, 0))

        # Add feedback button
        add_feedback_btn = ttk.Button(btn_frame, text="Add Feedback", command=self.add_feedback_window)
        add_feedback_btn.pack(side=tk.LEFT, padx=(0, 5))

        # Delete feedback button
        delete_feedback_btn = ttk.Button(btn_frame, text="Delete Feedback", command=self.delete_feedback)
        delete_feedback_btn.pack(side=tk.LEFT)

        # Load feedback data
        self.load_feedbacks()

    def create_report_page(self):
        report_frame = ttk.Frame(self.main_frame, padding=20)
        self.main_frame.add(report_frame, text="Report Generation")

        # Report type selection
        ttk.Label(report_frame, text="Select Report Type:").pack(anchor="w")
        self.report_var = tk.StringVar()
        report_combobox = ttk.Combobox(report_frame, textvariable=self.report_var, values=[
            "Member Statistics", "Activity Popularity", "Monthly Activity Report", "Recent 7 Days Registrations",
            "Member Activity Ranking", "Busiest Registration Day", "Most Popular Membership Type", "Location Activity Statistics"
        ])
        report_combobox.pack(fill=tk.X, pady=(0, 10))

        # Button frame
        btn_frame = ttk.Frame(report_frame)
        btn_frame.pack(fill=tk.X, pady=(0, 10))

        # Generate report button
        generate_btn = ttk.Button(btn_frame, text="Generate Report", command=self.generate_report)
        generate_btn.pack(side=tk.LEFT, padx=(0, 5))

        # Export Excel button
        export_btn = ttk.Button(btn_frame, text="Export to Excel", command=self.export_excel)
        export_btn.pack(side=tk.LEFT)

        # Report display area
        self.report_text = tk.Text(report_frame, height=20, width=80)
        self.report_text.pack(fill=tk.BOTH, expand=True)

    def load_members(self):
        try:
            self.cursor.execute("""
                SELECT m.members_id, m.members_name, m.members_date_of_birth, m.members_phone_number, 
                       m.members_gender, m.members_email, m.members_preferences, mt.type_name 
                FROM Members m 
                JOIN MembershipType mt ON m.membership_type_id = mt.membership_type_id
            """)
            members = self.cursor.fetchall()
            self.member_tree.delete(*self.member_tree.get_children())
            for member in members:
                self.member_tree.insert("", "end", values=member)
        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"Failed to load member data: {err}")

    def load_activities(self):
        try:
            self.cursor.execute("""
                SELECT a.activity_id, a.activity_name, a.description, a.activity_status, 
                       a.participation_quota, l.type 
                FROM Activity a 
                JOIN Location l ON a.location_id = l.location_id
            """)
            activities = self.cursor.fetchall()
            self.activity_tree.delete(*self.activity_tree.get_children())
            for activity in activities:
                self.activity_tree.insert("", "end", values=activity)
        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"Failed to load activity data: {err}")

    def load_locations(self):
        try:
            self.cursor.execute("SELECT location_id, capacity, type, availability FROM Location")
            locations = self.cursor.fetchall()
            self.location_tree.delete(*self.location_tree.get_children())
            for location in locations:
                self.location_tree.insert("", "end", values=location)
        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"Failed to load location data: {err}")

    def load_signups(self):
        try:
            self.cursor.execute("""
                SELECT s.signup_id, m.members_name, a.activity_name, s.signup_date, s.signup_time 
                FROM Signup s 
                JOIN Members m ON s.members_id = m.members_id 
                JOIN Activity a ON s.activity_id = a.activity_id
            """)
            signups = self.cursor.fetchall()
            self.signup_tree.delete(*self.signup_tree.get_children())
            for signup in signups:
                self.signup_tree.insert("", "end", values=signup)
        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"Failed to load signup data: {err}")

    def load_feedbacks(self):
        try:
            self.cursor.execute("""
                SELECT f.feedback_id, a.activity_name, m.members_name, f.rating, f.comments, f.feedback_date 
                FROM Feedback f 
                JOIN Activity a ON f.activity_id = a.activity_id 
                JOIN Members m ON f.members_id = m.members_id
            """)
            feedbacks = self.cursor.fetchall()
            self.feedback_tree.delete(*self.feedback_tree.get_children())
            for feedback in feedbacks:
                self.feedback_tree.insert("", "end", values=feedback)
        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"Failed to load feedback data: {err}")

    def load_member_names(self):
        try:
            self.cursor.execute("SELECT members_id, members_name FROM Members")
            members = self.cursor.fetchall()
            self.member_combobox['values'] = [f"{m[0]} - {m[1]}" for m in members]
        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"Failed to load member names: {err}")

    def load_activity_names(self):
        try:
            self.cursor.execute("SELECT activity_id, activity_name FROM Activity WHERE activity_status = 'Active'")
            activities = self.cursor.fetchall()
            self.activity_combobox['values'] = [f"{a[0]} - {a[1]}" for a in activities]
        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"Failed to load activity names: {err}")

    def add_member_window(self):
        add_window = tk.Toplevel(self.master)
        add_window.title("Add Member")
        add_window.geometry("400x400")
        add_window.configure(bg="#f0f0f0")

        frame = ttk.Frame(add_window, padding=20)
        frame.pack(fill=tk.BOTH, expand=True)

        fields = [("Name", "name"), ("Date of Birth", "dob"), ("Phone", "phone"), 
                  ("Gender", "gender"), ("Email", "email"), ("Preferences", "preferences")]

        entries = {}
        for i, (label, key) in enumerate(fields):
            ttk.Label(frame, text=f"{label}:").grid(row=i, column=0, sticky="e", pady=5)
            if key == "gender":
                entries[key] = ttk.Combobox(frame, values=["Male", "Female", "Other"])
            else:
                entries[key] = ttk.Entry(frame)
            entries[key].grid(row=i, column=1, sticky="ew", pady=5)

        ttk.Label(frame, text="Membership Type:").grid(row=len(fields), column=0, sticky="e", pady=5)
        membership_var = tk.StringVar()
        self.cursor.execute("SELECT membership_type_id, type_name FROM MembershipType")
        membership_types = self.cursor.fetchall()
        membership_combobox = ttk.Combobox(frame, textvariable=membership_var, 
                                           values=[f"{mt[0]} - {mt[1]}" for mt in membership_types])
        membership_combobox.grid(row=len(fields), column=1, sticky="ew", pady=5)

        submit_btn = ttk.Button(frame, text="Submit", command=lambda: self.add_member(
            entries["name"].get(), entries["dob"].get(), entries["phone"].get(),
            entries["gender"].get(), entries["email"].get(), entries["preferences"].get(),
            membership_var.get().split(" - ")[0], add_window
        ))
        submit_btn.grid(row=len(fields)+1, column=0, columnspan=2, pady=20)

        frame.columnconfigure(1, weight=1)

    def add_member(self, name, dob, phone, gender, email, preferences, membership_type_id, window):
        try:
            self.cursor.execute("""
                INSERT INTO Members (members_name, members_date_of_birth, members_phone_number, 
                members_gender, members_email, members_preferences, membership_type_id) 
                VALUES (%s, %s, %s, %s, %s, %s, %s)
            """, (name, dob, phone, gender, email, preferences, membership_type_id))
            self.db.commit()
            messagebox.showinfo("Success", "Member added successfully")
            window.destroy()
            self.load_members()
            self.load_member_names()
        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"Failed to add member: {err}")

    def edit_member_window(self):
        selected = self.member_tree.selection()
        if not selected:
            messagebox.showwarning("Warning", "Please select a member first")
            return
        member_id = self.member_tree.item(selected)['values'][0]
        
        edit_window = tk.Toplevel(self.master)
        edit_window.title("Edit Member")
        edit_window.geometry("400x400")
        edit_window.configure(bg="#f0f0f0")

        frame = ttk.Frame(edit_window, padding=20)
        frame.pack(fill=tk.BOTH, expand=True)

        self.cursor.execute("SELECT * FROM Members WHERE members_id = %s", (member_id,))
        member = self.cursor.fetchone()

        fields = [("Name", "name"), ("Date of Birth", "dob"), ("Phone", "phone"), 
                  ("Gender", "gender"), ("Email", "email"), ("Preferences", "preferences")]

        entries = {}
        for i, (label, key) in enumerate(fields):
            ttk.Label(frame, text=f"{label}:").grid(row=i, column=0, sticky="e", pady=5)
            if key == "gender":
                entries[key] = ttk.Combobox(frame, values=["Male", "Female", "Other"])
                entries[key].set(member[4])
            else:
                entries[key] = ttk.Entry(frame)
                entries[key].insert(0, member[i+1])
            entries[key].grid(row=i, column=1, sticky="ew", pady=5)

        ttk.Label(frame, text="Membership Type:").grid(row=len(fields), column=0, sticky="e", pady=5)
        membership_var = tk.StringVar()
        self.cursor.execute("SELECT membership_type_id, type_name FROM MembershipType")
        membership_types = self.cursor.fetchall()
        membership_combobox = ttk.Combobox(frame, textvariable=membership_var, 
                                           values=[f"{mt[0]} - {mt[1]}" for mt in membership_types])
        membership_combobox.set(f"{member[7]} - {dict(membership_types)[member[7]]}")
        membership_combobox.grid(row=len(fields), column=1, sticky="ew", pady=5)

        submit_btn = ttk.Button(frame, text="Update", command=lambda: self.update_member(
            member_id, entries["name"].get(), entries["dob"].get(), entries["phone"].get(),
            entries["gender"].get(), entries["email"].get(), entries["preferences"].get(),
            membership_var.get().split(" - ")[0], edit_window
        ))
        submit_btn.grid(row=len(fields)+1, column=0, columnspan=2, pady=20)

        frame.columnconfigure(1, weight=1)

    def update_member(self, member_id, name, dob, phone, gender, email, preferences, membership_type_id, window):
        try:
            self.cursor.execute("""
                UPDATE Members SET members_name=%s, members_date_of_birth=%s, members_phone_number=%s, 
                members_gender=%s, members_email=%s, members_preferences=%s, membership_type_id=%s 
                WHERE members_id=%s
            """, (name, dob, phone, gender, email, preferences, membership_type_id, member_id))
            self.db.commit()
            messagebox.showinfo("Success", "Member information updated successfully")
            window.destroy()
            self.load_members()
            self.load_member_names()
        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"Failed to update member information: {err}")

    def delete_member(self):
        selected = self.member_tree.selection()
        if not selected:
            messagebox.showwarning("Warning", "Please select a member first")
            return
        member_id = self.member_tree.item(selected)['values'][0]
        
        if messagebox.askyesno("Confirm", "Deleting a member will also delete all their registration records and feedback. Are you sure you want to delete?"):
            try:
                self.cursor.execute("DELETE FROM Signup WHERE members_id = %s", (member_id,))
                self.cursor.execute("DELETE FROM Feedback WHERE members_id = %s", (member_id,))
                self.cursor.execute("DELETE FROM Members WHERE members_id = %s", (member_id,))
                self.db.commit()
                messagebox.showinfo("Success", "Member deleted successfully")
                self.load_members()
                self.load_member_names()
                self.load_signups()
                self.load_feedbacks()
            except mysql.connector.Error as err:
                messagebox.showerror("Error", f"Failed to delete member: {err}")

    def add_activity_window(self):
        add_window = tk.Toplevel(self.master)
        add_window.title("Add Activity")
        add_window.geometry("400x400")
        add_window.configure(bg="#f0f0f0")

        frame = ttk.Frame(add_window, padding=20)
        frame.pack(fill=tk.BOTH, expand=True)

        ttk.Label(frame, text="Activity Name:").grid(row=0, column=0, sticky="e", pady=5)
        name_entry = ttk.Entry(frame)
        name_entry.grid(row=0, column=1, sticky="ew", pady=5)

        ttk.Label(frame, text="Description:").grid(row=1, column=0, sticky="e", pady=5)
        description_entry = ttk.Entry(frame)
        description_entry.grid(row=1, column=1, sticky="ew", pady=5)

        ttk.Label(frame, text="Status:").grid(row=2, column=0, sticky="e", pady=5)
        status_var = tk.StringVar()
        status_combobox = ttk.Combobox(frame, textvariable=status_var, values=["Active", "Inactive", "Cancelled"])
        status_combobox.grid(row=2, column=1, sticky="ew", pady=5)

        ttk.Label(frame, text="Participation Quota:").grid(row=3, column=0, sticky="e", pady=5)
        quota_entry = ttk.Entry(frame)
        quota_entry.grid(row=3, column=1, sticky="ew", pady=5)

        ttk.Label(frame, text="Location:").grid(row=4, column=0, sticky="e", pady=5)
        location_var = tk.StringVar()
        self.cursor.execute("SELECT location_id, type FROM Location")
        locations = self.cursor.fetchall()
        location_combobox = ttk.Combobox(frame, textvariable=location_var, values=[f"{l[0]} - {l[1]}" for l in locations])
        location_combobox.grid(row=4, column=1, sticky="ew", pady=5)

        submit_btn = ttk.Button(frame, text="Submit", command=lambda: self.add_activity(
            name_entry.get(), description_entry.get(), status_var.get(), 
            quota_entry.get(), location_var.get().split(" - ")[0], add_window
        ))
        submit_btn.grid(row=5, column=0, columnspan=2, pady=20)

        frame.columnconfigure(1, weight=1)

    def add_activity(self, name, description, status, quota, location_id, window):
        try:
            self.cursor.execute("""
                INSERT INTO Activity (activity_name, description, activity_status, participation_quota, location_id) 
                VALUES (%s, %s, %s, %s, %s)
            """, (name, description, status, quota, location_id))
            self.db.commit()
            messagebox.showinfo("Success", "Activity added successfully")
            window.destroy()
            self.load_activities()
            self.load_activity_names()
        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"Failed to add activity: {err}")

    def edit_activity_window(self):
        selected = self.activity_tree.selection()
        if not selected:
            messagebox.showwarning("Warning", "Please select an activity first")
            return
        activity_id = self.activity_tree.item(selected)['values'][0]
        
        edit_window = tk.Toplevel(self.master)
        edit_window.title("Edit Activity")
        edit_window.geometry("400x400")
        edit_window.configure(bg="#f0f0f0")

        frame = ttk.Frame(edit_window, padding=20)
        frame.pack(fill=tk.BOTH, expand=True)

        self.cursor.execute("SELECT * FROM Activity WHERE activity_id = %s", (activity_id,))
        activity = self.cursor.fetchone()

        ttk.Label(frame, text="Activity Name:").grid(row=0, column=0, sticky="e", pady=5)
        name_entry = ttk.Entry(frame)
        name_entry.insert(0, activity[1])
        name_entry.grid(row=0, column=1, sticky="ew", pady=5)

        ttk.Label(frame, text="Description:").grid(row=1, column=0, sticky="e", pady=5)
        description_entry = ttk.Entry(frame)
        description_entry.insert(0, activity[2])
        description_entry.grid(row=1, column=1, sticky="ew", pady=5)

        ttk.Label(frame, text="Status:").grid(row=2, column=0, sticky="e", pady=5)
        status_var = tk.StringVar(value=activity[3])
        status_combobox = ttk.Combobox(frame, textvariable=status_var, values=["Active", "Inactive", "Cancelled"])
        status_combobox.grid(row=2, column=1, sticky="ew", pady=5)

        ttk.Label(frame, text="Participation Quota:").grid(row=3, column=0, sticky="e", pady=5)
        quota_entry = ttk.Entry(frame)
        quota_entry.insert(0, activity[4])
        quota_entry.grid(row=3, column=1, sticky="ew", pady=5)

        ttk.Label(frame, text="Location:").grid(row=4, column=0, sticky="e", pady=5)
        location_var = tk.StringVar()
        self.cursor.execute("SELECT location_id, type FROM Location")
        locations = self.cursor.fetchall()
        location_combobox = ttk.Combobox(frame, textvariable=location_var, values=[f"{l[0]} - {l[1]}" for l in locations])
        location_combobox.set(f"{activity[5]} - {dict(locations)[activity[5]]}")
        location_combobox.grid(row=4, column=1, sticky="ew", pady=5)

        submit_btn = ttk.Button(frame, text="Update", command=lambda: self.update_activity(
            activity_id, name_entry.get(), description_entry.get(), status_var.get(), 
            quota_entry.get(), location_var.get().split(" - ")[0], edit_window
        ))
        submit_btn.grid(row=5, column=0, columnspan=2, pady=20)

        frame.columnconfigure(1, weight=1)

    def update_activity(self, activity_id, name, description, status, quota, location_id, window):
        try:
            self.cursor.execute("""
                UPDATE Activity SET activity_name=%s, description=%s, activity_status=%s, 
                participation_quota=%s, location_id=%s WHERE activity_id=%s
            """, (name, description, status, quota, location_id, activity_id))
            self.db.commit()
            messagebox.showinfo("Success", "Activity information updated successfully")
            window.destroy()
            self.load_activities()
            self.load_activity_names()
        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"Failed to update activity information: {err}")

    def delete_activity(self):
        selected = self.activity_tree.selection()
        if not selected:
            messagebox.showwarning("Warning", "Please select an activity first")
            return
        activity_id = self.activity_tree.item(selected)['values'][0]
        
        if messagebox.askyesno("Confirm", "Deleting an activity will also delete all related registration records and feedback. Are you sure you want to delete?"):
            try:
                self.cursor.execute("DELETE FROM Signup WHERE activity_id = %s", (activity_id,))
                self.cursor.execute("DELETE FROM Feedback WHERE activity_id = %s", (activity_id,))
                self.cursor.execute("DELETE FROM Activity WHERE activity_id = %s", (activity_id,))
                self.db.commit()
                messagebox.showinfo("Success", "Activity deleted successfully")
                self.load_activities()
                self.load_activity_names()
                self.load_signups()
                self.load_feedbacks()
            except mysql.connector.Error as err:
                messagebox.showerror("Error", f"Failed to delete activity: {err}")

    def add_location_window(self):
        add_window = tk.Toplevel(self.master)
        add_window.title("Add Location")
        add_window.geometry("300x200")
        add_window.configure(bg="#f0f0f0")

        frame = ttk.Frame(add_window, padding=20)
        frame.pack(fill=tk.BOTH, expand=True)

        ttk.Label(frame, text="Capacity:").grid(row=0, column=0, sticky="e", pady=5)
        capacity_entry = ttk.Entry(frame)
        capacity_entry.grid(row=0, column=1, sticky="ew", pady=5)

        ttk.Label(frame, text="Type:").grid(row=1, column=0, sticky="e", pady=5)
        type_entry = ttk.Entry(frame)
        type_entry.grid(row=1, column=1, sticky="ew", pady=5)

        ttk.Label(frame, text="Availability:").grid(row=2, column=0, sticky="e", pady=5)
        availability_var = tk.BooleanVar()
        availability_checkbutton = ttk.Checkbutton(frame, variable=availability_var)
        availability_checkbutton.grid(row=2, column=1, sticky="w", pady=5)

        submit_btn = ttk.Button(frame, text="Submit", command=lambda: self.add_location(
            capacity_entry.get(), type_entry.get(), availability_var.get(), add_window
        ))
        submit_btn.grid(row=3, column=0, columnspan=2, pady=20)

        frame.columnconfigure(1, weight=1)

    def add_location(self, capacity, type, availability, window):
        try:
            self.cursor.execute("""
                INSERT INTO Location (capacity, type, availability) 
                VALUES (%s, %s, %s)
            """, (capacity, type, availability))
            self.db.commit()
            messagebox.showinfo("Success", "Location added successfully")
            window.destroy()
            self.load_locations()
        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"Failed to add location: {err}")

    def edit_location_window(self):
        selected = self.location_tree.selection()
        if not selected:
            messagebox.showwarning("Warning", "Please select a location first")
            return
        location_id = self.location_tree.item(selected)['values'][0]
        
        edit_window = tk.Toplevel(self.master)
        edit_window.title("Edit Location")
        edit_window.geometry("300x200")
        edit_window.configure(bg="#f0f0f0")

        frame = ttk.Frame(edit_window, padding=20)
        frame.pack(fill=tk.BOTH, expand=True)

        self.cursor.execute("SELECT * FROM Location WHERE location_id = %s", (location_id,))
        location = self.cursor.fetchone()

        ttk.Label(frame, text="Capacity:").grid(row=0, column=0, sticky="e", pady=5)
        capacity_entry = ttk.Entry(frame)
        capacity_entry.insert(0, location[1])
        capacity_entry.grid(row=0, column=1, sticky="ew", pady=5)

        ttk.Label(frame, text="Type:").grid(row=1, column=0, sticky="e", pady=5)
        type_entry = ttk.Entry(frame)
        type_entry.insert(0, location[2])
        type_entry.grid(row=1, column=1, sticky="ew", pady=5)

        ttk.Label(frame, text="Availability:").grid(row=2, column=0, sticky="e", pady=5)
        availability_var = tk.BooleanVar(value=location[3])
        availability_checkbutton = ttk.Checkbutton(frame, variable=availability_var)
        availability_checkbutton.grid(row=2, column=1, sticky="w", pady=5)

        submit_btn = ttk.Button(frame, text="Update", command=lambda: self.update_location(
            location_id, capacity_entry.get(), type_entry.get(), availability_var.get(), edit_window
        ))
        submit_btn.grid(row=3, column=0, columnspan=2, pady=20)

        frame.columnconfigure(1, weight=1)

    def update_location(self, location_id, capacity, type, availability, window):
        try:
            self.cursor.execute("""
                UPDATE Location SET capacity=%s, type=%s, availability=%s 
                WHERE location_id=%s
            """, (capacity, type, availability, location_id))
            self.db.commit()
            messagebox.showinfo("Success", "Location information updated successfully")
            window.destroy()
            self.load_locations()
        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"Failed to update location information: {err}")

    def delete_location(self):
        selected = self.location_tree.selection()
        if not selected:
            messagebox.showwarning("Warning", "Please select a location first")
            return
        location_id = self.location_tree.item(selected)['values'][0]
        
        if messagebox.askyesno("Confirm", "Deleting a location will also delete all related activities, registration records, and feedback. Are you sure you want to delete?"):
            try:
                self.cursor.execute("SELECT activity_id FROM Activity WHERE location_id = %s", (location_id,))
                activities = self.cursor.fetchall()
                for activity in activities:
                    self.cursor.execute("DELETE FROM Signup WHERE activity_id = %s", (activity[0],))
                    self.cursor.execute("DELETE FROM Feedback WHERE activity_id = %s", (activity[0],))
                self.cursor.execute("DELETE FROM Activity WHERE location_id = %s", (location_id,))
                self.cursor.execute("DELETE FROM Location WHERE location_id = %s", (location_id,))
                self.db.commit()
                messagebox.showinfo("Success", "Location deleted successfully")
                self.load_locations()
                self.load_activities()
                self.load_activity_names()
                self.load_signups()
                self.load_feedbacks()
            except mysql.connector.Error as err:
                messagebox.showerror("Error", f"Failed to delete location: {err}")

    def signup_activity(self):
        member_id = self.member_var.get().split(" - ")[0]
        activity_id = self.activity_var.get().split(" - ")[0]
        signup_date = datetime.now().date()
        signup_time = datetime.now().time()

        try:
            self.cursor.execute("SELECT participation_quota FROM Activity WHERE activity_id = %s", (activity_id,))
            quota = self.cursor.fetchone()[0]
            self.cursor.execute("SELECT COUNT(*) FROM Signup WHERE activity_id = %s", (activity_id,))
            current_signups = self.cursor.fetchone()[0]

            if current_signups >= quota:
                messagebox.showwarning("Warning", "The activity has reached its participation limit")
                return

            self.cursor.execute("""
                INSERT INTO Signup (members_id, activity_id, signup_date, signup_time) 
                VALUES (%s, %s, %s, %s)
            """, (member_id, activity_id, signup_date, signup_time))
            self.db.commit()
            messagebox.showinfo("Success", "Activity registration successful")
            self.load_signups()
        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"Failed to register for activity: {err}")

    def cancel_signup(self):
        selected = self.signup_tree.selection()
        if not selected:
            messagebox.showwarning("Warning", "Please select a registration record first")
            return
        signup_id = self.signup_tree.item(selected)['values'][0]
        
        if messagebox.askyesno("Confirm", "Are you sure you want to cancel this registration?"):
            try:
                self.cursor.execute("DELETE FROM Signup WHERE signup_id = %s", (signup_id,))
                self.db.commit()
                messagebox.showinfo("Success", "Registration cancelled successfully")
                self.load_signups()
            except mysql.connector.Error as err:
                messagebox.showerror("Error", f"Failed to cancel registration: {err}")

    def add_feedback_window(self):
        add_window = tk.Toplevel(self.master)
        add_window.title("Add Feedback")
        add_window.geometry("400x300")
        add_window.configure(bg="#f0f0f0")

        frame = ttk.Frame(add_window, padding=20)
        frame.pack(fill=tk.BOTH, expand=True)

        ttk.Label(frame, text="Activity:").grid(row=0, column=0, sticky="e", pady=5)
        activity_var = tk.StringVar()
        self.cursor.execute("SELECT activity_id, activity_name FROM Activity")
        activities = self.cursor.fetchall()
        activity_combobox = ttk.Combobox(frame, textvariable=activity_var, values=[f"{a[0]} - {a[1]}" for a in activities])
        activity_combobox.grid(row=0, column=1, sticky="ew", pady=5)

        ttk.Label(frame, text="Member:").grid(row=1, column=0, sticky="e", pady=5)
        member_var = tk.StringVar()
        self.cursor.execute("SELECT members_id, members_name FROM Members")
        members = self.cursor.fetchall()
        member_combobox = ttk.Combobox(frame, textvariable=member_var, values=[f"{m[0]} - {m[1]}" for m in members])
        member_combobox.grid(row=1, column=1, sticky="ew", pady=5)

        ttk.Label(frame, text="Rating:").grid(row=2, column=0, sticky="e", pady=5)
        rating_var = tk.StringVar()
        rating_combobox = ttk.Combobox(frame, textvariable=rating_var, values=[1, 2, 3, 4, 5])
        rating_combobox.grid(row=2, column=1, sticky="ew", pady=5)

        ttk.Label(frame, text="Comments:").grid(row=3, column=0, sticky="e", pady=5)
        comments_entry = ttk.Entry(frame)
        comments_entry.grid(row=3, column=1, sticky="ew", pady=5)

        submit_btn = ttk.Button(frame, text="Submit", command=lambda: self.add_feedback(
            activity_var.get().split(" - ")[0], member_var.get().split(" - ")[0], 
            rating_var.get(), comments_entry.get(), add_window
        ))
        submit_btn.grid(row=4, column=0, columnspan=2, pady=20)

        frame.columnconfigure(1, weight=1)

    def add_feedback(self, activity_id, member_id, rating, comments, window):
        try:
            feedback_date = datetime.now().date()
            self.cursor.execute("""
                INSERT INTO Feedback (activity_id, members_id, rating, comments, feedback_date) 
                VALUES (%s, %s, %s, %s, %s)
            """, (activity_id, member_id, rating, comments, feedback_date))
            self.db.commit()
            messagebox.showinfo("Success", "Feedback added successfully")
            window.destroy()
            self.load_feedbacks()
        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"Failed to add feedback: {err}")

    def delete_feedback(self):
        selected = self.feedback_tree.selection()
        if not selected:
            messagebox.showwarning("Warning", "Please select a feedback first")
            return
        feedback_id = self.feedback_tree.item(selected)['values'][0]
        
        if messagebox.askyesno("Confirm", "Are you sure you want to delete this feedback?"):
            try:
                self.cursor.execute("DELETE FROM Feedback WHERE feedback_id = %s", (feedback_id,))
                self.db.commit()
                messagebox.showinfo("Success", "Feedback deleted successfully")
                self.load_feedbacks()
            except mysql.connector.Error as err:
                messagebox.showerror("Error", f"Failed to delete feedback: {err}")

    def generate_report(self):
        report_type = self.report_var.get()
        self.report_text.delete(1.0, tk.END)

        if report_type == "Member Statistics":
            try:
                self.cursor.execute("SELECT members_gender, COUNT(*) AS member_count FROM Members GROUP BY members_gender")
                results = self.cursor.fetchall()
                self.report_text.insert(tk.END, "Member Gender Statistics:\n")
                for result in results:
                    self.report_text.insert(tk.END, f"{result[0]}: {result[1]}\n")
            except mysql.connector.Error as err:
                messagebox.showerror("Error", f"Failed to generate member statistics report: {err}")

        elif report_type == "Activity Popularity":
            try:
                self.cursor.execute("""
                    SELECT a.activity_name, COUNT(DISTINCT s.members_id) AS signup_count, AVG(f.rating) AS avg_rating
                    FROM Activity a
                    LEFT JOIN Signup s ON a.activity_id = s.activity_id
                    LEFT JOIN Feedback f ON a.activity_id = f.activity_id
                    GROUP BY a.activity_id
                    ORDER BY signup_count DESC
                """)
                results = self.cursor.fetchall()
                self.report_text.insert(tk.END, "Activity Popularity:\n")
                for result in results:
                    self.report_text.insert(tk.END, f"{result[0]}: Signups - {result[1]}, Average Rating - {result[2]:.2f}\n")
            except mysql.connector.Error as err:
                messagebox.showerror("Error", f"Failed to generate activity popularity report: {err}")

        elif report_type == "Monthly Activity Report":
            try:
                self.cursor.execute("""
                    SELECT 
                        DATE_FORMAT(s.signup_date, '%Y-%m') AS month,
                        COUNT(DISTINCT a.activity_id) AS total_activities,
                        COUNT(DISTINCT s.members_id) AS total_participants
                    FROM Activity a
                    JOIN Signup s ON a.activity_id = s.activity_id
                    GROUP BY month
                    ORDER BY month DESC
                    LIMIT 12
                """)
                results = self.cursor.fetchall()
                self.report_text.insert(tk.END, "Monthly Activity Report:\n")
                for result in results:
                    self.report_text.insert(tk.END, f"Month: {result[0]}, Total Activities: {result[1]}, Total Participants: {result[2]}\n")
            except mysql.connector.Error as err:
                messagebox.showerror("Error", f"Failed to generate monthly activity report: {err}")

        elif report_type == "Recent 7 Days Registrations":
            try:
                self.cursor.execute("""
                    SELECT DISTINCT m.members_name
                    FROM Members m
                    JOIN Signup s ON m.members_id = s.members_id
                    WHERE s.signup_date >= CURDATE() - INTERVAL 7 DAY
                """)
                results = self.cursor.fetchall()
                self.report_text.insert(tk.END, "Members who registered in the last 7 days:\n")
                for result in results:
                    self.report_text.insert(tk.END, f"{result[0]}\n")
            except mysql.connector.Error as err:
                messagebox.showerror("Error", f"Failed to generate recent registrations report: {err}")

        elif report_type == "Member Activity Ranking":
            try:
                self.cursor.execute("""
                    SELECT 
                        m.members_name,
                        COUNT(s.activity_id) AS activity_count,
                        RANK() OVER (ORDER BY COUNT(s.activity_id) DESC) AS member_rank
                    FROM 
                        Members m
                    LEFT JOIN 
                        Signup s ON m.members_id = s.members_id
                    GROUP BY 
                        m.members_id, m.members_name
                    ORDER BY 
                        activity_count DESC
                """)
                results = self.cursor.fetchall()
                self.report_text.insert(tk.END, "Member Activity Participation Ranking:\n")
                for result in results:
                    self.report_text.insert(tk.END, f"Rank {result[2]}: {result[0]} - Activities Participated: {result[1]}\n")
            except mysql.connector.Error as err:
                messagebox.showerror("Error", f"Failed to generate member activity ranking report: {err}")

        elif report_type == "Busiest Registration Day":
            try:
                self.cursor.execute("""
                    SELECT DAYNAME(signup_date) AS day_of_week, 
                           COUNT(*) AS signup_count
                    FROM Signup
                    GROUP BY day_of_week
                    ORDER BY signup_count DESC
                    LIMIT 1
                """)
                result = self.cursor.fetchone()
                self.report_text.insert(tk.END, f"The busiest registration day is {result[0]} with {result[1]} registrations\n")
            except mysql.connector.Error as err:
                messagebox.showerror("Error", f"Failed to generate busiest registration day report: {err}")

        elif report_type == "Most Popular Membership Type":
            try:
                self.cursor.execute("""
                    SELECT mt.type_name, COUNT(DISTINCT s.members_id) as member_count, 
                           GROUP_CONCAT(DISTINCT a.activity_name) as popular_activities
                    FROM MembershipType mt
                    JOIN Members m ON mt.membership_type_id = m.membership_type_id
                    JOIN Signup s ON m.members_id = s.members_id
                    JOIN Activity a ON s.activity_id = a.activity_id
                    GROUP BY mt.membership_type_id
                    ORDER BY member_count DESC
                    LIMIT 1
                """)
                result = self.cursor.fetchone()
                self.report_text.insert(tk.END, f"The most popular membership type is {result[0]} with {result[1]} members\n")
                self.report_text.insert(tk.END, f"They participated in activities including: {result[2]}\n")
            except mysql.connector.Error as err:
                messagebox.showerror("Error", f"Failed to generate most popular membership type report: {err}")

        elif report_type == "Location Activity Statistics":
            try:
                self.cursor.execute("""
                    SELECT l.type AS location_type, a.activity_name, COUNT(s.signup_id) AS signup_count
                    FROM Location l
                    JOIN Activity a ON l.location_id = a.location_id
                    LEFT JOIN Signup s ON a.activity_id = s.activity_id
                    GROUP BY l.location_id, a.activity_id
                    HAVING signup_count = (
                        SELECT COUNT(s2.signup_id)
                        FROM Activity a2
                        LEFT JOIN Signup s2 ON a2.activity_id = s2.activity_id
                        WHERE a2.location_id = l.location_id
                        GROUP BY a2.activity_id
                        ORDER BY COUNT(s2.signup_id) DESC
                        LIMIT 1
                    )
                    ORDER BY l.type, signup_count DESC
                """)
                results = self.cursor.fetchall()
                self.report_text.insert(tk.END, "Most Popular Activities by Location:\n")
                for result in results:
                    self.report_text.insert(tk.END, f"Location Type: {result[0]}, Most Popular Activity: {result[1]}, Signups: {result[2]}\n")
            except mysql.connector.Error as err:
                messagebox.showerror("Error", f"Failed to generate location activity statistics report: {err}")

    def export_excel(self):
        report_type = self.report_var.get()
        if not report_type:
            messagebox.showwarning("Warning", "Please select a report type first")
            return

        filename = filedialog.asksaveasfilename(defaultextension=".xlsx", filetypes=[("Excel files", "*.xlsx")])
        if not filename:
            return

        wb = Workbook()
        ws = wb.active
        ws.title = report_type

        if report_type == "Member Statistics":
            self.export_member_statistics(ws)
        elif report_type == "Activity Popularity":
            self.export_activity_popularity(ws)
        elif report_type == "Monthly Activity Report":
            self.export_monthly_activity_report(ws)
        elif report_type == "Recent 7 Days Registrations":
            self.export_recent_signups(ws)
        elif report_type == "Member Activity Ranking":
            self.export_member_activity_ranking(ws)
        elif report_type == "Busiest Registration Day":
            self.export_busiest_signup_day(ws)
        elif report_type == "Most Popular Membership Type":
            self.export_popular_membership_type(ws)
        elif report_type == "Location Activity Statistics":
            self.export_location_activity_statistics(ws)

        wb.save(filename)
        messagebox.showinfo("Success", f"Report has been successfully exported to {filename}")

    def export_member_statistics(self, ws):
        ws.append(["Gender", "Member Count"])
        self.cursor.execute("SELECT members_gender, COUNT(*) AS member_count FROM Members GROUP BY members_gender")
        for row in self.cursor.fetchall():
            ws.append(row)

    def export_activity_popularity(self, ws):
        ws.append(["Activity Name", "Signup Count", "Average Rating"])
        self.cursor.execute("""
            SELECT a.activity_name, COUNT(DISTINCT s.members_id) AS signup_count, AVG(f.rating) AS avg_rating
            FROM Activity a
            LEFT JOIN Signup s ON a.activity_id = s.activity_id
            LEFT JOIN Feedback f ON a.activity_id = f.activity_id
            GROUP BY a.activity_id
            ORDER BY signup_count DESC
        """)
        for row in self.cursor.fetchall():
            ws.append(row)

    def export_monthly_activity_report(self, ws):
        ws.append(["Month", "Total Activities", "Total Participants"])
        self.cursor.execute("""
            SELECT 
                DATE_FORMAT(s.signup_date, '%Y-%m') AS month,
                COUNT(DISTINCT a.activity_id) AS total_activities,
                COUNT(DISTINCT s.members_id) AS total_participants
            FROM 
                Activity a
            JOIN 
                Signup s ON a.activity_id = s.activity_id
            GROUP BY 
                month
            ORDER BY 
                month DESC
            LIMIT 12
        """)
        for row in self.cursor.fetchall():
            ws.append(row)

    def export_recent_signups(self, ws):
        ws.append(["Member Name"])
        self.cursor.execute("""
            SELECT DISTINCT m.members_name
            FROM Members m
            JOIN Signup s ON m.members_id = s.members_id
            WHERE s.signup_date >= CURDATE() - INTERVAL 7 DAY
        """)
        for row in self.cursor.fetchall():
            ws.append(row)

    def export_member_activity_ranking(self, ws):
        ws.append(["Rank", "Member Name", "Activities Participated"])
        self.cursor.execute("""
            SELECT 
                m.members_name,
                COUNT(s.activity_id) AS activity_count
            FROM 
                Members m
            LEFT JOIN 
                Signup s ON m.members_id = s.members_id
            GROUP BY 
                m.members_id, m.members_name
            ORDER BY 
                activity_count DESC
        """)
        for rank, row in enumerate(self.cursor.fetchall(), 1):
            ws.append([rank] + list(row))

    def export_busiest_signup_day(self, ws):
        ws.append(["Day of Week", "Signup Count"])
        self.cursor.execute("""
            SELECT DAYNAME(signup_date) AS day_of_week, 
                   COUNT(*) AS signup_count
            FROM Signup
            GROUP BY day_of_week
            ORDER BY signup_count DESC
            LIMIT 1
        """)
        for row in self.cursor.fetchall():
            ws.append(row)

    def export_popular_membership_type(self, ws):
        ws.append(["Membership Type", "Member Count", "Popular Activities"])
        self.cursor.execute("""
            SELECT mt.type_name, COUNT(DISTINCT s.members_id) as member_count, 
                   GROUP_CONCAT(DISTINCT a.activity_name) as popular_activities
            FROM MembershipType mt
            JOIN Members m ON mt.membership_type_id = m.membership_type_id
            JOIN Signup s ON m.members_id = s.members_id
            JOIN Activity a ON s.activity_id = a.activity_id
            GROUP BY mt.membership_type_id
            ORDER BY member_count DESC
            LIMIT 1
        """)
        for row in self.cursor.fetchall():
            ws.append(row)

    def export_location_activity_statistics(self, ws):
        ws.append(["Location Type", "Most Popular Activity", "Signup Count"])
        self.cursor.execute("""
            WITH RankedActivities AS (
                SELECT 
                    l.location_id,
                    l.type AS location_type,
                    a.activity_name,
                    COUNT(s.signup_id) AS signup_count,
                    ROW_NUMBER() OVER (PARTITION BY l.location_id ORDER BY COUNT(s.signup_id) DESC) as rn
                FROM 
                    Location l
                JOIN 
                    Activity a ON l.location_id = a.location_id
                LEFT JOIN 
                    Signup s ON a.activity_id = s.activity_id
                GROUP BY 
                    l.location_id, l.type, a.activity_name
            )
            SELECT 
                location_type,
                activity_name,
                signup_count
            FROM 
                RankedActivities
            WHERE 
                rn = 1
            ORDER BY 
                signup_count DESC
        """)
        for row in self.cursor.fetchall():
            ws.append(row)

    def __del__(self):
        if hasattr(self, 'db') and self.db.is_connected():
            self.cursor.close()
            self.db.close()

def main():
    root = ThemedTk(theme="arc")
    app = RecreationClubApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()