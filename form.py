
from tkinter import *
from tkinter import ttk
from typing import Match
from PIL import Image,ImageTk
from tkinter import messagebox
import re
import pyttsx3 as pt
import speech_recognition as sr
import mysql.connector

class Base:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1610x700+0+0")          #(set window)
        #self.root.minsize(1200,700)
        #self.root.maxsize(1000,700)
        self.root.title(" USER REGISTRAION FORM")         #(set title)
        self.Font=font=("monospace 20 ")
        self.root["bg"]= "black"   
        self.loginpage()


        #-------------------text to voice messages----------------------------#

        self.speach=pt.init()
        self.voices=self.speach.getProperty("voices")
        self.speach.setProperty("voice",self.voices[1].id)

#----  ------------------------ LOGIN window------------------------

    def loginpage(self):

            self.v_user=StringVar()
            self.v_pass=StringVar()
    
        #-------- TITLE IAMGE / LABEL -------S


            #LOGO IMAGE LABEL (read the logo)
            lgo_img=Image.open("img/logimg.png")
            lgo_img=lgo_img.resize((50,50),Image.ANTIALIAS)
            self.image_icon=ImageTk.PhotoImage(lgo_img)

         #--------------------WINDOW ICON----------------------------

            img=PhotoImage(file="img/loginimg.png")
            root.iconphoto(FALSE,img)


        #----------TITLE  FRAME AND LABEL---------------------------------------------


            #TITLE FRAME (set title frame)
            tlt_frm=Frame(self.root,bd=1,relief=RIDGE)
            tlt_frm.place(x=330,y=180,width=550,height=70)

             #TITLE LABEL (set label and icon in frame)
            tlt_lbl=Label(tlt_frm,image=self.image_icon,compound=LEFT,text="LOGIN FORM",font=("monospace 30 bold"),fg="black")
            tlt_lbl.place(x=105,y=5)

        #-----FRAME INFORMATION--------------------------------------------------

            #login FRAME (set info frame)
            log_frm=Frame(self.root,bd=1,relief=RIDGE)
            log_frm.place(x=330,y=252,width=550,height=295)

            #-------------------NAME LABEL AND ENTRY BOX------------------------------------
        
            # NAME LABEL
           
            user_lbl=Label(log_frm,text="Username",font=self.Font)
            user_lbl.grid(row=0,column=0,padx=15,pady=35  ,sticky=W)
            
    
            # NAME ENTRY FILL
            self.user=ttk.Entry(log_frm,font=self.Font,textvariable=self.v_user,width=20)
            #self.v_name.set(self.v_name)
            self.user.grid(row=0,column=1,padx=0,pady=0,sticky=W)

        #----------------PASSWRD AND ENTRY BOX---------------------------------------
            # PASSWORD LABEL
            pass_lbl=Label(log_frm,text="Password: ",font=self.Font)
            pass_lbl.grid(row=1,column=0,padx=15,pady=0,sticky=W)
 
            #DEMO PASSWORD ENTRY FILL
            self.password=ttk.Entry(log_frm,font=self.Font,textvariable=self.v_pass  ,width=20,show="*")
            self.password.grid(row=1,column=1,padx=0,pady=0,sticky=W)

        #-----FRAME BUTTONS--------------------------------------------------


            # BUTTONS FRAME 
            btn_frm=ttk.Frame(log_frm)
            btn_frm.place(x=170,y=175,width=290,height=50)

        #-----ALL BUTTONS--------------------------------------------------

             # LOGIN BUTTON
            login_btn=Button(btn_frm,text="login",command=self.login,font=("monospace 15 bold"),width=7,cursor="hand2",bg="green",fg="black",activebackground="black",activeforeground="white")
            login_btn.grid(row=0,column=0,padx=30,pady=5,sticky=W)

             # REGISTER BUTTON
            reg_btn=Button(btn_frm,text="register",command=self.registerpage,font=("monospace 15 bold"),width=7,cursor="hand2",bg="green",fg="black",activebackground="black",activeforeground="white")
            reg_btn.grid(row=0,column=1,padx=10,pady=5,sticky=W)           
        
        


        


        


#----  ------------------------ REGISTER window---------------------------------------#
        

    def registerpage(self):
            self.v_name= StringVar()
            self.v_contact = StringVar()
            self.v_gender = StringVar()
            self.v_country = StringVar()
            self.v_id = StringVar()
            self.v_idno = StringVar()
            self.v_email = StringVar()
            self.v_password = StringVar()
            self.v_confirm = StringVar()
            self.v_check = IntVar()

            #------------------VARIABLES FOE GET DATA -----------------------------#

        

               

            #------------BACKGROUND IMAGE------------------------------------               
            self.bg=ImageTk.PhotoImage(file="img/BG.png")                   #(read the backgroung image)
            bg_lbl=Label(self.root,image=self.bg,bd=2,relief=RAISED)        #(set the backgroung image)
            bg_lbl.place(x=0,y=0,relwidth=1,relheight=1)


           #--------------------WINDOW ICON----------------------------
            img=PhotoImage(file="img/regicon.png")
            root.iconphoto(FALSE,img)


#--------- TITILE FRAME-------------------------------#
        

#                       -------- TITLE IAMGE / LABEL -------


            #LOGO IMAGE LABEL (read the logo)
            logo_img=Image.open("img/regimg.png")
            logo_img=logo_img.resize((60,60),Image.ANTIALIAS)
            self.image_icon=ImageTk.PhotoImage(logo_img)


            #TITLE FRAME (set title frame)
            title_frm=Frame(self.root,bd=1,relief=RIDGE)
            title_frm.place(x=450,y=15,width=550,height=70)

            #TITLE LABEL (set label and icon in frame)
            title_lbl=Label(title_frm,image=self.image_icon,compound=LEFT,text="REGISTRATION FORM",font=("monospace 30 bold"),fg="black")
            title_lbl.place(x=15,y=5)

#--------- INFORMATION FRAME------------------------------#

            #INFORMATION FRAME (set info frame)
            info_frm=Frame(self.root,bd=1,relief=RIDGE)
            info_frm.place(x=450,y=87,width=550,height=595)
        #-----------------------------------------------#

            # NAME LABEL
            name_lbl=Label(info_frm,text="Username: ",font=self.Font)
            name_lbl.grid(row=0,column=0,padx=5,pady=5,sticky=W)

            # NAME ENTRY FILL
            name_entry=ttk.Entry(info_frm,textvariable=self.v_name,font=self.Font,width=20)
            name_entry.grid(row=0,column=1,padx=0,pady=0,sticky=W)

            #BIND AND VALIDATION AND RAGISTER
            name_valid=self.root.register(self.validnanme)
            name_entry.config(validate="key",validatecommand=(name_valid,"%P"))                 #call back funtion

        #-----------------------------------------------#

            # CONTACT LABEL
            cont_lbl=Label(info_frm,text="Contact: ",font=self.Font)
            cont_lbl.grid(row=1,column=0,padx=5,pady=3,sticky=W)

            # CONTACT ENTRY FILL
            cont_entry=ttk.Entry(info_frm,textvariable=self.v_contact,font=self.Font,width=20)
            cont_entry.grid(row=1,column=1,padx=0,pady=5,sticky=W)

            #BIND AND VALIDATION AND RAGISTER
            contact_valid=self.root.register(self.validcontact)
            cont_entry.config(validate="key",validatecommand=(contact_valid,"%P"))                 #call back funtion

        #-----------------------------------------------#


            # GENDER ID LABEL
            gen_lbl=Label(info_frm,text="Gender: ",font=self.Font)
            gen_lbl.grid(row=2,column=0,padx=5,pady=3,sticky=W)


            #GENDER FRAME (set title frame)
            gen_frm=Frame(info_frm)
            gen_frm.place(x=160,y=105,width=280,height=35)

            # RADIO BUTTON FOR MALEs
            rdo_btn=Radiobutton(gen_frm,variable=self.v_gender,value="Male",text="Male",font=("monospace 12 bold"))
            rdo_btn.grid(row=0,column=0,padx=10,pady=0,stick=W)
            self.v_gender.set("Male")

            # RADIO BUTTON FOR FEMALE
            rdo_btn=Radiobutton(gen_frm,variable=self.v_gender,value="Female",text="Female",font=("monospace 12 bold"))
            rdo_btn.grid(row=0,column=1,padx=10,pady=0,stick=W)

        #-----------------------------------------------#

            # COUNTRY DROP BOX LABEL
            country_lbl=Label(info_frm,text="Country: ",font=self.Font)              #don't use textvariable
            country_lbl.grid(row=4,column=0,padx=3,pady=10,sticky=W)

            #set the diffrent option using option menu
        
            countries=["INDIA", "USA" ,"UAE","UK","ENGLAND","PAKISTAN","AFGANISTAN"]
            drp_lst=OptionMenu(info_frm,self.v_country, *countries)
            drp_lst.config(width=21,font=self.Font,bg="white")
            self.v_country.set("Select Your Country")
            drp_lst.grid(row=4,column=1,padx=0,pady=10,sticky=W)

        #-----------------------------------------------#

            # #ID  COMBOBOX LABEL
            id_lbl=Label(info_frm,text="ID Type: ",font=self.Font)
            id_lbl.grid(row=5,column=0,padx=3,pady=5,sticky=W)

            #set the diffrent option using combobox
        
            self.combo_id=ttk.Combobox(info_frm,textvariable=self.v_id,font=self.Font,justify="center",state="readonly",width=23)
            self.combo_id["values"]=("Select Your ID","Adhar card","Passport","Driving Licence","College id")
            self.combo_id.grid(row=5,column=1,padx=0,pady=5)
            self.combo_id.current(0)

        #-----------------------------------------------#

            #ID NUMBERLABEL
            id_lbl=Label(info_frm,text="ID number: ",font=self.Font)
            id_lbl.grid(row=6,column=0,padx=3,pady=5,sticky=W)
 
            #ID NUMBER ENTRY FILL
            name_entry=ttk.Entry(info_frm,textvariable=self.v_idno,font=self.Font,width=20)
            name_entry.grid(row=6,column=1,padx=0,pady=10,sticky=W)

            #-----------------------------------------------#

            # EMAIL ID LABEL
            email_lbl=Label(info_frm,text="Email: ",font=self.Font)
            email_lbl.grid(row=7,column=0,padx=3,pady=5,sticky=W)

            # EMAIL ID ENTRY FILL
            email_entry=ttk.Entry(info_frm,textvariable=self.v_email,font=self.Font,width=20)
            email_entry.grid(row=7,column=1,padx=0,pady=10,sticky=W)


            #-----------------------------------------------#
            #DEMO PASSWORD LABEL
            dpass_lbl=Label(info_frm,text="Password: ",font=self.Font)
            dpass_lbl.grid(row=8,column=0,padx=3,pady=5,sticky=W)
 
            #DEMO PASSWORD ENTRY FILL
            dpass_entry=ttk.Entry(info_frm,textvariable=self.v_password,show="*",font=self.Font,width=20)
            dpass_entry.grid(row=8,column=1,padx=0,pady=10,sticky=W)

        #-----------------------------------------------#

            # CONFIRM PASSWORD LABEL
            cpass_lbl=Label(info_frm,text="Confirm: ",font=self.Font)
            cpass_lbl.grid(row=9,column=0,padx=3,pady=5,sticky=W)
 
            # CONFIRM PASSWORD ENTRY FILL
            cpass_entry=ttk.Entry(info_frm,textvariable=self.v_confirm,show="*",font=self.Font,width=20)
            cpass_entry.grid(row=9,column=1,padx=0,pady=5,sticky=W)

            #-----------------------------------------------#

            #TERMS & CONDITION FRAME

            chk_frm=Frame(info_frm)
            chk_frm.place(x=20,y=480,width=350,height=55)


            # CHECK BUTTON

            chk_btn=Checkbutton(chk_frm,variable=self.v_check,text="Agree Our terms & Condition",font=("monospace 10 bold"),onvalue=1,offvalue=0)
            chk_btn.grid(row=0,column=0,padx=10,pady=1,sticky=W)

            self.chk_lbl=Label(chk_frm,text="",font=("monospace 10 bold"),fg="red")
            self.chk_lbl.grid(row=1,column=0,padx=10,pady=0,sticky=W)


        #-----------------------------------------------#
            # BUTTONS FRAME 
            btn_frm=Frame(info_frm)
            btn_frm.place(x=110,y=540,width=400,height=50)

            # SAVE BUTTON
            save_btn=Button(btn_frm,text="Save",command=self.validation,font=("monospace 15 bold"),width=7,cursor="hand2",bg="green",fg="blue",activebackground="black",activeforeground="white")
            save_btn.grid(row=0,column=0,padx=10,pady=0,sticky=W)

            # VERIFY BUTTON
            verify_btn=Button(btn_frm,text="Verify",command=self.verifydata,font=("monospace 15 bold"),width=7,cursor="hand2",bg="green",fg="blue",activebackground="black",activeforeground="white")
            verify_btn.grid(row=0,column=1,padx=10,pady=0,sticky=W)


            # CLEAR BUTTON
            clear_btn=Button(btn_frm,text="Clear",command=self.cleardata,font=("monospace 15 bold"),width=7,cursor="hand2",bg="green",fg="blue",activebackground="black",activeforeground="white")
            clear_btn.grid(row=0,column=2,padx=10,pady=0,sticky=W)


    
#-----------------validation for Entry fiels----------------------------------------------------------#

     #CALL BACK FUNTION FOR NAME
    def validnanme(self,name):
            if name.isalnum():
                return True
            elif name=="":
                return True
            else:
                    self.speach.say("This is Not Allowed")
                    self.speach.runAndWait()
                    messagebox.showerror("invalid","This is Not Allowed"+name[-1])
      
     
   # -----------------------------------------------------#
     #  CALL BACK FUNTION FOR CONTACT      
    def validcontact(self,contact):
            if contact.isdigit():
                    return True
            elif len(str(contact))==0:
                    return True
            else:
                    self.speach.say("Invalid Entry")
                    self.speach.runAndWait()
                    messagebox.showerror("invalid","Invalid entry")
                    return False



     
   #-----------------------------------------------------#
        # VALIDAE FUNCTION FOR EMAIL ID

    def validemail(self,email):
            if len(email)>7:
                    if re.match('^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$',email):
                            return True
                    else:
                            self.speach.say("invalid email enter valid user email (demo@gamil.com)")
                            self.speach.runAndWait()
                            messagebox.showwarning("Alert","invalid email enter valid user email (demo@gamil.com)")
                            return False
            else:
                    self.speach.say("Email length is too small")
                    self.speach.runAndWait()
                    messagebox.showerror("invalid","Email length is too small")
                    return False

            #  -----------------------------------------------------#
     

      #  VALIDAE FUNCTION FOR PASSWORD
    def validpassword(self,password):
            if len(password)<=11:
                    if re.match("^(?=.*[0-9])(?=.*[A-Z])(?=.*[^a-bA-B0-9])",password):
                            return True
                    else:
                            self.speach.say("Enter valid a password")
                            self.speach.runAndWait()
                            messagebox.showinfo("invalid","Enter Valid Password (Xyz@123)")
                            return False
            else:
                    self.speach.say("Length try you exceed")
                    self.speach.runAndWait()
                    messagebox.showerror("invalid","Length try you exceed")
                    return False
                    


                    
                    
# -----------------------------VALIDATION FOR ALL ENTRY FIELDS------------------------------------------------------------#

     #VALIDATION FUNCTION
    
    def validation(self):
            # if entry box is empty for(name , contact, gender, country, idname,idnumber,email, passwod, confirm password )
            if self.v_name.get()=="":
                    self.speach.say("Plese Enter You name")
                    self.speach.runAndWait()
                    messagebox.showerror("Error","Please Enter Your Name",parent=self.root)
            
            elif self.v_contact.get()=="" or len(self.v_contact.get())!=10:
                    self.speach.say("Plese Enter Your Valid Contact number")
                    self.speach.runAndWait()
                    messagebox.showerror("Error","Please Enter Your Valid Contact Number",parent=self.root)

            

                    self.speach.say("Plese Enter Your Valid Contact number")
                    self.speach.runAndWait()
                    messagebox.showerror("Error","Please Enter Your Valid Contact Number",parent=self.root)


                

            elif self.v_gender.get()=="":
                    self.speach.say("Plese Select Your Gender")
                    self.speach.runAndWait()
                    messagebox.showerror("Error","Please Select Your Gender",parent=self.root)
                     
            elif self.v_country.get()=="" or (self.v_country.get())=="Select Your Country":
                    self.speach.say("Plese Select Your Country Name")
                    self.speach.runAndWait()
                    messagebox.showerror("Error","Please Select Your Country Name",parent=self.root)
        
            elif self.v_id.get()=="Select Your ID":
                    self.speach.say("Plese Swelect Your Td Type")
                    self.speach.runAndWait() 
                    messagebox.showerror("Error","Please Select Your Id Type",parent=self.root)

            elif self.v_idno=="":
                    self.speach.say("Plese Enter Your Id Number")
                    self.speach.runAndWait() 
                    messagebox.showerror("Error","Please Enter Your ID Number",parent=self.root)

            elif len(self.v_idno.get())!=14:
                    self.speach.say("Plese Enter Your 14 Digit Number")
                    self.speach.runAndWait() 
                    messagebox.showerror("Error","Please Enter Your 14 digit",parent=self.root)

            elif self.v_email.get()=="":
                    self.speach.say("Plese Enter Your Email id")
                    self.speach.runAndWait()
                    messagebox.showerror("Error","Please Enter Your Email id",parent=self.root)


            elif self.v_password.get()=="":
                    self.speach.say("Plese Enter Your Password")
                    self.speach.runAndWait()
                    messagebox.showerror("Error","Please Enter Your Password",parent=self.root)

            elif self.v_confirm.get()=="":
                    self.speach.say("Plese Enter Your confirm Password")
                    self.speach.runAndWait()
                    messagebox.showerror("Error","Please Enter Your Confirm Password",parent=self.root)

            elif self.v_password.get()!= self.v_confirm.get():
                    self.speach.say("Password & Confirm Passwod must be same")
                    self.speach.runAndWait()
                    messagebox.showerror("Error","Password & Confirm Passwod must be same",parent=self.root)

            elif self.v_email.get()!= None and self.v_password.get()!= None:    
                    x =self.validemail(self.v_email.get())
                    y =self.validpassword(self.v_password.get())


                    
                  #---------------for check button--------------------------------#
                
            if (x == True) and (y == True):
                    
                    if self.v_check.get()==0:
                            self.speach.say("Please Agree Our terms & Condition")
                            self.speach.runAndWait()
                            self.chk_lbl.config(text="Please Agree Our terms & Condition",fg="red")

                    else:
                            self.chk_lbl.config(text="checked",fg="green")
                            try:
                                    my_connection=mysql.connector.connect(host="localhost",username="root",password="123456789",database="tkdb")
                                    my_cursur=my_connection.cursor()
                                    messagebox.showerror("Error","connection stablish")
                                    query=("select * from users where email=%s")
                                    value=(self.v_email.get(),)
                                    my_cursur.execute(query,value)
                                    row=my_cursur.fetchone()
                                    if row!=None:
                                            messagebox.showerror("Error","user already exist plaese try another email")
                                    else:
                                            my_cursur.execute("insert into users values(%s,%s,%s,%s,%s,%s,%s,%s)",(self.v_name.get(),
                                                                                self.v_contact.get(), 
                                                                                self.v_gender.get(), 
                                                                                self.v_country.get(),
                                                                                self.v_id.get(), 
                                                                                self.v_idno.get(), 
                                                                                self.v_email.get(), 
                                                                                self.v_password.get(),
                                            ))

                                   


                                    my_connection.commit()
                                    my_connection.close()

                                    
                            except Exception as e:
                                    messagebox.showerror("Error",f"Due to:{str(e)}",parent=self.root)                                                                                    


                            self.speach.say("Successfully")
                            self.speach.runAndWait()
                            messagebox.showinfo("Successfully",f"Your registration is completed your User name {self.v_name.get()} and password is {self.v_password.get()}")
   
   
   
                  #---------------for VERIFY DATA button--------------------------------#
    def verifydata(self):
            data=(f"Name:  {self.v_name.get()}\nContact:  {self.v_contact.get()}\nGender:  {self.v_gender.get()}\nCountry:  {self.v_country.get()}\nId: {self.v_id.get()}\nId Number:  {self.v_idno.get()}\nEmail:  {self.v_email.get()}\nPassword:  {self.v_password.get()}\n ")
            messagebox.showinfo("Details",data)

     #---------------for CLEAR button--------------------------------#
  
    def cleardata(self):
            self.v_name.set("")
            self.v_contact.set("") 
            self.v_gender.set("Male") 
            self.v_country.set("Select Your Country") 
            self.v_id.set("Select Your Id") 
            self.v_idno.set("") 
            self.v_email.set("") 
            self.v_password.set("") 
            self.v_confirm.set("") 
            self.v_check.set(0)



    def login(self):

            if self.user.get()=="" or self.password.get()=="":
                    self.speach.say("All fields sre required")
                    self.speach.runAndWait()
                    messagebox.showerror("Error","All fields sre required",parent=self.root)

            elif self.user.get()=="talha" or self.password.get()=="Talha@123":
                    messagebox.showwarning("succes","welcome your prgram is run")

            elif self.user.get()=="naseem" or self.password.get()=="Naseem@321":
                    messagebox.showwarning("succes","welcome your prgram is run")


            else:                   
                    try:
                            my_connection=mysql.connector.connect(host="localhost",username="root",password="123456789",database="tkdb")
                            my_cursur=my_connection.cursor()
                            my_cursur.execute("insert into users values(%s,%s)",(

                                                                                        self.user.get(),
                                                                                        self.password.get()))

                            row=my_cursur.fetchone()
                            if row==None:
                                    self.speach.say("Invalid user & password")
                                    self.speach.runAndWait()
                                    messagebox.showerror("Error","Invalid user & password")
                            else:
                                    open_main=messagebox.askyesno("YesNo","Access only Admin")
                                    if open_main>0:
                                            self.speach.say("your programm  in done")
                                            self.speach.runAndWait()
                                            messagebox.showerror("Error","your programm  in done")
                                    else:
                                            if not open_main:
                                                    return
                                            

                            my_connection.commit()
                            my_connection.close()   
                        
                    except Exception as e:                            
                            messagebox.showerror("Error",f"Due to:{str(e)}",parent=self.root)

        
        




     

         





        


if __name__=="__main__":
    root=Tk()
    obj=Base(root)
    root.mainloop()

        