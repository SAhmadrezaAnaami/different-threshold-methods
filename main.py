import tkinter
import cv2;
from PIL import ImageTk, Image


img = cv2.imread("1.jpg" , 0)
# b,g,r = cv2.split(img)
# img2 = cv2.merge((r,g,b))
img = cv2.resize(img , (590 , 495))





mainWindow = tkinter.Tk()
mainWindow.title("Threshold")
mainWindow.wm_attributes('-toolwindow', 'True')
winsize = "600x600"
mainWindow.geometry(winsize)
mainWindow.maxsize(600,600)
mainWindow.minsize(600,600)

def Binary ():
    ret, thresh1 = cv2.threshold(img, 120, 255, cv2.THRESH_BINARY)
    # b,g,r = cv2.split(thresh1)
    # thresh1 = cv2.merge((r,g,b))
    im = Image.fromarray(thresh1)
    imgtk = ImageTk.PhotoImage(image=im)
    label = tkinter.Label(mainWindow , image=imgtk  )
    label.config(height= 495 , width= 590  )
    label.place(x = 3,y = 100)
    mainWindow.mainloop()
def Binary_inv ():
    ret, thresh1 = cv2.threshold(img, 120, 255, cv2.THRESH_BINARY_INV)
    # b,g,r = cv2.split(thresh1)
    # thresh1 = cv2.merge((r,g,b))
    im = Image.fromarray(thresh1)
    imgtk = ImageTk.PhotoImage(image=im)
    label = tkinter.Label(mainWindow , image=imgtk  )
    label.config(height= 495 , width= 590  )
    label.place(x = 3,y = 100)
    mainWindow.mainloop()
def TRUNC ():
    ret, thresh1 = cv2.threshold(img, 120, 255, cv2.THRESH_TRUNC)
    # b,g,r = cv2.split(thresh1)
    # thresh1 = cv2.merge((r,g,b))
    im = Image.fromarray(thresh1)
    imgtk = ImageTk.PhotoImage(image=im)
    label = tkinter.Label(mainWindow , image=imgtk  )
    label.config(height= 495 , width= 590  )
    label.place(x = 3,y = 100)
    mainWindow.mainloop()
def Tozero ():
    ret, thresh1 = cv2.threshold(img, 120, 255, cv2.THRESH_TOZERO)
    # b,g,r = cv2.split(thresh1)
    # thresh1 = cv2.merge((r,g,b))
    im = Image.fromarray(thresh1)
    imgtk = ImageTk.PhotoImage(image=im)
    label = tkinter.Label(mainWindow , image=imgtk  )
    label.config(height= 495 , width= 590  )
    label.place(x = 3,y = 100)
    mainWindow.mainloop()
def Tozero_inv ():
    ret, thresh1 = cv2.threshold(img, 120, 255, cv2.THRESH_TOZERO_INV)
    # b,g,r = cv2.split(thresh1)
    # thresh1 = cv2.merge((r,g,b))
    im = Image.fromarray(thresh1)
    imgtk = ImageTk.PhotoImage(image=im)
    label = tkinter.Label(mainWindow , image=imgtk  )
    label.config(height= 495 , width= 590  )
    label.place(x = 3,y = 100)
    mainWindow.mainloop()
def Normals ():
    im = Image.fromarray(img)
    imgtk = ImageTk.PhotoImage(image=im)
    label = tkinter.Label(mainWindow , image=imgtk  )
    label.config(height= 495 , width= 590  )
    label.place(x = 3,y = 100)
    mainWindow.mainloop()


but1 = tkinter.Button(mainWindow , text="Binary" ,bd= 5 ,  height = 3 , width= 10 , bg= "yellow" , command = Binary).place(x = 0,y = 0)
but2 = tkinter.Button(mainWindow , text="Binary_inv" ,bd= 5 ,  height = 3 , width= 10 , bg= "green" , command = Binary_inv).place(x = 100,y = 0)
but3 = tkinter.Button(mainWindow , text="TRUNC" ,bd= 5 ,  height = 3 , width= 10 , bg= "blue" , fg="white", command = TRUNC).place(x = 200,y = 0)
but4 = tkinter.Button(mainWindow , text="Tozero" ,bd= 5 ,  height = 3 , width= 10 , bg= "orange" , command = Tozero).place(x = 300,y = 0)
but5 = tkinter.Button(mainWindow , text="Tozero_inv" ,bd= 5 ,  height = 3 , width= 10 , bg= "skyblue" , command = Tozero_inv).place(x = 400,y = 0)
but6 = tkinter.Button(mainWindow , text="Normal" ,bd= 5 ,  height = 3 , width= 10 , bg= "gold" , command = Normals).place(x = 500,y = 0)


im = Image.fromarray(img)
imgtk = ImageTk.PhotoImage(image=im)

label = tkinter.Label(mainWindow , image=imgtk  )
label.config(height= 495 , width= 590 )
label.place(x = 3,y = 100)




    


mainWindow.mainloop()