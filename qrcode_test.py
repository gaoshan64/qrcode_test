
from tkinter import *
from tkinter.ttk import *
import qrcode
from PIL import Image, ImageTk
import re
root = Tk()
root.title('二维码生成器')


def show_qr():
    top = Toplevel()
    str_txt=t.get(1.0,'end')
    top.title('二维码')
    msg = Message(top, text=str_txt[0:20] + '...' + '\nlen' + str(len(str_txt)))
    msg.pack()
    filename=str_txt[0:9]
    filename='./archive/'+ re.sub(r'[^A-Za-z0-9]+',' ',filename)+'.PNG'
    # 实例化QRCode生成qr对象
    qr = qrcode.QRCode(
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=3,
        border=4
    )
    # 传入数据
    qr.add_data(str_txt)
    qr.make(fit=True)
    # 生成二维码
    img = qr.make_image()
    # 保存二维码
    img.save(filename)
    # 展示二维码
    #img.show()
    #qrcode.make(str_txt).save('./archive/'+repr(filename)+'.PNG')
    img_open = Image.open(filename)
    global img_png
    img_png = ImageTk.PhotoImage(img_open)
    label_img = Label(top, image=img_png)
    label_img.pack()
    '''top.title('二维码')
    msg = Message(top, text=str_txt[0:20]+'...'+'\n'+'字符串长度'+str(len(str_txt)))
    msg.pack()'''
    dismiss = Button(top, text='关闭', command=top.destroy)
    dismiss.pack()

def strlong(event):
    str_text=t.get(1.0,'end')
    str_long_l['text']=str(len(t.get(1.0,'end')))
    try:
        qr = qrcode.QRCode(
            error_correction=qrcode.constants.ERROR_CORRECT_L,
        )
        # 传入数据
        qr.add_data(str_text)
        qr.make(fit=True)
        # 生成二维码
        qr.make_image()
        str_long_l.config(background='green')
        str_long_l.update()

    except qrcode.exceptions.DataOverflowError:
        str_long_l.config(background='red')
        str_long_l.update()
    else:
        pass




l=Label(text='请输入字符串')
l.pack
t = Text()
t.bind('<KeyPress>',strlong)
t.pack()
str_long_l = Label()
str_long_l.pack()

b=Button(text='确认',command=show_qr)
b.pack()

root.mainloop()