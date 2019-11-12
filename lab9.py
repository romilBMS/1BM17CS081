from tkinter import *
class Application(Frame):
    def __init__(self,master):
        super().__init__(master)
        self.grid()
        self.bookticket()
    
    def bookticket(self):
        Label(self,text="movie booking"). grid(row=0,column=0)
        Label(self,text="Select any one:").grid(row=1,column=0)

        self.movie=StringVar()
        self.movie.set(None)
        Radiobutton(self,text="Eng",variable=self.movie,value="English",command=self.eng).grid(row=2,column=0,columnspan=8,sticky="W")
        Radiobutton(self,text="Kan",variable=self.movie,value="Kannada",command=self.kan).grid(row=2,column=3,columnspan=8,sticky="W")
        Radiobutton(self,text="Hindi",variable=self.movie,value="Hindi",command=self.hin).grid(row=2,column=3,columnspan=8,sticky="W")

        Button(self,text="Book Ticket", command=self.book).grid(row=7,column=0,columnspan=2, sticky="W")
        self.txt=Text(self, width=40, height=5,wrap=WORD)
        self.txt.grid(row=8,column=0, columnspan=8,sticky="W")

    def kan(self):
        self.l4=Label(self,text="kabb")
        self.l4.grid(row=3,column=0,sticky="W")
        self.kan1=BooleanVar()
        Checkbutton(self,variable=self.kan1).grid(row=3,column=1,sticky="W")
        self.l5=Label(self,text="kann 2")
        self.l5.grid(row=3,column=2,sticky="W")
        self.kan2=BooleanVar()
        Checkbutton(self,variable=self.kan2).grid(row=3,column=3,sticky="W")

        self.l6=Label(self,text="ragha")
        self.l6.grid(row=3,column=4,sticky="W")
        self.kan3=BooleanVar()
        Checkbutton(self,variable=self.kan3).grid(row=3,column=5,sticky="W")

    def hin(self):
        self.l7=Label(self,text="KKKG")
        self.l7.grid(row=3,column=0,sticky="W")
        self.h1=BooleanVar()
        Checkbutton(self,variable=self.h1).grid(row=3,column=1,sticky="W")
        self.l8=Label(self,text="DHH")
        self.l8.grid(row=3,column=2,sticky="W")
        self.h2=BooleanVar()
        Checkbutton(self,variable=self.h2).grid(row=3,column=3,sticky="W")

        self.l9=Label(self,text="Sultan")
        self.l9.grid(row=3,column=4,sticky="W")
        self.h3=BooleanVar()
        Checkbutton(self,variable=self.h3).grid(row=3,column=5,sticky="W")
    def eng(self):
        self.l10=Label(self,text="queea")
        self.l10.grid(row=3,column=0,sticky="W")
        self.e1=BooleanVar()
        Checkbutton(self,variable=self.e1).grid(row=3,column=1,sticky="W")
        self.l11=Label(self,text="RED ")
        self.l11.grid(row=3,column=2,sticky="W")
        self.e2=BooleanVar()
        Checkbutton(self,variable=self.e2).grid(row=3,column=3,sticky="W")

        self.l9=Label(self,text="BLood")
        self.l9.grid(row=3,column=4,sticky="W")
        self.e3=BooleanVar()
        Checkbutton(self,variable=self.e3).grid(row=3,column=5,sticky="W")
        
    def book(self):
        msg=""
        if self.movie.get()=="Kannada":
            if self.kan1.get():
                msg="Your Booking was successful"
            elif self.kan2.get():
                 msg="Your Booking was successful"
            elif self.kan3.get():
                 msg="Your Booking was successful"
            else:
                msg="Please select the Movie"
        elif self.movie.get()=="Hindi":
            if self.h1.get():
                 msg="Your Booking was successful"
            elif self.h2.get():
                 msg="Your Booking was successful"
            elif self.h3.get():
                 msg="Your Booking was successful"
            else:
                msg="Please select the Movie"
        elif self.movie.get()=="English":
            if self.e1.get():
                 msg="Your Booking was successful"
            elif self.e2.get():
                 msg="Your Booking was successful"
            elif self.e3.get():
                 msg="Your Booking was successful"
            else:
                msg="Please select the Movie"
            self.txt.delete(0.0,END)
            self.txt.insert(0.0,msg)

r=Tk()
r.title("Movie Ticket App")
a=Application(r)
r.mainloop()