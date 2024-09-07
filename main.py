import tkinter as tk

def calculate_grade(score):
    if score >= 80:
        return 4
    elif score >= 70:
        return 3
    elif score >= 60:
        return 2
    elif score >= 50:
        return 1
    else:
        return 0

def update_grade(subject_key):
    try:
        score = float(subjects[subject_key].get())
        grade = calculate_grade(score)
        labels[subject_key].config(text=f"Grade: {grade}")
    except ValueError:
        labels[subject_key].config(text="Invalid Score")

def update_gpa():
    total_credits = 0
    total_score = 0
    
    for subject_key in subjects:
        try:
            score = float(subjects[subject_key].get())
            grade = calculate_grade(score)
            total_credits += 1
            total_score += grade
        except ValueError:
            continue
    
    if total_credits > 0:
        gpa = total_score / total_credits
        label_gpa.config(text=f"GPA: {gpa:.2f}")
    else:
        label_gpa.config(text="Invalid Input")

# สร้างหน้าต่างหลัก
root = tk.Tk()
root.title("Grade Calculator")
root.geometry("400x400")
root.config(bg="#E70867")

# เก็บข้อมูล labels และ entries 
labels = {}
subjects = {}

# สร้าง label, entry และเกรดสำหรับวิชาต่าง ๆ
subject_names = [("Thai", "thai"), ("Math", "math"), ("English", "english"), 
                ("Science", "science"), ("Social", "social"),("Conputer","computer")]

for i, (subject_name, subject_key) in enumerate(subject_names):
    tk.Label(root, text=f"{subject_name}:", font=("Arial", 14), bg="#f7f7f7").grid(row=i, column=0, padx=20, pady=10, sticky='w')
    
    var = tk.StringVar()
    var.trace_add("write", lambda name, index, mode, key=subject_key: update_grade(key))
    
    entry = tk.Entry(root, font=("Arial", 14), width=5, relief="solid", borderwidth=1, textvariable=var)
    entry.grid(row=i, column=1, padx=10, pady=10)
    
    label_grade = tk.Label(root, text="Grade: ", font=("Arial", 14), bg="#f7f7f7")
    label_grade.grid(row=i, column=2, padx=10, pady=10)
    
    labels[subject_key] = label_grade
    subjects[subject_key] = var

# button GPA
button_calculate = tk.Button(root, text="Calculate GPA", font=("Arial", 14), command=update_gpa, bg="#4CAF50", fg="white", relief="raised", borderwidth=2)
button_calculate.grid(row=6, column=0, columnspan=3, pady=20)

# label GPA
label_gpa = tk.Label(root, text="GPA: ", font=("Arial", 16), bg="#f7f7f7")
label_gpa.grid(row=7, column=0, columnspan=3, pady=10)

# start Tkinter loop
root.mainloop()
