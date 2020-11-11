from tkinter import *
# import mysql.connector
import sqlite3
from tkinter import messagebox
import os
import datetime

os.system('espeak "{}"'.format("welcome to capstone manager project"))
os.system('espeak "{}"'.format("version 2 point 1"))
os.system('espeak "{}"'.format("created by PRINCE PATEL"))
# os.system('espeak "{}"'.format("registration number 1 1 7 0 9 3 4 7"))
class SeaofBTCapp(Tk):
    def __init__(self, *args, **kwargs):

        Tk.__init__(self, *args, **kwargs)

        container = Frame(self)
        container.pack(side='top', fill='both', expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPage, StudentRegistration, SupervisorRegistration, StudentLogin, SupervisorLogin, logout, About):

            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky='nsew')

        self.show_frame(StartPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


class StartPage(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent, bg='orange')
        # label = Label(self, text='Start Page')
        # label.pack(pady=10, padx=10)

        # ========================================================================================================DATABASE CREATION
        cnx = sqlite3.connect('projectdatabase.db')
        cursor = cnx.cursor()
        cursor.execute("PRAGMA foreign_keys = ON")

        cursor.execute("CREATE TABLE IF NOT EXISTS supervisor(uid VARCHAR(40) PRIMARY KEY, fnamesup VARCHAR(40) NOT NULL, lnamesup VARCHAR(40) NOT NULL, specialization VARCHAR(40) NOT NULL, mobilesup VARCHAR(10) NOT NULL, emailsup VARCHAR(40) NOT NULL)")
        cnx.commit()
        print('Supervisor table created')

        cursor.execute("CREATE TABLE IF NOT EXISTS student(regno VARCHAR(40) PRIMARY KEY, fnames VARCHAR(40) NOT NULL, lnames VARCHAR(40) NOT NULL, specialization VARCHAR(40) NOT NULL,mobiles VARCHAR(10) NOT NULL, emails VARCHAR(40) NOT NULL, superid VARCHAR(40) DEFAULT 'NOT ASSINGED' REFERENCES supervisor(uid) ON DELETE SET DEFAULT)")
        cnx.commit()
        print('Student table created')


        # cursor.execute("ALTER TABLE student ADD superid VARCHAR(40) DEFAULT 'Not Selected'")
        # cnx.commit()
        # cursor.execute("ALTER TABLE student ADD FOREIGN KEY (superid) REFERENCES supervisor(uid)")
        # cnx.commit()

        cursor.close()
        cnx.close()
        print('all connections are closed')

        # ========================================================================================================DTABASE CREATION END

        frame1 = Frame(self, bg='green')
        frame1.pack(fill=X)

        framedate = Frame(frame1, bg='green')
        framedate.pack(fill=X, side=BOTTOM)

        Label(frame1, text='Capstone Manager', fg='white', bg='green', font=('bold', 22)).pack(padx=10, pady=10)

        frame2 = Frame(self, bg='orange')
        frame2.pack(fill=BOTH, expand=1)

        # =========================================================================STUDENT BUTTON ZONE
        Label(frame2, text='Student Zone', width=32, anchor=CENTER, bg='orange').grid(row=1, column=1, pady=10)
        # Label(frame2, text='\n', bg='orange').grid(row=2, column=1, columnspan=2)


        # button = Button(frame2, text='Visit Page 1', command=lambda: controller.show_frame(PageOne))
        # button.grid()

        button1 = Button(frame2, text='Registration', relief=GROOVE, width=15, bg='orange', command=lambda: controller.show_frame(StudentRegistration))
        button1.grid(row=3, column=1, pady=10)

        button2 = Button(frame2, text='Login', relief=GROOVE, width=15, bg='orange', command=lambda: controller.show_frame(StudentLogin))
        button2.grid(row=4, column=1, pady=10)

        # ========================================================================-SUPERVISOR BUTTON ZONE
        Label(frame2, text='Supervisor Zone', width=32, anchor=CENTER, bg='orange').grid(row=1, column=2, pady=10)
        button3 = Button(frame2, text='Registration', relief=GROOVE, width=15, bg='orange', command=lambda: controller.show_frame(SupervisorRegistration))
        button3.grid(row=3, column=2, pady=10)

        button4 = Button(frame2, text='Login', relief=GROOVE, width=15, bg='orange', command=lambda: controller.show_frame(SupervisorLogin))
        button4.grid(row=4, column=2, pady=10)

        #==========================================================================DATE
        text = datetime.datetime.now()

        print(text.strftime("%Y-%m-%d"))

        date = text.strftime("%Y-%m-%d")
        text1 = StringVar()
        text1.set(date)
        Label(framedate, textvariable=text1, width=32, anchor=CENTER, bg='green', fg='white').pack(side=RIGHT)

        # =========================================================================ABOUT BUTTON
        button4 = Button(frame2, text='About', relief=GROOVE, width=15, bg='green', fg='white', command=lambda: controller.show_frame(About))
        button4.grid(row=5, column=1, pady=10)

        # =========================================================================EXIT BUTTON
        button4 = Button(frame2, text='Exit', relief=GROOVE, width=15, bg='red', fg='white', command=self.exit)
        button4.grid(row=5, column=2, pady=10)

    def exit(self):
        if messagebox.askyesno('Exit', 'Do you want to quit!!'):
            self.__del__()

    def __del__(self):
        os.system('espeak "{}"'.format("Thank You"))
        self.quit()

# ====================================================================================================STUDENT REGISTRATION FORM
class StudentRegistration(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)


        frame1 = Frame(self, bd=2, bg='green', relief=GROOVE)
        frame1.pack(fill=X)
        Label(frame1, text='Student Registration Form',height=2, padx=30,  anchor=CENTER, bg='green', fg='white', font=('bold', 22)).pack()


        frame2 = Frame(self, bd=2, relief=GROOVE, bg='orange')
        frame2.pack(fill=BOTH, expand=1)

        # Label(frame2, text='\t\t\t                ', bg='orange').grid(row=0, column=0, columnspan=2)
        Label(frame2, text='\t\t\t                             ', bg='orange').grid(row=0, column=0, columnspan=2)
        Label(frame2, text='First Name', width=20, anchor=W, bg='orange').grid(row=1, column=1)
        self.firstNameVar = StringVar()
        self.e1 = Entry(frame2, textvariable=self.firstNameVar, width=34)
        self.e1.grid(row=1, column=2)

        Label(frame2, text='Last Name',width=20, anchor=W, bg='orange').grid(row=2, column=1)
        self.lastNameVar = StringVar()
        Entry(frame2, textvariable=self.lastNameVar, width=34).grid(row=2, column=2)

        Label(frame2, text='Registration Number', width=20, anchor=W, bg='orange').grid(row=3, column=1)
        self.regVar = StringVar()
        Entry(frame2, textvariable=self.regVar, width=34).grid(row=3, column=2)

        Label(frame2, text='Specialization', width=20, anchor=W, bg='orange').grid(row=4, column=1)
        self.specializationVar = StringVar()
        Entry(frame2, textvariable=self.specializationVar, width=34).grid(row=4, column=2)

        Label(frame2, text='Mobile No', width=20, anchor=W, bg='orange').grid(row=5, column=1)
        self.mobileNoVar = StringVar()
        Entry(frame2, textvariable=self.mobileNoVar, width=34).grid(row=5, column=2)

        Label(frame2, text='Email', width=20, anchor=W, bg='orange').grid(row=6, column=1)
        self.emailVar = StringVar()
        Entry(frame2, textvariable=self.emailVar, width=34).grid(row=6, column=2)

        Button(frame2, text='Submit', command=self.checkValidation, bg='green', fg='white', relief=RAISED).grid(row=7, column=2, sticky=E)

        button = Button(frame2, text=' Home ', bg='red', fg='white', relief=RAISED, command=lambda: controller.show_frame(StartPage))
        button.grid(row=7, column=1, sticky=W)


        self.e1.focus()
        # window.mainloop()


    def checkValidation(self):
        self.fn = self.firstNameVar.get().strip().title()
        self.ln = self.lastNameVar.get().strip().title()
        self.rn = self.regVar.get().strip()
        self.sp = self.specializationVar.get().strip().title()
        self.mn = self.mobileNoVar.get().strip()
        self.email = self.emailVar.get().strip()
        a = self.email.split('@')
        acount = self.email.count('@')

        call = True

        if len(a) == 1:
            a += ['']


        if self.fn == '':
            messagebox.showerror('Error', 'Enter First Name...!!')
            call = False
        elif not self.fn.isalpha():
            messagebox.showerror('Error', 'Enter a Valid First Name...!!')
            call = False
        elif self.ln == '':
            messagebox.showerror('Error', 'Enter Last Name...!!')
            call = False
        elif not self.ln.isalpha():
            messagebox.showerror('Error', 'Enter a Valid Last Name...!!')
            call = False
        elif self.rn == '':
            messagebox.showerror('Error', 'Enter Registration Number...!!')
            call = False
        elif len(self.rn) != 8 or not self.rn.isdigit():
            messagebox.showerror('Error', 'Enter a valid Registration Number...!!')
            call = False
        elif self.sp == '':
            messagebox.showerror('Error', 'Enter a Specialization...!!')
            call = False
        elif self.mn == '':
            messagebox.showerror('Error', 'Enter a Mobile Number...!!')
            call = False
        elif len(self.mn) != 10 or not self.mn.isdigit():
            messagebox.showerror('Error', 'Invalid Mobile Number...!!')
            call = False
        elif self.email == '':
            messagebox.showerror('Error', 'Enter an Email address...!!')
            call = False
        elif acount != 1:
            messagebox.showerror('Error', 'Etner a valid Email...!!')
            call = False
        elif not a[0].isalnum() or not ('.' in a[1]):
            messagebox.showerror('Error', 'Enter a valid Email...!!')
            call = False



        # print(fn, ln, rn, sp, mn, email, a)
        if call == True:
            self.writeData()


    def writeData(self):
        '''cnx = mysql.connector.connect(user='root', password='#smoothcriminal', host='localhost', database='practice')
        print('connection successfull...')
        cursor = cnx.cursor()

        query = 'INSERT INTO student1 VALUES(%s, %s, %s, %s, %s, %s)'
        values = (self.fn, self.ln, self.rn,
                  self.sp, self.mn, self.email)

        cursor.execute(query, values)
        # code = cursor.lastrowid
        # print('last row updated=', code)
        messagebox.showinfo('Info', 'ID Created Successfully...')
        cnx.commit()
        cursor.close()
        cnx.close()'''
        try:
            cnx = sqlite3.connect('projectdatabase.db')
            cursor = cnx.cursor()
            superid = 'Not Assinged'
            cursor.execute("INSERT INTO student VALUES(?, ?, ?, ?, ?, ?, ?)", (self.rn, self.fn, self.ln, self.sp, self.mn, self.email, superid))
            cnx.commit()
            cursor.close()
            cnx.close()

            messagebox.showinfo('Info', 'ID Created Successfully...')

            print('Student registration successful')
            self.firstNameVar.set('')
            self.lastNameVar.set('')
            self.regVar.set('')
            self.specializationVar.set('')
            self.mobileNoVar.set('')
            self.emailVar.set('')
            self.e1.focus()
            print('Entry field variables set to none')

        except sqlite3.IntegrityError:
            messagebox.showinfo('Info', 'Entered Registration Number has been already registered')
# ===============================================================================================================STUDENT REGISTRATION FORM END

# ===============================================================================================================SUPERVISOR REGISTRATION FORM
class SupervisorRegistration(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        frame1 = Frame(self, bd=2, relief=GROOVE, bg='green')
        frame1.pack(fill=X)
        Label(frame1, text='Supervisor Registration Form',height=2, padx=30,  anchor=CENTER, bg='green', fg='white', font=('bold', 22)).pack()


        frame2 = Frame(self, bd=2, relief=GROOVE, bg='orange')
        frame2.pack(fill=BOTH, expand=1)

        Label(frame2, text='\t\t\t                             ', bg='orange').grid(row=0, column=0, columnspan=2)

        Label(frame2, text='First Name', width=20, anchor=W, bg='orange').grid(row=1, column=1)
        self.firstNameVar = StringVar()
        self.e1 = Entry(frame2, textvariable=self.firstNameVar, width=34)
        self.e1.grid(row=1, column=2)

        Label(frame2, text='Last Name',width=20, anchor=W, bg='orange').grid(row=2, column=1)
        self.lastNameVar = StringVar()
        Entry(frame2, textvariable=self.lastNameVar, width=34).grid(row=2, column=2)

        Label(frame2, text='UID', width=20, anchor=W, bg='orange').grid(row=3, column=1)
        self.uidVar = StringVar()
        Entry(frame2, textvariable=self.uidVar, width=34).grid(row=3, column=2)

        Label(frame2, text='Specialization', width=20, anchor=W, bg='orange').grid(row=4, column=1)
        self.specializationVar = StringVar()
        Entry(frame2, textvariable=self.specializationVar, width=34).grid(row=4, column=2)

        Label(frame2, text='Mobile No', width=20, anchor=W, bg='orange').grid(row=5, column=1)
        self.mobileNoVar = StringVar()
        Entry(frame2, textvariable=self.mobileNoVar, width=34).grid(row=5, column=2)

        Label(frame2, text='Email', width=20, anchor=W, bg='orange').grid(row=6, column=1)
        self.emailVar = StringVar()
        Entry(frame2, textvariable=self.emailVar, width=34).grid(row=6, column=2)

        Button(frame2, text='Submit', command=self.checkValidation, bg='green', fg='white', relief=RAISED).grid(row=7, column=2, sticky=E)

        button = Button(frame2, text=' Home ', bg='red', fg='white', relief=RAISED, command=lambda: controller.show_frame(StartPage))
        button.grid(row=7, column=1, sticky=W)

        self.e1.focus()

        # window.mainloop()


    def checkValidation(self):
        self.fn = self.firstNameVar.get().strip().title()
        self.ln = self.lastNameVar.get().strip().title()
        self.uid = self.uidVar.get().strip()
        self.sp = self.specializationVar.get().strip().title()
        self.mn = self.mobileNoVar.get().strip()
        self.email = self.emailVar.get().strip()
        a = self.email.split('@')
        acount = self.email.count('@')

        call = True

        if len(a) == 1:
            a += ['']


        if self.fn == '':
            messagebox.showerror('Error', 'Enter First Name...!!')
            call = False
        elif not self.fn.isalpha():
            messagebox.showerror('Error', 'Enter a Valid First Name...!!')
            call = False
        elif self.ln == '':
            messagebox.showerror('Error', 'Enter Last Name...!!')
            call = False
        elif not self.ln.isalpha():
            messagebox.showerror('Error', 'Enter a Valid Last Name...!!')
            call = False
        elif self.uid == '':
            messagebox.showerror('Error', 'Enter UID...!!')
            call = False
        elif len(self.uid) != 5 or not self.uid.isdigit():
            messagebox.showerror('Error', 'Enter a valid UID...!!')
            call = False
        elif self.sp == '':
            messagebox.showerror('Error', 'Enter a Specialization...!!')
            call = False
        elif self.mn == '':
            messagebox.showerror('Error', 'Enter a Mobile Number...!!')
            call = False
        elif len(self.mn) != 10 or not self.mn.isdigit():
            messagebox.showerror('Error', 'Invalid Mobile Number...!!')
            call = False
        elif self.email == '':
            messagebox.showerror('Error', 'Enter an Email address...!!')
            call = False
        elif acount != 1:
            messagebox.showerror('Error', 'Etner a valid Email...!!')
            call = False
        elif not a[0].isalnum() or not ('.' in a[1]):
            messagebox.showerror('Error', 'Enter a valid Email...!!')
            call = False



        # print(fn, ln, rn, sp, mn, email, a)
        if call == True:
            self.writeData()


    def writeData(self):
        '''cnx = mysql.connector.connect(user='root', password='#smoothcriminal', host='localhost', database='practice')
        print('connection successfull...')
        cursor = cnx.cursor()

        query = 'INSERT INTO student1 VALUES(%s, %s, %s, %s, %s, %s)'
        values = (self.fn, self.ln, self.uid,
                  self.sp, self.mn, self.email)

        cursor.execute(query, values)
        # code = cursor.lastrowid
        # print('last row updated=', code)
        messagebox.showinfo('Info', 'ID Created Successfully...')
        cnx.commit()
        cursor.close()
        cnx.close()'''

        try:
            cnx = sqlite3.connect('projectdatabase.db')
            cursor = cnx.cursor()
            cursor.execute("INSERT INTO supervisor VALUES(?, ?, ?, ?, ?, ?)", (self.uid, self.fn, self.ln, self.sp, self.mn, self.email))
            cnx.commit()
            cursor.close()
            cnx.close()

            messagebox.showinfo('Info', 'ID Created Successfully...')

            print('Supervisor registered successfully')
            self.firstNameVar.set('')
            self.lastNameVar.set('')
            self.uidVar.set('')
            self.specializationVar.set('')
            self.mobileNoVar.set('')
            self.emailVar.set('')
            self.e1.focus()
            print('Entry field variables are set to none')
        except sqlite3.IntegrityError:
            messagebox.showinfo('Info', 'Entered UID has been already registered')
# ====================================================================================================SUPERVISOR REGISTRATION END

# ====================================================================================================STUDENT LOGIN
class StudentLogin(Frame):
    def __init__(self, parent, controller):
        self.controller = controller
        Frame.__init__(self, parent)

        self.frame1 = Frame(self, bg='green')
        self.frame1.pack(fill=X)

        Label(self.frame1, text='Student Login', fg='white', bg='green', font=('bold', 22)).pack()       # =========TITLE

        self.frame2 = Frame(self, bg='orange')
        self.frame2.pack(fill=BOTH, expand=1)

        Label(self.frame2, text='\t\t\t                             ', bg='orange').grid(row=0, column=0, columnspan=2)

        Label(self.frame2, text='First Name', width=20, anchor=W, bg='orange').grid(row=1, column=1, padx=10, pady=10)
        self.firstNameVar = StringVar()
        Entry(self.frame2, textvariable=self.firstNameVar, width=34).grid(row=1, column=2, padx=10, pady=10)

        Label(self.frame2, text='Last Name', width=20, anchor=W, bg='orange').grid(row=2, column=1, padx=10, pady=10)
        self.lastNameVar = StringVar()
        Entry(self.frame2, textvariable=self.lastNameVar, width=34).grid(row=2, column=2, padx=10, pady=10)

        Label(self.frame2, text='Registration Number', width=20, anchor=W, bg='orange').grid(row=3, column=1, padx=10, pady=10)
        self.regVar = StringVar()
        Entry(self.frame2, textvariable=self.regVar, width=34).grid(row=3, column=2, padx=10, pady=10)


        self.buttontext = StringVar()
        self.buttontext.set('Login')

        self.b1 = Button(self.frame2, textvariable=self.buttontext, fg='white', bg='green', width=15, command=self.check)
        self.b1.grid(row=4, column=2, sticky=E, padx=10, pady=10)

        Button(self.frame2, text='Home', fg='white', bg='red', width=15, command=lambda: controller.show_frame(StartPage)).grid(row=4, column=1, sticky=W, padx=10, pady=10)



    def check(self):
        self.fname = self.firstNameVar.get().strip().lower()
        self.lname = self.lastNameVar.get().strip().lower()
        self.reg = self.regVar.get().strip()



        call = True


        if self.fname == '':
            messagebox.showerror('Error', 'Enter First Name...!!')
            call = False
        elif not self.fname.isalpha():
            messagebox.showerror('Error', 'Enter a Valid First Name...!!')
            call = False
        elif self.lname == '':
            messagebox.showerror('Error', 'Enter Last Name...!!')
            call = False
        elif not self.lname.isalpha():
            messagebox.showerror('Error', 'Enter a Valid Last Name...!!')
            call = False
        elif self.reg == '':
            messagebox.showerror('Error', 'Enter Registration Number...!!')
            call = False
        elif len(self.reg) != 8 or not self.reg.isdigit():
            messagebox.showerror('Error', 'Enter a valid Registration Number...!!')
            call = False

        if call == True:
            # self.reg = int(self.reg)
            self.change()

        print(self.fname, self.lname, self.reg)

    def change(self):
        cnx = sqlite3.connect('projectdatabase.db')
        cursor = cnx.cursor()
        data = cursor.execute("""SELECT fnames, lnames, regno FROM student""")
        changewin = True

        for i in data:
            print(i)
            print(i[0].lower(), i[1].lower(), i[2])
            self.a = i[0].lower()
            self.b = i[1].lower()
            self.c = i[2]

            if self.fname == self.a and self.lname == self.b and self.reg == self.c:
                print('match successful')
                # self.buttontext.set('Click Here!')
                # self.b1.config(command=lambda: self.controller.show_frame(StudentLoggedIn))
                self.frame1.pack_forget()
                self.frame2.pack_forget()
                # self.LoggedIn()
                changewin = True
                break


            else:
                changewin = False
                print('not match')


        cnx.commit()
        cursor.close()
        cnx.close()
        print('connections are closed\nmoving to the logged in page')
        if changewin == True:
            self.LoggedIn()
        else:
            messagebox.showerror('LoginError', 'Invalid Credentials Provided')

    def LoggedIn(self):
        self.frame4 = Frame(self, bg='green')
        self.frame4.pack(fill=X)
        # =========================================================USER PAGE AFTER LOGIN
        # =========================GREETING FOR THE CURRENT USER
        self.nameVar = StringVar()
        greet = 'Welcome ' + self.a
        self.nameVar.set(greet)
        Label(self.frame4, textvariable=self.nameVar, fg='white', bg='green', font=('bold', 22)).pack()
        # =========================END OF GREETING
        self.frame3 = Frame(self, bg='orange')
        self.frame3.pack(fill=BOTH, expand=1)
        # ==========================================================FUNCTIONS AVIALABLE FOR USER
        # =========================UPDATE INFORMATION
        '''Button(self.frame3, text='view details', command=self.viewdetails).pack()
        Button(self.frame3, text='Update Information', command=self.updateinfo).pack()'''

        Button(self.frame3, text='View Details', relief=GROOVE, width=25, bg='orange', command=self.viewdetails).grid(row=1, column=1, pady=15, padx=15)
        Button(self.frame3, text='Update Information', relief=GROOVE, width=25, bg='orange', command=self.updateinfo).grid(row=1, column=2, pady=15, padx=15)



        # =========================ASSING SUPERVISOR AND CHANGE SUPERVISOR
        # Button(self.frame3, text='Assing/change Supervisor', command=self.assingsupervisor).pack()
        '''Button(self.frame3, text='Change Supervisor', command=self.changesupervisor).pack()'''
        Button(self.frame3, text='Assing/change Supervisor', relief=GROOVE, width=25, bg='orange', command=self.assingsupervisor).grid(row=2, column=1, pady=15, padx=15)




        # =========================VIEW SUPERVISOR DETAILS
        # Button(self.frame3, text='View Supervisor Details', command=self.viewsupervisordetails).pack()
        Button(self.frame3, text='View Supervisor Details', relief=GROOVE, width=25, bg='orange', command=self.viewsupervisordetails).grid(row=2, column=2, pady=15, padx=15)





        # =========================DELETE ACCOUNT
        # Button(self.frame3, text='Delete Account', command=self.deleteaccount).pack()
        Button(self.frame3, text='Delete Account', relief=GROOVE, width=25, bg='orange', command=self.deleteaccount).grid(row=3, column=2, pady=15, padx=15)


        # ======================================================================LOGOUT
        '''Button(self.frame3, text='Logout', command=self.logout).pack()'''
        button = Button(self.frame3, text=' Logout ', bg='red', fg='white', width=25, relief=RAISED, command=lambda: self.controller.show_frame(logout))
        button.grid(row=3, column=1, pady=15, padx=15)

    def viewdetails(self):
        print(self.reg)
        cnx = sqlite3.connect('projectdatabase.db')
        cursor = cnx.cursor()



        command = 'SELECT * FROM student WHERE regno=' + str(self.reg)
        data = cursor.execute(command)
        # print(data)
        for i in data:
            print(i)
            root = Tk()
            root.title('Details')

            listbox = Listbox(root, width=80, height=20)
            listbox.pack()
            listbox.insert(END, 'Reg No. :: ' + i[0])
            listbox.insert(END, 'First Name :: ' + i[1])
            listbox.insert(END, 'Last Name :: ' + i[2])
            listbox.insert(END, 'Specialization :: ' + i[3])
            listbox.insert(END, 'Mob No. :: ' + i[4])
            listbox.insert(END, 'Email :: ' + i[5])
            listbox.insert(END, 'Supervisor Id :: ' + i[6])




        cnx.commit()
        cursor.close()
        cnx.close()
        print('connections are closed')

    def updateinfo(self):
        print(self.reg)

        self.root = Tk()
        self.root.title('Update information')
        frame1 = Frame(self.root, bg='green')
        frame1.pack(fill=X)


        greet = self.a + ', insert into the field(s) you want to change'
        print(greet)
        Message(frame1, text=greet, fg='white', bg='green', font=('bold', 20)).pack()


        frame2 = Frame(self.root, bg='orange')
        frame2.pack(fill=BOTH, expand=1)

        Label(frame2, text='Mobile No', width=20, anchor=W, bg='orange').grid(row=1, column=1, pady=5)
        # self.mVar = StringVar()
        self.mob = Entry(frame2, width=34)
        self.mob.grid(row=1, column=2, pady=5)

        Label(frame2, text='Email', width=20, anchor=W, bg='orange').grid(row=2, column=1, pady=5)
        # self.eVar = StringVar()
        self.email = Entry(frame2, width=34)
        self.email.grid(row=2, column=2, pady=5)

        Button(frame2, text='Submit', width=15, command=self.validate, bg='green', fg='white', relief=RAISED).grid(row=3, column=2, sticky=E, pady=5)


    def validate(self):
        # print(self.mob.get(), self.email.get())
        self.mn = self.mob.get().strip()
        self.email = self.email.get().strip()
        print(self.mn, self.email)
        if self.email != '':
            a = self.email.split('@')
            acount = self.email.count('@')

        call = True

        if self.mn != '':
            if len(self.mn) != 10 or not self.mn.isdigit():
                messagebox.showerror('Error', 'Invalid Mobile Number...!!')
                call = False
        elif self.email != '':
            if acount != 1:
                messagebox.showerror('Error', 'Etner a valid Email...!!')
                call = False
            elif not a[0].isalnum() or not ('.' in a[1]):
                messagebox.showerror('Error', 'Enter a valid Email...!!')
                call = False

        if call == True:
            self.updatedatabase()
        else:
            self.root.destroy()

    def updatedatabase(self):
        print('Database update function')
        cnx = sqlite3.connect('projectdatabase.db')
        cursor = cnx.cursor()

        command = str()
        if self.mn != '' and self.email != '':
            command = 'UPDATE student SET mobiles=\'' + self.mn + '\' , emails=\'' + self.email + '\' WHERE regno=\'' + self.c + '\''
        elif self.mn != '':
            command = "UPDATE student SET mobiles='" + self.mn + "' WHERE regno='" + self.c + "'"
        elif self.email != '':
            command = "UPDATE student SET emails='" + self.email + "' WHERE regno='" + self.c + "'"

        if command != '':
            cursor.execute(command)


        cnx.commit()
        cursor.close()
        cnx.close()

        self.root.destroy()
        messagebox.showinfo('Updation', 'Changes has been successfully saved')

        print('connections has been closed\nTable updated successfully')

    def assingsupervisor(self):
        cnx = sqlite3.connect('projectdatabase.db')
        cursor = cnx.cursor()
        data = cursor.execute("""SELECT uid, fnamesup, lnamesup, specialization FROM supervisor""")
        cnx.commit()

        self.wsupervisor = Tk()
        self.wsupervisor.title('Supervisor details')
        list = 1
        listbox = Listbox(self.wsupervisor, width=80, height=20)
        listbox.pack()

        self.uidlist = []

        for i in data:
            listbox.insert(END, list)
            listbox.insert(END, 'UID :: ' + i[0])
            listbox.insert(END, 'First Name :: ' + i[1])
            listbox.insert(END, 'Last Name :: ' + i[2])
            listbox.insert(END, 'Specialization :: ' + i[3])
            listbox.insert(END, '\n')
            self.uidlist += [i[0]]
            list += 1

        print(self.uidlist)



        # =============================================WINDOW TO INSERT SUPERVISOR ID
        self.insertid = Tk()
        self.insertid.title('Insert UID')

        frame1 = Frame(self.insertid, bg='green')
        frame1.pack(fill=X)
        frame2 = Frame(self.insertid, bg='orange')
        frame2.pack(fill=BOTH, expand=1)

        greet = self.a + ', insert supervisor UID'
        print(greet)
        Label(frame1, text=greet, fg='white', bg='green', font=('bold', 20)).pack()

        Label(frame2, text='Supervisor UID', width=20, anchor=W, bg='orange').grid(row=1, column=1, padx=10, pady=10)

        self.uid = Entry(frame2, width=30)
        self.uid.grid(row=1, column=2, padx=10, pady=10)

        cnx.commit()
        cursor.close()
        cnx.close()
        print('all connections are closed in assingmentsupervisor')

        Button(frame2, text='Submit', fg='white', bg='green', width=15, command=self.addsupervisor).grid(row=2, column=2, sticky=E, padx=10, pady=10)


    def addsupervisor(self):
        cnx = sqlite3.connect('projectdatabase.db')
        cursor = cnx.cursor()

        uid = self.uid.get()

        print('supervisor uid and student regno inside add supervisor', uid, self.c)

        if uid in self.uidlist:
            self.wsupervisor.destroy()
            self.insertid.destroy()
            command = "UPDATE student SET superid='" + uid + ("' WHERE regno='") + self.c + "'"
            cursor.execute(command)
            messagebox.showinfo('Assingment', 'Supervisor assinged successfully')
        else:
            messagebox.showerror('Assingment Error', 'No such supervisor id present')


        cnx.commit()
        cursor.close()
        cnx.close()


    def deleteaccount(self):
        cnx = sqlite3.connect('projectdatabase.db')
        cursor = cnx.cursor()

        if messagebox.askyesno('Delete Account', 'Sure to delete!!!'):
            command = "DELETE FROM student WHERE regno='" + self.c + "'"
            messagebox.showinfo('Account', 'Account deleted successfully...')
            cursor.execute(command)

        cnx.commit()
        cursor.close()
        cnx.close()

    def viewsupervisordetails(self):
        cnx = sqlite3.connect('projectdatabase.db')
        cursor = cnx.cursor()

        superid = ''
        data = cursor.execute("SELECT superid FROM student WHERE regno='" + self.c + "'")
        for i in data:
            superid = i[0]
            print(superid)

        cnx.commit()

        data2 = []

        if superid == 'Not Assinged':
            messagebox.showerror('Error', 'No supervisor assinged')
        else:
            data1 = cursor.execute("SELECT * FROM supervisor WHERE uid='" + superid + "'")
            for i in data1:
                data2 += list(i)
                # print(data2)

        print(data2)


        if len(data2) != 0:
            root = Tk()
            root.title('Supervisor Details')
            listbox = Listbox(root, width=80, height=20)
            listbox.pack()
            listbox.insert(END, 'UID :: ' + i[0])
            listbox.insert(END, 'First Name :: ' + i[1])
            listbox.insert(END, 'Last Name :: ' + i[2])
            listbox.insert(END, 'Specialization :: ' + i[3])
            listbox.insert(END, 'Mobile No. :: ' + i[4])
            listbox.insert(END, 'Email :: ' + i[5])

        cnx.commit()
        cursor.close()
        cnx.close()



class SupervisorLogin(Frame):
    def __init__(self, parent, controller):
        self.controller = controller
        Frame.__init__(self, parent)

        self.frame1 = Frame(self, bg='green')
        self.frame1.pack(fill=X)

        Label(self.frame1, text='Supervisor Login', fg='white', bg='green', font=('bold', 22)).pack()       # =========TITLE

        self.frame2 = Frame(self, bg='orange')
        self.frame2.pack(fill=BOTH, expand=1)

        Label(self.frame2, text='\t\t\t                             ', bg='orange').grid(row=0, column=0, columnspan=2)

        Label(self.frame2, text='First Name', width=20, anchor=W, bg='orange').grid(row=1, column=1, padx=10, pady=10)
        self.firstNameVar = StringVar()
        Entry(self.frame2, textvariable=self.firstNameVar, width=34).grid(row=1, column=2, padx=10, pady=10)

        Label(self.frame2, text='Last Name', width=20, anchor=W, bg='orange').grid(row=2, column=1, padx=10, pady=10)
        self.lastNameVar = StringVar()
        Entry(self.frame2, textvariable=self.lastNameVar, width=34).grid(row=2, column=2, padx=10, pady=10)

        Label(self.frame2, text='UID', width=20, anchor=W, bg='orange').grid(row=3, column=1, padx=10, pady=10)
        self.regVar = StringVar()
        Entry(self.frame2, textvariable=self.regVar, width=34).grid(row=3, column=2, padx=10, pady=10)


        self.buttontext = StringVar()
        self.buttontext.set('Login')

        self.b1 = Button(self.frame2, textvariable=self.buttontext, fg='white', bg='green', width=15, command=self.check)
        self.b1.grid(row=4, column=2, sticky=E, padx=10, pady=10)

        Button(self.frame2, text='Home', fg='white', bg='red', width=15, command=lambda: controller.show_frame(StartPage)).grid(row=4, column=1, sticky=W, padx=10, pady=10)



    def check(self):
        self.fname = self.firstNameVar.get().strip().lower()
        self.lname = self.lastNameVar.get().strip().lower()
        self.reg = self.regVar.get().strip()



        call = True


        if self.fname == '':
            messagebox.showerror('Error', 'Enter First Name...!!')
            call = False
        elif not self.fname.isalpha():
            messagebox.showerror('Error', 'Enter a Valid First Name...!!')
            call = False
        elif self.lname == '':
            messagebox.showerror('Error', 'Enter Last Name...!!')
            call = False
        elif not self.lname.isalpha():
            messagebox.showerror('Error', 'Enter a Valid Last Name...!!')
            call = False
        elif self.reg == '':
            messagebox.showerror('Error', 'Enter Registration Number...!!')
            call = False
        elif len(self.reg) != 5 or not self.reg.isdigit():
            messagebox.showerror('Error', 'Enter a valid Registration Number...!!')
            call = False

        if call == True:
            # self.reg = int(self.reg)
            self.change()

        print(self.fname, self.lname, self.reg)

    def change(self):
        cnx = sqlite3.connect('projectdatabase.db')
        cursor = cnx.cursor()
        data = cursor.execute("""SELECT fnamesup, lnamesup, uid FROM supervisor""")
        changewin = True

        for i in data:
            print(i)
            print(i[0].lower(), i[1].lower(), i[2])
            self.a = i[0].lower()
            self.b = i[1].lower()
            self.c = i[2]

            if self.fname == self.a and self.lname == self.b and self.reg == self.c:
                print('match successful')
                # self.buttontext.set('Click Here!')
                # self.b1.config(command=lambda: self.controller.show_frame(StudentLoggedIn))
                self.frame1.pack_forget()
                self.frame2.pack_forget()
                # self.LoggedIn()
                changewin = True
                break


            else:
                changewin = False
                print('not match')


        cnx.commit()
        cursor.close()
        cnx.close()
        print('connections are closed\nmoving to the logged in page')
        if changewin == True:
            self.LoggedIn()
        else:
            messagebox.showerror('LoginError', 'Invalid Credentials Provided')

    def LoggedIn(self):
        self.frame4 = Frame(self, bg='green')
        self.frame4.pack(fill=X)
        # =========================================================USER PAGE AFTER LOGIN
        # =========================GREETING FOR THE CURRENT USER

        greet = 'Welcome ' + self.a
        Label(self.frame4, text=greet, fg='white', bg='green', font=('bold', 22)).pack()
        # =========================END OF GREETING
        self.frame3 = Frame(self, bg='orange')
        self.frame3.pack(fill=BOTH, expand=1)
        # ==========================================================FUNCTIONS AVIALABLE FOR USER
        # =========================UPDATE INFORMATION
        '''Button(self.frame3, text='view details', command=self.viewdetails).pack()
        Button(self.frame3, text='Update Information', command=self.updateinfo).pack()'''

        Button(self.frame3, text='View Details', relief=GROOVE, width=25, bg='orange', command=self.viewdetails).grid(row=1, column=1, pady=15, padx=15)
        Button(self.frame3, text='Update Information', relief=GROOVE, width=25, bg='orange', command=self.updateinfo).grid(row=1, column=2, pady=15, padx=15)



        # =========================VIEW STUDENTS

        Button(self.frame3, text='View Student', relief=GROOVE, width=25, bg='orange', command=self.ViewStudent).grid(row=2, column=1, pady=15, padx=15)






        # =========================DELETE ACCOUNT
        # Button(self.frame3, text='Delete Account', command=self.deleteaccount).pack()
        Button(self.frame3, text='Delete Account', relief=GROOVE, width=25, bg='orange', command=self.deleteaccount).grid(row=2, column=2, pady=15, padx=15)


        # ======================================================================LOGOUT
        '''Button(self.frame3, text='Logout', command=self.logout).pack()'''
        button = Button(self.frame3, text=' Logout ', bg='red', fg='white', width=25, relief=RAISED, command=lambda: self.controller.show_frame(logout))
        button.grid(row=3, column=1, pady=15, padx=15)

    def viewdetails(self):
        print(self.reg)
        cnx = sqlite3.connect('projectdatabase.db')
        cursor = cnx.cursor()



        command = 'SELECT * FROM supervisor WHERE uid=' + str(self.reg)
        data = cursor.execute(command)
        # print(data)
        for i in data:
            print(i)
            root = Tk()
            root.title('Details')

            listbox = Listbox(root, width=80, height=20)
            listbox.pack()
            listbox.insert(END, 'Reg No. :: ' + i[0])
            listbox.insert(END, 'First Name :: ' + i[1])
            listbox.insert(END, 'Last Name :: ' + i[2])
            listbox.insert(END, 'Specialization :: ' + i[3])
            listbox.insert(END, 'Mob No. :: ' + i[4])
            listbox.insert(END, 'Email :: ' + i[5])




        cnx.commit()
        cursor.close()
        cnx.close()
        print('connections are closed')

    def updateinfo(self):
        print(self.reg)

        self.root = Tk()
        self.root.title('Update information')
        frame1 = Frame(self.root, bg='green')
        frame1.pack(fill=X)


        greet = self.a + ', insert into the field(s) you want to change'
        print(greet)
        Message(frame1, text=greet, fg='white', bg='green', font=('bold', 20)).pack()


        frame2 = Frame(self.root, bg='orange')
        frame2.pack(fill=BOTH, expand=1)

        Label(frame2, text='Mobile No', width=20, anchor=W, bg='orange').grid(row=1, column=1, pady=5)
        # self.mVar = StringVar()
        self.mob = Entry(frame2, width=34)
        self.mob.grid(row=1, column=2, pady=5)

        Label(frame2, text='Email', width=20, anchor=W, bg='orange').grid(row=2, column=1, pady=5)
        # self.eVar = StringVar()
        self.email = Entry(frame2, width=34)
        self.email.grid(row=2, column=2, pady=5)

        Button(frame2, text='Submit', width=15, command=self.validate, bg='green', fg='white', relief=RAISED).grid(row=3, column=2, sticky=E, pady=5)


    def validate(self):
        # print(self.mob.get(), self.email.get())
        self.mn = self.mob.get().strip()
        self.email = self.email.get().strip()
        print(self.mn, self.email)
        if self.email != '':
            a = self.email.split('@')
            acount = self.email.count('@')

        call = True

        if self.mn != '':
            if len(self.mn) != 10 or not self.mn.isdigit():
                messagebox.showerror('Error', 'Invalid Mobile Number...!!')
                call = False
        elif self.email != '':
            if acount != 1:
                messagebox.showerror('Error', 'Etner a valid Email...!!')
                call = False
            elif not a[0].isalnum() or not ('.' in a[1]):
                messagebox.showerror('Error', 'Enter a valid Email...!!')
                call = False

        if call == True:
            self.updatedatabase()
        else:
            self.root.destroy()

    def updatedatabase(self):
        print('Database update function')
        cnx = sqlite3.connect('projectdatabase.db')
        cursor = cnx.cursor()

        command = str()
        if self.mn != '' and self.email != '':
            command = 'UPDATE supervisor SET mobilesup=\'' + self.mn + '\' , emailsup=\'' + self.email + '\' WHERE uid=\'' + self.c + '\''
        elif self.mn != '':
            command = "UPDATE supervisor SET mobilesup='" + self.mn + "' WHERE uid='" + self.c + "'"
        elif self.email != '':
            command = "UPDATE supervisor SET emailsup='" + self.email + "' WHERE uid='" + self.c + "'"

        if command != '':
            cursor.execute(command)


        cnx.commit()
        cursor.close()
        cnx.close()

        self.root.destroy()
        messagebox.showinfo('Updation', 'Changes has been successfully saved')

        print('connections has been closed\nTable updated successfully')




    def deleteaccount(self):
        cnx = sqlite3.connect('projectdatabase.db')
        cursor = cnx.cursor()

        if messagebox.askyesno('Delete Account', 'Sure to delete!!!'):
            command = "DELETE FROM supervisor WHERE uid='" + self.c + "'"
            messagebox.showinfo('Account', 'Account deleted successfully...')
            cursor.execute(command)
            cnx.commit()
            cursor.execute("UPDATE student SET superid='Not Assinged' WHERE superid='" + self.c + "'")
            cnx.commit()

        cnx.commit()
        cursor.close()
        cnx.close()

    def ViewStudent(self):
        cnx = sqlite3.connect('projectdatabase.db')
        cursor = cnx.cursor()
        j = 0
        data = cursor.execute("SELECT * FROM STUDENT WHERE superid='" + self.c + "'")

        for i in data:
            j += 1

        cnx.commit()
        data = cursor.execute("SELECT * FROM STUDENT WHERE superid='" + self.c + "'")

        if j != 0:
            j = 1
            root = Tk()
            root.title('Student Information')

            listbox = Listbox(root, width=80, height=20)
            listbox.pack()
            for a in data:
                print(a)
                listbox.insert(END, j)
                listbox.insert(END, 'Reg no. :: ' + a[0])
                listbox.insert(END, 'First Name :: ' + a[1])
                listbox.insert(END, 'Last Name :: ' + a[2])
                listbox.insert(END, 'Specialization :: ' + a[3])
                listbox.insert(END, 'Mobile No. :: ' + a[4])
                listbox.insert(END, 'Email :: ' + a[5])
                listbox.insert(END, '\n')
                j += 1
        else:
            messagebox.showinfo('Sorry', 'No student is connected with you')

        '''root = Tk()
        root.title('Student Information')

        listbox = Listbox(root, width=80, height=20)
        listbox.pack()
        for a in data:
            print(a)
            listbox.insert(END, j)
            listbox.insert(END, 'Reg no. :: ' + a[0])
            listbox.insert(END, 'First Name :: ' + a[1])
            listbox.insert(END, 'Last Name :: ' + a[2])
            listbox.insert(END, 'Specialization :: ' + a[3])
            listbox.insert(END, 'Mobile No. :: ' + a[4])
            listbox.insert(END, 'Email :: ' + a[5])
            listbox.insert(END, '\n')
            j += 1
        print(j)

        if j == 1:
            messagebox.showinfo('Sorry', 'No student is connected with you')
            root.destroy()'''


        cnx.commit()
        cursor.close()
        cnx.close()


class logout(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.frame1 = Frame(self, bg='green')
        self.frame1.pack(fill=X)

        Label(self.frame1, text='Thanks 4 using this software', fg='white', bg='green', font=('bold', 22)).pack()  # =========TITLE

        self.frame2 = Frame(self, bg='orange')
        self.frame2.pack(fill=BOTH, expand=1)
        '''canvas = Canvas(self.frame2, width=470, height=490)
        canvas.pack()
        # image = PhotoImage(file="C:\\Users\\razi\\Downloads\\thank1.png")
        # image = image.subsample(4, 4)
        image = PhotoImage(file="E:\\Downloads\\Capture1.PNG")
        canvas.create_image(0, 0, anchor=NW, image=image)
        # Label(self.frame2, image=image).pack()'''
        Label(self.frame2, text="Capstone Manager project\n::Made by::\n Prince Patel", bg='orange').pack()
        Label(self.frame2, text="\n\n", bg='orange').pack()
        Label(self.frame2, text="Copyright: CRIMINAL@abd 2020", bg='orange', font=('bold, 15')).pack()

        Button(self.frame2, text='Exit', relief=GROOVE, width=25, bg='red', fg='white', command=self.__del__).pack(side=BOTTOM, pady=10)

    def __del__(self):
        os.system('espeak "{}"'.format("Thank you"))
        self.quit()



class About(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        frame1 = Frame(self, bg='green')
        frame1.pack(fill=X)

        Label(frame1, text='About', fg='white', bg='green', font=('bold', 22)).pack()
        Label(frame1, text='version - 2.1', fg='white', bg='green').pack()

        frame2 = Frame(self, bg='orange')
        frame2.pack(fill=BOTH, expand=1)

        Label(frame2, text="Languages used 'Python'- for front-end & 'Sqlite3'- for back-end", bg='orange', font=('bold, 15')).pack()
        Label(frame2, text=":: Made by ::\nPRINCE PATEL - Mob(6239775238)", bg='orange', font=('bold, 14')).pack()
        Label(frame2, text="\"LOVELY PROFESSIONAL UNIVERSITY\"", bg='orange', font=('bold, 20')).pack()

        button = Button(frame2, text=' Home ', bg='red', fg='white', relief=RAISED, command=lambda: controller.show_frame(StartPage))
        button.pack()

app = SeaofBTCapp()
app.mainloop()
