import tkinter as tk
from tkinter import Button, StringVar, Widget, ttk
from tkinter.constants import END

win = tk.Tk()
win.geometry("1350x700+0+0")
win.title("Student Information System")

#Background Color
win.config(bg="lightgray")

#Adding some style
style = ttk.Style()

#Pick a theme 
style.theme_use("default")

style.configure("Treeview",
  background="white",
  foreground="black",
  rowheight=25,
  fieldbackground="white"
)

#Change selected color
style.map(
  "Treeview",
  background=[("selected", "darkred")]
)

#Top Menu 

title_label = tk.Label(
  win, 
  text="Student Information System",
  font=("Arial", 20, "bold"),
  padx=15,
  pady=15, 
  border=0, 
  relief=tk.GROOVE, 
  bg="teal",
  foreground="white"
)
title_label.pack(side=tk.TOP, fill=tk.X)

#Left Menu

detail_frame = tk.LabelFrame(
  win, text="Student Data", 
  font=("Arial", 14), 
  bg="lightgray", 
  foreground="black",
  relief=tk.GROOVE
)
detail_frame.place(x=40, y=90, width=420, height=570)


#Data Frame

data_frame = tk.Frame(
  win,  
  bg="teal",
  relief=tk.GROOVE
)
data_frame.place(x=490, y=98, width=830, height=565)



#Label with Entry

id_lab = tk.Label(
  detail_frame, 
  text="ID:", 
  font=("Arial", 16), 
  bg="lightgray", 
  foreground="black"
)
id_lab.place(x=20, y=15)

#entry
id_ent = tk.Entry(
  detail_frame, 
  bd=1,
  font=("arial", 16), 
  bg="white", 
  foreground="black",
)
id_ent.place(x=110, y=17, width=250, height=30)

#2
name_lab = tk.Label(
  detail_frame, 
  text="Name:", 
  font=("Arial", 16), 
  bg="lightgray", 
  foreground="black"
)
name_lab.place(x=20, y=65)

#entry
name_ent = tk.Entry(
  detail_frame, 
  bd=1,
  font=("arial", 16), 
  bg="white", 
  foreground="black",
)
name_ent.place(x=110, y=65, width=250, height=30)

#3
year_lab = tk.Label(
  detail_frame, 
  text="Year Level:", 
  font=("Arial", 16), 
  bg="lightgray", 
  foreground="black"
)
year_lab.place(x=20, y=161)

#entry
year_ent = tk.Entry(
  detail_frame, 
  bd=1,
  font=("arial", 16), 
  bg="white", 
  foreground="black",
)
year_ent.place(x=110, y=161, width=250, height=30)

#4
gen_lab = tk.Label(
  detail_frame, 
  text="Gender:", 
  font=("Arial", 16), 
  bg="lightgray", 
  foreground="black"
)
gen_lab.place(x=20, y=113)

#entry
gen_ent = ttk.Combobox(
  detail_frame, 
  font=("arial", 16),
)
gen_ent["values"] = ("Male", "Female", "others")
gen_ent.place(x=110, y=113, width=250, height=30)


#5
course_lab = tk.Label(
  detail_frame, 
  text="Course:", 
  font=("Arial", 16), 
  bg="lightgray", 
  foreground="black"
)
course_lab.place(x=20, y=209)

#entry
course_ent = tk.Entry(
  detail_frame, 
  bd=1,
  font=("arial", 16), 
  bg="white", 
  foreground="black",
)
course_ent.place(x=110, y=209, width=250, height=30)


#Database frame 

main_frame = tk.Frame(
  data_frame,
  bg="teal",
  bd=2,
  relief=tk.GROOVE
)
main_frame.pack(fill=tk.BOTH, expand=True)

y_scroll = tk.Scrollbar(main_frame, orient=tk.VERTICAL)
x_scroll = tk.Scrollbar(main_frame, orient=tk.HORIZONTAL)

#Treeview database

student_table = ttk.Treeview(main_frame, columns=(
  "ID", "Name", "Year Level", "Gender", "Course"
), yscrollcommand=y_scroll.set, xscrollcommand=x_scroll.set)

y_scroll.config(command=student_table.yview)
x_scroll.config(command=student_table.xview)

y_scroll.pack(side=tk.RIGHT, fill=tk.Y)
x_scroll.pack(side=tk.BOTTOM, fill=tk.X)

student_table.heading("ID", text="ID")
student_table.heading("Name", text="Name")
student_table.heading("Year Level", text="Year Level")
student_table.heading("Gender", text="Gender")
student_table.heading("Course", text="Course")


student_table["show"] = "headings"

student_table.column("ID", width=100)
student_table.column("Name", width=100)
student_table.column("Year Level", width=100)
student_table.column("Gender", width=100)
student_table.column("Course", width=100)



student_table.pack(fill=tk.BOTH, expand=True)

#Default data 

data=[
  ["2019-8953", "Bagul, Fatima L.", "3", "Female", "BS Statistics"],
  ["2019-0655", "Bendit, Rutchegen C.", "3", "Female", "BS Statistics"],
  ["2019-1453", "Oledan, Christine Jane B.", "3", "Female", "BS Statistics"],
  ["2019-1352", "Vidal, Vincent A.", "3", "Male", "BS Statistics"],
  ["2019-0001", "Mira-ato, Saimah M.", "3", "Female", "BS Accountancy"]
]

#Create stripped row tags
student_table.tag_configure("oddrow", background="white")
student_table.tag_configure("evenrow", background="#00AEAE")

global count
count=0
for record in data:
  if count % 2 == 0:
    student_table.insert(parent="", index="end", iid=count, text="", values=(record[0], record[1],record[2],record[3],record[4]), tags=("evenrow"))
  else:
    student_table.insert(parent="", index="end", iid=count, text="", values=(record[0], record[1],record[2],record[3],record[4]), tags=("oddrow"))

  count += 1


#Functions

#Add Function
def add_record():
  student_table.tag_configure("oddrow", background="white")
  student_table.tag_configure("evenrow", background="#00AEAE")

  global count
  if count % 2 == 0:
    student_table.insert(parent="", index="end", iid=count, text="", values=(
    id_ent.get(),
    name_ent.get(),
    year_ent.get(),
    gen_ent.get(),
    course_ent.get()  
),
    tags=("evenrow")
)
  else:
    student_table.insert(parent="", index="end", iid=count, text="", values=(
    id_ent.get(),
    name_ent.get(),
    year_ent.get(),
    gen_ent.get(),
    course_ent.get()     
),
    tags=("oddrow")
)
  count += 1

#Delete All Function
def delete_all():
  for record in student_table.get_children():
    student_table.delete(record)

#Delete One Function
def delete_one():
  x = student_table.selection()[0]
  student_table.delete(x)

#Select Record
def select_record():
  
  id_ent.delete(0, END)
  name_ent.delete(0, END)
  year_ent.delete(0, END)
  gen_ent.delete(0, END)
  course_ent.delete(0, END)
 

  selected = student_table.focus()
  values = student_table.item(selected, "values")

  id_ent.insert(0, values[0])
  name_ent.insert(0, values[1])
  year_ent.insert(0, values[2])
  gen_ent.insert(0, values[3])
  course_ent.insert(0, values[4])
 

#Update Button
def update_record():
  selected = student_table.focus()
  student_table.item(selected, text="", values=(id_ent.get(),name_ent.get(),year_ent.get(),gen_ent.get(),course_ent.get(), ))

  id_ent.delete(0, END)
  name_ent.delete(0, END)
  year_ent.delete(0, END)
  gen_ent.delete(0, END)
  course_ent.delete(0, END)


#Clear boxes
  id_ent.delete(0, END)
  name_ent.delete(0, END)
  year_ent.delete(0, END)
  gen_ent.delete(0, END)
  course_ent.delete(0, END)


#Buttons

btn_frame = tk.Frame(
  detail_frame,
  bg="lightgray",
  bd=0,
  relief=tk.GROOVE
)
btn_frame.place(x=40, y=400, width=310, height=130)



#Add Button
add_btn = tk.Button(
  btn_frame,
  bg="teal",
  foreground="white",
  text="Add",
  bd=2,
  font=("Arial", 13), width=15,
  command=add_record
)
add_btn.grid(row=0, column=0, padx=2, pady=2)


#Update Button
update_btn = tk.Button(
  btn_frame,
  bg="teal",
  foreground="white",
  text="Update",
  bd=2,
  font=("Arial", 13), width=15,
  command=select_record
)
update_btn.grid(row=0, column=1, padx=2, pady=2)


#Save Button
save_btn = tk.Button(
  btn_frame,
  bg="teal",
  foreground="white",
  text="Clear",
  bd=2,
  font=("Arial", 13), width=15,
  command=delete_all
)
save_btn.grid(row=2, column=0, padx=2, pady=2)

#Delete Button
delete_btn = tk.Button(
  btn_frame,
  bg="teal",
  foreground="white",
  text="Delete",
  bd=2,
  font=("Arial", 13), width=15,
  command=delete_one
)
delete_btn.grid(row=2, column=1, padx=2, pady=2)










win.mainloop()
