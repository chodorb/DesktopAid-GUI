from tkinter import *
import webbrowser
from PIL import Image,ImageTk
from tkinter import ttk
root = Tk()
root.title("Desktop Aid App")
root.geometry("750x300")
root.resizable(False,False)
root.iconbitmap('icon.ico')





#button section
def Yt_Butt():
    string =  YtEnt.get()
    webbrowser.open("https://www.youtube.com/results?search_query="+string)
    YtEnt.delete(0,END)
def Goo_Butt():
    string = GooEnt.get()
    webbrowser.open("https://www.google.com/search?&q="+string)
    GooEnt.delete(0,END)
def Int_Butt():
    string=IntEnt.get()    
    webbrowser.open(string)    
    IntEnt.delete(0,END)



#Youtube Section
YtEnt = Entry(root,width=45)
YtEnt.grid(row=1,column=1)
YtButt = Button(root, text="Search", command=Yt_Butt,fg="white",bg="red")
YtButt.grid(row=1,column=3)
Ytload = Image.open("youtube.png") 
Ytload = Ytload.resize((75,75))   
Ytrender = ImageTk.PhotoImage(Ytload)
Ytimg=Label(image=Ytrender)
Ytimg.grid(row=1,column=0)

#Google Section
GooEnt = Entry(root,width=45)
GooEnt.grid(row=3,column=1)
GooButt = Button(root,text="Search",command=Goo_Butt,fg="white",bg="red")
GooButt.grid(row=3,column=3)
Gooload = Image.open("google.png")
Gooload = Gooload.resize((75,75))
Goorender = ImageTk.PhotoImage(Gooload)
Gooimg = Label(image=Goorender)
Gooimg.grid(row=3,column=0)

#Internet Section
IntEnt = Entry(root,width=45)
IntEnt.grid(row=5,column=1)
IntButt = Button(root,text = "Go",command=Int_Butt,fg="white",bg="red")
IntButt.grid(row=5,column=3)
Intload = Image.open("net.png")
Intload = Intload.resize((75,75))
Intrender = ImageTk.PhotoImage(Intload)
Intimg = Label(image=Intrender)
Intimg.grid(row=5,column=0)


VerLab = Label(text="Desktop Aid v0.0.1", font=("arial",18)).grid(row=0,column=0)
AuthLab = Label(text="by Bazyli Chodor 2020", font=("arial",7)).grid(row=7, column=3)   
root.mainloop()