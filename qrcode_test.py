from tkinter import *
from tkinter.ttk import *
import qrcode
from PIL import Image, ImageTk

root = Tk()
root.title('二维码生成器')

def show_qr():
    top = Toplevel()
    str=t.get(1.0,'end')
    filename=str[0:9]

    qrcode.make(str).save('./archive/'+repr(filename)+'.PNG')


    img_open = Image.open('./archive/'+repr(filename)+'.PNG')
    global img_png
    img_png = ImageTk.PhotoImage(img_open)
    label_img = Label(top, image=img_png)
    label_img.pack()
    top.title('二维码')
    msg = Message(top, text=str)
    msg.pack()
    dismiss = Button(top, text='关闭', command=top.destroy)
    dismiss.pack()

l=Label(text='请输入字符串')
l.pack
t = Text()
t.pack()

b=Button(text='确认',command=show_qr)
b.pack()

root.mainloop()