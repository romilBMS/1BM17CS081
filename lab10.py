from tkinter import *
class Application(Frame):

    def __init__(self, master):
   
        super(Application,self).__init__(master)
        self.grid()
        self.create_widgets()
    def create_widgets(self):
        Label(self,text="BMSCE Canteen").grid(row=0,column=0,sticky=W)
        Label(self,text="Items-Price").grid(row=1,column=0,sticky=W)
        Label(self,text="Quantity").grid(row=1,column=2,sticky=W)
        Label(self,text="Order").grid(row=1,column=3,sticky=W)
        Label(self,text="Idli-Rs 20/-").grid(row=2,column=0,sticky=W)
        self.q_idli=Entry(self)
        self.q_idli.grid(row=2,column=2,sticky=W)
        self.idli=BooleanVar()
        Checkbutton(self,text="",variable=self.idli).grid(row=2,column=3,sticky=W)
        Label(self,text="Vada-Rs 10/-").grid(row=3,column=0,sticky=W)
        self.q_vada=Entry(self)
        self.q_vada.grid(row=3,column=2,sticky=W)
        self.vada=BooleanVar()

        Checkbutton(self,text="",variable=self.vada).grid(row=3,column=3,sticky=W)
        Label(self,text="Dosa-Rs 30/-").grid(row=4,column=0,sticky=W)
        self.q_dosa=Entry(self)
        self.q_dosa.grid(row=4,column=2,sticky=W)
        self.dosa=BooleanVar()
        Checkbutton(self,text="",variable=self.dosa).grid(row=4,column=3,sticky=W)
        Label(self,text="Pulav-Rs 25/-").grid(row=5,column=0,sticky=W)
        self.q_pulav=Entry(self)
        self.q_pulav.grid(row=5,column=2,sticky=W)
        self.pulav=BooleanVar()
        Checkbutton(self,text="",variable=self.pulav).grid(row=5,column=3,sticky=W)
        self.btn=Button(self,text="Total Price",command=self.price)
        self.btn.grid(row=6,column=0,columnspan=2,sticky=W)
        self.t=Text(self,width=50,height=20,wrap=WORD)
        self.t.grid(row=7,column=0,rowspan=2,sticky=W)
    def price(self):
        bill_amount=0
        msg=""
        if self.idli.get():
            idlip=20*int(self.q_idli.get())
            bill_amount=bill_amount+idlip
        if self.vada.get():
            vadap=10*int(self.q_vada.get())
            bill_amount=bill_amount+vadap
        if self.dosa.get():
            dosap=30*int(self.q_dosa.get())
            bill_amount=bill_amount+dosap
        if self.pulav.get():
            pulp=25*int(self.q_pulav.get())
            bill_amount=bill_amount+pulp
            bill=str(bill_amount)
            msg+="Your total bill amount will be...RS"
            msg+=bill
            msg+=" .Thank you:)"

        self.t.delete(0.0,END)
        self.t.insert(0.0,msg)
root=Tk()
root.title("Order Up")
app=Application(root)
root.mainloop()