import tkinter as tk
from tkinter import ttk, messagebox

import student_utils as su


class CampusConnectApp:

    def __init__(self, root):

        self.root = root

        self.root.title("Campus Connect - Student Management System")
        self.root.geometry("750x520")
        self.root.resizable(False, False)

        # Load existing student data
        self.students = su.load_data()

        self.build_header()
        self.build_form()
        self.build_buttons()
        self.build_table()

        # Display existing records
        self.refresh_table()

    # =====================================================
    # HEADER
    # =====================================================

    def build_header(self):

        header = tk.Label(
            self.root,
            text="Campus Connect",
            font=("Segoe UI", 20, "bold"),
            fg="#2c3e50"
        )

        header.pack(pady=(15, 0))

        subheader = tk.Label(
            self.root,
            text="Student Management Application",
            font=("Segoe UI", 11),
            fg="#7f8c8d"
        )

        subheader.pack(pady=(0, 10))

    # =====================================================
    # INPUT FORM
    # =====================================================

    def build_form(self):

        form_frame = tk.Frame(self.root)
        form_frame.pack(pady=5)

        labels = ["Roll No", "Name", "Marks"]

        self.entries = {}

        for i, label_text in enumerate(labels):

            tk.Label(
                form_frame,
                text=label_text,
                font=("Segoe UI", 10)
            ).grid(
                row=0,
                column=i * 2,
                padx=5,
                pady=5
            )

            entry = tk.Entry(
                form_frame,
                width=15,
                font=("Segoe UI", 10)
            )

            entry.grid(
                row=0,
                column=i * 2 + 1,
                padx=5,
                pady=5
            )

            self.entries[label_text] = entry

    # =====================================================
    # BUTTONS
    # =====================================================

    def build_buttons(self):

        btn_frame = tk.Frame(self.root)
        btn_frame.pack(pady=10)

        buttons = [
            ("Add", self.add_student, "#27ae60"),
            ("Update", self.update_student, "#2980b9"),
            ("Delete", self.delete_student, "#c0392b"),
            ("Search", self.search_student, "#8e44ad"),
            ("Clear", self.clear_form, "#7f8c8d"),
            ("Class Average", self.show_average, "#d35400"),
        ]

        for text, command, color in buttons:

            tk.Button(
                btn_frame,
                text=text,
                command=command,
                bg=color,
                fg="white",
                font=("Segoe UI", 9, "bold"),
                width=13,
                relief="flat",
                cursor="hand2"
            ).pack(
                side="left",
                padx=4
            )

    # =====================================================
    # TABLE
    # =====================================================

    def build_table(self):

        columns = (
            "roll_no",
            "name",
            "marks",
            "grade"
        )

        self.tree = ttk.Treeview(
            self.root,
            columns=columns,
            show="headings",
            height=14
        )

        headings = {
            "roll_no": "Roll No",
            "name": "Name",
            "marks": "Marks",
            "grade": "Grade"
        }

        for col in columns:

            self.tree.heading(
                col,
                text=headings[col]
            )

            self.tree.column(
                col,
                anchor="center",
                width=150
            )

        self.tree.pack(
            pady=10,
            padx=15,
            fill="x"
        )

        self.tree.bind(
            "<<TreeviewSelect>>",
            self.on_row_select
        )

    # =====================================================
    # REFRESH TABLE
    # =====================================================

    def refresh_table(self):

        # Delete old rows
        for row in self.tree.get_children():
            self.tree.delete(row)

        # Add current student data
        for roll_no, info in self.students.items():

            self.tree.insert(
                "",
                "end",
                values=(
                    roll_no,
                    info["name"],
                    info["marks"],
                    info["grade"]
                )
            )

    # =====================================================
    # GET FORM VALUES
    # =====================================================

    def get_form_values(self):

        roll_no = self.entries["Roll No"].get().strip()

        name = self.entries["Name"].get().strip()

        marks_text = self.entries["Marks"].get().strip()

        return roll_no, name, marks_text

    # =====================================================
    # ADD STUDENT
    # =====================================================

    def add_student(self):

        roll_no, name, marks_text = self.get_form_values()

        if not roll_no or not name or not marks_text:

            messagebox.showwarning(
                "Missing Information",
                "Please fill all fields."
            )

            return

        try:

            marks = float(marks_text)

        except ValueError:

            messagebox.showerror(
                "Invalid Marks",
                "Marks must be a number."
            )

            return

        # Marks validation
        if marks < 0 or marks > 100:

            messagebox.showerror(
                "Invalid Marks",
                "Marks must be between 0 and 100."
            )

            return

        # Duplicate Roll Number
        if roll_no in self.students:

            messagebox.showerror(
                "Duplicate Roll No",
                "This Roll No already exists."
            )

            return

        # Add student
        su.add_student(
            self.students,
            roll_no,
            name,
            marks
        )

        self.refresh_table()

        self.clear_form()

        messagebox.showinfo(
            "Success",
            f"Student '{name}' added successfully."
        )

    # =====================================================
    # UPDATE STUDENT
    # =====================================================

    def update_student(self):

        roll_no, _, marks_text = self.get_form_values()

        if not roll_no or not marks_text:

            messagebox.showwarning(
                "Missing Information",
                "Enter Roll No and Marks to update."
            )

            return

        try:

            marks = float(marks_text)

        except ValueError:

            messagebox.showerror(
                "Invalid Marks",
                "Marks must be a number."
            )

            return

        if marks < 0 or marks > 100:

            messagebox.showerror(
                "Invalid Marks",
                "Marks must be between 0 and 100."
            )

            return

        success = su.update_marks(
            self.students,
            roll_no,
            marks
        )

        if success:

            self.refresh_table()

            self.clear_form()

            messagebox.showinfo(
                "Updated",
                f"Marks updated for Roll No {roll_no}."
            )

        else:

            messagebox.showerror(
                "Not Found",
                f"No student found with Roll No {roll_no}."
            )

    # =====================================================
    # DELETE STUDENT
    # =====================================================

    def delete_student(self):

        roll_no, _, _ = self.get_form_values()

        if not roll_no:

            messagebox.showwarning(
                "Missing Information",
                "Enter Roll No to delete."
            )

            return

        # Confirmation
        confirm = messagebox.askyesno(
            "Confirm Delete",
            f"Are you sure you want to delete Roll No {roll_no}?"
        )

        if not confirm:
            return

        success = su.delete_student(
            self.students,
            roll_no
        )

        if success:

            self.refresh_table()

            self.clear_form()

            messagebox.showinfo(
                "Deleted",
                f"Student with Roll No {roll_no} removed."
            )

        else:

            messagebox.showerror(
                "Not Found",
                f"No student found with Roll No {roll_no}."
            )

    # =====================================================
    # SEARCH STUDENT
    # =====================================================

    def search_student(self):

        roll_no, _, _ = self.get_form_values()

        if not roll_no:

            messagebox.showwarning(
                "Missing Information",
                "Enter Roll No to search."
            )

            return

        if roll_no in self.students:

            info = self.students[roll_no]

            self.entries["Name"].delete(
                0,
                tk.END
            )

            self.entries["Name"].insert(
                0,
                info["name"]
            )

            self.entries["Marks"].delete(
                0,
                tk.END
            )

            self.entries["Marks"].insert(
                0,
                info["marks"]
            )

            messagebox.showinfo(
                "Student Found",
                f"Roll No: {roll_no}\n"
                f"Name: {info['name']}\n"
                f"Marks: {info['marks']}\n"
                f"Grade: {info['grade']}"
            )

        else:

            messagebox.showerror(
                "Not Found",
                f"No student found with Roll No {roll_no}."
            )

    # =====================================================
    # CLASS AVERAGE
    # =====================================================

    def show_average(self):

        if not self.students:

            messagebox.showinfo(
                "Class Average",
                "No student records available."
            )

            return

        avg = su.class_average(
            self.students
        )

        messagebox.showinfo(
            "Class Average",
            f"Class Average Marks: {avg:.2f}"
        )

    # =====================================================
    # TABLE ROW SELECTION
    # =====================================================

    def on_row_select(self, event):

        selected = self.tree.focus()

        if not selected:
            return

        values = self.tree.item(
            selected,
            "values"
        )

        self.clear_form()

        self.entries["Roll No"].insert(
            0,
            values[0]
        )

        self.entries["Name"].insert(
            0,
            values[1]
        )

        self.entries["Marks"].insert(
            0,
            values[2]
        )

    # =====================================================
    # CLEAR FORM
    # =====================================================

    def clear_form(self):

        for entry in self.entries.values():

            entry.delete(
                0,
                tk.END
            )


# =========================================================
# PROGRAM START
# =========================================================

if __name__ == "__main__":

    root = tk.Tk()

    app = CampusConnectApp(root)

    root.mainloop()
    
    
    
