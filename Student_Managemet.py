from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import pymysql 

class student:
     #---------------- انشاء نافذه البرنامج -------------------
     def __init__(self,root):
          self.root = root
          self.root.geometry("1250x635+5+5")
          self.root.title("Registration")
          self.root.configure(background="silver")
          self.root.resizable(False,False)
          title_1 = Label(self.root,
          text="[نظام تسجيل الطلاب]",
          bg="#1AAECB",
          font =("monospace",14),
          fg="white"

          ) 
          title_1.pack(fill=X)
          #--------------variable----------------
          self.ID_var = StringVar()
          self.Name_var = StringVar()
          self.Email_var = StringVar()
          self.Phone_var = StringVar()
          self.Certification_var = StringVar()
          self.Gender_var = StringVar()
          self.Address_var = StringVar()
          self.Delete_var = StringVar()
          self.write_Var = StringVar()
          self.se_by = StringVar()
          self.se_var = StringVar()
          # ------------- ادوات التحكم بالبرنامج----------------------
          Manage_Frame = Frame(self.root ,bg="white")
          Manage_Frame.place(x=1034 ,y=30,width= 210,height= 370)
          lbl_ID = Label(Manage_Frame ,text = "ID",bg="white")
          lbl_ID.pack()
          ID_entry = Entry(Manage_Frame,textvariable=self.ID_var,bd='2',justify="center")
          ID_entry.pack()
          lbl_name = Label(Manage_Frame,text="Name",bg= "white")
          lbl_name.pack()
          Name_entry = Entry(Manage_Frame,textvariable=self.Name_var,bd='2',justify= "center")
          Name_entry.pack()
          lbl_email = Label(Manage_Frame,text ="Phone",bg= "white")
          lbl_email.pack()
          Email_entry = Entry(Manage_Frame,textvariable=self.Email_var,bd= '2',justify= "center")
          Email_entry.pack()
          lbl_phone = Label(Manage_Frame,text="Email ",bg= "white")
          lbl_phone.pack()
          Phone_entry = Entry(Manage_Frame,textvariable=self.Phone_var,bd= '2',justify= "center")
          Phone_entry.pack()
          lbl_certification = Label(Manage_Frame,text = "Certification",bg= "white")
          lbl_certification.pack()
          Certification_entery = Entry(Manage_Frame,textvariable=self.Certification_var,bd='2',justify="center")
          Certification_entery.pack()
          lbl_gender = Label(Manage_Frame,text="Gender",bg= "white" )
          lbl_gender.pack()
          compo_gender =ttk.Combobox(Manage_Frame,textvariable=self.Gender_var)
          compo_gender["value"]=("Male","Female")
          compo_gender.pack()
          lbl_address = Label(Manage_Frame,text= "Address",bg= "white")
          lbl_address.pack()
          Address_entry = Entry(Manage_Frame,textvariable=self.Address_var,bd='2',justify= "center")
          Address_entry.pack()
          lbl_delete = Label(Manage_Frame,text= "Delete_Student",fg='red',bg="white" )
          lbl_delete.pack()
          Delete_entry = Entry(Manage_Frame,textvariable=self.Delete_var,bd ='2',justify= "center")
          Delete_entry.pack()

          # ---------- buttons ---------------
          Button_Frame = Frame(self.root,bg="white")
          Button_Frame.place(x=1034 ,y=403 ,width=210,height=229)

          title_2 = Label(Button_Frame,text= "لوحة التحكم",font=("Deco",14),fg="white",bg="#2980B9")
          title_2.pack(fill=X)

          ADD_button = Button (Button_Frame,text="Add_Student" ,bg="#85929E",fg="white",command=self.add_student )
          ADD_button.place(x=45,y=35,width=120 ,height=33)

          Delete_button  = Button (Button_Frame,text="Delete_Student" ,bg="#85929E",fg="white",command=self.delete_student )
          Delete_button.place(x=45,y=69,width=120 ,height=33)

          update_button  = Button (Button_Frame,text="Update_Info_Student" ,bg="#85929E",fg="white",command=self.update )
          update_button.place(x=45,y=103,width=120 ,height=33)

          Clear_button  = Button (Button_Frame,text="Delete_Items" ,bg="#85929E",fg="white",command=self.clear)
          Clear_button.place(x=45,y=137,width=120 ,height=33)

          About_button = Button (Button_Frame,text="Who are we?" ,bg="#85929E" ,fg="white",command=self.about)
          About_button.place(x=45,y=171,width=120 ,height=33)

          Exit_button  = Button (Button_Frame,text="Close_Program" ,bg="#85929E" ,fg="white",command=root.quit) 
          Exit_button.place(x=45,y=205,width=120 ,height=33)


          # ------------- search manage ----------------------
          Search_Frame = Frame(self.root,bg= "white")
          Search_Frame.place(x=1 ,y=30 ,width=1031 ,height=50)

          lbl_search = Label(Search_Frame,text="Search_ON_Student",bg="white")
          lbl_search.place(x=915 ,y=15)
          compo_search = ttk.Combobox(Search_Frame,textvariable=self.se_by,justify="right")
          compo_search["value"] =("ID","Name","Email","Phone")
          compo_search.place(x= 770,y=16 )

          search_entry = Entry(Search_Frame,textvariable=self.se_var,bd='2',justify="right")
          search_entry.place(x=640,y=17)

          search_button = Button(Search_Frame,text ="Search",bg="#3498DB",fg="white",command=self.search)
          search_button.place(x =590,y = 17 ,width=45,height=20)


          # ---------- details عرض النتائج والبيانات --------------

          Details_Frame = Frame(self.root,bg="#F2F4F4")
          Details_Frame.place(x=4 ,y=83 ,width= 1028,height= 547 )

          # create scroll 
          scroll_x = Scrollbar(Details_Frame,orient=HORIZONTAL)
          scroll_y = Scrollbar(Details_Frame,orient=VERTICAL)

          # ------treeview -------
          self.student_table = ttk.Treeview(Details_Frame,
          columns=("ID","Name","Email","Phone","Certification","Gender","Address") ,  
          xscrollcommand= scroll_x.set,
          yscrollcommand= scroll_y.set)
          self.student_table.place(x=30,y=1,width=1003,height=520)
          scroll_x.pack(side=BOTTOM,fill=X)
          scroll_y.pack(side=LEFT,fill=Y)
          scroll_x.config(command=self.student_table.xview)
          scroll_y.config(command=self.student_table.yview)

          self.student_table["show"] ="headings"
          self.student_table.heading("ID",text="ID")
          self.student_table.heading("Name",text="Name")
          self.student_table.heading("Email",text="Email")
          self.student_table.heading("Phone",text="Phone")
          self.student_table.heading("Certification",text="Certification")
          self.student_table.heading("Gender",text="Gender")
          self.student_table.heading("Address",text="Address")

          self.student_table.column("ID",width=20)
          self.student_table.column("Name",width=100)
          self.student_table.column("Email",width=105)
          self.student_table.column("Phone",width=15)
          self.student_table.column("Certification",width=50)
          self.student_table.column("Gender",width=30)
          self.student_table.column("Address",width=100)
          self.student_table.bind("<<TreeviewSelect>>", self.get_selected_row )
          
          # -----------Database-------------------
          self.fetch_all()
     def add_student(self):

          Database = pymysql.connect(
          host = "localhost",
          user = "root",
          password = "",
          database= "student")
          cur = Database.cursor()
          cur.execute("insert into students values(%s,%s,%s,%s,%s,%s,%s)",(
               self.ID_var.get(),
               self.Name_var.get(),
               self.Email_var.get(),
               self.Phone_var.get(),
               self.Certification_var.get(),
               self.Gender_var.get(),
               self.Address_var.get(),

          ))
          Database.commit()
          self.fetch_all()
          self.clear()
          print("Student added")
          Database.close()

     def fetch_all(self):
          Database = pymysql.connect(
           host="localhost",
          user="root",
          password="",
          database="student"
        )
          cur = Database.cursor()
          cur.execute("SELECT * FROM students")
          rows =cur.fetchall()
          if len(rows) != 0:
               self.student_table.delete(*self.student_table.get_children())
               for row in rows:
                    self.student_table.insert("", END, values=(row[0],row[1],row[3],row[2],row[4],row[5],row[6]))
               Database.commit()
          Database.close()

     def clear(self):
          self.ID_var.set("")
          self.Name_var.set("")
          self.Email_var.set("")
          self.Phone_var.set("")
          self.Certification_var.set("")
          self.Gender_var.set("")
          self.Address_var.set("")
 
     def get_selected_row(self,event):
          
               index = self.student_table.selection()
               selected_row = self.student_table.item(index)
               data= selected_row["values"]
               self.ID_var.set(data[0])
               self.Name_var.set(data[1])
               self.Email_var.set(data[3])
               self.Phone_var.set(data[2])
               self.Certification_var.set(data[4])
               self.Gender_var.set(data[5])
               self.Address_var.set(data[6])


     # update information 
     def update(self):
        try:
          Database = pymysql.connect(
          host="localhost",
          user="root",
          password="",
          database="student"
               )
          cur = Database.cursor()
          cur.execute("UPDATE students SET Address = %s, Gender = %s, Certification = %s, Email = %s, Phone = %s, Name = %s WHERE ID = %s", (
          self.Address_var.get(),
          self.Gender_var.get(),
          self.Certification_var.get(),
          self.Email_var.get(),
          self.Phone_var.get(),
          self.Name_var.get(),
          self.ID_var.get()))

          Database.commit()
          self.fetch_all()
          self.clear()
          Database.close()
          print("Record updated successfully!")
        except:
             print("Error occurred while updating the record")


     def search(self):
          Database = pymysql.connect(
          host="localhost",
          user="root",
          password="",
          database="student"
        )
          cur = Database.cursor()
          cur.execute("SELECT * FROM students WHERE "+
                      str(self.se_by.get())+" LIKE '%"+str(self.se_var.get())+"%'")
                      
          rows =cur.fetchall()
          if len(rows) != 0:
               self.student_table.delete(*self.student_table.get_children())
               for row in rows:
                    self.student_table.insert("", END, values=(row[0],row[1],row[3],row[2],row[4],row[5],row[6]))
               Database.commit()
          Database.close()
     
     def about(self):
          messagebox.showinfo("Registration","Welcome to the Student Registration Program")
     

     def delete_student(self):
         
          Database = pymysql.connect(
          host="localhost",
          user="root",
          password="",
          database="student"
          )
          cur = Database.cursor()
          cur.execute("delete from students where id =%s",self.Delete_var.get())
          Database.commit()
          self.fetch_all()
          self.clear()
          print("student deleted")
          Database.close()
           
     
          
     
         
          
          


if __name__ == "__main__":
     root = Tk()
     person = student(root)
     root.mainloop()