from tkinter import *
import tkinter.messagebox
import time
import sqlite3

root=Tk()
root.geometry("900x500")
root.title("Attendance System")

#create/connect the database
conn = sqlite3.connect('student_db.db')

# create cursor
c = conn.cursor()

# create table
'''
c.execute("""CREATE TABLE student_data (
        usn text,
        name text,
        course text,
        semester integer
)""")


c.execute("""CREATE TABLE attendance (
        date text,
        usn text,
        status text
)""")
'''

student_login_frame=None
student_password_entry=None
student_username_entry=None

student_sem_entry=None
student_course_entry=None
student_name_entry=None
student_usn_entry=None


def authorize(event):
    return

def student_exit():
    main_window()

def daily_record():
    global daily_record_frame
    daily_record_frame=Frame(student_login_frame,width=900,height=500,bg='#EBF2F8')
    daily_record_frame.place(x=0,y=0)
    daily_record_frame.tkraise()

    header_label = Label(student_login_frame, text="DATE\tSTATUS", font=('Berlin Sans FB', 30), bg='#EBF2F8')
    header_label.place(x=0, y=0)

    record_label = Label(student_login_frame, text=daily, font=('Berlin Sans FB', 16), bg='#EBF2F8')
    record_label.place(x=0, y=70)

    back_button = Button(student_login_frame, image=img20, bd=0, bg='#EBF2F8', command=student_login)
    back_button.place(x=820, y=420)

def student_attendence():
    conn = sqlite3.connect('student_db.db')

    # create cursor
    c = conn.cursor()

    
    # insert into table
    #c.execute("SELECT *,oid FROM attendance")
    c.execute("SELECT  date,status FROM attendance WHERE usn = (?)",(student_password_entry.get(),))

    daily_list = c.fetchall()
    print(daily_list)
    
    global daily
    daily =''

    for data in range(len(daily_list)):
        for i in range(2):
            daily += str(daily_list[data][i]) + "\t\t"
        daily+="\n" 
    
    print(daily)

    daily_record()
    
    # commit changes
    conn.commit()

    #close connection
    conn.close()

def student_login():
    global student_login_frame
    student_login_frame = Frame(student_admin_frame, width=900, height=500, bg='#EBF2F8')
    student_login_frame.place(x=0, y=0)
    student_login_frame.tkraise()

    student_icon = Label(student_login_frame, image=img15, bd=0, bg='#EBF2F8')
    student_icon.place(x=370, y=10)

    username_label = Label(student_login_frame, text='Student_name', font=('Berlin Sans FB', 16), bg='#EBF2F8')
    username_label.place(x=405, y=200)
    global student_username_entry
    student_username_entry = Entry(student_login_frame, bg='white', relief='sunken', highlightcolor='#D2E0F1',highlightthickness=1, highlightbackground='#D8D6D7', font=('Tw Cen MT', 14))
    student_username_entry.place(x=350, y=240)
    password_label = Label(student_login_frame, text='Password', font=('Berlin Sans FB', 16), bg='#EBF2F8')
    password_label.place(x=405, y=280)
    global student_password_entry
    student_password_entry = Entry(student_login_frame, bg='white', show='*', relief='sunken', highlightcolor='#D2E0F1',highlightthickness=1, highlightbackground='#D8D6D7', font=('Tw Cen MT', 14))
    student_password_entry.place(x=350, y=320)
    student_password_entry.bind('<Return>', authorize)
    login_button = Button(student_login_frame, image=img24, bd=0, bg='#EBF2F8',command=student_attendence)
    login_button.bind('<Button-1>',authorize)
    login_button.place(x=357, y=380)
    cancel_button = Button(student_login_frame, image=img14, bd=0, bg='#EBF2F8', command=student_exit)
    cancel_button.place(x=357, y=430)

admin_username_entry=None
admin_password_entry=None
admin_login_frame=None


def add_student():
    #create/connect the database
    conn = sqlite3.connect('student_db.db')

    # create cursor
    c = conn.cursor()


    # insert into table
    c.execute("INSERT INTO student_data VALUES (:usn, :name, :course, :sem)",
                {
                    'usn': student_usn_entry.get(),
                    'name': student_name_entry.get(),
                    'course': student_course_entry.get(),
                    'sem': student_sem_entry.get()
                })

    # clear text boxes
    student_usn_entry.delete(0, END)
    student_name_entry.delete(0, END)
    student_course_entry.delete(0, END)
    student_sem_entry.delete(0, END)


    # commit changes
    conn.commit()

    #close connection
    conn.close()

student=None
def show_student():
    #create/connect the database
    conn = sqlite3.connect('student_db.db')

    # create cursor
    c = conn.cursor()

    c.execute("SELECT *,oid FROM student_data")

    student_list = c.fetchall()
    print(student_list)
    
    global student
    student =''

    for data in range(len(student_list)):
        for i in range(4):
            student += str(student_list[data][i]) + "\t\t"
        student+="\n" 
    
    print(student)
    
    student_record()

    # commit changes
    conn.commit()

    #close connection
    conn.close()

student_usn_entry = None
def delete_student():
    #create/connect the database
    conn = sqlite3.connect('student_db.db')

    # create cursor
    c = conn.cursor()
    global student_usn_entry
    #delete student record
    #c.execute("DELETE FROM attendance")
    c.execute("DELETE FROM student_data WHERE usn = (?)",(student_usn_entry.get(),))

    
    # commit changes
    conn.commit()

    #close connection
    conn.close()

def student_record():
    global student_record_frame
    student_record_frame=Frame(student_detail_frame,width=900,height=500,bg='#EBF2F8')
    student_record_frame.place(x=0,y=0)
    student_record_frame.tkraise()

    header_label = Label(student_record_frame, text="USN\tNAME\tCLASS\tSEMESTER", font=('Berlin Sans FB', 30), bg='#EBF2F8')
    header_label.place(x=0, y=0)

    record_label = Label(student_record_frame, text=student, font=('Berlin Sans FB', 16), bg='#EBF2F8')
    record_label.place(x=0, y=70)

    back_button = Button(student_record_frame, image=img20, bd=0, bg='#EBF2F8', command=student_detail)
    back_button.place(x=820, y=420)

def student_detail():
    global student_detail_frame
    student_detail_frame=Frame(admin_login_frame,width=900,height=500,bg='#EBF2F8')
    student_detail_frame.place(x=0,y=0)
    student_detail_frame.tkraise()

    usn_label = Label(student_detail_frame, text='USN:', font=('Berlin Sans FB', 16), bg='#EBF2F8')
    usn_label.place(x=300, y=100)
    global student_usn_entry
    student_usn_entry = Entry(student_detail_frame, bg='white', relief='sunken', highlightcolor='#D2E0F1',highlightthickness=1, highlightbackground='#D8D6D7', font=('Tw Cen MT', 14))
    student_usn_entry.place(x=400, y=100)

    name_label = Label(student_detail_frame, text='NAME:', font=('Berlin Sans FB', 16), bg='#EBF2F8')
    name_label.place(x=300, y=150)
    global student_name_entry
    student_name_entry = Entry(student_detail_frame, bg='white', relief='sunken', highlightcolor='#D2E0F1',highlightthickness=1, highlightbackground='#D8D6D7', font=('Tw Cen MT', 14))
    student_name_entry.place(x=400, y=150)

    course_label = Label(student_detail_frame, text='CLASS:', font=('Berlin Sans FB', 16), bg='#EBF2F8')
    course_label.place(x=300, y=200)
    global student_course_entry
    student_course_entry = Entry(student_detail_frame, bg='white', relief='sunken', highlightcolor='#D2E0F1',highlightthickness=1, highlightbackground='#D8D6D7', font=('Tw Cen MT', 14))
    student_course_entry.place(x=400, y=200)

    sem_label = Label(student_detail_frame, text='SEMESTER:', font=('Berlin Sans FB', 16), bg='#EBF2F8')
    sem_label.place(x=300, y=250)
    global student_sem_entry
    student_sem_entry = Entry(student_detail_frame, bg='white', relief='sunken', highlightcolor='#D2E0F1',highlightthickness=1, highlightbackground='#D8D6D7', font=('Tw Cen MT', 14))
    student_sem_entry.place(x=400, y=250)

    add_button=Button(student_detail_frame,image=img25,bd=0,bg='#EBF2F8',command=add_student)
    add_button.place(x=70,y=350)

    show_button=Button(student_detail_frame,image=img18,bd=0,bg='#EBF2F8',command=show_student)
    show_button.place(x=320,y=350)

    delete_button=Button(student_detail_frame,image=img26,bd=0,bg='#EBF2F8',command=delete_student)
    delete_button.place(x=570,y=350)

    back_button = Button(student_detail_frame, image=img20, bd=0, bg='#EBF2F8', command=admin_portal)
    back_button.place(x=820, y=420)

def add_attendance():
    
    #create/connect the database
    conn = sqlite3.connect('student_db.db')

    # create cursor
    c = conn.cursor()


    # insert into table
    c.execute("INSERT INTO attendance VALUES (:date, :usn, :status)",
                {
                    'date': student_date_entry.get(),
                    'usn': student_usn_entry.get(),
                    'status': student_status_entry.get(),
                    
                })

    # clear text boxes
    student_usn_entry.delete(0, END)
    student_status_entry.delete(0, END)
    


    # commit changes
    conn.commit()

    #close connection
    conn.close()

def attendance_record():
    global attendance_record_frame
    attendance_record_frame=Frame(open_attendance_frame,width=900,height=500,bg='#EBF2F8')
    attendance_record_frame.place(x=0,y=0)
    attendance_record_frame.tkraise()

    header_label = Label(attendance_record_frame, text="USN\tSTATUS", font=('Berlin Sans FB', 30), bg='#EBF2F8')
    header_label.place(x=0, y=0)

    record_label = Label(attendance_record_frame, text=attendance, font=('Berlin Sans FB', 16), bg='#EBF2F8')
    record_label.place(x=0, y=70)

    back_button = Button(attendance_record_frame, image=img20, bd=0, bg='#EBF2F8', command=open_attendance)
    back_button.place(x=820, y=420)

def show_attendance():
    
    #create/connect the database
    conn = sqlite3.connect('student_db.db')

    # create cursor
    c = conn.cursor()

    
    # insert into table
    #c.execute("SELECT *,oid FROM attendance")
    c.execute("SELECT  usn,status FROM attendance WHERE date = (?)",(student_date_entry.get(),))

    attendance_list = c.fetchall()
    print(attendance_list)
    
    global attendance
    attendance =''

    for data in range(len(attendance_list)):
        for i in range(2):
            attendance += str(attendance_list[data][i]) + "\t\t"
        attendance+="\n" 
    
    print(attendance)

    attendance_record()
    
    # commit changes
    conn.commit()

    #close connection
    conn.close()
    
def open_attendance():
    global open_attendance_frame
    open_attendance_frame=Frame(admin_login_frame,width=900,height=500,bg='#EBF2F8')
    open_attendance_frame.place(x=0,y=0)
    open_attendance_frame.tkraise()

    date_label = Label(open_attendance_frame, text='DATE(DD/MM/YYYY):', font=('Berlin Sans FB', 16), bg='#EBF2F8')
    date_label.place(x=200, y=50)
    global student_date_entry
    student_date_entry = Entry(open_attendance_frame, bg='white', relief='sunken', highlightcolor='#D2E0F1',highlightthickness=1, highlightbackground='#D8D6D7', font=('Tw Cen MT', 14))
    student_date_entry.place(x=400, y=50)

    update_button=Button(open_attendance_frame,image=img28,bd=0,bg='#EBF2F8',command=show_attendance)
    update_button.place(x=300,y=100)

    back_button = Button(open_attendance_frame, image=img20, bd=0, bg='#EBF2F8', command=admin_portal)
    back_button.place(x=820, y=420)

def attendance_detail():
    global attendance_detail_frame
    attendance_detail_frame=Frame(admin_login_frame,width=900,height=500,bg='#EBF2F8')
    attendance_detail_frame.place(x=0,y=0)
    attendance_detail_frame.tkraise()

    date_label = Label(attendance_detail_frame, text='DATE(DD/MM/YYYY):', font=('Berlin Sans FB', 16), bg='#EBF2F8')
    date_label.place(x=200, y=50)
    global student_date_entry
    student_date_entry = Entry(attendance_detail_frame, bg='white', relief='sunken', highlightcolor='#D2E0F1',highlightthickness=1, highlightbackground='#D8D6D7', font=('Tw Cen MT', 14))
    student_date_entry.place(x=400, y=50)

    usn_label = Label(attendance_detail_frame, text='USN:', font=('Berlin Sans FB', 16), bg='#EBF2F8')
    usn_label.place(x=300, y=150)
    global student_usn_entry
    student_usn_entry = Entry(attendance_detail_frame, bg='white', relief='sunken', highlightcolor='#D2E0F1',highlightthickness=1, highlightbackground='#D8D6D7', font=('Tw Cen MT', 14))
    student_usn_entry.place(x=400, y=150)

    status_label = Label(attendance_detail_frame, text='STATUS:', font=('Berlin Sans FB', 16), bg='#EBF2F8')
    status_label.place(x=300, y=250)
    global student_status_entry
    student_status_entry = Entry(attendance_detail_frame, bg='white', relief='sunken', highlightcolor='#D2E0F1',highlightthickness=1, highlightbackground='#D8D6D7', font=('Tw Cen MT', 14))
    student_status_entry.place(x=400, y=250)

    update_button=Button(attendance_detail_frame,image=img27,bd=0,bg='#EBF2F8',command=add_attendance)
    update_button.place(x=350,y=350)

    back_button = Button(attendance_detail_frame, image=img20, bd=0, bg='#EBF2F8', command=admin_portal)
    back_button.place(x=820, y=420)

    

def admin_portal():
    global admin_dashboard_frame
    admin_dashboard_frame=Frame(admin_login_frame,width=900,height=500,bg='#EBF2F8')
    admin_dashboard_frame.place(x=0,y=0)
    admin_dashboard_frame.tkraise()
    '''
    class_button = Button(admin_dashboard_frame,image=img17, bd=0,bg="#EBF2F8")
    class_button.place(x=150, y=100)
    class_label=Label(admin_dashboard_frame,text='New_Class',font=('Berlin Sans FB',16),bg='#EBF2F8')
    class_label.place(x=175,y=250)
    '''
    student_button = Button(admin_dashboard_frame,image=img15, bd=0,bg="#EBF2F8",command=student_detail)
    student_button.place(x=600, y=100)
    student_label=Label(admin_dashboard_frame,text='New_Student',font=('Berlin Sans FB',16),bg='#EBF2F8')
    student_label.place(x=625,y=250)
    
    attendence_button = Button(admin_dashboard_frame,image=img6, bd=0,bg="#EBF2F8",command=attendance_detail)
    attendence_button.place(x=150, y=100)
    attendence_label=Label(admin_dashboard_frame,text='New_Attendence',font=('Berlin Sans FB',16),bg='#EBF2F8')
    attendence_label.place(x=175,y=180)
    
    record_button = Button(admin_dashboard_frame,image=img7, bd=0,bg="#EBF2F8",command=open_attendance)
    record_button.place(x=300, y=350)
    record_label=Label(admin_dashboard_frame,text='View_Record',font=('Berlin Sans FB',16),bg='#EBF2F8')
    record_label.place(x=425,y=415)
    
    back_button = Button(admin_dashboard_frame, image=img20, bd=0, bg='#EBF2F8', command=admin_login)
    back_button.place(x=820, y=420)

    
def admin_authorize(event):
    if admin_username_entry.get()=='ADMIN' and admin_password_entry.get()=='PASSWORD':
        admin_portal()

def admin_exit():
    main_window()


def admin_login():
    global admin_login_frame
    admin_login_frame=Frame(student_admin_frame,width=900,height=500,bg='#EBF2F8')
    admin_login_frame.place(x=0,y=0)
    admin_login_frame.tkraise()
    admin_icon=Label(admin_login_frame,image=img13,bd=0,bg='#EBF2F8')
    admin_icon.place(x=370,y=10)
    username_label=Label(admin_login_frame,text='Username',font=('Berlin Sans FB',16),bg='#EBF2F8')
    username_label.place(x=405,y=200)
    global admin_username_entry
    admin_username_entry=Entry(admin_login_frame,bg='white',relief='sunken',highlightcolor='#D2E0F1',highlightthickness=1,highlightbackground='#D8D6D7',font=('Tw Cen MT',14))
    admin_username_entry.place(x=350,y=240)
    password_label = Label(admin_login_frame, text='Password', font=('Berlin Sans FB', 16), bg='#EBF2F8')
    password_label.place(x=405, y=280)
    global admin_password_entry
    admin_password_entry = Entry(admin_login_frame, bg='white',show='*', relief='sunken', highlightcolor='#D2E0F1',highlightthickness=1,highlightbackground='#D8D6D7', font=('Tw Cen MT', 14))
    admin_password_entry.place(x=350, y=320)
    admin_password_entry.bind('<Return>',admin_authorize)
    login_button=Button(admin_login_frame,image=img24,bd=0,bg='#EBF2F8')
    login_button.bind('<Button-1>',admin_authorize)
    login_button.place(x=357,y=380)
    cancel_button=Button(admin_login_frame,image=img14,bd=0,bg='#EBF2F8',command=admin_exit)
    cancel_button.place(x=357,y=430)
 

student_admin_frame=None

def main_window():
    global student_admin_frame
    student_admin_frame = Frame(root, width=900, height=500,bg="#EBF2F8")
    student_admin_frame.place(x=0, y=0)
    main_logo_image=Label(student_admin_frame,image=img23,bg='#EBF2F8')
    main_logo_image.place(x=200,y=50)
    black_button_student = Button(student_admin_frame,image=img11, bd=0, command=student_login,bg="#EBF2F8")
    black_button_student.place(x=100, y=300)
    black_button_teacher = Button(student_admin_frame,image=img12, bd=0, command=admin_login,bg="#EBF2F8")
    black_button_teacher.place(x=500, y=300)


img1= PhotoImage(file='black-button-student.png')
img2= PhotoImage(file='black-button-teacher.png')
img3=PhotoImage(file='ned-student-portal-logo.png')
img4=PhotoImage(file='student_portal-logo.png')
img5=PhotoImage(file='dashboard-logo.png')
img6=PhotoImage(file='attendance-logo.png')
img7=PhotoImage(file='view-records-logo.png')
img8=PhotoImage(file='logout-logo.png')
img9=PhotoImage(file='divider-logo.png')
img10=PhotoImage(file='heading-seperator.png')
img11=PhotoImage(file='student-login.png')
img12=PhotoImage(file='admin-login.png')
img20=PhotoImage(file='back-button.png')
img21=PhotoImage(file='show-record-button.png')
img22=PhotoImage(file='main-logo.png')
img23=PhotoImage(file='aaa.png')
img24=PhotoImage(file='login-button.png')
img13=PhotoImage(file='admin-icon1.png')
img14=PhotoImage(file='cancel-button.png')
img15=PhotoImage(file='student-icon.png')
img16=PhotoImage(file='dropdown.png')
img17=PhotoImage(file='take-attendance.png')
img18=PhotoImage(file='black-button.png')
img19=PhotoImage(file='admin-portal-logo.png')
img25=PhotoImage(file='add.png')
photo=PhotoImage(file='test.png')
img26=PhotoImage(file='delete.png')
img27=PhotoImage(file='update.png')
img28=PhotoImage(file='ok.png')


# commit changes
conn.commit()

#close connection
conn.close()

main_window()

root.mainloop()