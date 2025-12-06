from tkinter import*
from tkinter import ttk
import mysql.connector
from tkinter import messagebox
import tkinter
import datetime


class LibraryManagementSystem:
    def __init__(self,root):
        self.root=root
        self.root.title("LIBRARY MANAGEMENT SYSTEM")

        # ==============================variable==========================================

        self.member_var = StringVar()
        self.prn_var = StringVar()
        self.id_var = StringVar()
        self.firstname_var = StringVar()
        self.lastname_var = StringVar()
        self.address_var = StringVar()
        self.postcode_var = StringVar()
        self.phone_var = StringVar()
        self.bookid_var = StringVar()
        self.booktitle_var = StringVar()
        self.authorname_var = StringVar()
        self.dateborrowed_var = StringVar()
        self.datedue_var = StringVar()
        self.daysonbook_var = StringVar()
        self.latereturnfine_var = StringVar()
        self.actualprice_var = StringVar()

        lbltitle=Label(self.root,text="LIBRARY MANAGEMENT SYSTEM",bg="powder blue",fg="green",bd=20,relief=RIDGE,font=("times in roman",50,"bold"),padx=2,pady=6)
        lbltitle.pack(side=TOP,fill=X)


        frame=Frame(self.root,bd=12,relief=RIDGE,padx=20,bg="powder blue")
        frame.place(x=0,y=130,width=1530,height=400)

        #======================================DataFrameLeft============================================
        DataFrameLeft=LabelFrame(frame,text="LIBRARY MEMBERSHIP INFORMATION",bg="powder blue",fg="green",bd=12,relief=RIDGE,font=("times in roman",12,"bold"))
        DataFrameLeft.place(x=0,y=5,width=900,height=350)

        lblMember=Label(DataFrameLeft,bg="powder blue",text="Member Type",font=("times in roman",12,"bold"),textvariable=self.member_var,padx=2,pady=6)
        lblMember.grid(row=0,column=0,sticky=W)

        comMember=ttk.Combobox(DataFrameLeft,font=("times in roman",12,"bold"),width=27,state="readonly")
        comMember["value"]=("Admin staf","Student","Lecturer")
        comMember.grid(row=0,column=1)


        lblPRN_No=Label(DataFrameLeft,bg="powder blue",text="PRN_No",font=("times in roman",12,"bold"),textvariable=self.prn_var,padx=2,pady=6)
        lblPRN_No.grid(row=1,column=0,sticky=W)
        txtPRN_No=Entry(DataFrameLeft,font=("times in roman",12,"bold"),width=29)
        txtPRN_No.grid(row=1,column=1)


        lblTitle=Label(DataFrameLeft,bg="powder blue",text="ID No",font=("times in roman",12,"bold"),textvariable=self.id_var,padx=2,pady=6)
        lblTitle.grid(row=2,column=0,sticky=W)
        txtTitle=Entry(DataFrameLeft,font=("times in roman",12,"bold"),width=29)
        txtTitle.grid(row=2,column=1)

        lblFirstName=Label(DataFrameLeft,bg="powder blue",text="First Name",font=("times in roman",12,"bold"),textvariable=self.firstname_var,padx=2,pady=6)
        lblFirstName.grid(row=3,column=0,sticky=W)
        txtFirstName=Entry(DataFrameLeft,font=("times in roman",12,"bold"),width=29)
        txtFirstName.grid(row=3,column=1)

        lblLastName=Label(DataFrameLeft,bg="powder blue",text="Last Name",font=("times in roman",12,"bold"),textvariable=self.lastname_var,padx=2,pady=6)
        lblLastName.grid(row=4,column=0,sticky=W)
        txtLastName=Entry(DataFrameLeft,font=("times in roman",12,"bold"),width=29)
        txtLastName.grid(row=4,column=1)

        lblAddress=Label(DataFrameLeft,bg="powder blue",text="Address",font=("times in roman",12,"bold"),textvariable=self.address_var,padx=2,pady=6)
        lblAddress.grid(row=5,column=0,sticky=W)
        txtAddress=Entry(DataFrameLeft,font=("times in roman",12,"bold"),width=29)
        txtAddress.grid(row=5,column=1)

        lblPostCode=Label(DataFrameLeft,bg="powder blue",text="Post Code",font=("times in roman",12,"bold"),textvariable=self.postcode_var,padx=2,pady=6)
        lblPostCode.grid(row=6,column=0,sticky=W)
        txtPostCode=Entry(DataFrameLeft,font=("times in roman",12,"bold"),width=29)
        txtPostCode.grid(row=6,column=1)

        lblPhone_No=Label(DataFrameLeft,bg="powder blue",text="Phone No",font=("times in roman",12,"bold"),textvariable=self.phone_var,padx=2,pady=6)
        lblPhone_No.grid(row=7,column=0,sticky=W)
        txtPhone_No=Entry(DataFrameLeft,font=("times in roman",12,"bold"),width=29)
        txtPhone_No.grid(row=7,column=1)

        lblBookId=Label(DataFrameLeft,bg="powder blue",text="Book Id",font=("times in roman",12,"bold"),textvariable=self.bookid_var,padx=2,pady=6)
        lblBookId.grid(row=0,column=2,sticky=W)
        txtBookId=Entry(DataFrameLeft,font=("times in roman",12,"bold"),width=29)
        txtBookId.grid(row=0,column=3)

        lblBookTitle=Label(DataFrameLeft,bg="powder blue",text="Book Title",font=("times in roman",12,"bold"),textvariable=self.booktitle_var,padx=2,pady=6)
        lblBookTitle.grid(row=1,column=2,sticky=W)
        txtBookTitle=Entry(DataFrameLeft,font=("times in roman",12,"bold"),width=29)
        txtBookTitle.grid(row=1,column=3)


        lblAuthorName=Label(DataFrameLeft,bg="powder blue",text="Author Name",font=("times in roman",12,"bold"),textvariable=self.authorname_var,padx=2,pady=6)
        lblAuthorName.grid(row=2,column=2,sticky=W)
        txtAuthorName=Entry(DataFrameLeft,font=("times in roman",12,"bold"),width=29)
        txtAuthorName.grid(row=2,column=3)


        lblDateBorrowed=Label(DataFrameLeft,bg="powder blue",text="Date Borrowed",font=("times in roman",12,"bold"),textvariable=self.dateborrowed_var,padx=2,pady=6)
        lblDateBorrowed.grid(row=3,column=2,sticky=W)
        txtDateBorrowed=Entry(DataFrameLeft,font=("times in roman",12,"bold"),width=29)
        txtDateBorrowed.grid(row=3,column=3)

        lblDateDue=Label(DataFrameLeft,bg="powder blue",text="Date Due",font=("times in roman",12,"bold"),textvariable=self.datedue_var,padx=2,pady=6)
        lblDateDue.grid(row=4,column=2,sticky=W)
        txtDateDue=Entry(DataFrameLeft,font=("times in roman",12,"bold"),width=29)
        txtDateDue.grid(row=4,column=3)

        lblDaysOnBook=Label(DataFrameLeft,bg="powder blue",text="Days On Book",font=("times in roman",12,"bold"),textvariable=self.daysonbook_var,padx=2,pady=6)
        lblDaysOnBook.grid(row=5,column=2,sticky=W)
        txtDaysOnBook=Entry(DataFrameLeft,font=("times in roman",12,"bold"),width=29)
        txtDaysOnBook.grid(row=5,column=3)

        lblLateReturnFine=Label(DataFrameLeft,bg="powder blue",text="Late Return Fine",font=("times in roman",12,"bold"),textvariable=self.latereturnfine_var,padx=2,pady=6)
        lblLateReturnFine.grid(row=6,column=2,sticky=W)
        txtLateReturnFine=Entry(DataFrameLeft,font=("times in roman",12,"bold"),width=29)
        txtLateReturnFine.grid(row=6,column=3)

        lblActualPrice=Label(DataFrameLeft,bg="powder blue",text="Actual Price",font=("times in roman",12,"bold"),textvariable=self.actualprice_var,padx=2,pady=6)
        lblActualPrice.grid(row=7,column=2,sticky=W)
        txtActualPrice=Entry(DataFrameLeft,font=("times in roman",12,"bold"),width=29)
        txtActualPrice.grid(row=7,column=3)


        #====================================DateFrameRight============================================

        DataFrameRight=LabelFrame(frame,text="BOOK DETAILS",bg="powder blue",fg="green",bd=12,relief=RIDGE,font=("times in roman",12,"bold"))
        DataFrameRight.place(x=910,y=5,width=540,height=350)

        self.txtBox=Text(DataFrameRight,font=("times in roman",12,"bold"),width=32,height=16,padx=2,pady=6)
        self.txtBox.grid(row=0,column=2)

        listScrollbar=Scrollbar(DataFrameRight)
        listScrollbar.grid(row=0,column=1,sticky="ns")

        ListBook=['Automate the Boring Stuff with Python','Python Crash Course','Learning Python','Fluent Python','Python for Data Analysis','Effective Python','Python Cookbook','Test-Driven Development with Python',' Python Machine Learning',' Python Data Science Handbook']


        def SelectBook(event=""):
            value=str(listBox.get(listBox.curselection))
            x=value
            if (x=="Automate the Boring Stuff with Python"):
                self.bookid_var.set("BKID4545")
                self.booktitle_var.set("python")
                self.authorname_var("Al Sweigart")
                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs.45")
                self.actualprice_var.set("Rs.2000")

            elif (x=="Python Crash Course"):
                self.bookid_var.set("BKID1234")
                self.booktitle_var.set("python")
                self.authorname_var("Eric Matthes")
                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs.50")
                self.actualprice_var.set("Rs.1500")

            elif  (x=="Learning Python"):
                self.bookid_var.set("BKID2964")
                self.booktitle_var.set("python")
                self.authorname_var("Mark Lutz")
                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs.50")
                self.actualprice_var.set("Rs.3500")

            elif  (x=="Fluent Python"):
                self.bookid_var.set("BKID3792")
                self.booktitle_var.set("python")
                self.authorname_var("Luciano Ramalho")
                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs.50")
                self.actualprice_var.set("Rs.4000")

            elif  (x=="Python for Data Analysis"):
                self.bookid_var.set("BKID5389")
                self.booktitle_var.set("python")
                self.authorname_var(" Wes McKinney")
                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs.50")
                self.actualprice_var.set("Rs.4500")

            elif  (x=="Effective Python"):
                self.bookid_var.set("BKID2681")
                self.booktitle_var.set("python")
                self.authorname_var("Brett Slatkin")
                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs.50")
                self.actualprice_var.set("Rs.4000")

            elif  (x=="Python Cookbook"):
                self.bookid_var.set("BKID1744")
                self.booktitle_var.set("python")
                self.authorname_var("David Beazley and Brian K. Jones")
                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs.50")
                self.actualprice_var.set("Rs.2500")

            elif  (x=="Test-Driven Development with Python"):
                self.bookid_var.set("BKID6542")
                self.booktitle_var.set("python")
                self.authorname_var("Harry J.W. Percival")
                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs.50")
                self.actualprice_var.set("Rs.4500")

            elif  (x=="Python Machine Learning"):
                self.bookid_var.set("BKID5643")
                self.booktitle_var.set("python")
                self.authorname_var("Sebastian Raschka")
                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs.50")
                self.actualprice_var.set("Rs.4500")

            elif  (x=="Python Data Science Handbook"):
                self.bookid_var.set("BKID7865")
                self.booktitle_var.set("python")
                self.authorname_var("Jake VanderPlas")
                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs.50")
                self.actualprice_var.set("Rs.3500")

        listBox=Listbox(DataFrameRight,font=("times in roman",12,"bold"),width=20,height=16)
        listBox.bind("<<ListboxSelect>>",SelectBook)
        listBox.grid(row=0,column=0,padx=4)
        listScrollbar.config(command=listBox.yview)

        for item in ListBook:
            listBox.insert(END,item)


        #======================================Buttons Frame=============================================
        Framebutton=Frame(self.root,bd=12,relief=RIDGE,padx=20,bg="powder blue")
        Framebutton.place(x=0,y=530,width=1530,height=70)

        btnAddData=Button(Framebutton,command=self.add_data,text="Add Data",font=("times in roman",12,"bold"),width=23,bg="blue",fg="white")
        btnAddData.grid(row=0,column=0)

        btnAddData=Button(Framebutton,command=self.showData,text="Show Data",font=("times in roman",12,"bold"),width=23,bg="blue",fg="white")
        btnAddData.grid(row=0,column=1)

        btnAddData=Button(Framebutton,command=self.update,text="Update",font=("times in roman",12,"bold"),width=23,bg="blue",fg="white")
        btnAddData.grid(row=0,column=2)

        btnAddData=Button(Framebutton,command=self.delete,text="Delete",font=("times in roman",12,"bold"),width=23,bg="blue",fg="white")
        btnAddData.grid(row=0,column=3)

        btnAddData=Button(Framebutton,command=self.reset,text="Reset",font=("times in roman",12,"bold"),width=23,bg="blue",fg="white")
        btnAddData.grid(row=0,column=4)

        btnAddData=Button(Framebutton,command=self.iExit,text="Exit",font=("times in roman",12,"bold"),width=23,bg="blue",fg="white")
        btnAddData.grid(row=0,column=5)








        #======================================Information Frame=============================================
        FrameDetails=Frame(self.root,bd=12,relief=RIDGE,padx=20,bg="powder blue")
        FrameDetails.place(x=0,y=600,width=1530,height=195)


        Table_frame=Frame(FrameDetails,bd=6,relief=RIDGE,bg="powder blue")
        Table_frame.place(x=0,y=2,width=1460,height=190)

        xscroll=ttk.Scrollbar(Table_frame,orient=HORIZONTAL)
        yscroll=ttk.Scrollbar(Table_frame,orient=VERTICAL)


        self.library_table=ttk.Treeview(Table_frame,column=("membertype","prnno","title","firstname","lastname","address","postid","phoneno","bookid","booktitle","authorname","dateborrowed","datedue","days","latereturnfine","finalprice"),xscrollcommand=xscroll.set,yscrollcommand=yscroll.set)
        xscroll.pack(side=BOTTOM,fill=X)
        yscroll.pack(side=RIGHT,fill=Y)

        xscroll.config(command=self.library_table.xview)
        yscroll.config(command=self.library_table.yview)

        self.library_table.heading("membertype",text="Member Type")
        self.library_table.heading("prnno",text="PRN No")
        self.library_table.heading("title",text="Title")
        self.library_table.heading("firstname",text="First Name")
        self.library_table.heading("lastname",text="Last Name")
        self.library_table.heading("address",text="Address")
        self.library_table.heading("postid",text="Post Id")
        self.library_table.heading("phoneno",text="Phone No")
        self.library_table.heading("bookid",text="Book Id")
        self.library_table.heading("booktitle",text="Book Title")
        self.library_table.heading("authorname",text="Author Name")
        self.library_table.heading("dateborrowed",text="Date of Borrowed")
        self.library_table.heading("datedue",text="Date Due")
        self.library_table.heading("days",text="Days on Book")
        self.library_table.heading("latereturnfine",text="Late Return Fine")
        self.library_table.heading("finalprice",text="Final Price")

        self.library_table["show"]="headings"
        self.library_table.pack(fill=BOTH,expand=1)


        self.library_table.column("membertype",width=100)
        self.library_table.column("prnno",width=100)
        self.library_table.column("title",width=100)
        self.library_table.column("firstname",width=100)
        self.library_table.column("lastname",width=100)
        self.library_table.column("address",width=100)
        self.library_table.column("postid",width=100)
        self.library_table.column("phoneno",width=100)
        self.library_table.column("bookid",width=100)
        self.library_table.column("booktitle",width=100)
        self.library_table.column("authorname",width=100)
        self.library_table.column("dateborrowed",width=100)
        self.library_table.column("datedue",width=100)
        self.library_table.column("days",width=100)
        self.library_table.column("latereturnfine",width=100)
        self.library_table.column("finalprice",width=100)

        self.fatch_data()
        self.library_table.bind("<<ButtonRelease-1>>",self.get_cursor)

    def add_data(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="Nushika@10", database="mydata")
        my_cursor = conn.cursor()
        my_cursor.execute("insert into library values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (
            self.member_var.get(),
            self.prn_var.get(),
            self.id_var.get(),
            self.firstname_var.get(),
            self.lastname_var.get(),
            self.address_var.get(),
            self.postcode_var.get(),
            self.phone_var.get(),
            self.bookid_var.get(),
            self.booktitle_var.get(),
            self.authorname_var.get(),
            self.dateborrowed_var.get(),
            self.datedue_var.get(),
            self.daysonbook_var.get(),
            self.latereturnfine_var.get(),
            self.actualprice_var.get()
        ))
        conn.commit()
        self.fatch_data()
        conn.close()

        messagebox.showinfo("success", "Member has inserted successfully")

    def update(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="Nushika@10", database="mydata")
        my_cursor = conn.cursor()
        my_cursor.execute("update library set Member=%s,Id=%s,FirstName=%s,LastName=%s,Address=%s,Postid=%s,Phone=%s,Bookid=%s,BookTitle=%s,AuthorName=%s,DateBorrowed=%s,DateDue=%s,DaysOnBook=%s,LateReturnfine=%s,ActualPrice=%s where PRN_No=%s",(
            self.member_var.get(),
            self.prn_var.get(),
            self.id_var.get(),
            self.firstname_var.get(),
            self.lastname_var.get(),
            self.address_var.get(),
            self.postcode_var.get(),
            self.phone_var.get(),
            self.bookid_var.get(),
            self.booktitle_var.get(),
            self.authorname_var.get(),
            self.dateborrowed_var.get(),
            self.datedue_var.get(),
            self.daysonbook_var.get(),
            self.latereturnfine_var.get(),
            self.actualprice_var.get(),
            self.prn_var.get()

        ))
        conn.commit()
        self.fatch_data()
        self.reset()
        conn.close()

        messagebox.showinfo("Success","Member has been updated")



    def fatch_data(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="Nushika@10", database="mydata")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from library")
        rows=my_cursor.fetchall()

        if len(rows)!=0:
            self.library_table.delete(*self.library_table.get_children())
            for i in rows:
                self.library_table.insert("",END,values=i)
            conn.commit()
            conn.close()

    def get_cursor(self,events=""):
        cursor_row=self.library_table.focus()
        content=self.library_table.item(cursor_row)
        row=content['values']

        self.member_var.set(row[0]),
        self.prn_var.set(row[1]),
        self.id_var.set(row[2]),
        self.firstname_var.set(row[3]),
        self.lastname_var.set(row[4]),
        self.address_var.set(row[5]),
        self.postcode_var.set(row[6]),
        self.bookid_var.set(row[7]),
        self.booktitle_var.set(row[8]),
        self.authorname_var.set(row[9]),
        self.dateborrowed_var.set(row[10]),
        self.datedue_var.set(row[11]),
        self.daysonbook_var.set(row[12]),
        self.latereturnfine_var.set(row[13]),
        self.actualprice_var.set(row[14]),

    def showData(self):
        self.txtBox.insert(END,"Member Type:\t\t"+self.member_var.get()+"\n")
        self.txtBox.insert(END, "PRN no:\t\t" + self.prn_var.get() + "\n")
        self.txtBox.insert(END, "ID no:\t\t" + self.id_var.get() + "\n")
        self.txtBox.insert(END, "FirstName\t\t" + self.firstname_var.get() + "\n")
        self.txtBox.insert(END, "LastName\t\t" + self.lastname_var.get() + "\n")
        self.txtBox.insert(END, "Address\t\t" + self.address_var.get() + "\n")
        self.txtBox.insert(END, "PostCode\t\t" + self.postcode_var.get() + "\n")
        self.txtBox.insert(END, "BookId\t\t" + self.bookid_var.get() + "\n")
        self.txtBox.insert(END, "BookTitle\t\t" + self.booktitle_var.get() + "\n")
        self.txtBox.insert(END, "AuthorName\t\t" + self.authorname_var.get() + "\n")
        self.txtBox.insert(END, "DateBorrowed\t\t" + self.dateborrowed_var.get() + "\n")
        self.txtBox.insert(END, "DateDue\t\t" + self.datedue_var.get() + "\n")
        self.txtBox.insert(END, "DaysOnBook\t\t" + self.daysonbook_var.get() + "\n")
        self.txtBox.insert(END, "LateReturnFine\t\t" + self.latereturnfine_var.get() + "\n")
        self.txtBox.insert(END, "ActualPrice\t\t" + self.actualprice_var.get() + "\n")

    def reset(self):
        self.member_var.set(""),
        self.prn_var.set(""),
        self.id_var.set(""),
        self.firstname_var.set(""),
        self.lastname_var.set(""),
        self.address_var.set(""),
        self.postcode_var.set(""),
        self.bookid_var.set(""),
        self.booktitle_var.set(""),
        self.authorname_var.set(""),
        self.dateborrowed_var.set(""),
        self.datedue_var.set(""),
        self.daysonbook_var.set(""),
        self.latereturnfine_var.set(""),
        self.actualprice_var.set("")


    def iExit(self):
        iExit=tkinter.messagebox.askyesno("Library Management System","Do you want to Exit")
        if iExit>0:
            self.root.destroy()
            return

    def delete(self):
        if self.prn_var.get()==""or self.id_var.get()=="":
            messagebox.showerror("Error","First select the member")
        else:
            conn = mysql.connector.connect(host="localhost", username="root", password="Nushika@10", database="mydata")
            my_cursor = conn.cursor()
            query="delete from library where PRN_NO=%s"
            value=(self.prn_var.get(),)
            my_cursor.execute(query,value)

            conn.commit()
            self.fatch_data()
            self.reset()
            conn.close()

            messagebox.showinfo("success","Member has been deleted")








if __name__=="__main__":
    root=Tk()
    obj=LibraryManagementSystem(root)
    root.mainloop()