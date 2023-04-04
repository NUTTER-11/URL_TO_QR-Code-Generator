import pyqrcode
from tkinter import *
from tkinter import messagebox


root=Tk()


def generateQR():
    if len(entertextfeild.get())!=0 :
        global qr,photo
        qr = pyqrcode.create(entertextfeild.get())
        photo = BitmapImage(data = qr.xbm(scale=5))
    else:
        messagebox.showinfo("Please Enter something")
    try:
        showcode()
    except:
        pass

def showcode():
    imageLabel.config(image = photo)
    subLabel.config(text="QR of " + entertextlabel.get())


def clearALL():
    entertextfeild.delete(0,END)
    entertextfeild.focus_set()

root.configure(background="light green")
root.geometry("600x100")
root.title("QR GERNATOR")
entertextlabel=Label(root,text="Enter text",fg="black",bg="white")
entertextlabel.grid(row=1,column=1,sticky="E",padx=10,pady=10)


entertextfeild=Entry(root)
entertextfeild.grid(row=1,column=2,sticky="E",ipadx=60,pady=60)

generatebutton=Button(root,text="Generate",bg="red",fg="black",command=generateQR)
clearbutton=Button(root,text="clear",bg="red",fg="black",command=clearALL)
generatebutton.grid(row=1,column=3)
clearbutton.grid(row=1,column=5,pady=5)
imageLabel = Label(root)
imageLabel.grid(row =3,column =2,sticky=N+S+W+E)

root.mainloop()
