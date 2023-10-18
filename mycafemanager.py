from tkinter import *
import tkinter.messagebox
import time
import datetime
import random

form1=tkinter.Tk()
form1.title('my cafe')
form1.geometry('1350x750+0+0')
form1.configure(background="white")
rest=Canvas(form1,width=300,height=500)
rest.place(x=200,y=200)
rest=PhotoImage(file="C:/Users\/Dahiya/OneDrive/Desktop/wineb1.PNG")
lblimg=Label(image=rest,background='black',bd=4,bg='black').place(x=510,y=150)

#frames
f1_caption=Frame(form1,bg="crimson",borderwidth=8,relief=RIDGE,bd=16)
f1_caption.pack(side=TOP)
f2_menu=Frame(form1,bg="sea green",borderwidth=4,bd=8,relief=RIDGE)
f2_menu.place(x=0,y=113)
f2_drinks=Frame(f2_menu,bg="sea green",borderwidth=4,bd=8,relief=RIDGE)
f2_drinks.pack(side=LEFT)
f2_dishes=Frame(f2_menu,bg="sea green",borderwidth=4,bd=8,relief=RIDGE)
f2_dishes.pack(side=RIGHT)
f2_details=Frame(form1,bg="sea green",bd=4,relief=RIDGE)
f2_details.place(x=925,y=113)
cal_main=Frame(form1,bg="sea green",borderwidth=4,bd=8,relief=RIDGE)
cal_main.place(x=7,y=418)
cal_buttons=Frame(cal_main,bg="sea green",borderwidth=4,bd=8,relief=RIDGE)
cal_buttons.pack(side=TOP)
cal_receipt=Frame(form1,bg="sea green",borderwidth=8,relief=RIDGE,bd=8)
cal_receipt.place(x=925,y=218)
cal_lastbtn=Frame(form1,bg="sea green",borderwidth=4,bd=8,relief=RIDGE)
cal_lastbtn.place(x=925,y=635)

#form1 labels
lbl1=Label(f1_caption,text="----****----Rahul's Food----****----",font=("arial",48,"bold"),background="crimson")
lbl1.pack(side=TOP)
#lbl8=Label(form1,text="Drinks",font=("arial",32,"bold"),background="orange")
#lbl8.place(x=80,y=65)
#lbl9=Label(form1,text="Dishes",font=("arial",32,"bold"),background="orange")
#lbl9.place(x=290,y=65)

#variables
var1=IntVar()
var2=IntVar()
var3=IntVar()
var4=IntVar()
var5=IntVar()
var6=IntVar()
var7=IntVar()
var8=IntVar()
var9=IntVar()
var10=IntVar()
var11=IntVar()
var12=IntVar()
var13=IntVar()
var14=IntVar()
var15=IntVar()
var16=IntVar()

dateoforder=StringVar()
receipt_ref=StringVar()
paidtax=StringVar()
subtotal=StringVar()
totalcost=StringVar()
costofdrinks=StringVar()
costofdishes=StringVar()
servicecharge=StringVar()

text_Input=StringVar()
operator=""

E_thumbsup=StringVar()
E_redbull=StringVar()
E_7up=StringVar()
E_bira=StringVar()
E_corona=StringVar()
E_cocacola=StringVar()
E_fanta=StringVar()
E_beer=StringVar()

E_pizza=StringVar()
E_burger=StringVar()
E_fries=StringVar()
E_paneer=StringVar()
E_dal=StringVar()
E_roti=StringVar()
E_paratha=StringVar()
E_chefspecial=StringVar()

E_thumbsup.set("0")
E_redbull.set("0")
E_7up.set("0")
E_bira.set("0")
E_corona.set("0")
E_cocacola.set("0")
E_fanta.set("0")
E_beer.set("0")

E_pizza.set("0")
E_burger.set("0")
E_fries.set("0")
E_paneer.set("0")
E_dal.set("0")
E_roti.set("0")
E_paratha.set("0")
E_chefspecial.set("0")

dateoforder.set(time.strftime("%d/%m/%y"))

#function decleration
class fundeclare:
    def iExit(self):
        iExit=tkinter.messagebox.askyesno("Exit","are you sure?")
        if iExit>0:
            form1.destroy()
            return

    def reset(self):
        E_thumbsup.set("0")
        E_redbull.set("0")
        E_7up.set("0")
        E_bira.set("0")
        E_corona.set("0")
        E_cocacola.set("0")
        E_fanta.set("0")
        E_beer.set("0")

        E_pizza.set("0")
        E_burger.set("0")
        E_fries.set("0")
        E_paneer.set("0")
        E_dal.set("0")
        E_roti.set("0")
        E_paratha.set("0")
        E_chefspecial.set("0")

        costofdishes.set("0")
        costofdrinks.set("0")
        servicecharge.set("0")
        subtotal.set("0")
        paidtax.set("0")
        totalcost.set("0")

        var1.set(0)
        var2.set(0)
        var3.set(0)
        var4.set(0)
        var5.set(0)
        var6.set(0)
        var7.set(0)
        var8.set(0)
        var9.set(0)
        var10.set(0)
        var11.set(0)
        var12.set(0)
        var13.set(0)
        var14.set(0)
        var15.set(0)
        var16.set(0)

        txtthumbsup.configure(state=DISABLED)
        txtredbull.configure(state=DISABLED)
        txt7up.configure(state=DISABLED)
        txtbira.configure(state=DISABLED)
        txtcorona.configure(state=DISABLED)
        txtcocacola.configure(state=DISABLED)
        txtfanta.configure(state=DISABLED)
        txtbeer.configure(state=DISABLED)
        txtpizza.configure(state=DISABLED)
        txtburger.configure(state=DISABLED)
        txtfries.configure(state=DISABLED)
        txtpaneer.configure(state=DISABLED)
        txtdal.configure(state=DISABLED)
        txtroti.configure(state=DISABLED)
        txtparatha.configure(state=DISABLED)
        txtchefspecial.configure(state=DISABLED)

    def costofitems(self):
        item1=float(E_thumbsup.get())
        item2=float(E_redbull.get())
        item3=float(E_7up.get())
        item4=float(E_bira.get())
        item5=float(E_corona.get())
        item6=float(E_cocacola.get())
        item7=float(E_fanta.get())
        item8=float(E_beer.get())

        item9=float(E_pizza.get())
        item10=float(E_burger.get())
        item11=float(E_fries.get())
        item12=float(E_paneer.get())
        item13=float(E_dal.get())
        item14=float(E_roti.get())
        item15=float(E_paratha.get())
        item16=float(E_chefspecial.get())

        priceofdrinks=((item1 * 40)+(item2 * 120)+(item3 * 40)+(item4 * 200)+
                       (item5 * 150)+(item6 * 40)+(item7 * 40)+(item8 * 200))
        priceofdishes=((item9 * 200)+(item10 * 150)+(item11 * 100)+(item12 * 200)
                       +(item13 * 180)+(item14 * 40)+(item15 * 80)+(item16 * 400))

        drinksprice="Rs",str('%.2f'%(priceofdrinks))
        dishesprice="Rs",str('%.2f'%(priceofdishes))
        costofdishes.set(dishesprice)
        costofdrinks.set(drinksprice)
        sc="Rs",str('%.2f'%(2.5))
        servicecharge.set(sc)

        SubTotalofItems="Rs",str('%.2f'%(priceofdrinks+priceofdishes+2.5))
        subtotal.set(SubTotalofItems)

        tax="Rs",str('%.2f'%((priceofdishes+priceofdrinks+2.5)*0.2))
        paidtax.set(tax)
        tt=((priceofdishes+priceofdrinks+2.5)*0.2)
        tc="Rs",str('%.2f'%(priceofdishes+priceofdrinks+2.5+tt))
        totalcost.set(tc)

    def chkthumbsup(self):
        if (var1.get()==1):
            txtthumbsup.configure(state=NORMAL)
            txtthumbsup.focus()
            txtthumbsup.delete('0',END)
            E_thumbsup.set("")
        elif(var1.get()==0):
            txtthumbsup.configure(state=DISABLED)
            E_thumbsup.set("0")

    def chkredbull(self):
        if(var2.get()==1):
            txtredbull.configure(state=NORMAL)
            txtredbull.focus()
            txtredbull.delete('0',END)
            E_redbull.set("")
        elif(var1.get()==0):
            txtredbull.configure(state=DISABLED)
            E_redbull.set("0")
        
    def chk7up(self):
        if(var3.get()==1):
            txt7up.configure(state=NORMAL)
            txt7up.focus()
            txt7up.delete('0',END)
            E_7up.set("")
        elif(var3.get()==0):
            txt7up.configure(state=DISABLED)
            E_7up.set("0")

    def chkbira(self):
        if(var4.get()==1):
            txtbira.configure(state=NORMAL)
            txtbira.focus()
            txtbira.delete('0',END)
            E_bira.set("")
        elif(var4.get()==0):
            txtbira.configure(state=DISABLED)
            E_bira.set("")

    def chkcorona(self):
        if(var5.get()==1):
            txtcorona.configure(state=NORMAL)
            txtcorona.focus()
            txtcorona.delete('0',END)
            E_corona.set("")
        elif(var5.get()==0):
            txtcorona.configure(state=DISABLED)
            E_corona.set("")

    def chkcocacola(self):
        if(var6.get()==1):
            txtcocacola.configure(state=NORMAL)
            txtcocacola.focus()
            txtcocacola.delete('0',END)
            E_cocacola.set("")
        elif(var6.get()==0):
            txtcocacola.congfigure(state=DISABLED)
            E_cocacola.set("")

    def chkfanta(self):
        if(var7.get()==1):
            txtfanta.configure(state=NORMAL)
            txtfanta.focus()
            txtfanta.delete('0',END)
            E_fanta.set("")
        elif(var7.get()==0):
            txtfanta.configure(state=DISABLED)
            E_fanta.set("")

    def chkbeer(self):
        if(var8.get()==1):
            txtbeer.configure(state=NORMAL)
            txtbeer.focus()
            txtbeer.delete('0',END)
            E_beer.set("")
        elif(var8.get()==0):
            txtbeer.configure(state=DISABLED)
            E_fanta.set("")
    
    def chkpizza(self):
        if(var9.get()==1):
            txtpizza.configure(state=NORMAL)
            txtpizza.focus()
            txtpizza.delete('0',END)
            E_pizza.set("")
        elif(var9.get()==0):
            txtpizza.configure(state=DISABLED)
            E_pizza.set("")

    def chkburger(self):
        if(var10.get()==1):
            txtburger.configure(state=NORMAL)
            txtburger.focus()
            txtburger.delete('0',END)
            E_burger.set("")
        elif(var10.get()==0):
            txtburger.configure(state=DISABLED)
            E_burger.set("")

    def chkfries(self):
        if(var11.get()==1):
            txtfries.configure(state=NORMAL)
            txtfries.focus()
            txtfries.delete('0',END)
            E_fries.set("")
        elif(var11.get()==0):
            txtfries.configure(state=DISABLED)
            E_fries.set("")

    def chkpaneer(self):
        if(var12.get()==1):
            txtpaneer.configure(state=NORMAL)
            txtpaneer.focus()
            txtpaneer.delete('0',END)
        elif(var12.get()==0):
            txtpaneer.configure(state=DISABLED)
            E_paneer.set("")

    def chkdal(self):
        if(var13.get()==1):
            txtdal.configure(state=NORMAL)
            txtdal.focus()
            txtdal.delete('0',END)
        elif(var13.get()==0):
            txtdal.configure(state=DISABLED)
            E_dal.set("")

    def chkroti(self):
        if(var14.get()==1):
            txtroti.configure(state=NORMAL)
            txtroti.focus()
            txtroti.delete('0',END)
        elif(var14.get()==0):
            txtroti.configure(state=DISABLED)
            E_roti.set("")

    def chkparatha(self):
        if(var15.get()==1):
            txtparatha.configure(state=NORMAL)
            txtparatha.focus()
            txtparatha.delete('0',END)
        elif(var15.get()==0):
            txtparatha.configure(state=DISABLED)
            E_paratha.set("")

    def chkchefspecial(self):
        if(var16.get()==1):
            txtchefspecial.configure(state=NORMAL)
            txtchefspecial.focus()
            txtchefspecial.delete('0',END)
        elif(var16.get()==0):
            txtchefspecial.configure(state=DISABLED)
            E_chefspecial.set("")

    def receipt(self):
        txtreceipt.delete("1.0",END)
        x=random.randint(10903,609235)
        randomref=str(x)
        receipt_ref.set("Bill"+randomref)

        txtreceipt.insert(END,'Receipt Ref:\t'+receipt_ref.get()+"\t\t"+dateoforder.get()+"\n")
        txtreceipt.insert(END,'Item:\t\t\t'+"No of Items\n")
        txtreceipt.insert(END,'Thumbsup:\t\t\t'+E_thumbsup.get()+"\n")
        txtreceipt.insert(END,'Redbull:\t\t\t'+E_redbull.get()+"\n")
        txtreceipt.insert(END,'7Up:\t\t\t'+E_7up.get()+"\n")
        txtreceipt.insert(END,'Bira:\t\t\t'+E_bira.get()+"\n")
        txtreceipt.insert(END,'Corona:\t\t\t'+E_corona.get()+"\n")
        txtreceipt.insert(END,'Cocacola:\t\t\t'+E_cocacola.get()+"\n")
        txtreceipt.insert(END,'Fanta:\t\t\t'+E_fanta.get()+"\n")
        txtreceipt.insert(END,'Beer:\t\t\t'+E_beer.get()+"\n")
        txtreceipt.insert(END,'Pizza:\t\t\t'+E_pizza.get()+"\n")
        txtreceipt.insert(END,'Burger:\t\t\t'+E_burger.get()+"\n")
        txtreceipt.insert(END,'Fries:\t\t\t'+E_fries.get()+"\n")
        txtreceipt.insert(END,'Paneer:\t\t\t'+E_paneer.get()+"\n")
        txtreceipt.insert(END,'Dal:\t\t\t'+E_dal.get()+"\n")
        txtreceipt.insert(END,'Roti:\t\t\t'+E_roti.get()+"\n")
        txtreceipt.insert(END,'Paratha:\t\t\t'+E_paratha.get()+"\n")
        txtreceipt.insert(END,'Chefs Special:\t\t\t'+E_chefspecial.get()+"\n")

obj=fundeclare()

#checkbuttons for drinks
cthumbsup=Checkbutton(f2_drinks,text="ThumbsUp",font=("arial",14,"bold"),bg="sea green",variable=var1,onvalue=1,offvalue=0,command=obj.chkthumbsup)
cthumbsup.grid(row=1,column=0,sticky=W)
credbull=Checkbutton(f2_drinks,text="Red Bull",font=("arial",14,"bold"),bg="sea green",variable=var2,onvalue=1,offvalue=0,command=obj.chkredbull)
credbull.grid(row=2,column=0,sticky=W)
c7up=Checkbutton(f2_drinks,text="7 Up",font=("arial",14,"bold"),bg="sea green",variable=var3,onvalue=1,offvalue=0,command=obj.chk7up)
c7up.grid(row=3,column=0,sticky=W)
cbira=Checkbutton(f2_drinks,text="Bira",font=("arial",14,"bold"),bg="sea green",variable=var4,onvalue=1,offvalue=0,command=obj.chkbira)
cbira.grid(row=4,column=0,sticky=W)
ccorona=Checkbutton(f2_drinks,text="Corona",font=("arial",14,"bold"),bg="sea green",variable=var5,onvalue=1,offvalue=0,command=obj.chkcorona)
ccorona.grid(row=5,column=0,sticky=W)
ccocacola=Checkbutton(f2_drinks,text="Coca Cola",font=("arial",14,"bold"),bg="sea green",variable=var6,onvalue=1,offvalue=0,command=obj.chkcocacola)
ccocacola.grid(row=6,column=0,sticky=W)
cfanta=Checkbutton(f2_drinks,text="Fanta",font=("arial",14,"bold"),bg="sea green",variable=var7,onvalue=1,offvalue=0,command=obj.chkfanta)
cfanta.grid(row=7,column=0,sticky=W)
cbeer=Checkbutton(f2_drinks,text="Beer",font=("arial",14,"bold"),bg="sea green",variable=var8,onvalue=1,offvalue=0,command=obj.chkbeer)
cbeer.grid(row=8,column=0,sticky=W)

#entrybox for drinks
txtthumbsup=Entry(f2_drinks,font=("arial",14,"bold"),bd=4,width=7,justify=LEFT,state=DISABLED,textvariable=E_thumbsup)
txtthumbsup.grid(row=1,column=1,sticky=E)
txtredbull=Entry(f2_drinks,font=("arial",14,"bold"),bd=4,width=7,justify=LEFT,state=DISABLED,textvariable=E_redbull)
txtredbull.grid(row=2,column=1,sticky=E)
txt7up=Entry(f2_drinks,font=("arial",14,"bold"),bd=4,width=7,justify=LEFT,state=DISABLED,textvariable=E_7up)
txt7up.grid(row=3,column=1,sticky=E)
txtbira=Entry(f2_drinks,font=("arial",14,"bold"),bd=4,width=7,justify=LEFT,state=DISABLED,textvariable=E_bira)
txtbira.grid(row=4,column=1,sticky=E)
txtcorona=Entry(f2_drinks,font=("arial",14,"bold"),bd=4,width=7,justify=LEFT,state=DISABLED,textvariable=E_corona)
txtcorona.grid(row=5,column=1,sticky=E)
txtcocacola=Entry(f2_drinks,font=("arial",14,"bold"),bd=4,width=7,justify=LEFT,state=DISABLED,textvariable=E_cocacola)
txtcocacola.grid(row=6,column=1,sticky=E)
txtfanta=Entry(f2_drinks,font=("arial",14,"bold"),bd=4,width=7,justify=LEFT,state=DISABLED,textvariable=E_fanta)
txtfanta.grid(row=7,column=1,sticky=E)
txtbeer=Entry(f2_drinks,font=("arial",14,"bold"),bd=4,width=7,justify=LEFT,state=DISABLED,textvariable=E_beer)
txtbeer.grid(row=8,column=1,sticky=E)


#checkbuttons for dishes
cpizza=Checkbutton(f2_dishes,text="Pizza",font=("arial",14,"bold"),bg="sea green",variable=var9,onvalue=1,offvalue=0,command=obj.chkpizza)
cpizza.grid(row=1,column=0,sticky=W)
cburger=Checkbutton(f2_dishes,text="Burger",font=("arial",14,"bold"),bg="sea green",variable=var10,onvalue=1,offvalue=0,command=obj.chkburger)
cburger.grid(row=2,column=0,sticky=W)
cfries=Checkbutton(f2_dishes,text="Fries",font=("arial",14,"bold"),bg="sea green",variable=var11,onvalue=1,offvalue=0,command=obj.chkfries)
cfries.grid(row=3,column=0,sticky=W)
cpaneer=Checkbutton(f2_dishes,text="Paneer",font=("arial",14,"bold"),bg="sea green",variable=var12,onvalue=1,offvalue=0,command=obj.chkpaneer)
cpaneer.grid(row=4,column=0,sticky=W)
cdal=Checkbutton(f2_dishes,text="Dal",font=("arial",14,"bold"),bg="sea green",variable=var13,onvalue=1,offvalue=0,command=obj.chkdal)
cdal.grid(row=5,column=0,sticky=W)
croti=Checkbutton(f2_dishes,text="Roti",font=("arial",14,"bold"),bg="sea green",variable=var14,onvalue=1,offvalue=0,command=obj.chkroti)
croti.grid(row=6,column=0,sticky=W)
cparatha=Checkbutton(f2_dishes,text="Paratha",font=("arial",14,"bold"),bg="sea green",variable=var15,onvalue=1,offvalue=0,command=obj.chkparatha)
cparatha.grid(row=7,column=0,sticky=W)
cchefspecial=Checkbutton(f2_dishes,text="Chef Sp.",font=("arial",14,"bold"),bg="sea green",variable=var16,onvalue=1,offvalue=0,command=obj.chkchefspecial)
cchefspecial.grid(row=8,column=0,sticky=W)

#Entrybpox for dishes
txtpizza=Entry(f2_dishes,font=("arial",14,"bold"),bd=4,width=7,justify=LEFT,state=DISABLED,textvariable=E_pizza)
txtpizza.grid(row=1,column=1,sticky=E)
txtburger=Entry(f2_dishes,font=("arial",14,"bold"),bd=4,width=7,justify=LEFT,state=DISABLED,textvariable=E_burger)
txtburger.grid(row=2,column=1,sticky=E)
txtfries=Entry(f2_dishes,font=("arial",14,"bold"),bd=4,width=7,justify=LEFT,state=DISABLED,textvariable=E_fries)
txtfries.grid(row=3,column=1,sticky=E)
txtpaneer=Entry(f2_dishes,font=("arial",14,"bold"),bd=4,width=7,justify=LEFT,state=DISABLED,textvariable=E_paneer)
txtpaneer.grid(row=4,column=1,sticky=E)
txtdal=Entry(f2_dishes,font=("arial",14,"bold"),bd=4,width=7,justify=LEFT,state=DISABLED,textvariable=E_dal)
txtdal.grid(row=5,column=1,sticky=E)
txtroti=Entry(f2_dishes,font=("arial",14,"bold"),bd=4,width=7,justify=LEFT,state=DISABLED,textvariable=E_roti)
txtroti.grid(row=6,column=1,sticky=E)
txtparatha=Entry(f2_dishes,font=("arial",14,"bold"),bd=4,width=7,justify=LEFT,state=DISABLED,textvariable=E_paratha)
txtparatha.grid(row=7,column=1,sticky=E)
txtchefspecial=Entry(f2_dishes,font=("arial",14,"bold"),bd=4,width=7,justify=LEFT,state=DISABLED,textvariable=E_chefspecial)
txtchefspecial.grid(row=8,column=1,sticky=E)

#total cost
lblcostofdrinks=Label(f2_details,text="Cost of Drinks",font=("arial",12,"bold"),background="sea green")
lblcostofdrinks.grid(row=1,column=0,sticky=W)
txtcostofdrinks=Entry(f2_details,font=("arial",14,"bold"),bd=4,width=8,justify=LEFT,textvariable=costofdrinks)
txtcostofdrinks.grid(row=1,column=1)

lblcostofdishes=Label(f2_details,text="Cost of Dishes",font=("arial",12,"bold"),background="sea green")
lblcostofdishes.grid(row=2,column=0,sticky=W)
txtcostofdishes=Entry(f2_details,font=("arial",14,"bold"),bd=4,width=8,justify=LEFT,textvariable=costofdishes)
txtcostofdishes.grid(row=2,column=1)

lblservicecharge=Label(f2_details,text="Service Charge",font=("arial",12,"bold"),background="sea green")
lblservicecharge.grid(row=3,column=0,sticky=W)
txtservicecharge=Entry(f2_details,font=("arial",14,"bold"),bd=4,width=8,justify=LEFT,textvariable=servicecharge)
txtservicecharge.grid(row=3,column=1)

#payment information
lbltaxpaid=Label(f2_details,text="Paid Tax",font=("arial",12,"bold"),background="sea green")
lbltaxpaid.grid(row=1,column=2)
txtpaidtax=Entry(f2_details,font=("arial",14,"bold"),bd=4,width=10,justify=LEFT,textvariable=paidtax)
txtpaidtax.grid(row=1,column=4)

lblsubtotal=Label(f2_details,text="Sub Total",font=("arial",12,"bold"),background="sea green")
lblsubtotal.grid(row=2,column=2)
txtsubtotal=Entry(f2_details,font=("arial",14,"bold"),bd=4,width=10,justify=LEFT,textvariable=subtotal)
txtsubtotal.grid(row=2,column=4)

lbltotalcost=Label(f2_details,text="Total Cost",font=("arial",12,"bold"),background="sea green")
lbltotalcost.grid(row=3,column=2)
txttotalcost=Entry(f2_details,font=("arial",14,"bold"),bd=4,width=10,justify=LEFT,textvariable=totalcost)
txttotalcost.grid(row=3,column=4)

#receipt
txtreceipt=Text(cal_receipt,height=18,width=38,bg="white",font=("arial",14,"bold"))
txtreceipt.grid(row=0,column=0)

#receipt buttons
btntotal=Button(cal_lastbtn,padx=16,pady=1,bd=7,fg="black",font=("arial",16,"bold"),
                width=4,text="Total",bg="Powder Blue",command=obj.costofitems)
btntotal.grid(row=1,column=0)
btnreceipt=Button(cal_lastbtn,padx=16,pady=1,bd=7,fg="black",font=("arial",16,"bold"),
                width=4,text="Receipt",bg="Powder Blue",command=obj.receipt)
btnreceipt.grid(row=1,column=1)
btnreset=Button(cal_lastbtn,padx=16,pady=1,bd=7,fg="black",font=("arial",16,"bold"),
                width=4,text="Reset",bg="Powder Blue",command=obj.reset)
btnreset.grid(row=1,column=2)
btnexit=Button(cal_lastbtn,padx=16,pady=1,bd=7,fg="black",font=("arial",16,"bold"),
                width=5,text="Exit",bg="Powder Blue",command=obj.iExit)
btnexit.grid(row=1,column=3)

#calulator display
class calcfunc:
    def btnclick(self,numbers):
        global operator
        operator=operator+str(numbers)
        text_Input.set(operator)

    def btnClear(self):
        global operator
        operator=""
        text_Input.set("")
    
    def btnEqual(self):
        global operator
        sumup=str(eval(operator))
        text_Input.set(sumup)
        operator=""
    txtdisplay=Entry(cal_buttons,font=("arial",14,"bold"),bd=4,width=37,justify=RIGHT,textvariable=text_Input)
    txtdisplay.grid(row=0,column=0,columnspan=4,padx=1) 
    txtdisplay.insert(0,"0")

obj1=calcfunc()

#calculator buttons
#7-9
btn7=Button(cal_buttons,padx=16,pady=1,bd=7,fg='black',font=("arial",16,"bold"),
            width=4, text="7",bg="Powder blue",command=lambda:obj1.btnclick(7))
btn7.grid(row=1,column=0)
btn8=Button(cal_buttons,padx=16,pady=1,bd=7,fg='black',font=("arial",16,"bold"),
            width=4, text="8",bg="Powder blue",command=lambda:obj1.btnclick(8))
btn8.grid(row=1,column=1)
btn9=Button(cal_buttons,padx=16,pady=1,bd=7,fg='black',font=("arial",16,"bold"),
            width=4, text="9",bg="Powder blue",command=lambda:obj1.btnclick(9))
btn9.grid(row=1,column=2)
btnplus=Button(cal_buttons,padx=16,pady=1,bd=7,fg='black',font=("arial",16,"bold"),
            width=4, text="+",bg="Powder blue",command=lambda:obj1.btnclick("+"))
btnplus.grid(row=1,column=3)

#4-6
btn4=Button(cal_buttons,padx=16,pady=1,bd=7,fg='black',font=("arial",16,"bold"),
            width=4, text="4",bg="Powder blue",command=lambda:obj1.btnclick(4))
btn4.grid(row=2,column=0)
btn5=Button(cal_buttons,padx=16,pady=1,bd=7,fg='black',font=("arial",16,"bold"),
            width=4, text="5",bg="Powder blue",command=lambda:obj1.btnclick(5))
btn5.grid(row=2,column=1)
btn6=Button(cal_buttons,padx=16,pady=1,bd=7,fg='black',font=("arial",16,"bold"),
            width=4, text="6",bg="Powder blue",command=lambda:obj1.btnclick(6))
btn6.grid(row=2,column=2)
btnsub=Button(cal_buttons,padx=16,pady=1,bd=7,fg='black',font=("arial",16,"bold"),
            width=4, text="-",bg="Powder blue",command=lambda:obj1.btnclick("-"))
btnsub.grid(row=2,column=3)

#1-3
btn1=Button(cal_buttons,padx=16,pady=1,bd=7,fg='black',font=("arial",16,"bold"),
            width=4, text="1",bg="Powder blue",command=lambda:obj1.btnclick(1))
btn1.grid(row=3,column=0)
btn2=Button(cal_buttons,padx=16,pady=1,bd=7,fg='black',font=("arial",16,"bold"),
            width=4, text="2",bg="Powder blue",command=lambda:obj1.btnclick(2))
btn2.grid(row=3,column=1)
btn3=Button(cal_buttons,padx=16,pady=1,bd=7,fg='black',font=("arial",16,"bold"),
            width=4, text="3",bg="Powder blue",command=lambda:obj1.btnclick(3))
btn3.grid(row=3,column=2)
btnmul=Button(cal_buttons,padx=16,pady=1,bd=7,fg='black',font=("arial",16,"bold"),
            width=4, text="*",bg="Powder blue",command=lambda:obj1.btnclick("*"))
btnmul.grid(row=3,column=3)

#others
btn0=Button(cal_buttons,padx=16,pady=1,bd=7,fg='black',font=("arial",16,"bold"),
            width=4, text="0",bg="Powder blue",command=lambda:obj1.btnclick(0))
btn0.grid(row=4,column=0)
btnC=Button(cal_buttons,padx=16,pady=1,bd=7,fg='black',font=("arial",16,"bold"),
            width=4, text="C",bg="Powder blue",command=lambda:obj1.btnclick)
btnC.grid(row=4,column=1)
btneq=Button(cal_buttons,padx=16,pady=1,bd=7,fg='black',font=("arial",16,"bold"),
            width=4, text="=",bg="Powder blue",command=lambda:obj1.btnEqual)
btneq.grid(row=4,column=2)
btndiv=Button(cal_buttons,padx=16,pady=1,bd=7,fg='black',font=("arial",16,"bold"),
            width=4, text="/",bg="Powder blue",command=lambda:obj1.btnClear("/"))
btndiv.grid(row=4,column=3)

form1.mainloop()