from tkinter import*
from tkinter import ttk
import random
import tkinter.messagebox
from datetime import datetime
import time;

class Customer:
    def __init__(self,roo):
        self.root = root
        self.root.title("HOTEL MANAGEMENT SYSTEM")
        self.root.geometry("1350x750+0+0")
        self.root.config(background="powder blue")
        
        ABC = Frame(self.root, bg="powder blue", bd=20, relief=RIDGE)
        ABC.grid()
        ABC1 = Frame(ABC, bd=14, width=1380,height=500,padx=10,bg="powder blue", relief=RIDGE)
        ABC1.grid(row=0, column=0, columnspan=4,sticky=W)
        ABC2 = Frame(ABC, bd=14,width=350,height=488,padx=10, bg="cadet blue", relief=RIDGE)
        ABC2.grid(row=1,column=0,sticky=W)
        ABC3 = Frame(ABC, bd=14,width=450,height=488,padx=10, bg="powder blue", relief=RIDGE)
        ABC3.grid(row=1,column=1,sticky=W)
        ABC4 = Frame(ABC, bd=14,width=460,height=488,padx=10, bg="cadet blue", relief=RIDGE)
        ABC4.grid(row=1,column=2,sticky=W)
        ABC5 = Frame(ABC4, bd=14,width=470,height=340,padx=10, bg="cadet blue", relief=RIDGE)
        ABC5.grid(row=0,column=0,sticky=W)
        ABC6 = Frame(ABC4, bd=14,width=470,height=120,padx=10, bg="cadet blue", relief=RIDGE)
        ABC6.grid(row=1, column=0, columnspan=4, sticky=W)

        Date1 = StringVar()
        Date2 = StringVar()
        Time1 = StringVar()
        Date1.set(time.strftime("%d/%m/%y"))
        
        Time1.set(time.strftime("%H:%M:%S"))

        #================================================================================================================
        
        #self.lblTitle = Label(ABC1, textvariable=Date1,font=('Arial',30,'bold'),pady=9,
            #                     bd=5,bg='cadet blue',fg="cornsilk").grid(row=0,column=0)
        self.lblTitle = Label(ABC1, text="\tHOTEL MANAGEMENT SYSTEM   \t\t",font=('Arial',30,'bold'),pady=9,
                              bd=5,bg='cadet blue',fg="cornsilk",justify=CENTER).grid(row=0,column=0)  
        self.lblTitle = Label(ABC1, textvariable=Time1,font=('Arial',30,'bold'),pady=9,
                              bd=5,bg='cadet blue',fg="cornsilk").grid(row=0,column=2)
        
        #===============================================Exit==============================================================

        def iExit():
            iExit = tkinter.messagebox.askyesno("HOTEL MANAGEMENT SYSTEM", "Confirm if you want to exit")
            if iExit > 0:
                root.destroy()
                return

        #==============================================Reset==============================================================
        def Reset():
            self.txtReceipt.delete("1.0",END)
            E_Latta.set("0")
            E_Espresso.set("0")
            E_Iced_Latta.set("0")
            E_Vale_Coffee.set("0")
            E_Cappuccino.set("0")
            E_African_Coffee.set("0")
            E_American_Coffee.set("0")
            E_Iced_Cappuccino.set("0")

            Var1.set(0)
            Var2.set(0)
            Var3.set(0)
            Var4.set(0)
            Var5.set(0)
            Var6.set(0)
            Var7.set(0)
            Var8.set(0)

            Date2.set("")
            
            CustomerRef.set("")
            Firstname.set("")
            Surname.set("")
            Address.set("")
            PostCode.set("")
            Mobile.set("")
            Email.set("")
            Nationality.set("")
            DOB.set("")
            IDType.set("")
            Gender.set("")
            CheckInDate.set("")
            CheckOutDate.set("")
            Meal.set("")
            RoomType.set("")
            RoomNo.set("")
            RoomExtNo.set("")
            TotalCost.set("")
            SubTotal.set("")
            PaidTax.set("")
            TotalDays.set("")
        #====================================================================================================================

        def chkLatta():
            if (Var1.get() ==1):
                self.txtLatta.configure(state=NORMAL)
                self.txtLatta.focus()
                self.txtLatta.delete('0', END)
                E_Latta.set("")
            elif (Var1.get() ==0):
                self.txtLatta.configure(state=DISABLED)
                E_Latta.set("0")
        def chkEspresso():
            if (Var2.get() ==1):
                self.txtEspresso.configure(state=NORMAL)
                self.txtEspresso.focus()
                self.txtEspresso.delete('0', END)
                E_Espresso.set("")
            elif (Var2.get() ==0):
                self.txtEspresso.configure(state=DISABLED)
                E_Espresso.set("0")
        def chkIced_Latta():
            if (Var3.get() ==1):
                self.txtIced_Latta.configure(state=NORMAL)
                self.txtIced_Latta.focus()
                self.txtIced_Latta.delete('0', END)
                E_Iced_Latta.set("")
            elif (Var3.get() ==0):
                self.txtIced_Latta.configure(state=DISABLED)
                E_Iced_Latta.set("0")
        def chkVale_Coffee():
            if (Var4.get() ==1):
                self.txtVale_Coffee.configure(state=NORMAL)
                self.txtVale_Coffee.focus()
                self.txtVale_Coffee.delete('0', END)
                E_Vale_Coffee.set("")
            elif (Var4.get() ==0):
                self.txtVale_Coffee.configure(state=DISABLED)
                E_Vale_Coffee.set("0")
        def chkCappuccino ():
            if (Var5.get() ==1):
                self.txtCappuccino .configure(state=NORMAL)
                self.txtCappuccino .focus()
                self.txtCappuccino .delete('0', END)
                E_Cappuccino .set("")
            elif (Var5.get() ==0):
                self.txtCappuccino .configure(state=DISABLED)
                E_Cappuccino .set("0")
        def chkAfrican_Coffee():
            if (Var6.get() ==1):
                self.txtAfrican_Coffee.configure(state=NORMAL)
                self.txtAfrican_Coffee.focus()
                self.txtAfrican_Coffee.delete('0', END)
                E_African_Coffee.set("")
            elif (Var6.get() ==0):
                self.txtAfrican_Coffee.configure(state=DISABLED)
                E_African_Coffee.set("0")
        def chkAmerican_Coffee():
            if (Var7.get() ==1):
                self.txtAmerican_Coffee.configure(state=NORMAL)
                self.txtAmerican_Coffee.focus()
                self.txtAmerican_Coffee.delete('0', END)
                E_American_Coffee.set("")
            elif (Var7.get() ==0):
                self.txtAmerican_Coffee.configure(state=DISABLED)
                E_American_Coffee.set("0")
        def chkIced_Cappuccino():
            if (Var8.get() ==1):
                self.txtIced_Cappuccino.configure(state=NORMAL)
                self.txtIced_Cappuccino.focus()
                self.txtIced_Cappuccino.delete('0', END)
                E_Iced_Cappuccino.set("")
            elif (Var8.get() ==0):
                self.txtIced_Cappuccino.configure(state=DISABLED)
                E_Iced_Cappuccino.set("0")
        #==========================================================================================================================
        def CostOfItem():
            CustomerRef.set(random.randint(19800,9875648))
            Item1=float(E_Latta.get())
            Item2=float(E_Espresso.get())
            Item3=float(E_Iced_Latta.get())
            Item4=float(E_Vale_Coffee.get())
            Item5=float(E_Cappuccino.get())
            Item6=float(E_African_Coffee.get())
            Item7=float(E_American_Coffee.get())
            Item8=float(E_Iced_Cappuccino.get())

            PriceofDrinks = (Item1 * 120) + (Item2 * 230)\
                                + (Item3 * 300) + (Item4 * 430) + (Item5 * 150) + (Item6 * 530) + (Item7 * 930) + (Item8 * 202)
            SubTotalofITEMS = "Rs", str('%.2f'% PriceofDrinks)
            SubTotal.set(SubTotalofITEMS)
            Tax="Rs", str('%.2f'% ((PriceofDrinks) * 0.15))
            PaidTax.set(Tax)
            TTax=((PriceofDrinks)*0.15)
            TCost="Rs",str('%.2f'%(PriceofDrinks+TTax))
            TotalCost.set(TCost)

            self.txtReceipt.insert(END,'Items\t\t\t\t'+"Cost of Items \n")
            self.txtReceipt.insert(END,'Customer Ref.set:\t\t\t\t\t'+CustomerRef.get()+"\n")
            self.txtReceipt.insert(END,'PIZZA:\t\t\t\t\t'+E_Latta.get()+"\n")
            self.txtReceipt.insert(END,'KHICHDI:\t\t\t\t\t'+E_Espresso.get()+"\n")
            self.txtReceipt.insert(END,'HAKKA NOODLES:\t\t\t\t\t'+E_Iced_Latta.get()+"\n")
            self.txtReceipt.insert(END,'FRANKIEE:\t\t\t\t\t'+E_Vale_Coffee.get()+"\n")
            self.txtReceipt.insert(END,'PANIPURI:\t\t\t\t\t'+E_Cappuccino.get()+"\n")
            self.txtReceipt.insert(END,'FRENCH FRIES\t\t\t\t\t'+E_African_Coffee.get()+"\n")
            self.txtReceipt.insert(END,'CHOCOLATE MOUSSE:\t\t\t\t\t'+E_American_Coffee.get()+"\n")
            self.txtReceipt.insert(END,'ICE :\t\t\t\t\t'+E_Iced_Cappuccino.get()+"\n ")

            self.txtReceipt.insert(END,'\nTax Paid:\t\t\t\t'+PaidTax.get()+"\n")
            self.txtReceipt.insert(END,'\nSubtotal\t\t\t\t'+str(SubTotal.get())+"\n")
            self.txtReceipt.insert(END,'\nTotal cost:\t\t\t\t'+str(TotalCost.get())+"\n")

            
        #========================================================================================================================
                
        CustomerRef =StringVar()
        Firstname =StringVar()
        Surname =StringVar()
        Address=StringVar()
        PostCode =StringVar()
        Mobile =StringVar()
        Email =StringVar()
        Nationality =StringVar()
        DOB =StringVar()
        IDType =StringVar()
        Gender =StringVar()
        CheckInDate =StringVar()
        CheckOutDate =StringVar()
        Meal =StringVar()
        RoomType =StringVar()
        RoomNo =StringVar()
        RoomExtNo =StringVar()
        TotalCost =StringVar()
        SubTotal =StringVar()
        PaidTax =StringVar()
        TotalDays =StringVar()

        CustomerRef.set(random.randint(19800,9875648))

        Var1=IntVar()
        Var2=IntVar()
        Var3=IntVar()
        Var4=IntVar()
        Var5=IntVar()
        Var6=IntVar()
        Var7=IntVar()
        Var8=IntVar()

        E_Latta=StringVar()
        E_Espresso=StringVar()
        E_Iced_Latta=StringVar()
        E_Vale_Coffee=StringVar()
        E_Cappuccino=StringVar()
        E_African_Coffee=StringVar()
        E_American_Coffee=StringVar()
        E_Iced_Cappuccino=StringVar()

        E_Latta.set("0")
        E_Espresso.set("0")
        E_Iced_Latta.set("0")
        E_Vale_Coffee.set("0")
        E_Cappuccino.set("0")
        E_African_Coffee.set("0")
        E_American_Coffee.set("0")
        E_Iced_Cappuccino.set("0")

        #===================================================================================================================
        
        self.lblCus_Ref=Label(ABC2,font=('arial',12,'bold'),text="Customer Ref:",padx=2,fg="Cornsilk",bg="cadet Blue",)
        self.lblCus_Ref.grid(row=0,column=0,sticky=W)
        self.txtCus_Ref=Entry(ABC2,font=('arial',12,'bold'),textvariable= CustomerRef,width=20)
        self.txtCus_Ref.grid(row=0,column=1,pady=3,padx=20)
        
        
        self.lblFirstname=Label(ABC2,font=('arial',12,'bold'),text="Firstname:",padx=2,fg="Cornsilk",bg="cadet Blue",)
        self.lblFirstname.grid(row=1,column=0,sticky=W)
        self.txtFirstname=Entry(ABC2,font=('arial',12,'bold'), textvariable=Firstname,width=20)
        self.txtFirstname.grid(row=1,column=1,pady=3,padx=20)
        
        self.lblSurname=Label(ABC2,font=('arial',12,'bold'),text="Surname:",padx=2,fg="Cornsilk",bg="cadet Blue",)
        self.lblSurname.grid(row=2,column=0,sticky=W)
        self.txtSurname=Entry(ABC2,font=('arial',12,'bold'),textvariable=Surname,width=20)
        self.txtSurname.grid(row=2,column=1,pady=3,padx=20)

        self.lblAddress=Label(ABC2,font=('arial',12,'bold'),text="Address:",padx=2,pady=2,fg="Cornsilk",bg="cadet Blue",)
        self.lblAddress.grid(row=3,column=0,sticky=W)
        self.txtAddress=Entry(ABC2,font=('arial',12,'bold'),textvariable=Address,width=20)
        self.txtAddress.grid(row=3,column=1,pady=3,padx=20)


        self.lblPCode=Label(ABC2,font=('arial',12,'bold'),text="PostCode:",padx=2,pady=2,fg="Cornsilk",bg="cadet Blue",)
        self.lblPCode.grid(row=4,column=0,sticky=W)
        self.txtPCode=Entry(ABC2,font=('arial',12,'bold'),textvariable=PostCode,width=20)
        self.txtPCode.grid(row=4,column=1,pady=3,padx=20)
        
        
        self.lblMoblie=Label(ABC2,font=('arial',12,'bold'),text="Moblie:",padx=2,pady=2,fg="Cornsilk",bg="cadet Blue",)
        self.lblMoblie.grid(row=5,column=0,sticky=W)
        self.txtMoblie=Entry(ABC2,font=('arial',12,'bold'),textvariable=Mobile,width=20)
        self.txtMoblie.grid(row=5,column=1,pady=3,padx=20)

        self.lblEmail=Label(ABC2,font=('arial',12,'bold'),text="Email:",padx=2,pady=2,fg="Cornsilk",bg="cadet Blue",)
        self.lblEmail.grid(row=6,column=0,sticky=W)
        self.txtEmail=Entry(ABC2,font=('arial',12,'bold'),textvariable=Email,width=20)
        self.txtEmail.grid(row=6,column=1,pady=3,padx=20)

        self.lblN=Label(ABC2,font=('arial',12,'bold'),text="Nationality:",padx=2,pady=2,fg="Cornsilk",bg="cadet Blue",)
        self.lblN.grid(row=7,column=0,sticky=W)
        self.cboN=ttk.Combobox(ABC2,textvariable=Nationality,state='readonly',font=('arial',12,'bold'),width=18)
        self.cboN['value']=('', 'British', 'Nigeria', 'Kenya', 'India', 'France', 'Iran', 'Norway', 'Canada', 'Morocco')
        self.cboN.current(0)
        self.cboN.grid(row=7,column=1,pady=3,padx=20)


        self.lblDOB=Label(ABC2,font=('arial',12,'bold'),text="Date of Birth:",padx=2,pady=2,fg="Cornsilk",bg="cadet Blue",)
        self.lblDOB.grid(row=8,column=0,sticky=W)
        self.txtDOB=Entry(ABC2,font=('arial',12,'bold'),textvariable=DOB,width=20)
        self.txtDOB.grid(row=8,column=1,pady=3,padx=20)

        self.lb1IDType=Label(ABC2,font=('arial',12,'bold'),text="Type Of Id:",padx=2,pady=2,fg="Cornsilk",bg="cadet Blue",)
        self.lb1IDType.grid(row=9,column=0,sticky=W)
        self.cboIDType=ttk.Combobox(ABC2,textvariable=IDType,state='readonly',font=('arial',12,'bold'),width=18)
        self.cboIDType['value']=('','Pilot Licence','Driving Licence','Student ID','Passport')
        self.cboIDType.current(0)
        self.cboIDType.grid(row=9,column=1,pady=3,padx=20)

        self.lb1Gender=Label(ABC2,font=('arial',12,'bold'),text="Gender:",padx=2,pady=2,fg="Cornsilk",bg="cadet Blue",)
        self.lb1Gender.grid(row=10,column=0,sticky=W)
        
        self.cboGender=ttk.Combobox(ABC2,textvariable=Gender,state='readonly',font=('arial',12,'bold'),width=18)
        self.cboGender['value']=('Male','Female')
        #self.cboGender.current(0)
        self.cboGender.grid(row=10,column=1,pady=3,padx=20)
        

        self.lb1Check_In_Date=Label(ABC2,font=('arial',12,'bold'),text="Check In Date:",padx=2,pady=2,fg="Cornsilk",bg="cadet Blue",)
        self.lb1Check_In_Date.grid(row=11,column=0,sticky=W)
        self.txtCheck_In_Date=Entry(ABC2,font=('arial',12,'bold'),textvariable=Date1,width=20)
        self.txtCheck_In_Date.grid(row=11,column=1,pady=3,padx=20)
        
        self.lb1Check_Out_Date=Label(ABC2,font=('arial',12,'bold'),text="Check Out Date:",padx=2,pady=2,fg="Cornsilk",bg="cadet Blue",)
        self.lb1Check_Out_Date.grid(row=12,column=0,sticky=W)
        self.txtCheck_Out_Date=Entry(ABC2,font=('arial',12,'bold'),textvariable=Date2,width=20)
        self.txtCheck_Out_Date.grid(row=12,column=1,pady=9,padx=40)

        self.lb1Meal=Label(ABC2,font=('arial',12,'bold'),text="Meal:",padx=2,pady=2,fg="Cornsilk",bg="cadet Blue",)
        self.lb1Meal.grid(row=13,column=0,sticky=W)
        self.cboMeal=ttk.Combobox(ABC2,textvariable=Meal,state='readonly',font=('arial',12,'bold'),width=18)
        self.cboMeal['value']=('','Breakfast','Lunch','Dinner')
        self.cboMeal.current(0)
        self.cboMeal.grid(row=13,column=1,pady=3,padx=20)

        self.lb1RoomType=Label(ABC2,font=('arial',12,'bold'),text="Room Type:",padx=2,pady=2,fg="Cornsilk",bg="cadet Blue",)
        self.lb1RoomType.grid(row=14,column=0,sticky=W)
        self.cboRoomType=ttk.Combobox(ABC2,textvariable=RoomType,state='readonly',font=('arial',12,'bold'),width=18)

        self.cboRoomType['value']=('','Single','Double','family')
        self.cboRoomType.current(0)
        self.cboRoomType.grid(row=14,column=1,pady=3,padx=20)
        
        #===========================================================================================================================
        
        self.Latta = Checkbutton(ABC3, text="PIZZA", variable=Var1, onvalue = 1, offvalue = 0,
                         font=('arial',12, 'bold'),bg="powder blue",command=chkLatta).grid(row=0,sticky=W)
        self.txtLatta = Entry(ABC3,font=('arial',12,'bold'), textvariable=E_Latta, bd=8,
                             width=20,justify='left',state= DISABLED)
        self.txtLatta.grid(row=0,column=1)

        self.Espresso = Checkbutton(ABC3, text="KHICHDI", variable=Var2,onvalue = 1,offvalue = 0,
                                 font=('arial',12,'bold'),bg="powder blue",command=chkEspresso).grid(row=1,sticky=W)
        self.txtEspresso =Entry(ABC3,font=('arial',12,'bold'),textvariable=E_Espresso,bd=8,
                             width=20,justify='left',state=DISABLED)
        self.txtEspresso.grid(row=1,column=1)        
        
        self.Iced_Latta = Checkbutton(ABC3, text="HAKKA NOODLES", variable=Var3,onvalue = 1,offvalue = 0,
                                 font=('arial',12,'bold'),bg="powder blue",command=chkIced_Latta).grid(row=2,sticky=W)
        self.txtIced_Latta =Entry(ABC3,font=('arial',12,'bold'),textvariable=E_Iced_Latta,bd=8,
                             width=20,justify='left',state=DISABLED)
        self.txtIced_Latta.grid(row=2,column=1)
    
        self.Vale_Coffee = Checkbutton(ABC3, text="FRANKIEE", variable=Var4,onvalue = 1,offvalue = 0,
                                 font=('arial',12,'bold'),bg="powder blue",command=chkVale_Coffee).grid(row=3,sticky=W)
        self.txtVale_Coffee =Entry(ABC3,font=('arial',12,'bold'),textvariable=E_Vale_Coffee,bd=8,
                             width=20,justify='left',state=DISABLED)
        self.txtVale_Coffee.grid(row=3,column=1)

        self.Cappuccino = Checkbutton(ABC3, text="PANIPURI", variable=Var5,onvalue = 1,offvalue = 0,
                                 font=('arial',12,'bold'),bg="powder blue",command=chkCappuccino).grid(row=4,sticky=W)
        self.txtCappuccino =Entry(ABC3,font=('arial',12,'bold'),textvariable=E_Cappuccino,bd=8,
                             width=20,justify='left',state=DISABLED)
        self.txtCappuccino.grid(row=4,column=1)

        self.African_Coffee = Checkbutton(ABC3, text="FRENCH FRIES", variable=Var6,onvalue = 1,offvalue = 0,
                                 font=('arial',12,'bold'),bg="powder blue",command=chkAfrican_Coffee).grid(row=5,sticky=W)
        self.txtAfrican_Coffee =Entry(ABC3,font=('arial',12,'bold'),textvariable=E_African_Coffee,bd=8,
                             width=20,justify='left',state=DISABLED)
        self.txtAfrican_Coffee.grid(row=5,column=1)
        
        self.American_Coffee = Checkbutton(ABC3, text="CHOCOLATE MOUSSE", variable=Var7,onvalue = 1,offvalue = 0,
                                 font=('arial',12,'bold'),bg="powder blue",command=chkAmerican_Coffee).grid(row=6,sticky=W)
        self.txtAmerican_Coffee =Entry(ABC3,font=('arial',12,'bold'),textvariable=E_American_Coffee,bd=8,
                             width=20,justify='left',state=DISABLED)
        self.txtAmerican_Coffee.grid(row=6,column=1)

        self.Iced_Cappuccino = Checkbutton(ABC3, text="ICE CREAM", variable=Var8,onvalue = 1,offvalue = 0,
                                 font=('arial',12,'bold'),bg="powder blue",command=chkIced_Cappuccino).grid(row=7,sticky=W)
        self.txtIced_Cappuccino =Entry(ABC3,font=('arial',12,'bold'),textvariable=E_Iced_Cappuccino,bd=8,
                             width=20,justify='left',state=DISABLED)
        self.txtIced_Cappuccino.grid(row=7,column=1)
       
        self.lblspace=Label(ABC3,text="Total And Total Sum", font=('arial',18,'bold'),pady=1, bd=9, bg="cadet blue",
                            fg="cornsilk", width=26, justify=CENTER).grid(row=8,column=0,columnspan=4)
            
        #==========================================Receipt======================================================================

        self.lblPaidTax =Label(ABC3,font=('arial',12,'bold'),text="paid tax",bd=7,bg="powder blue",fg="black",)
        self.lblPaidTax.grid(row=10,column=0,sticky=W)
        self.txtPaidTax= Entry(ABC3,font=('arial',12,'bold'),textvariable=PaidTax,bd=7,bg="white",
                               width=20,justify=LEFT)
        self.txtPaidTax.grid(row=10,column=1)

        self.lblSubTotal =Label(ABC3,font=('arial',12,'bold'),text="sub total",bd=7,bg="powder blue",fg="black",)
        self.lblSubTotal.grid(row=11,column=0,sticky=W)
        self.txtSubTotal= Entry(ABC3,font=('arial',12,'bold'),textvariable=SubTotal,bd=7,bg="white",
                               width=20,justify=LEFT)
        self.txtSubTotal.grid(row=11,column=1)

        self.lblTotalCost =Label(ABC3,font=('arial',12,'bold'),text="total cost",bd=7,bg="powder blue",fg="black",)
        self.lblTotalCost.grid(row=12,column=0,sticky=W)
        self.txtTotalCost= Entry(ABC3,font=('arial',12,'bold'),textvariable=TotalCost,bd=7,bg="white",
                               width=20,justify=LEFT)
        self.txtTotalCost.grid(row=12,column=1)

        #=================================================Text===================================================================

        self.txtReceipt=Text(ABC5,height=19,width=43,bd=10,font=('arial',9,'bold'))
        self.txtReceipt.grid(row=0,column=0)
        
        #======================================================buttons============================================================
        self.btnTotal = Button(ABC6, padx=14, pady=7,bd=5,fg="black",font=('Arial',16,'bold'),width=5,height=2,
                             bg="powder blue",text="Total",command=CostOfItem).grid(row=0,column=0)
        self.btnReset = Button(ABC6,padx=14,pady=7,bd=5,fg="black",font=('Arial',16,'bold'),width=5,height=2,
                             bg="powder blue",text="Reset",command=Reset).grid(row=0,column=1)
        self.btnExit = Button(ABC6,padx=14,pady=7,bd=5,fg="black",font=('Arial',16,'bold'),width=5,height=2,
                             bg="powder blue",text="Exit",command=iExit).grid(row=0,column=2)
        
        #==========================================================================================================================       
if __name__=='__main__':
    root=Tk()
    application = Customer(root)
    root.mainloop()
