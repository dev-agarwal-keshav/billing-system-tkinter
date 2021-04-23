from tkinter import *
import random
from tkinter import messagebox
import os

class Bill_app:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1350x700+0+0")
        self.root.title("Billing Software")
        bg_color="#074463"
        title=Label(self.root,text="Billing Software",bd=12,relief=GROOVE,bg=bg_color,fg="white",font=("times new roman",30,'bold'),pady=2).pack(fill=X)
        #==================================var declare===================
        #================cosmetic
        self.c1=IntVar()
        self.c2=IntVar()
        self.c3=IntVar()
        self.c4=IntVar()
        self.c5=IntVar()
        self.c6=IntVar()
        self.c1_t=IntVar()
        self.c2_t=IntVar()
        self.c3_t=IntVar()
        self.c4_t=IntVar()
        self.c5_t=IntVar()
        self.c6_t=IntVar()
        #==============================groceries
        self.g1=IntVar()
        self.g2=IntVar()
        self.g3=IntVar()
        self.g4=IntVar()
        self.g5=IntVar()
        self.g6=IntVar()
        self.g1_t=IntVar()
        self.g2_t=IntVar()
        self.g3_t=IntVar()
        self.g4_t=IntVar()
        self.g5_t=IntVar()
        self.g6_t=IntVar()

        #=================================beverages
        self.b1=IntVar()
        self.b2=IntVar()
        self.b3=IntVar()
        self.b4=IntVar()
        self.b5=IntVar()
        self.b6=IntVar()
        self.b1_t=IntVar()
        self.b2_t=IntVar()
        self.b3_t=IntVar()
        self.b4_t=IntVar()
        self.b5_t=IntVar()
        self.b6_t=IntVar()
        #=======================cust details
        self.cname=StringVar()
        self.cphn=StringVar()
        x=random.randint(1000,9999)
        self.bill_no=StringVar()
        self.bill_no.set(str(x))
        self.search_bill=StringVar()

        #========================amount end
        self.c_total=StringVar()
        self.g_total=StringVar()
        self.b_total=StringVar()
        self.c_tax=StringVar()
        self.b_tax=StringVar()
        self.g_tax=StringVar()
        self.total_amt=IntVar()
        self.total_tax=IntVar()
        self.Total=IntVar()


        #==============================total each


        #==========cust details================
        F1=LabelFrame(self.root,bd=10,relief=GROOVE,text="Customer details",font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
        F1.place(x=0,y=80,relwidth=1)

        cname_lbl=Label(F1,text="Customer Name",font=("times new roman",18,"bold"),bg=bg_color,fg="white").grid(row=0,column=0,padx=20,pady=5)
        xname_txt=Entry(F1,width=15,textvariable=self.cname,font=("arial",15),relief=SUNKEN,bd=2).grid(row=0,column=1,pady=5,padx=10)
        
        cphn_lbl=Label(F1,text="Phone No.",font=("times new roman",18,"bold"),bg=bg_color,fg="white").grid(row=0,column=2,padx=20,pady=5)
        xphn_txt=Entry(F1,width=15,font=("arial",15),relief=SUNKEN,bd=2,textvariable=self.cphn).grid(row=0,column=3,pady=5,padx=10)
        
        cbill_lbl=Label(F1,text="Bill Number",font=("times new roman",18,"bold"),bg=bg_color,fg="white").grid(row=0,column=4,padx=20,pady=5)
        xbill_txt=Entry(F1,width=15,font=("arial",15),relief=SUNKEN,bd=2,textvariable=self.search_bill).grid(row=0,column=5,pady=5,padx=10)

        bill_btn=Button(F1,text="Search",command=self.find_bill,width=10,bd=7,font="arial 12 bold").grid(row=0,column=6,pady=5,padx=10)
        #==================cosmetic 
        F2=LabelFrame(self.root,bd=10,relief=GROOVE,text="Cosmetics",font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
        F2.place(x=0,y=170,width=325,height=380)

        c1_lbl=Label(F2,text="Bath soap",font=("times new roman",18,"bold"),bg=bg_color,fg="lightgreen").grid(row=0,column=0,padx=10,pady=12,sticky="w")
        c1_txt=Entry(F2,width=10,font=("arial",15),relief=SUNKEN,bd=2,textvariable=self.c1).grid(row=0,column=1,pady=10,padx=10)

        c2_lbl=Label(F2,text="Face cream",font=("times new roman",18,"bold"),bg=bg_color,fg="lightgreen").grid(row=1,column=0,padx=10,pady=12,sticky="w")
        c2_txt=Entry(F2,width=10,font=("arial",15),relief=SUNKEN,bd=2,textvariable=self.c2).grid(row=1,column=1,pady=10,padx=10)

        c3_lbl=Label(F2,text="Face wash",font=("times new roman",18,"bold"),bg=bg_color,fg="lightgreen").grid(row=2,column=0,padx=10,pady=12,sticky="w")
        c3_txt=Entry(F2,width=10,font=("arial",15),relief=SUNKEN,bd=2,textvariable=self.c3).grid(row=2,column=1,pady=10,padx=10)

        c4_lbl=Label(F2,text="Shampoo",font=("times new roman",18,"bold"),bg=bg_color,fg="lightgreen").grid(row=3,column=0,padx=10,pady=12,sticky="w")
        c4_txt=Entry(F2,width=10,font=("arial",15),relief=SUNKEN,bd=2,textvariable=self.c4).grid(row=3,column=1,pady=10,padx=10)

        c5_lbl=Label(F2,text="Body Lotion",font=("times new roman",18,"bold"),bg=bg_color,fg="lightgreen").grid(row=4,column=0,padx=10,pady=12,sticky="w")
        c5_txt=Entry(F2,width=10,font=("arial",15),relief=SUNKEN,bd=2,textvariable=self.c5).grid(row=4,column=1,pady=10,padx=10)

        c6_lbl=Label(F2,text="Deodrant",font=("times new roman",18,"bold"),bg=bg_color,fg="lightgreen").grid(row=5,column=0,padx=10,pady=12,sticky="w")
        c6_txt=Entry(F2,width=10,font=("arial",15),relief=SUNKEN,bd=2,textvariable=self.c6).grid(row=5,column=1,pady=10,padx=10)

        #=============================grocery
        F3=LabelFrame(self.root,bd=10,relief=GROOVE,text="Groceries",font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
        F3.place(x=330,y=170,width=325,height=380)

        g1_lbl=Label(F3,text="Rice",font=("times new roman",18,"bold"),bg=bg_color,fg="lightgreen").grid(row=0,column=0,padx=10,pady=12,sticky="w")
        g1_txt=Entry(F3,width=10,font=("arial",15),relief=SUNKEN,bd=2,textvariable=self.g1).grid(row=0,column=1,pady=10,padx=10)

        g2_lbl=Label(F3,text="Pulses",font=("times new roman",18,"bold"),bg=bg_color,fg="lightgreen").grid(row=1,column=0,padx=10,pady=12,sticky="w")
        g2_txt=Entry(F3,width=10,font=("arial",15),relief=SUNKEN,bd=2,textvariable=self.g2).grid(row=1,column=1,pady=10,padx=10)

        g3_lbl=Label(F3,text="Wheat",font=("times new roman",18,"bold"),bg=bg_color,fg="lightgreen").grid(row=2,column=0,padx=10,pady=12,sticky="w")
        g3_txt=Entry(F3,width=10,font=("arial",15),relief=SUNKEN,bd=2,textvariable=self.g3).grid(row=2,column=1,pady=10,padx=10)

        g4_lbl=Label(F3,text="Food oil",font=("times new roman",18,"bold"),bg=bg_color,fg="lightgreen").grid(row=3,column=0,padx=10,pady=12,sticky="w")
        g4_txt=Entry(F3,width=10,font=("arial",15),relief=SUNKEN,bd=2,textvariable=self.g4).grid(row=3,column=1,pady=10,padx=10)

        g5_lbl=Label(F3,text="Biscuits",font=("times new roman",18,"bold"),bg=bg_color,fg="lightgreen").grid(row=4,column=0,padx=10,pady=12,sticky="w")
        g5_txt=Entry(F3,width=10,font=("arial",15),relief=SUNKEN,bd=2,textvariable=self.g5).grid(row=4,column=1,pady=10,padx=10)

        g6_lbl=Label(F3,text="Sugar",font=("times new roman",18,"bold"),bg=bg_color,fg="lightgreen").grid(row=5,column=0,padx=10,pady=12,sticky="w")
        g6_txt=Entry(F3,width=10,font=("arial",15),relief=SUNKEN,bd=2,textvariable=self.g6).grid(row=5,column=1,pady=10,padx=10)

        #===============================beverage
        F4=LabelFrame(self.root,bd=10,relief=GROOVE,text="Beverages",font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
        F4.place(x=655,y=170,width=325,height=380)

        b1_lbl=Label(F4,text="Tea",font=("times new roman",18,"bold"),bg=bg_color,fg="lightgreen").grid(row=0,column=0,padx=10,pady=12,sticky="w")
        b1_txt=Entry(F4,width=10,font=("arial",15),relief=SUNKEN,bd=2,textvariable=self.b1).grid(row=0,column=1,pady=10,padx=10)

        b2_lbl=Label(F4,text="Thumbs up",font=("times new roman",18,"bold"),bg=bg_color,fg="lightgreen").grid(row=1,column=0,padx=10,pady=12,sticky="w")
        b2_txt=Entry(F4,width=10,font=("arial",15),relief=SUNKEN,bd=2,textvariable=self.b2).grid(row=1,column=1,pady=10,padx=10)

        b3_lbl=Label(F4,text="Coffee",font=("times new roman",18,"bold"),bg=bg_color,fg="lightgreen").grid(row=2,column=0,padx=10,pady=12,sticky="w")
        b3_txt=Entry(F4,width=10,font=("arial",15),relief=SUNKEN,bd=2,textvariable=self.b3).grid(row=2,column=1,pady=10,padx=10)

        b4_lbl=Label(F4,text="Coca Cola",font=("times new roman",18,"bold"),bg=bg_color,fg="lightgreen").grid(row=3,column=0,padx=10,pady=12,sticky="w")
        b4_txt=Entry(F4,width=10,font=("arial",15),relief=SUNKEN,bd=2,textvariable=self.b4).grid(row=3,column=1,pady=10,padx=10)

        b5_lbl=Label(F4,text="Mtn Dew",font=("times new roman",18,"bold"),bg=bg_color,fg="lightgreen").grid(row=4,column=0,padx=10,pady=12,sticky="w")
        b5_txt=Entry(F4,width=10,font=("arial",15),relief=SUNKEN,bd=2,textvariable=self.b5).grid(row=4,column=1,pady=10,padx=10)

        b6_lbl=Label(F4,text="Fanta",font=("times new roman",18,"bold"),bg=bg_color,fg="lightgreen").grid(row=5,column=0,padx=10,pady=12,sticky="w")
        b6_txt=Entry(F4,width=10,font=("arial",15),relief=SUNKEN,bd=2,textvariable=self.b6).grid(row=5,column=1,pady=10,padx=10)

        #==================bill area

        F5=Frame(self.root,bd=10,relief=GROOVE)
        F5.place(x=980,y=170,width=360,height=380)

        bill_title=Label(F5,text="Bill Area",font='arial 15 bold',bd=7,relief=GROOVE).pack(fill=X)
        scroll_y=Scrollbar(F5,orient=VERTICAL)
        self.txtarea=Text(F5,yscrollcommand=scroll_y.set)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_y.config(command=self.txtarea.yview)
        self.txtarea.pack()

        #============button frame==========
        F6=LabelFrame(self.root,bd=10,relief=GROOVE,text="Function Panel",font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
        F6.place(x=0,y=550,relwidth=1,height=140)

        m1_lbl=Label(F6,text="Total Cosmetic Amount",font=("times new roman",15,"bold"),bg=bg_color,fg="lightgreen").grid(row=0,column=0,padx=10,pady=1,sticky="w")
        m1_txt=Entry(F6,width=10,font=("arial",15),relief=SUNKEN,bd=2,textvariable=self.c_total).grid(row=0,column=1,pady=1,padx=10)

        m2_lbl=Label(F6,text="Total Groceries Amount",font=("times new roman",15,"bold"),bg=bg_color,fg="lightgreen").grid(row=1,column=0,padx=10,pady=1,sticky="w")
        m2_txt=Entry(F6,width=10,font=("arial",15),relief=SUNKEN,bd=2,textvariable=self.g_total).grid(row=1,column=1,pady=1,padx=10)

        m3_lbl=Label(F6,text="Total Beverages Amount",font=("times new roman",15,"bold"),bg=bg_color,fg="lightgreen").grid(row=2,column=0,padx=10,pady=1,sticky="w")
        m3_txt=Entry(F6,width=10,font=("arial",15),relief=SUNKEN,bd=2,textvariable=self.b_total).grid(row=2,column=1,pady=1,padx=10)
        
        m4_lbl=Label(F6,text="Cosmetic Tax",font=("times new roman",15,"bold"),bg=bg_color,fg="lightgreen").grid(row=0,column=2,padx=10,pady=1,sticky="w")
        m4_txt=Entry(F6,width=10,font=("arial",15),relief=SUNKEN,bd=2,textvariable=self.c_tax).grid(row=0,column=3,pady=1,padx=10)

        m5_lbl=Label(F6,text="Groceries Tax",font=("times new roman",15,"bold"),bg=bg_color,fg="lightgreen").grid(row=1,column=2,padx=10,pady=1,sticky="w")
        m5_txt=Entry(F6,width=10,font=("arial",15),relief=SUNKEN,bd=2,textvariable=self.g_tax).grid(row=1,column=3,pady=1,padx=10)

        m6_lbl=Label(F6,text="Beverages Tax",font=("times new roman",15,"bold"),bg=bg_color,fg="lightgreen").grid(row=2,column=2,padx=10,pady=1,sticky="w")
        m6_txt=Entry(F6,width=10,font=("arial",15),relief=SUNKEN,bd=2,textvariable=self.b_tax).grid(row=2,column=3,pady=1,padx=10)
        
        btn_F=Frame(F6,bd=7,relief=GROOVE)
        btn_F.place(x=750,width=580,height=105)

        total_btn=Button(btn_F,text="Total",command=self.total,bg='cadetblue',fg='white',bd=2,width=10,pady=15,font='arial 15 bold').grid(row=0,column=0,padx=5,pady=5)
        gen_bill_btn=Button(btn_F,text="Generate Bill",command=self.bill_area,bg='cadetblue',fg='white',bd=2,width=10,pady=15,font='arial 15 bold').grid(row=0,column=1,padx=5,pady=5)
        clear_btn=Button(btn_F,text="Clear",command=self.clear_bill,bg='cadetblue',fg='white',bd=2,width=10,pady=15,font='arial 15 bold').grid(row=0,column=2,padx=5,pady=5)
        exit_btn=Button(btn_F,text="Exit",command=self.exit_app,bg='cadetblue',fg='white',bd=2,width=10,pady=15,font='arial 15 bold').grid(row=0,column=3,padx=5,pady=5)
        self.welcome_bill()
    
    def total(self):
        self.c1_t=self.c1.get()*40
        self.c2_t=self.c2.get()*200
        self.c3_t=self.c3.get()*70
        self.c4_t=self.c4.get()*150
        self.c5_t=self.c5.get()*100
        self.c6_t=self.c6.get()*300
        self.total_c=float(self.c1_t+self.c2_t+self.c3_t+self.c4_t+self.c5_t+self.c6_t)
        self.c_total.set('Rs.'+str(self.total_c))
        self.c_tax.set('Rs.'+str(self.total_c*0.05))

        self.g1_t=self.g1.get()*40
        self.g2_t=self.g2.get()*200
        self.g3_t=self.g3.get()*70
        self.g4_t=self.g4.get()*150
        self.g5_t=self.g5.get()*100
        self.g6_t=self.g6.get()*300
        self.total_g=float(self.g1_t+self.g2_t+self.g3_t+self.g4_t+self.g5_t+self.g6_t)
        self.g_total.set('Rs.'+str(self.total_g))
        self.g_tax.set('Rs.'+str(self.total_g*0.05))

        self.b1_t=self.b1.get()*40
        self.b2_t=self.b2.get()*200
        self.b3_t=self.b3.get()*70
        self.b4_t=self.b4.get()*150
        self.b5_t=self.b5.get()*100
        self.b6_t=self.b6.get()*300
        self.total_b=float(self.b1_t+self.b2_t+self.b3_t+self.b4_t+self.b5_t+self.b6_t)
        self.b_total.set('Rs.'+str(self.total_b))
        self.b_tax.set('Rs.'+str(self.total_b*0.05))

        self.total_amt=self.total_b+self.total_g+self.total_c
        self.total_tax=(self.total_b*0.05)+(self.total_g*0.05)+(self.total_c*0.05)
        self.Total=self.total_amt+self.total_tax

        
    
    def welcome_bill(self):
        self.txtarea.delete(1.0,END)
        self.txtarea.insert(END,'\t  Welcome to Spencers')
        self.txtarea.insert(END,f"\n Bill Number :{self.bill_no.get()}")
        self.txtarea.insert(END,f'\n Customer Name :{self.cname.get()}')
        self.txtarea.insert(END,f'\n Customer Phone :{self.cphn.get()}')
        self.txtarea.insert(END,'\n=======================================')
        self.txtarea.insert(END,'\n Products\t\t\tQTY\tAmount')
        self.txtarea.insert(END,'\n=======================================')

    def bill_area(self):
        if self.cname.get()=="" or self.cphn.get()=="":
            messagebox.showerror('Error','Customer Details Mandatory')
        elif self.total_amt==0.0:
            messagebox.showerror('Error','No items selected')
        else:
            self.welcome_bill()
            #====================cosmetics=========================
            if self.c1.get()!=0:
                self.txtarea.insert(END,f'\nBath Soap\t\t\t{self.c1.get()}\t{self.c1_t}')
            if self.c2.get()!=0:
                self.txtarea.insert(END,f'\nFace Cream\t\t\t{self.c2.get()}\t{self.c2_t}')
            if self.c3.get()!=0:
                self.txtarea.insert(END,f'\nFace Wash\t\t\t{self.c3.get()}\t{self.c3_t}')
            if self.c4.get()!=0:
                self.txtarea.insert(END,f'\nShampoo\t\t\t{self.c4.get()}\t{self.c4_t}')
            if self.c5.get()!=0:
                self.txtarea.insert(END,f'\nBody Lotion\t\t\t{self.c5.get()}\t{self.c5_t}')
            if self.c6.get()!=0:
                self.txtarea.insert(END,f'\nDeodrant\t\t\t{self.c6.get()}\t{self.c6_t}')
            #============================groceries===========================
            if self.g1.get()!=0:
                self.txtarea.insert(END,f'\nRice\t\t\t{self.g1.get()}\t{self.g1_t}')
            if self.g2.get()!=0:
                self.txtarea.insert(END,f'\nPulses\t\t\t{self.g2.get()}\t{self.g2_t}')
            if self.g3.get()!=0:
                self.txtarea.insert(END,f'\nWheat\t\t\t{self.g3.get()}\t{self.g3_t}')
            if self.g4.get()!=0:
                self.txtarea.insert(END,f'\nFood Oil\t\t\t{self.g4.get()}\t{self.g4_t}')
            if self.g5.get()!=0:
                self.txtarea.insert(END,f'\nBiscuits\t\t\t{self.g5.get()}\t{self.g5_t}')
            if self.g6.get()!=0:
                self.txtarea.insert(END,f'\nSugar\t\t\t{self.g6.get()}\t{self.g6_t}')

            #==============================beverages=============================
            if self.b1.get()!=0:
                self.txtarea.insert(END,f'\nTea\t\t\t{self.b1.get()}\t{self.b1_t}')
            if self.b2.get()!=0:
                self.txtarea.insert(END,f'\nThums Up\t\t\t{self.b2.get()}\t{self.b2_t}')
            if self.b3.get()!=0:
                self.txtarea.insert(END,f'\nCoffee\t\t\t{self.b3.get()}\t{self.b3_t}')
            if self.b4.get()!=0:
                self.txtarea.insert(END,f'\nCoca Cola\t\t\t{self.b4.get()}\t{self.b4_t}')
            if self.b5.get()!=0:
                self.txtarea.insert(END,f'\nMtn Dew\t\t\t{self.b5.get()}\t{self.b5_t}')
            if self.b6.get()!=0:
                self.txtarea.insert(END,f'\nFanta\t\t\t{self.b6.get()}\t{self.b6_t}')
            
            #=======================bill=================================
            self.txtarea.insert(END,'\n=======================================')
            self.txtarea.insert(END,f'\nTotal amount:\t\t\t\t {self.total_amt}')
            self.txtarea.insert(END,f'\nTotal tax:\t\t\t\t   {self.total_tax}')
            self.txtarea.insert(END,'\n=======================================')
            self.txtarea.insert(END,f'\nTotal amount to pay:\t\t\t\t  {self.Total}')
            self.save_bill()
    

    def save_bill(self):
        op=messagebox.askyesno('Save Bill','Do you want to save bill?')
        if op>0:
            self.bill_data=self.txtarea.get('1.0',END)
            f=open('E:\\Programming Lang and Projects\\Python\\Bills Gen\\'+str(self.bill_no.get())+'.txt','w')
            messagebox.showinfo('Saved',f'Bill no.:{self.bill_no.get()} saved successfully')
            f.write(self.bill_data)
            f.close()
        else:
            return
    
    def find_bill(self):
        present='NO'
        for i in os.listdir('E:\\Programming Lang and Projects\\Python\\Bills Gen\\'):
            if i.split('.')[0]==self.search_bill.get():
                f1=open(f'E:\\Programming Lang and Projects\\Python\\Bills Gen\\{i}','r')
                self.txtarea.delete('1.0',END)
                for d in f1:
                    self.txtarea.insert(END,d)
                f1.close()
                present='YES'
        if present=='NO':
                messagebox.showerror('Error',f'Invalid Bill no.:{self.search_bill.get()}')

    
    def clear_bill(self):
        op=messagebox.askyesno('Clear Bill','Do you want to clear the bill?')
        if op>0:
            self.c1.set(0)
            self.c2.set(0)
            self.c3.set(0)
            self.c4.set(0)
            self.c5.set(0)
            self.c6.set(0)
            self.c1_t=0
            self.c2_t=0
            self.c3_t=0
            self.c4_t=0
            self.c5_t=0
            self.c6_t=0
            #==============================groceries
            self.g1.set(0)
            self.g2.set(0)
            self.g3.set(0)
            self.g4.set(0)
            self.g5.set(0)
            self.g6.set(0)
            self.g1_t=0
            self.g2_t=0
            self.g3_t=0
            self.g4_t=0
            self.g5_t=0
            self.g6_t=0

            #=================================beverages
            self.b1.set(0)
            self.b2.set(0)
            self.b3.set(0)
            self.b4.set(0)
            self.b5.set(0)
            self.b6.set(0)
            self.b1_t=0
            self.b2_t=0
            self.b3_t=0
            self.b4_t=0
            self.b5_t=0
            self.b6_t=0
            #=======================cust details
            self.cname.set("")
            self.cphn.set("")
            x=random.randint(1000,9999)
            self.bill_no.set("")
            self.bill_no.set(str(x))
            self.search_bill.set("")

            #========================amount end
            self.c_total.set("")
            self.g_total.set("")
            self.b_total.set("")
            self.c_tax.set("")
            self.b_tax.set("")
            self.g_tax.set("")
            self.total_amt=0
            self.total_tax=0
            self.Total=0
            self.welcome_bill()
        else:
            return
    
    def exit_app(self):
        op=messagebox.askyesno('Exit','Do you want to exit the app?')
        if op>0:
            self.root.destroy()
        else:
            return


root=Tk()
obj=Bill_app(root)
root.mainloop()
