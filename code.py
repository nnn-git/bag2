import tkinter as tk
import mysql.connector

def emailcheck(Email):
    con = mysql.connector.connect(host='localhost', database='grointern', user='root', password='')
    if con.is_connected():
        qry = "select Email from elearn where Email ='{}'".format(Email)
        c1 = con.cursor()
        c1.execute(qry)
        rows = c1.fetchall()
        if c1.rowcount>0:
            x=True
        else:
            x=False
        return x

def passcheck(Password):
    con = mysql.connector.connect(host='localhost', database='grointern', user='root', password='')
    if con.is_connected():
        qry = "select Pass from elearn where Pass='{}'".format(Password)
        c1 = con.cursor()
        c1.execute(qry)
        rows = c1.fetchall()
        if c1.rowcount>0:
            x=True
        else:
            x=False
        return x

class MainMenu(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.grid()
        self.label1 = tk.Label(self, text="GroIntern \n Live learning live growth",padx=235,pady=47, fg='black', bg='#99FFFF',font=('arial',25))
        self.label1.pack(pady=1.5)
        self.sign_in_button = tk.Button(self, text='Registration', command=self.Sign_in, padx=62, pady=18,bg='#00CCCC', font=('arial', 15))
        self.sign_in_button.pack(pady=1.5)
        self.log_in_button = tk.Button(self, text='LOG IN', command=self.Log_in, padx=62, pady=18, bg='#00CCCC',font=('arial', 15))
        self.log_in_button.pack(pady=1.5)
        self.quit_button = tk.Button(self, text="Quit", command=self.master.quit)
        self.quit_button.pack(pady=5)

    def Sign_in(self):
        self.master.switch_frame(Sign_in)

    def Log_in(self):
        self.master.switch_frame(Log_in)

class Sign_in(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.grid()
        self.label1 = tk.Label(self, text="GroIntern \n Live learning live growth",padx=235,pady=47, fg='black', bg='#FF99CC',font=('arial',25))
        self.label1.pack(pady=1.5)
        self.label2 = tk.Label(self, text="New Registration", font=("Arial", 20))
        self.label2.pack(pady=10)
        self.Name_label = tk.Label(self, text="Enter Your Name:")
        self.Name_label.pack()
        self.Name_entry = tk.Entry(self)
        self.Name_entry.pack(pady=5)
        self.email_label = tk.Label(self, text="Enter Your Email ID:")
        self.email_label.pack()
        self.email_entry = tk.Entry(self)
        self.email_entry.pack(pady=5)
        self.dob_label = tk.Label(self, text="Enter Your DOB:")
        self.dob_label.pack()
        self.dob_entry = tk.Entry(self)
        self.dob_entry.pack(pady=5)
        self.pass_label = tk.Label(self, text="Enter Your Password:")
        self.pass_label.pack()
        self.pass_entry = tk.Entry(self)
        self.pass_entry.pack(pady=5)
        self.add_button = tk.Button(self, text='Register', command=self.add ,font=('arial', 15))
        self.add_button.pack(pady=1.5)
        self.back_button = tk.Button(self, text="Back to Main Menu", command=self.go_to_main_menu)
        self.back_button.pack(pady=8)

    def go_to_main_menu(self):
        self.master.switch_frame(MainMenu)

    def add(self):
        con = mysql.connector.connect(host='localhost', database='grointern', user='root', password='')
        if con.is_connected():
            Name = self.Name_entry.get()
            Email = self.email_entry.get()
            DOB = self.dob_entry.get()
            Pass = self.pass_entry.get()
            cu = 'No course'
            pro = '0%'
            qry = "insert into elearn values ('{}','{}','{}','{}','{}','{}')".format(Name, Email,DOB, Pass,cu,pro)
            c1 = con.cursor()
            c1.execute(qry)
            con.commit()
            con.close
            self.label1 = tk.Label(self, text="Welcome in \n GroIntern \n Live learning live growth ", font=("Arial", 10))
            self.label1.pack(pady=5)
        else:
            self.label = tk.Label(self, text="Server Error(MySQL is not Connected)", font=("Arial", 10))
            self.label.pack(pady=5)
            con.close

class Log_in(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.grid()
        self.label1 = tk.Label(self, text="GroIntern \n Live learning live growth", padx=235, pady=47, fg='black',bg='#FF99CC', font=('arial', 25))
        self.label1.pack(pady=1.5)
        self.label2 = tk.Label(self, text="Student Portal", font=("Arial", 20))
        self.label2.pack(pady=10)
        self.email_label = tk.Label(self, text="Enter Your Email ID:")
        self.email_label.pack()
        self.email_entry = tk.Entry(self)
        self.email_entry.pack(pady=5)
        self.label2.pack(pady=10)
        self.pass_label = tk.Label(self, text="Enter Your Password:")
        self.pass_label.pack()
        self.pass_entry = tk.Entry(self)
        self.pass_entry.pack(pady=5)
        self.search_button = tk.Button(self, text='Log in', command=self.search ,font=('arial', 15))
        self.search_button.pack(pady=1.5)
        self.forpass_button = tk.Button(self, text='Forget Password', command=self.forpass,font=('arial', 15))
        self.forpass_button.pack(pady=1.5)
        self.back_button = tk.Button(self, text="Back to Main Menu", command=self.go_to_main_menu)
        self.back_button.pack(pady=8)

    def search(self):
        con = mysql.connector.connect(host='localhost', database='grointern', user='root', password='')
        if con.is_connected():
            Email = self.email_entry.get()
            Password = self.pass_entry.get()
            if emailcheck(Email):
                if passcheck(Password):
                    self.master.switch_frame(student)
                else:
                    self.label = tk.Label(self, text="Incorrect password", font=("Arial", 10))
                    self.label.pack(pady=5)
            else:
                self.label = tk.Label(self, text="Incorrect email", font=("Arial", 10))
                self.label.pack(pady=5)
        else:
            self.label = tk.Label(self, text="Server Error (MySQL is not connected)", font=("Arial", 10))
            self.label.pack(pady=5)
            con.close()

    def forpass(self):
        self.master.switch_frame(forgetpass)

    def go_to_main_menu(self):
        self.master.switch_frame(MainMenu)

class forgetpass(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.grid()
        self.label1 = tk.Label(self, text="GroIntern \n Live learning live growth", padx=235, pady=47, fg='black',bg='#FF99CC', font=('arial', 25))
        self.label1.pack(pady=1.5)
        self.label2 = tk.Label(self, text="Password portal", font=("Arial", 20))
        self.label2.pack(pady=10)
        self.email_label = tk.Label(self, text="Enter Your Mail:")
        self.email_label.pack()
        self.email_entry = tk.Entry(self)
        self.email_entry.pack(pady=5)
        self.forpass_button = tk.Button(self, text='Check', command=self.fop,font=('arial', 15))
        self.forpass_button.pack(pady=1.5)
        self.back_button = tk.Button(self, text="Back to Main Menu", command=self.go_to_main_menu)
        self.back_button.pack(pady=8)

    def fop(self):
        con = mysql.connector.connect(host='localhost', database='grointern', user='root', password='')
        if con.is_connected():
            Email = self.email_entry.get()
            if emailcheck(Email):
                self.pass_label = tk.Label(self, text="Enter New Password:")
                self.pass_label.pack()
                self.pass_entry = tk.Entry(self)
                self.pass_entry.pack(pady=5)
                self.up_pas_button = tk.Button(self, text='Update', command=self.up, font=('arial', 15))
                self.up_pas_button.pack(pady=1.5)
            else:
                self.label = tk.Label(self, text="Incorrect email", font=("Arial", 10))
                self.label.pack(pady=5)
        else:
            self.label = tk.Label(self, text="Server Error (MySQL is not connected)", font=("Arial", 10))
            self.label.pack(pady=5)

    def up(self):
        con = mysql.connector.connect(host='localhost', database='grointern', user='root', password='')
        if con.is_connected():
            Email = self.email_entry.get()
            Pass = self.pass_entry.get()
            qry = "update elearn SET Pass='{}' where Email='{}'".format(Pass,Email)
            c1 = con.cursor()
            c1.execute(qry)
            con.commit()
            con.close
            self.label = tk.Label(self, text="Password Change", font=("Arial", 10))
            self.label.pack(pady=5)
        else:
            self.label = tk.Label(self, text="Server Error (MySQL is not connected)", font=("Arial", 10))
            self.label.pack(pady=5)

    def go_to_main_menu(self):
        self.master.switch_frame(Log_in)

class student(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.grid()
        self.label1 = tk.Label(self, text="GroIntern \n Live learning live growth", padx=235, pady=47, fg='black',bg='#FF99CC', font=('arial', 25))
        self.label1.pack(pady=1.5)
        self.label2 = tk.Label(self, text="Student Portal", font=("Arial", 20))
        self.label2.pack(pady=10)
        self.Show_detail_button = tk.Button(self, text='SHOW DETAIL', command=self.sh, padx=62, pady=18,bg='#00CCCC', font=('arial', 15))
        self.Show_detail_button.pack(pady=1.5)
        self.cur_button = tk.Button(self, text='Courses', command=self.Course, padx=62, pady=18, bg='#00CCCC',font=('arial', 15))
        self.cur_button.pack(pady=1.5)
        self.cc_button = tk.Button(self, text='Course Contain', command=self.cc,padx=62, pady=18, bg='#00CCCC',font=('arial', 15))
        self.cc_button.pack(pady=1.5)
        self.del_button = tk.Button(self,text='Delete Account',command=self.dele ,padx=62, pady=18, bg='#00CCCC',font=('arial', 15))
        self.del_button.pack(pady=1.5)
        self.pro_button = tk.Button(self, text='Course Progress', command=self.pro, padx=62, pady=18, bg='#00CCCC',font=('arial', 15))
        self.pro_button.pack(pady=1.5)
        self.back_button = tk.Button(self, text="Back", command=self.go_to_main_menu)
        self.back_button.pack(pady=8)

    def Course(self):
        self.master.switch_frame(cur)

    def go_to_main_menu(self):
        self.master.switch_frame(Log_in)

    def cc(self):
        self.master.switch_frame(cc)

    def dele(self):
        self.master.switch_frame(Delete)

    def sh(self):
        self.master.switch_frame(Show_de)

    def pro(self):
        self.master.switch_frame(Progress)

class cur(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.grid()
        self.label1 = tk.Label(self, text="GroIntern \n Live learning live growth", padx=235, pady=47, fg='black',bg='#FF99CC', font=('arial', 25))
        self.label1.pack(pady=1.5)
        self.label2 = tk.Label(self, text="Course List", font=("Arial", 20))
        self.label2.pack(pady=10)
        self.label2 = tk.Label(self, text="1. Python \n 2. Python Advance \n 3. Core Java \n 4. Advance Java \n 5. C Language \n 6. C++", font=("Arial", 10))
        self.label2.pack(pady=10)
        self.cn_label = tk.Label(self, text="Enter Your Course Number:")
        self.cn_label.pack()
        self.cn_entry = tk.Entry(self)
        self.cn_entry.pack(pady=5)
        self.ca_button = tk.Button(self, text='Course Add', command=self.cadd, font=('arial', 9))
        self.ca_button.pack(pady=1.5)
        self.back_button = tk.Button(self, text="Back", command=self.go_to_main_menu)
        self.back_button.pack(pady=8)

    def go_to_main_menu(self):
        self.master.switch_frame(student)

    def cadd(self):
        self.email_label = tk.Label(self, text="Conform Your Email ID:")
        self.email_label.pack()
        self.email_entry = tk.Entry(self)
        self.email_entry.pack(pady=5)
        self.cfa_button = tk.Button(self, text='Course Add', command=self.cfadd, font=('arial', 9))
        self.cfa_button.pack(pady=1.5)

    def cfadd(self):
        con = mysql.connector.connect(host='localhost', database='grointern', user='root', password='')
        if con.is_connected():
            no = self.cn_entry.get()
            Email = self.email_entry.get()
            if no == '1':
                cu = 'Python'
            elif no == '2':
                cu = 'Python Advance'
            elif no == '3':
                cu = 'Core Java'
            elif no == '4':
                cu = 'Advance Java'
            elif no == '5':
                cu = 'C Language'
            elif no == '6':
                cu = 'C++'
            else:
                cu = 'No Course'
            qry = "update elearn SET cu='{}' where Email='{}'".format(cu, Email)
            c1 = con.cursor()
            c1.execute(qry)
            con.commit()
            con.close
            self.label1 = tk.Label(self, text="Thanks For purchasing the course \n GroIntern \n Live learning live growth ",font=("Arial", 10))
            self.label1.pack(pady=5)
        else:
            self.label = tk.Label(self, text="Server Error (MySQL is not connected)", font=("Arial", 10))
            self.label.pack(pady=5)
            con.close()

class Show_de(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.grid()
        self.label1 = tk.Label(self, text="GroIntern \n Live learning live growth", padx=235, pady=47, fg='black',bg='#FF99CC', font=('arial', 25))
        self.label1.pack(pady=1.5)
        self.label2 = tk.Label(self, text="About", font=("Arial", 20))
        self.label2.pack(pady=10)
        self.email_label = tk.Label(self, text="Conform Your Email ID:")
        self.email_label.pack()
        self.email_entry = tk.Entry(self)
        self.email_entry.pack(pady=5)
        self.show_button = tk.Button(self, text='Show', command=self.sw, font=('arial', 9))
        self.show_button.pack(pady=1.5)
        self.back_button = tk.Button(self, text="Back", command=self.go_to_main_menu)
        self.back_button.pack(pady=8)

    def go_to_main_menu(self):
        self.master.switch_frame(student)

    def sw(self):
        con = mysql.connector.connect(host='localhost', database='grointern', user='root', password='')
        if con.is_connected():
            Email = self.email_entry.get()
            if emailcheck(Email):
                qry = "select * from elearn where Email='{}'".format(Email)
                c1 = con.cursor()
                c1.execute(qry)
                rows = c1.fetchall()
                for x in rows:
                    self.label1 = tk.Label(self, text="your Name is --> {}".format(x[0]), font=("Arial", 10))
                    self.label1.pack(pady=5)
                    self.label2 = tk.Label(self, text="your Email is --> {}".format(x[1]), font=("Arial", 10))
                    self.label2.pack(pady=5)
                    self.label3 = tk.Label(self, text="your DOB is --> {}".format(x[2]), font=("Arial", 10))
                    self.label3.pack(pady=5)
                    self.label4 = tk.Label(self, text="your Course is --> {}".format(x[4]), font=("Arial", 10))
                    self.label4.pack(pady=5)
                c1.close
            else:
                self.label = tk.Label(self, text="Incorrect email", font=("Arial", 10))
                self.label.pack(pady=5)
        else:
            self.label = tk.Label(self, text="Server Error (MySQL is not connected)", font=("Arial", 10))
            self.label.pack(pady=5)
            con.close()

class Delete(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.grid()
        self.label1 = tk.Label(self, text="GroIntern \n Live learning live growth", padx=235, pady=47, fg='black',bg='#FF99CC', font=('arial', 25))
        self.label1.pack(pady=1.5)
        self.label2 = tk.Label(self, text="Delete", font=("Arial", 20))
        self.label2.pack(pady=10)
        self.email_label = tk.Label(self, text="Conform Your Email ID:")
        self.email_label.pack()
        self.email_entry = tk.Entry(self)
        self.email_entry.pack(pady=5)
        self.Del_button = tk.Button(self, text='Delete', command=self.de, font=('arial', 9))
        self.Del_button.pack(pady=1.5)
        self.back_button = tk.Button(self, text="Back", command=self.go_to_main_menu)
        self.back_button.pack(pady=8)

    def go_to_main_menu(self):
        self.master.switch_frame(MainMenu)

    def de(self):
        con = mysql.connector.connect(host='localhost', database='grointern', user='root', password='')
        if con.is_connected():
            Email = self.email_entry.get()
            if emailcheck(Email):
                qry = "delete from elearn where Email='{}'".format(Email)
                c1 = con.cursor()
                c1.execute(qry)
                con.commit()
                con.close
                self.label = tk.Label(self, text='Your Account has Been Deleted \n Thanks for Connected With Us \n GroIntern \n Live learning live growth', font=("Arial", 10))
                self.label.pack(pady=5)
            else:
                self.label = tk.Label(self, text="Incorrect email", font=("Arial", 10))
                self.label.pack(pady=5)
        else:
            self.label = tk.Label(self, text="Server Error (MySQL is not connected)", font=("Arial", 10))
            self.label.pack(pady=5)
            con.close()

class Progress(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.grid()
        self.label1 = tk.Label(self, text="GroIntern \n Live learning live growth", padx=235, pady=47, fg='black',bg='#FF99CC', font=('arial', 25))
        self.label1.pack(pady=1.5)
        self.label2 = tk.Label(self, text="Course Progress", font=("Arial", 20))
        self.label2.pack(pady=10)
        self.email_label = tk.Label(self, text="Enter Your Email ID:")
        self.email_label.pack()
        self.email_entry = tk.Entry(self)
        self.email_entry.pack(pady=5)
        self.ser_Button = tk.Button(self,text='Search',command=self.ser,font=('arial', 9))
        self.ser_Button.pack(pady=1.5)
        self.back_button = tk.Button(self, text="Back", command=self.go_to_main_menu)
        self.back_button.pack(pady=8)

    def go_to_main_menu(self):
        self.master.switch_frame(student)

    def ser(self):
        con = mysql.connector.connect(host='localhost', database='grointern', user='root', password='')
        if con.is_connected():
            Email = self.email_entry.get()
            if emailcheck(Email):
                qry = "select * from elearn where Email='{}'".format(Email)
                c1 = con.cursor()
                c1.execute(qry)
                rows = c1.fetchall()
                for x in rows:
                    self.label1 = tk.Label(self, text="your Course is --> {}".format(x[4]), font=("Arial", 10))
                    self.label1.pack(pady=5)
                    self.label2 = tk.Label(self, text="your Course Progress is --> {}".format(x[5]), font=("Arial", 10))
                    self.label2.pack(pady=5)
                c1.close
            else:
                self.label = tk.Label(self, text="Incorrect email", font=("Arial", 10))
                self.label.pack(pady=5)
        else:
            self.label = tk.Label(self, text="Server Error (MySQL is not connected)", font=("Arial", 10))
            self.label.pack(pady=5)
            con.close()

class cc(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.grid()
        self.label1 = tk.Label(self, text="GroIntern \n Live learning live growth", padx=235, pady=47, fg='black',bg='#FF99CC', font=('arial', 25))
        self.label1.pack(pady=1.5)
        self.label2 = tk.Label(self, text="Course Contain", font=("Arial", 20))
        self.label2.pack(pady=10)
        self.cur_label = tk.Label(self, text="Enter Your Course:")
        self.cur_label.pack()
        self.cur_entry = tk.Entry(self)
        self.cur_entry.pack(pady=5)
        self.st_button = tk.Button(self, text='Start', command=self.st, font=('arial', 9))
        self.st_button.pack(pady=1.5)
        self.back_button = tk.Button(self, text="Back", command=self.go_to_main_menu)
        self.back_button.pack(pady=8)

    def go_to_main_menu(self):
        self.master.switch_frame(student)

    def st(self):
        curs = self.cur_entry.get()
        if curs == 'Python':
            self.master.switch_frame(Py)
        elif curs == 'Python Advance':
            self.master.switch_frame(Py_adv)
        elif curs == 'Core Java':
            self.master.switch_frame(c_ja)
        elif curs == 'Advance Java':
            self.master.switch_frame(a_ja)
        elif curs == 'C Language':
            self.master.switch_frame(c_lan)
        elif curs == 'C++':
            self.master.switch_frame(cpp_lan)
        else:
            self.label = tk.Label(self,text='Sorry We Dont Provide That Course',font=("Arial", 10))
            self.label.pack(pady=5)

class Py(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.grid()
        self.label1 = tk.Label(self, text="GroIntern \n Live learning live growth", padx=235, pady=47, fg='black',bg='#FF99CC', font=('arial', 25))
        self.label1.pack(pady=1.5)
        self.label2 = tk.Label(self, text="Welcome To Python Course", font=("Arial", 20))
        self.label2.pack(pady=10)
        self.label3 = tk.Label(self, text="Python Topic \n "
                                          "1. What is Python \n "
                                          "2. Feature of python \n "
                                          "3. List, Tuple, Dictionary \n "
                                          "4. Class", font=("Arial", 10))
        self.label3.pack(pady=10)
        self.st_button = tk.Button(self, text='Start', command=self.sta, font=('arial', 9))
        self.st_button.pack(pady=1.5)
        self.back_button = tk.Button(self, text="Back", command=self.go_to_main_menu)
        self.back_button.pack(pady=8)

    def go_to_main_menu(self):
        self.master.switch_frame(cc)

    def sta(self):
        self.master.switch_frame(py_fr1)

class py_fr1(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.grid()
        self.label1 = tk.Label(self, text="GroIntern \n Live learning live growth", padx=235, pady=47, fg='black',bg='#FF99CC', font=('arial', 25))
        self.label1.pack(pady=1.5)
        self.label2 = tk.Label(self, text="What is Python", font=("Arial", 20))
        self.label2.pack(pady=10)
        self.label3 = tk.Label(self,text='Python is an interpreted, object-oriented, high-level programming language with dynamic se- \n '
                                         "mantics. Its high-level built in data structures, combined with dynamic typing and dynamic \n "
                                         "binding, make it very attractive for Rapid Application Development, as well as for use as a \n "
                                         "scripting or glue language to connect existing components together. Python simple, easy to \n"
                                         "learn syntax emphasizes readability and therefore reduces the cost of program maintenance. \n"
                                         "Python supports modules and packages, which encourages program modularity and code re- \n"
                                         "use. The Python interpreter and the extensive standard library are available in source or bi- \n"
                                         "nary form without charge for all major platforms, and can be freely distributed." ,font=("Arial", 10))
        self.label3.pack(pady=10)
        self.email_label = tk.Label(self, text="Enter Your Email ID:")
        self.email_label.pack()
        self.email_entry = tk.Entry(self)
        self.email_entry.pack(pady=5)
        self.ne_button = tk.Button(self, text='Next', command=self.ne, font=('arial', 9))
        self.ne_button.pack(pady=1.5)
        self.back_button = tk.Button(self, text="Back", command=self.go_to_main_menu)
        self.back_button.pack(pady=8)

    def ne(self):
        con = mysql.connector.connect(host='localhost', database='grointern', user='root', password='')
        if con.is_connected():
            Email = self.email_entry.get()
            if emailcheck(Email):
                qry = "update elearn SET pro='25%' where Email='{}'".format(Email)
                c1 = con.cursor()
                c1.execute(qry)
                con.commit()
                con.close
                self.master.switch_frame(py_fr2)
            else:
                self.label = tk.Label(self, text="Incorrect email", font=("Arial", 10))
                self.label.pack(pady=5)
        else:
            self.label = tk.Label(self, text="Server Error (MySQL is not connected)", font=("Arial", 10))
            self.label.pack(pady=5)
            con.close()

    def go_to_main_menu(self):
        self.master.switch_frame(cc)

class py_fr2(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.grid()
        self.label1 = tk.Label(self, text="GroIntern \n Live learning live growth", padx=235, pady=47, fg='black',bg='#FF99CC', font=('arial', 25))
        self.label1.pack(pady=1.5)
        self.label2 = tk.Label(self, text="Feature of Python", font=("Arial", 20))
        self.label2.pack(pady=10)
        self.Label3 = tk.Label(self, text='Python is a dynamic, high-level, free open source, and interpreted programming \n'
                                          'language. It supports object-oriented programming as well as procedural-oriented \n'
                                          'programming. In Python, we don’t need to declare the type of variable because it is \n'
                                          'a dynamically typed language. \n'
                                          '1. Free and Open Source \n '
                                          '2. Easy to code \n '
                                          '3. Easy to Read \n '
                                          '4. Object-Oriented Language \n '
                                          '5. GUI Programming Support \n '
                                          '6. High-Level Language \n '
                                          '7. Large Community Support \n '
                                          '8. Easy to Debug',font=("Arial", 10))
        self.Label3.pack(pady=10)
        self.email_label = tk.Label(self, text="Enter Your Email ID:")
        self.email_label.pack()
        self.email_entry = tk.Entry(self)
        self.email_entry.pack(pady=5)
        self.ne_button = tk.Button(self, text='Next', command=self.ne, font=('arial', 9))
        self.ne_button.pack(pady=1.5)
        self.back_button = tk.Button(self, text="Back", command=self.go_to_main_menu)
        self.back_button.pack(pady=8)

    def ne(self):
        con = mysql.connector.connect(host='localhost', database='grointern', user='root', password='')
        if con.is_connected():
            Email = self.email_entry.get()
            if emailcheck(Email):
                qry = "update elearn SET pro='50%' where Email='{}'".format(Email)
                c1 = con.cursor()
                c1.execute(qry)
                con.commit()
                con.close
                self.master.switch_frame(py_fr3)
            else:
                self.label = tk.Label(self, text="Incorrect email", font=("Arial", 10))
                self.label.pack(pady=5)
        else:
            self.label = tk.Label(self, text="Server Error (MySQL is not connected)", font=("Arial", 10))
            self.label.pack(pady=5)
            con.close()

    def go_to_main_menu(self):
        self.master.switch_frame(cc)

class py_fr3(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.grid()
        self.label1 = tk.Label(self, text="GroIntern \n Live learning live growth", padx=235, pady=47, fg='black',bg='#FF99CC', font=('arial', 25))
        self.label1.pack(pady=1.5)
        self.label2 = tk.Label(self, text="List, Tuple, Dictionary", font=("Arial", 20))
        self.label2.pack(pady=10)
        self.label3 = tk.Label(self,text='LIST \n '
                                         'List is one of the data structures available in python which is used to store \n'
                                         'multiple values in a single data structure. We can create a list in Python \n'
                                         'using the square braces[ ]. It is mutable which means that we can modify a \n'
                                         'list once it is created.' , font=("Arial", 10))
        self.label3.pack(pady=10)
        self.label4 = tk.Label(self, text='TUPLE \n'
                                          'Tuple is one of the data structures of the python programming language. It \n'
                                          'is used to store multiple values separated by comma in an ordered manner. \n'
                                          'It is represented by brackets (). It is immutable in the sense that once the \n'
                                          'tuple is created, we cannot modify it.', font=("Arial",9))
        self.label4.pack(pady=10)
        self.label5 = tk.Label(self, text='Dictionary \n'
                                          'Dictionary is the data structure available in python. The dictionaries are also \n'
                                          'known as associative memories or associative arrays. We can create a \n'
                                          'dictionary using the curly braces {}. A dictionary stores the data in the form \n'
                                          'of key and value pairs.', font=("Arial", 9))
        self.label5.pack(pady=10)
        self.email_label = tk.Label(self, text="Enter Your Email ID:")
        self.email_label.pack()
        self.email_entry = tk.Entry(self)
        self.email_entry.pack(pady=5)
        self.ne_button = tk.Button(self, text='Next', command=self.ne, font=('arial', 9))
        self.ne_button.pack(pady=1.5)
        self.back_button = tk.Button(self, text="Back", command=self.go_to_main_menu)
        self.back_button.pack(pady=8)

    def ne(self):
        con = mysql.connector.connect(host='localhost', database='grointern', user='root', password='')
        if con.is_connected():
            Email = self.email_entry.get()
            if emailcheck(Email):
                qry = "update elearn SET pro='75%' where Email='{}'".format(Email)
                c1 = con.cursor()
                c1.execute(qry)
                con.commit()
                con.close
                self.master.switch_frame(py_fr4)
            else:
                self.label = tk.Label(self, text="Incorrect email", font=("Arial", 10))
                self.label.pack(pady=5)
        else:
            self.label = tk.Label(self, text="Server Error (MySQL is not connected)", font=("Arial", 10))
            self.label.pack(pady=5)
            con.close()

    def go_to_main_menu(self):
        self.master.switch_frame(cc)

class py_fr4(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.grid()
        self.label1 = tk.Label(self, text="GroIntern \n Live learning live growth", padx=235, pady=47, fg='black',bg='#FF99CC', font=('arial', 25))
        self.label1.pack(pady=1.5)
        self.label2 = tk.Label(self, text="Class", font=("Arial", 10))
        self.label2.pack(pady=10)
        self.label3 = tk.Label(self,text='A class is a user-defined blueprint or prototype from which objects are created. \n'
                                         'Classes provide a means of bundling data and functionality together. Creating a \n'
                                         'new class creates a new type of object, allowing new instances of that type to be \n'
                                         'made. Each class instance can have attributes attached to it for maintaining its state. \n'
                                         'Class instances can also have methods (defined by their class) for modifying their \n'
                                         'state. \n'
                                         '\n'
                                         'Some points on Python class: \n'
                                         '1.Classes are created by keyword class. \n '
                                         '2.Attributes are the variables that belong to a class. \n '
                                         '3.Attributes are always public and can be accessed using the dot (.) operator. \n'
                                         'Eg. My class. Myattribute' , font=("Arial", 9))
        self.label3.pack(pady=10)
        self.email_label = tk.Label(self, text="Enter Your Email ID:")
        self.email_label.pack()
        self.email_entry = tk.Entry(self)
        self.email_entry.pack(pady=5)
        self.ne_button = tk.Button(self, text='Finish', command=self.ne, font=('arial', 9))
        self.ne_button.pack(pady=1.5)

    def ne(self):
        con = mysql.connector.connect(host='localhost', database='grointern', user='root', password='')
        if con.is_connected():
            Email = self.email_entry.get()
            if emailcheck(Email):
                qry = "update elearn SET pro='100%' where Email='{}'".format(Email)
                c1 = con.cursor()
                c1.execute(qry)
                con.commit()
                con.close
                self.master.switch_frame(student)
            else:
                self.label = tk.Label(self, text="Incorrect email", font=("Arial", 10))
                self.label.pack(pady=5)
        else:
            self.label = tk.Label(self, text="Server Error (MySQL is not connected)", font=("Arial", 10))
            self.label.pack(pady=5)
            con.close()

class Py_adv(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.grid()
        self.label1 = tk.Label(self, text="GroIntern \n Live learning live growth", padx=235, pady=47, fg='black',bg='#FF99CC', font=('arial', 25))
        self.label1.pack(pady=1.5)
        self.label2 = tk.Label(self, text="Welcome To Python Advance Course", font=("Arial", 20))
        self.label2.pack(pady=10)
        self.label3 = tk.Label(self, text="Python Advance Topic \n "
                                          "1. Recursive Functions \n "
                                          "2. Iterators and Iterables \n "
                                          "3. Generators and Iterators \n "
                                          "4. Lambda Operator", font=("Arial", 10))
        self.label3.pack(pady=10)
        self.st_button = tk.Button(self, text='Start', command=self.sta, font=('arial', 9))
        self.st_button.pack(pady=1.5)
        self.back_button = tk.Button(self, text="Back", command=self.go_to_main_menu)
        self.back_button.pack(pady=8)

    def go_to_main_menu(self):
        self.master.switch_frame(cc)

    def sta(self):
        self.master.switch_frame(py_ad_fr1)

class py_ad_fr1(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.grid()
        self.label1 = tk.Label(self, text="GroIntern \n Live learning live growth", padx=235, pady=47, fg='black',bg='#FF99CC', font=('arial', 25))
        self.label1.pack(pady=1.5)
        self.label2 = tk.Label(self, text="Recursive Functions", font=("Arial", 20))
        self.label2.pack(pady=10)
        self.label3 = tk.Label(self, text="Recursion is a method of programming or coding a problem, in which a function calls itself one \n"
                                          "or more times in its body. Usually, it is returning the return value of this function call. If a function \n"
                                          "definition satisfies the condition of recursion, we call this function a recursive function.", font=("Arial", 10))
        self.label3.pack(pady=10)
        self.email_label = tk.Label(self, text="Enter Your Email ID:")
        self.email_label.pack()
        self.email_entry = tk.Entry(self)
        self.email_entry.pack(pady=5)
        self.ne_button = tk.Button(self, text='Next', command=self.ne, font=('arial', 9))
        self.ne_button.pack(pady=1.5)

    def ne(self):
        con = mysql.connector.connect(host='localhost', database='grointern', user='root', password='')
        if con.is_connected():
            Email = self.email_entry.get()
            if emailcheck(Email):
                qry = "update elearn SET pro='25%' where Email='{}'".format(Email)
                c1 = con.cursor()
                c1.execute(qry)
                con.commit()
                con.close
                self.master.switch_frame(py_ad_fr2)
            else:
                self.label = tk.Label(self, text="Incorrect email", font=("Arial", 10))
                self.label.pack(pady=5)
        else:
            self.label = tk.Label(self, text="Server Error (MySQL is not connected)", font=("Arial", 10))
            self.label.pack(pady=5)
            con.close()

    def go_to_main_menu(self):
        self.master.switch_frame(cc)

class py_ad_fr2(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.grid()
        self.label1 = tk.Label(self, text="GroIntern \n Live learning live growth", padx=235, pady=47, fg='black',bg='#FF99CC', font=('arial', 25))
        self.label1.pack(pady=1.5)
        self.label2 = tk.Label(self, text="Iterators and Iterables", font=("Arial", 20))
        self.label2.pack(pady=10)
        self.label3 = tk.Label(self, text="The Python forums and other question-and-answer websites like Quora and Stackoverflow are \n"
                                          "full of questions concerning 'iterators' and 'iterable'. Some want to know how they are defined \n"
                                          "and others want to know if there is an easy way to check, if an object is an iterator or an iterable. \n"
                                          "We will provide a function for this purpose.", font=("Arial", 10))
        self.label3.pack(pady=10)
        self.email_label = tk.Label(self, text="Enter Your Email ID:")
        self.email_label.pack()
        self.email_entry = tk.Entry(self)
        self.email_entry.pack(pady=5)
        self.ne_button = tk.Button(self, text='Next', command=self.ne, font=('arial', 9))
        self.ne_button.pack(pady=1.5)

    def ne(self):
        con = mysql.connector.connect(host='localhost', database='grointern', user='root', password='')
        if con.is_connected():
            Email = self.email_entry.get()
            if emailcheck(Email):
                qry = "update elearn SET pro='50%' where Email='{}'".format(Email)
                c1 = con.cursor()
                c1.execute(qry)
                con.commit()
                con.close
                self.master.switch_frame(py_ad_fr3)
            else:
                self.label = tk.Label(self, text="Incorrect email", font=("Arial", 10))
                self.label.pack(pady=5)
        else:
            self.label = tk.Label(self, text="Server Error (MySQL is not connected)", font=("Arial", 10))
            self.label.pack(pady=5)
            con.close()

    def go_to_main_menu(self):
        self.master.switch_frame(cc)

class py_ad_fr3(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.grid()
        self.label1 = tk.Label(self, text="GroIntern \n Live learning live growth", padx=235, pady=47, fg='black',bg='#FF99CC', font=('arial', 25))
        self.label1.pack(pady=1.5)
        self.label2 = tk.Label(self, text="Generators and Iterators", font=("Arial", 20))
        self.label2.pack(pady=10)
        self.label3 = tk.Label(self, text="What is an iterator? Iterators are objects that can be iterated over like we do in a for loop. We \n"
                                          "can also say that an iterator is an object, which returns data, one element at a time. That is, they \n"
                                          "do not do any work until we explicitly ask for their next item. They work on a principle, which is \n"
                                          "known in computer science as lazy evaluation. Lazy evaluation is an evaluation strategy which \n"
                                          "delays the evaluation of an expression until its value is really needed. Due to the laziness of \n"
                                          "Python iterators, they are a great way to deal with infinity, i.e. iterables which can iterate for ever. \n"
                                          "You can hardly find Python programs that are not teaming with iterators.", font=("Arial", 10))
        self.label3.pack(pady=10)
        self.email_label = tk.Label(self, text="Enter Your Email ID:")
        self.email_label.pack()
        self.email_entry = tk.Entry(self)
        self.email_entry.pack(pady=5)
        self.ne_button = tk.Button(self, text='Next', command=self.ne, font=('arial', 9))
        self.ne_button.pack(pady=1.5)

    def ne(self):
        con = mysql.connector.connect(host='localhost', database='grointern', user='root', password='')
        if con.is_connected():
            Email = self.email_entry.get()
            if emailcheck(Email):
                qry = "update elearn SET pro='75%' where Email='{}'".format(Email)
                c1 = con.cursor()
                c1.execute(qry)
                con.commit()
                con.close
                self.master.switch_frame(py_ad_fr4)
            else:
                self.label = tk.Label(self, text="Incorrect email", font=("Arial", 10))
                self.label.pack(pady=5)
        else:
            self.label = tk.Label(self, text="Server Error (MySQL is not connected)", font=("Arial", 10))
            self.label.pack(pady=5)
            con.close()

    def go_to_main_menu(self):
        self.master.switch_frame(cc)

class py_ad_fr4(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.grid()
        self.label1 = tk.Label(self, text="GroIntern \n Live learning live growth", padx=235, pady=47, fg='black',bg='#FF99CC', font=('arial', 25))
        self.label1.pack(pady=1.5)
        self.label2 = tk.Label(self, text="Lambda Operator", font=("Arial", 20))
        self.label2.pack(pady=10)
        self.label3 = tk.Label(self, text="Lambda functions are similar to user-defined functions but without a name. \n"
                                          "They're commonly referred to as anonymous functions.\n"
                                          "\n"
                                          "Lambda functions are efficient whenever you want to create a function that \n"
                                          "will only contain simple expressions – that is, expressions that are usually a \n"
                                          "single line of a statement. They're also useful when you want to use the \n"
                                          "function once.", font=("Arial", 10))
        self.label3.pack(pady=10)
        self.email_label = tk.Label(self, text="Enter Your Email ID:")
        self.email_label.pack()
        self.email_entry = tk.Entry(self)
        self.email_entry.pack(pady=5)
        self.ne_button = tk.Button(self, text='Finish', command=self.ne, font=('arial', 9))
        self.ne_button.pack(pady=1.5)

    def ne(self):
        con = mysql.connector.connect(host='localhost', database='grointern', user='root', password='')
        if con.is_connected():
            Email = self.email_entry.get()
            if emailcheck(Email):
                qry = "update elearn SET pro='100%' where Email='{}'".format(Email)
                c1 = con.cursor()
                c1.execute(qry)
                con.commit()
                con.close
                self.master.switch_frame(student)
            else:
                self.label = tk.Label(self, text="Incorrect email", font=("Arial", 10))
                self.label.pack(pady=5)
        else:
            self.label = tk.Label(self, text="Server Error (MySQL is not connected)", font=("Arial", 10))
            self.label.pack(pady=5)
            con.close()


class c_ja(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.grid()
        self.label1 = tk.Label(self, text="GroIntern \n Live learning live growth", padx=235, pady=47, fg='black',bg='#FF99CC', font=('arial', 25))
        self.label1.pack(pady=1.5)
        self.label2 = tk.Label(self, text="Welcome To Core Java Course", font=("Arial", 20))
        self.label2.pack(pady=10)
        self.label3 = tk.Label(self, text="Core Java Topic \n "
                                          "1. What is Java? \n "
                                          "2. Multithreading in Java \n "
                                          "3. Inheritance in Java \n "
                                          "4. Java Networking ", font=("Arial", 10))
        self.label3.pack(pady=10)
        self.st_button = tk.Button(self, text='Start', command=self.sta, font=('arial', 9))
        self.st_button.pack(pady=1.5)
        self.back_button = tk.Button(self, text="Back", command=self.go_to_main_menu)
        self.back_button.pack(pady=8)

    def go_to_main_menu(self):
        self.master.switch_frame(cc)

    def sta(self):
        self.master.switch_frame(c_ja_fr1)

class c_ja_fr1(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.grid()
        self.label1 = tk.Label(self, text="GroIntern \n Live learning live growth", padx=235, pady=47, fg='black',bg='#FF99CC', font=('arial', 25))
        self.label1.pack(pady=1.5)
        self.label2 = tk.Label(self, text="What is Java?", font=("Arial", 20))
        self.label2.pack(pady=10)
        self.label3 = tk.Label(self, text="Java is a most popular, object-oriented, widely used programming language and platform that is \n"
                                          "utilized for Android development, web development, artificial intelligence, cloud applications, \n"
                                          "and much more. So, mastering this gives you great opportunities in bigger organizations.", font=("Arial", 10))
        self.label3.pack(pady=10)
        self.email_label = tk.Label(self, text="Enter Your Email ID:")
        self.email_label.pack()
        self.email_entry = tk.Entry(self)
        self.email_entry.pack(pady=5)
        self.ne_button = tk.Button(self, text='Next', command=self.ne, font=('arial', 9))
        self.ne_button.pack(pady=1.5)
        self.back_button = tk.Button(self, text="Back", command=self.go_to_main_menu)
        self.back_button.pack(pady=8)

    def ne(self):
        con = mysql.connector.connect(host='localhost', database='grointern', user='root', password='')
        if con.is_connected():
            Email = self.email_entry.get()
            if emailcheck(Email):
                qry = "update elearn SET pro='25%' where Email='{}'".format(Email)
                c1 = con.cursor()
                c1.execute(qry)
                con.commit()
                con.close
                self.master.switch_frame(c_ja_fr2)
            else:
                self.label = tk.Label(self, text="Incorrect email", font=("Arial", 10))
                self.label.pack(pady=5)
        else:
            self.label = tk.Label(self, text="Server Error (MySQL is not connected)", font=("Arial", 10))
            self.label.pack(pady=5)
            con.close()


    def go_to_main_menu(self):
        self.master.switch_frame(cc)

class c_ja_fr2(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.grid()
        self.label1 = tk.Label(self, text="GroIntern \n Live learning live growth", padx=235, pady=47, fg='black',bg='#FF99CC', font=('arial', 25))
        self.label1.pack(pady=1.5)
        self.label2 = tk.Label(self, text="Multithreading in Java", font=("Arial", 20))
        self.label2.pack(pady=10)
        self.label3 = tk.Label(self, text="Multithreading is a Java feature that allows concurrent execution of two or more \n"
                                          "parts of a program for maximum utilization of CPU. Each part of such program is \n"
                                          "called a thread. So, threads are light-weight processes within a process.\n"
                                          "Threads can be created by using two mechanisms : \n"
                                          "1. Extending the Thread class \n"
                                          "2. Implementing the Runnable Interface", font=("Arial", 10))
        self.label3.pack(pady=10)
        self.email_label = tk.Label(self, text="Enter Your Email ID:")
        self.email_label.pack()
        self.email_entry = tk.Entry(self)
        self.email_entry.pack(pady=5)
        self.ne_button = tk.Button(self, text='Next', command=self.ne, font=('arial', 9))
        self.ne_button.pack(pady=1.5)
        self.back_button = tk.Button(self, text="Back", command=self.go_to_main_menu)
        self.back_button.pack(pady=8)

    def ne(self):
        con = mysql.connector.connect(host='localhost', database='grointern', user='root', password='')
        if con.is_connected():
            Email = self.email_entry.get()
            if emailcheck(Email):
                qry = "update elearn SET pro='50%' where Email='{}'".format(Email)
                c1 = con.cursor()
                c1.execute(qry)
                con.commit()
                con.close
                self.master.switch_frame(a_ja_fr3)
            else:
                self.label = tk.Label(self, text="Incorrect email", font=("Arial", 10))
                self.label.pack(pady=5)
        else:
            self.label = tk.Label(self, text="Server Error (MySQL is not connected)", font=("Arial", 10))
            self.label.pack(pady=5)
            con.close()

    def go_to_main_menu(self):
        self.master.switch_frame(cc)

class c_ja_fr3(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.grid()
        self.label1 = tk.Label(self, text="GroIntern \n Live learning live growth", padx=235, pady=47, fg='black',bg='#FF99CC', font=('arial', 25))
        self.label1.pack(pady=1.5)
        self.label2 = tk.Label(self, text="Inheritance in Java", font=("Arial", 20))
        self.label2.pack(pady=10)
        self.label3 = tk.Label(self, text="Java, Inheritance is an important pillar of OOP(Object-Oriented Programming). It is \n"
                                          "the mechanism in Java by which one class is allowed to inherit the features(fields \n"
                                          "and methods) of another class. In Java, Inheritance means creating new classes \n"
                                          "based on existing ones. A class that inherits from another class can reuse the \n"
                                          "methods and fields of that class. In addition, you can add new fields and methods to \n"
                                          "your current class as well.  ", font=("Arial", 10))
        self.label3.pack(pady=10)
        self.email_label = tk.Label(self, text="Enter Your Email ID:")
        self.email_label.pack()
        self.email_entry = tk.Entry(self)
        self.email_entry.pack(pady=5)
        self.ne_button = tk.Button(self, text='Next', command=self.ne, font=('arial', 9))
        self.ne_button.pack(pady=1.5)
        self.back_button = tk.Button(self, text="Back", command=self.go_to_main_menu)
        self.back_button.pack(pady=8)

    def ne(self):
        con = mysql.connector.connect(host='localhost', database='grointern', user='root', password='')
        if con.is_connected():
            Email = self.email_entry.get()
            if emailcheck(Email):
                qry = "update elearn SET pro='75%' where Email='{}'".format(Email)
                c1 = con.cursor()
                c1.execute(qry)
                con.commit()
                con.close
                self.master.switch_frame(c_ja_fr4)
            else:
                self.label = tk.Label(self, text="Incorrect email", font=("Arial", 10))
                self.label.pack(pady=5)
        else:
            self.label = tk.Label(self, text="Server Error (MySQL is not connected)", font=("Arial", 10))
            self.label.pack(pady=5)
            con.close()

    def go_to_main_menu(self):
        self.master.switch_frame(cc)

class c_ja_fr4(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.grid()
        self.label1 = tk.Label(self, text="GroIntern \n Live learning live growth", padx=235, pady=47, fg='black',bg='#FF99CC', font=('arial', 25))
        self.label1.pack(pady=1.5)
        self.label2 = tk.Label(self, text="Java Networking", font=("Arial", 20))
        self.label2.pack(pady=10)
        self.label3 = tk.Label(self, text="In simple words, the term network programming or networking associates with \n"
                                          "writing programs that can be executed over various computer devices, in which all \n"
                                          "the devices are connected to each other to share resources using a network. Here, \n"
                                          "we are going to discuss Java Networking. \n"
                                          "1. What is Java Networking? \n"
                                          "2. Common Network Protocols \n"
                                          "3. Java Network Terminology \n"
                                          "4. Java Networking Classes \n"
                                          "5. Java Networking Interfaces \n"
                                          "6. Socket Programming \n"
                                          "7. Inet Address \n"
                                          "8. URL Class", font=("Arial", 10))
        self.label3.pack(pady=10)
        self.email_label = tk.Label(self, text="Enter Your Email ID:")
        self.email_label.pack()
        self.email_entry = tk.Entry(self)
        self.email_entry.pack(pady=5)
        self.ne_button = tk.Button(self, text='Finish', command=self.ne, font=('arial', 9))
        self.ne_button.pack(pady=1.5)

    def ne(self):
        con = mysql.connector.connect(host='localhost', database='grointern', user='root', password='')
        if con.is_connected():
            Email = self.email_entry.get()
            if emailcheck(Email):
                qry = "update elearn SET pro='100%' where Email='{}'".format(Email)
                c1 = con.cursor()
                c1.execute(qry)
                con.commit()
                con.close
                self.master.switch_frame(student)
            else:
                self.label = tk.Label(self, text="Incorrect email", font=("Arial", 10))
                self.label.pack(pady=5)
        else:
            self.label = tk.Label(self, text="Server Error (MySQL is not connected)", font=("Arial", 10))
            self.label.pack(pady=5)
            con.close()


class a_ja(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.grid()
        self.label1 = tk.Label(self, text="GroIntern \n Live learning live growth", padx=235, pady=47, fg='black',bg='#FF99CC', font=('arial', 25))
        self.label1.pack(pady=1.5)
        self.label2 = tk.Label(self, text="Welcome To Advance Java Course", font=("Arial", 20))
        self.label2.pack(pady=10)
        self.label3 = tk.Label(self, text="Advance Java Topic \n "
                                          "1. Java Enterprise Edition \n "
                                          "2. Concurrency \n "
                                          "3. Java Database Connectivity \n "
                                          "4. Java Persistence API", font=("Arial", 10))
        self.label3.pack(pady=10)
        self.st_button = tk.Button(self, text='Start', command=self.sta, font=('arial', 9))
        self.st_button.pack(pady=1.5)
        self.back_button = tk.Button(self, text="Back", command=self.go_to_main_menu)
        self.back_button.pack(pady=8)

    def go_to_main_menu(self):
        self.master.switch_frame(cc)

    def sta(self):
        self.master.switch_frame(a_ja_fr1)

class a_ja_fr1(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.grid()
        self.label1 = tk.Label(self, text="GroIntern \n Live learning live growth", padx=235, pady=47, fg='black',bg='#FF99CC', font=('arial', 25))
        self.label1.pack(pady=1.5)
        self.label2 = tk.Label(self, text="Java Enterprise Edition", font=("Arial", 20))
        self.label2.pack(pady=10)
        self.label3 = tk.Label(self, text="Java Enterprise Edition (Java EE), now known as Jakarta EE, it’s an remarkable \n"
                                          "component of Advanced Java programming. It gives Scalability for Big-League \n"
                                          "applications, that provides a smooth pattern to create applications that could grow \n"
                                          "seamlessly as your user base expands. Basically, it’s designed to help developers \n"
                                          "create powerful, scalable, and robust enterprise-level applications. So, let’s delve \n"
                                          "into what Java EE brings in the context of Advanced Java.", font=("Arial", 10))
        self.label3.pack(pady=10)
        self.email_label = tk.Label(self, text="Enter Your Email ID:")
        self.email_label.pack()
        self.email_entry = tk.Entry(self)
        self.email_entry.pack(pady=5)
        self.ne_button = tk.Button(self, text='Next', command=self.ne, font=('arial', 9))
        self.ne_button.pack(pady=1.5)
        self.back_button = tk.Button(self, text="Back", command=self.go_to_main_menu)
        self.back_button.pack(pady=8)

    def ne(self):
        con = mysql.connector.connect(host='localhost', database='grointern', user='root', password='')
        if con.is_connected():
            Email = self.email_entry.get()
            if emailcheck(Email):
                qry = "update elearn SET pro='25%' where Email='{}'".format(Email)
                c1 = con.cursor()
                c1.execute(qry)
                con.commit()
                con.close
                self.master.switch_frame(a_ja_fr2)
            else:
                self.label = tk.Label(self, text="Incorrect email", font=("Arial", 10))
                self.label.pack(pady=5)
        else:
            self.label = tk.Label(self, text="Server Error (MySQL is not connected)", font=("Arial", 10))
            self.label.pack(pady=5)
            con.close()

    def go_to_main_menu(self):
        self.master.switch_frame(cc)

class a_ja_fr2(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.grid()
        self.label1 = tk.Label(self, text="GroIntern \n Live learning live growth", padx=235, pady=47, fg='black',bg='#FF99CC', font=('arial', 25))
        self.label1.pack(pady=1.5)
        self.label2 = tk.Label(self, text="Concurrency", font=("Arial", 20))
        self.label2.pack(pady=10)
        self.label3 = tk.Label(self, text="Concurrency having the ability in Advanced Java to execute multiple tasks \n"
                                          "simultaneously, that runs independently and concurrently by allowing different \n"
                                          "programs. Concurrency plays an important role as it maximises the performance, \n"
                                          "enhances responsiveness, in simpler terms concurrency implements multiple tasks \n"
                                          "at once, it has the synchronisation that prevents the data corruption and race \n"
                                          "conditions, and deadlocks. Concurrency is vital in modern software development \n"
                                          "where Java provides thread-safe collections like ConcurrentMap and \n"
                                          "ConcurrentQueue that are accessed by multiple threads concurrently.", font=("Arial", 10))
        self.label3.pack(pady=10)
        self.email_label = tk.Label(self, text="Enter Your Email ID:")
        self.email_label.pack()
        self.email_entry = tk.Entry(self)
        self.email_entry.pack(pady=5)
        self.ne_button = tk.Button(self, text='Next', command=self.ne, font=('arial', 9))
        self.ne_button.pack(pady=1.5)
        self.back_button = tk.Button(self, text="Back", command=self.go_to_main_menu)
        self.back_button.pack(pady=8)

    def ne(self):
        con = mysql.connector.connect(host='localhost', database='grointern', user='root', password='')
        if con.is_connected():
            Email = self.email_entry.get()
            if emailcheck(Email):
                qry = "update elearn SET pro='50%' where Email='{}'".format(Email)
                c1 = con.cursor()
                c1.execute(qry)
                con.commit()
                con.close
                self.master.switch_frame(a_ja_fr3)
            else:
                self.label = tk.Label(self, text="Incorrect email", font=("Arial", 10))
                self.label.pack(pady=5)
        else:
            self.label = tk.Label(self, text="Server Error (MySQL is not connected)", font=("Arial", 10))
            self.label.pack(pady=5)
            con.close()

    def go_to_main_menu(self):
        self.master.switch_frame(cc)

class a_ja_fr3(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.grid()
        self.label1 = tk.Label(self, text="GroIntern \n Live learning live growth", padx=235, pady=47, fg='black',bg='#FF99CC', font=('arial', 25))
        self.label1.pack(pady=1.5)
        self.label2 = tk.Label(self, text="Java Database Connectivity", font=("Arial", 20))
        self.label2.pack(pady=10)
        self.label3 = tk.Label(self, text="JDBC stands for “Java Database Connectivity” which is a very essential component \n"
                                          "in Advanced Java for interacting with databases. JDBC connects with various \n"
                                          "relational databases that executes the queries, and manipulates the data with the \n"
                                          "help of Java APIs (Application Programming Interfaces). JDBC allows the Java \n"
                                          "program to interact with the databases to retrieve information, store the data, and \n"
                                          "update the data. In order to overcome the problems by using JDBC directly,Spring \n"
                                          "framework has provided one abstraction layer on top of existing JDBC technology", font=("Arial", 10))
        self.label3.pack(pady=10)
        self.email_label = tk.Label(self, text="Enter Your Email ID:")
        self.email_label.pack()
        self.email_entry = tk.Entry(self)
        self.email_entry.pack(pady=5)
        self.ne_button = tk.Button(self, text='Next', command=self.ne, font=('arial', 9))
        self.ne_button.pack(pady=1.5)
        self.back_button = tk.Button(self, text="Back", command=self.go_to_main_menu)
        self.back_button.pack(pady=8)

    def ne(self):
        con = mysql.connector.connect(host='localhost', database='grointern', user='root', password='')
        if con.is_connected():
            Email = self.email_entry.get()
            if emailcheck(Email):
                qry = "update elearn SET pro='75%' where Email='{}'".format(Email)
                c1 = con.cursor()
                c1.execute(qry)
                con.commit()
                con.close
                self.master.switch_frame(a_ja_fr4)
            else:
                self.label = tk.Label(self, text="Incorrect email", font=("Arial", 10))
                self.label.pack(pady=5)
        else:
            self.label = tk.Label(self, text="Server Error (MySQL is not connected)", font=("Arial", 10))
            self.label.pack(pady=5)
            con.close()

    def go_to_main_menu(self):
        self.master.switch_frame(cc)

class a_ja_fr4(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.grid()
        self.label1 = tk.Label(self, text="GroIntern \n Live learning live growth", padx=235, pady=47, fg='black',bg='#FF99CC', font=('arial', 25))
        self.label1.pack(pady=1.5)
        self.label2 = tk.Label(self, text="Java Persistence API", font=("Arial", 20))
        self.label2.pack(pady=10)
        self.label3 = tk.Label(self, text="Java Persistence API is a collection of classes and methods to persist or store the \n"
                                          "vast amount of data into a database. JPA is a specification to store or manage Java \n"
                                          "objects or classes into the databases, which use Object-Relational Mapping (ORM) \n"
                                          "as implementation internally to persist the database. JPA Persistence framework \n"
                                          "needs to follow: \n"
                                          "1. Spring Data JPA \n"
                                          "2. Spring Repository", font=("Arial", 10))
        self.label3.pack(pady=10)
        self.email_label = tk.Label(self, text="Enter Your Email ID:")
        self.email_label.pack()
        self.email_entry = tk.Entry(self)
        self.email_entry.pack(pady=5)
        self.ne_button = tk.Button(self, text='Finish', command=self.ne, font=('arial', 9))
        self.ne_button.pack(pady=1.5)


    def ne(self):
        con = mysql.connector.connect(host='localhost', database='grointern', user='root', password='')
        if con.is_connected():
            Email = self.email_entry.get()
            if emailcheck(Email):
                qry = "update elearn SET pro='100%' where Email='{}'".format(Email)
                c1 = con.cursor()
                c1.execute(qry)
                con.commit()
                con.close
                self.master.switch_frame(student)
            else:
                self.label = tk.Label(self, text="Incorrect email", font=("Arial", 10))
                self.label.pack(pady=5)
        else:
            self.label = tk.Label(self, text="Server Error (MySQL is not connected)", font=("Arial", 10))
            self.label.pack(pady=5)
            con.close()


class c_lan(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.grid()
        self.label1 = tk.Label(self, text="GroIntern \n Live learning live growth", padx=235, pady=47, fg='black',bg='#FF99CC', font=('arial', 25))
        self.label1.pack(pady=1.5)
        self.label2 = tk.Label(self, text="Welcome To C Language Course", font=("Arial", 20))
        self.label2.pack(pady=10)
        self.label3 = tk.Label(self, text="C Language Topic \n "
                                          "1. What is C? \n "
                                          "2. What is a Pointer in C? \n "
                                          "3. Basics of File Handling in C \n "
                                          "4. C Structures ", font=("Arial", 10))
        self.label3.pack(pady=10)
        self.st_button = tk.Button(self, text='Start', command=self.sta, font=('arial', 9))
        self.st_button.pack(pady=1.5)
        self.back_button = tk.Button(self, text="Back", command=self.go_to_main_menu)
        self.back_button.pack(pady=8)

    def go_to_main_menu(self):
        self.master.switch_frame(cc)

    def sta(self):
        self.master.switch_frame(c_lan_fr1)

class c_lan_fr1(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.grid()
        self.label1 = tk.Label(self, text="GroIntern \n Live learning live growth", padx=235, pady=47, fg='black',bg='#FF99CC', font=('arial', 25))
        self.label1.pack(pady=1.5)
        self.label2 = tk.Label(self, text="What is C?", font=("Arial", 20))
        self.label2.pack(pady=10)
        self.label3 = tk.Label(self, text="C is a general-purpose, procedural, high-level programming language used in the development \n"
                                          "of computer software and applications, system programming, games, web development, and \n"
                                          "more. C language was developed by Dennis M. Ritchie at the Bell Telephone Laboratories in \n"
                                          "1972. It is a powerful and flexible language which was first developed for the programming of \n"
                                          "the UNIX operating System. C is one of the most widely used programming language.", font=("Arial", 10))
        self.label3.pack(pady=10)
        self.email_label = tk.Label(self, text="Enter Your Email ID:")
        self.email_label.pack()
        self.email_entry = tk.Entry(self)
        self.email_entry.pack(pady=5)
        self.ne_button = tk.Button(self, text='Next', command=self.ne, font=('arial', 9))
        self.ne_button.pack(pady=1.5)

    def ne(self):
        con = mysql.connector.connect(host='localhost', database='grointern', user='root', password='')
        if con.is_connected():
            Email = self.email_entry.get()
            if emailcheck(Email):
                qry = "update elearn SET pro='25%' where Email='{}'".format(Email)
                c1 = con.cursor()
                c1.execute(qry)
                con.commit()
                con.close
                self.master.switch_frame(c_lan_fr2)
            else:
                self.label = tk.Label(self, text="Incorrect email", font=("Arial", 10))
                self.label.pack(pady=5)
        else:
            self.label = tk.Label(self, text="Server Error (MySQL is not connected)", font=("Arial", 10))
            self.label.pack(pady=5)
            con.close()

    def go_to_main_menu(self):
        self.master.switch_frame(cc)

class c_lan_fr2(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.grid()
        self.label1 = tk.Label(self, text="GroIntern \n Live learning live growth", padx=235, pady=47, fg='black',bg='#FF99CC', font=('arial', 25))
        self.label1.pack(pady=1.5)
        self.label2 = tk.Label(self, text="What is a Pointer in C?", font=("Arial", 20))
        self.label2.pack(pady=10)
        self.label3 = tk.Label(self, text="A pointer is defined as a derived data type that can store the address of other \n"
                                          "C variables or a memory location. We can access and manipulate the data \n"
                                          "stored in that memory location using pointers.", font=("Arial", 10))
        self.label3.pack(pady=10)
        self.email_label = tk.Label(self, text="Enter Your Email ID:")
        self.email_label.pack()
        self.email_entry = tk.Entry(self)
        self.email_entry.pack(pady=5)
        self.ne_button = tk.Button(self, text='Next', command=self.ne, font=('arial', 9))
        self.ne_button.pack(pady=1.5)

    def ne(self):
        con = mysql.connector.connect(host='localhost', database='grointern', user='root', password='')
        if con.is_connected():
            Email = self.email_entry.get()
            if emailcheck(Email):
                qry = "update elearn SET pro='50%' where Email='{}'".format(Email)
                c1 = con.cursor()
                c1.execute(qry)
                con.commit()
                con.close
                self.master.switch_frame(c_lan_fr3)
            else:
                self.label = tk.Label(self, text="Incorrect email", font=("Arial", 10))
                self.label.pack(pady=5)
        else:
            self.label = tk.Label(self, text="Server Error (MySQL is not connected)", font=("Arial", 10))
            self.label.pack(pady=5)
            con.close()

    def go_to_main_menu(self):
        self.master.switch_frame(cc)

class c_lan_fr3(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.grid()
        self.label1 = tk.Label(self, text="GroIntern \n Live learning live growth", padx=235, pady=47, fg='black',bg='#FF99CC', font=('arial', 25))
        self.label1.pack(pady=1.5)
        self.label2 = tk.Label(self, text="Basics of File Handling in C", font=("Arial", 20))
        self.label2.pack(pady=10)
        self.label3 = tk.Label(self, text="File handing in C is the process in which we create, open, read, write, and close \n"
                                          "operations on a file. C language provides different functions such as fopen(), \n"
                                          "fwrite(), fread(), fseek(), fprintf(), etc. to perform input, output, and many different C \n"
                                          "file operations in our program.", font=("Arial", 10))
        self.label3.pack(pady=10)
        self.email_label = tk.Label(self, text="Enter Your Email ID:")
        self.email_label.pack()
        self.email_entry = tk.Entry(self)
        self.email_entry.pack(pady=5)
        self.ne_button = tk.Button(self, text='Next', command=self.ne, font=('arial', 9))
        self.ne_button.pack(pady=1.5)

    def ne(self):
        con = mysql.connector.connect(host='localhost', database='grointern', user='root', password='')
        if con.is_connected():
            Email = self.email_entry.get()
            if emailcheck(Email):
                qry = "update elearn SET pro='75%' where Email='{}'".format(Email)
                c1 = con.cursor()
                c1.execute(qry)
                con.commit()
                con.close
                self.master.switch_frame(c_lan_fr4)
            else:
                self.label = tk.Label(self, text="Incorrect email", font=("Arial", 10))
                self.label.pack(pady=5)
        else:
            self.label = tk.Label(self, text="Server Error (MySQL is not connected)", font=("Arial", 10))
            self.label.pack(pady=5)
            con.close()

    def go_to_main_menu(self):
        self.master.switch_frame(cc)

class c_lan_fr4(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.grid()
        self.label1 = tk.Label(self, text="GroIntern \n Live learning live growth", padx=235, pady=47, fg='black',bg='#FF99CC', font=('arial', 25))
        self.label1.pack(pady=1.5)
        self.label2 = tk.Label(self, text="C Structures", font=("Arial", 20))
        self.label2.pack(pady=10)
        self.label3 = tk.Label(self, text="The structure in C is a user-defined data type that can be used to group items of \n"
                                          "possibly different types into a single type. The struct keyword is used to define the \n"
                                          "structure in the C programming language. The items in the structure are called its \n"
                                          "member and they can be of any valid data type.", font=("Arial", 10))
        self.label3.pack(pady=10)
        self.email_label = tk.Label(self, text="Enter Your Email ID:")
        self.email_label.pack()
        self.email_entry = tk.Entry(self)
        self.email_entry.pack(pady=5)
        self.ne_button = tk.Button(self, text='Finish', command=self.ne, font=('arial', 9))
        self.ne_button.pack(pady=1.5)

    def ne(self):
        con = mysql.connector.connect(host='localhost', database='grointern', user='root', password='')
        if con.is_connected():
            Email = self.email_entry.get()
            if emailcheck(Email):
                qry = "update elearn SET pro='100%' where Email='{}'".format(Email)
                c1 = con.cursor()
                c1.execute(qry)
                con.commit()
                con.close
                self.master.switch_frame(student)
            else:
                self.label = tk.Label(self, text="Incorrect email", font=("Arial", 10))
                self.label.pack(pady=5)
        else:
            self.label = tk.Label(self, text="Server Error (MySQL is not connected)", font=("Arial", 10))
            self.label.pack(pady=5)
            con.close()

class cpp_lan(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.grid()
        self.label1 = tk.Label(self, text="GroIntern \n Live learning live growth", padx=235, pady=47, fg='black',bg='#FF99CC', font=('arial', 25))
        self.label1.pack(pady=1.5)
        self.label2 = tk.Label(self, text="Welcome To C++ Language Course", font=("Arial", 20))
        self.label2.pack(pady=10)
        self.label3 = tk.Label(self, text="C++ Language Topic \n "
                                          "1. What is C++? \n "
                                          "2. C++ Polymorphism \n "
                                          "3. Operator Overloading in C++ \n "
                                          "4. Inheritance in C++ ", font=("Arial", 10))
        self.label3.pack(pady=10)
        self.st_button = tk.Button(self, text='Start', command=self.sta, font=('arial', 9))
        self.st_button.pack(pady=1.5)
        self.back_button = tk.Button(self, text="Back", command=self.go_to_main_menu)
        self.back_button.pack(pady=8)

    def go_to_main_menu(self):
        self.master.switch_frame(cc)

    def sta(self):
        self.master.switch_frame(cpp_lan_fr1)

class cpp_lan_fr1(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.grid()
        self.label1 = tk.Label(self, text="GroIntern \n Live learning live growth", padx=235, pady=47, fg='black',bg='#FF99CC', font=('arial', 25))
        self.label1.pack(pady=1.5)
        self.label2 = tk.Label(self, text="What is C++?", font=("Arial", 20))
        self.label2.pack(pady=10)
        self.label3 = tk.Label(self, text="C++ is a most popular cross-platform programming language which is used to create high-performance \n"
                                          "applications and software like OS, Games, E-commerce software, etc. It was developed \n"
                                          "by Bjarne Stroustrup, as an extension of C language. C++ give a high level of control over \n"
                                          "system resources and memory.", font=("Arial", 10))
        self.label3.pack(pady=10)
        self.email_label = tk.Label(self, text="Enter Your Email ID:")
        self.email_label.pack()
        self.email_entry = tk.Entry(self)
        self.email_entry.pack(pady=5)
        self.ne_button = tk.Button(self, text='Next', command=self.ne, font=('arial', 9))
        self.ne_button.pack(pady=1.5)
        self.back_button = tk.Button(self, text="Back", command=self.go_to_main_menu)
        self.back_button.pack(pady=8)

    def ne(self):
        con = mysql.connector.connect(host='localhost', database='grointern', user='root', password='')
        if con.is_connected():
            Email = self.email_entry.get()
            if emailcheck(Email):
                qry = "update elearn SET pro='25%' where Email='{}'".format(Email)
                c1 = con.cursor()
                c1.execute(qry)
                con.commit()
                con.close
                self.master.switch_frame(cpp_lan_fr2)
            else:
                self.label = tk.Label(self, text="Incorrect email", font=("Arial", 10))
                self.label.pack(pady=5)
        else:
            self.label = tk.Label(self, text="Server Error (MySQL is not connected)", font=("Arial", 10))
            self.label.pack(pady=5)
            con.close()

    def go_to_main_menu(self):
        self.master.switch_frame(cc)

class cpp_lan_fr2(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.grid()
        self.label1 = tk.Label(self, text="GroIntern \n Live learning live growth", padx=235, pady=47, fg='black',bg='#FF99CC', font=('arial', 25))
        self.label1.pack(pady=1.5)
        self.label2 = tk.Label(self, text="C++ Polymorphism", font=("Arial", 20))
        self.label2.pack(pady=10)
        self.label3 = tk.Label(self, text="The word “polymorphism” means having many forms. In simple words, we can \n"
                                          "define polymorphism as the ability of a message to be displayed in more than one \n"
                                          "form. A real-life example of polymorphism is a person who at the same time can \n"
                                          "have different characteristics. A man at the same time is a father, a husband, and an \n"
                                          "employee. So the same person exhibits different behavior in different situations. \n"
                                          "This is called polymorphism. Polymorphism is considered one of the important \n"
                                          "features of Object-Oriented Programming.", font=("Arial", 10))
        self.label3.pack(pady=10)
        self.email_label = tk.Label(self, text="Enter Your Email ID:")
        self.email_label.pack()
        self.email_entry = tk.Entry(self)
        self.email_entry.pack(pady=5)
        self.ne_button = tk.Button(self, text='Next', command=self.ne, font=('arial', 9))
        self.ne_button.pack(pady=1.5)
        self.back_button = tk.Button(self, text="Back", command=self.go_to_main_menu)
        self.back_button.pack(pady=8)

    def ne(self):
        con = mysql.connector.connect(host='localhost', database='grointern', user='root', password='')
        if con.is_connected():
            Email = self.email_entry.get()
            if emailcheck(Email):
                qry = "update elearn SET pro='50%' where Email='{}'".format(Email)
                c1 = con.cursor()
                c1.execute(qry)
                con.commit()
                con.close
                self.master.switch_frame(cpp_lan_fr3)
            else:
                self.label = tk.Label(self, text="Incorrect email", font=("Arial", 10))
                self.label.pack(pady=5)
        else:
            self.label = tk.Label(self, text="Server Error (MySQL is not connected)", font=("Arial", 10))
            self.label.pack(pady=5)
            con.close()

    def go_to_main_menu(self):
        self.master.switch_frame(cc)

class cpp_lan_fr3(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.grid()
        self.label1 = tk.Label(self, text="GroIntern \n Live learning live growth", padx=235, pady=47, fg='black',bg='#FF99CC', font=('arial', 25))
        self.label1.pack(pady=1.5)
        self.label2 = tk.Label(self, text="Operator Overloading in C++", font=("Arial", 20))
        self.label2.pack(pady=10)
        self.label3 = tk.Label(self, text="In C++, we can make operators work for user-defined classes. This means C++ has \n"
                                          "the ability to provide the operators with a special meaning for a data type, this \n"
                                          "ability is known as operator overloading. For example, we can overload an operator \n"
                                          "‘+’ in a class like String so that we can concatenate two strings by just using +. \n"
                                          "Other example classes where arithmetic operators may be overloaded are Complex \n"
                                          "Numbers, Fractional Numbers, Big integers, etc.", font=("Arial", 10))
        self.label3.pack(pady=10)
        self.email_label = tk.Label(self, text="Enter Your Email ID:")
        self.email_label.pack()
        self.email_entry = tk.Entry(self)
        self.email_entry.pack(pady=5)
        self.ne_button = tk.Button(self, text='Next', command=self.ne, font=('arial', 9))
        self.ne_button.pack(pady=1.5)
        self.back_button = tk.Button(self, text="Back", command=self.go_to_main_menu)
        self.back_button.pack(pady=8)

    def ne(self):
        con = mysql.connector.connect(host='localhost', database='grointern', user='root', password='')
        if con.is_connected():
            Email = self.email_entry.get()
            if emailcheck(Email):
                qry = "update elearn SET pro='75%' where Email='{}'".format(Email)
                c1 = con.cursor()
                c1.execute(qry)
                con.commit()
                con.close
                self.master.switch_frame(cpp_lan_fr4)
            else:
                self.label = tk.Label(self, text="Incorrect email", font=("Arial", 10))
                self.label.pack(pady=5)
        else:
            self.label = tk.Label(self, text="Server Error (MySQL is not connected)", font=("Arial", 10))
            self.label.pack(pady=5)
            con.close()

    def go_to_main_menu(self):
        self.master.switch_frame(cc)

class cpp_lan_fr4(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.grid()
        self.label1 = tk.Label(self, text="GroIntern \n Live learning live growth", padx=235, pady=47, fg='black',bg='#FF99CC', font=('arial', 25))
        self.label1.pack(pady=1.5)
        self.label2 = tk.Label(self, text="Inheritance in C++", font=("Arial", 20))
        self.label2.pack(pady=10)
        self.label3 = tk.Label(self, text="Inheritance is a feature or a process in which, new classes are created from the \n"
                                          "existing classes. The new class created is called “derived class” or “child class” and \n"
                                          "the existing class is known as the “base class” or “parent class”. The derived class \n"
                                          "now is said to be inherited from the base class.", font=("Arial", 10))
        self.label3.pack(pady=10)
        self.email_label = tk.Label(self, text="Enter Your Email ID:")
        self.email_label.pack()
        self.email_entry = tk.Entry(self)
        self.email_entry.pack(pady=5)
        self.ne_button = tk.Button(self, text='Finish', command=self.ne, font=('arial', 9))
        self.ne_button.pack(pady=1.5)

    def ne(self):
        con = mysql.connector.connect(host='localhost', database='grointern', user='root', password='')
        if con.is_connected():
            Email = self.email_entry.get()
            if emailcheck(Email):
                qry = "update elearn SET pro='100%' where Email='{}'".format(Email)
                c1 = con.cursor()
                c1.execute(qry)
                con.commit()
                con.close
                self.master.switch_frame(student)
            else:
                self.label = tk.Label(self, text="Incorrect email", font=("Arial", 10))
                self.label.pack(pady=5)
        else:
            self.label = tk.Label(self, text="Server Error (MySQL is not connected)", font=("Arial", 10))
            self.label.pack(pady=5)
            con.close()

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("E-learning Platform.")
        self.geometry("670x700")
        self.frames = {}
        for F in (MainMenu,Sign_in,Log_in,forgetpass,cur,student,Show_de,Delete,Progress,cc,Py,py_fr1,py_fr2,py_fr3,py_fr4,Py_adv,py_ad_fr1,py_ad_fr2,py_ad_fr3,py_ad_fr4,c_ja,c_ja_fr1,c_ja_fr2,c_ja_fr3,c_ja_fr4,a_ja,a_ja_fr1,a_ja_fr2,a_ja_fr3,a_ja_fr4,c_lan,c_lan_fr1,c_lan_fr2,c_lan_fr3,c_lan_fr4,cpp_lan,cpp_lan_fr1,cpp_lan_fr2,cpp_lan_fr3,cpp_lan_fr4):
            frame = F(self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        self.switch_frame(MainMenu)

    def switch_frame(self, frame_class):
        frame = self.frames[frame_class]
        frame.tkraise()

if __name__ == "__main__":
    app = App()
    app.mainloop()