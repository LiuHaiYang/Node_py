__authot__ = 'Ocean'
# -*- encoding: utf8 -*-
from tkinter  import *
from tkinter import messagebox as tkms
from tkinter.filedialog import *
import os


filename = ''


def author():
    tkms.showinfo('作者信息','本软件有Ocean开发！')

def banquan():
    tkms.showinfo('版权信息','本软件的归属为Ocean！')
def openfile():
    global  filename
    filename = askopenfilename(defaultextension = '.txt')
    if filename == '':
        filename = None
    else:
        root.title('FileName:'+os.path.basename(filename))
        textPad.delete(1.0,END)
        f = open(filename,'r',encoding='utf-8')
        textPad.insert(1.0,f.read())
        f.close()
def newfile():
    global filename
    root.title('未命名文件')
    filename = None
    textPad.delete(1.0,END)

def save():
    global  filename
    try:
        f = open(filename,'w')
        msg = textPad.get(1.0,END)
        f.write(msg)
    except:
        othersave()

def othersave():
    f = asksaveasfilename(initialfile = '未命名.txt',defaultextension='.txt')
    global filename
    filename = f
    fh = open(f,'w')
    msg = textPad.get(1.0,END)
    fh.write(msg)
    fh.close()
    root.title('FileName:'+os.path.basename(f))
def cut():
    textPad.event_generate('<<Cut>>')
def copy():
    textPad.event_generate('<<Copy>>')
def paste():
    textPad.event_generate('<<Paste>>')
def redo():
    textPad.event_generate('<<Redo>>')
def undo():
    textPad.event_generate('<<Undo>>')

def selectAll():
    textPad.tag_add('sel','1.0',END)
def search():
    topsearch = Toplevel(root)
    topsearch.geometry('230x30+200+250')
    label1 = Label(topsearch,text='Find')
    label1.grid(row= 0,column=0,padx=5)
    entry1 = Entry(topsearch,width=20)
    entry1.grid(row= 0,column=1,padx=5)
    button1 = Button(topsearch,text='查找')
    button1.grid(row= 0,column=2)

root = Tk()
root.title('Ocean Node')
root.geometry("800x500+100+100")

#Create Menu
menubar = Menu(root)
root.config(menu = menubar )

filemenu = Menu(menubar)
filemenu.add_command(label='新建',accelerator='Ctrl + N',command=newfile)
filemenu.add_command(label='打开',accelerator='Ctrl + O',command=openfile)
filemenu.add_command(label='保存',accelerator='Ctrl + S',command=save)
filemenu.add_command(label='另存',accelerator='Ctrl + Shift + S',command=othersave)
menubar.add_cascade(label='文件',menu=filemenu)

edit = Menu(menubar)
edit.add_command(label='撤销',accelerator='Ctrl + Z',command=undo)
edit.add_command(label='重做',accelerator='Ctrl + y',command=redo)
edit.add_separator()
edit.add_command(label='剪贴',accelerator='Ctrl + X',command=cut)
edit.add_command(label='复制',accelerator='Ctrl + C',command=copy)
edit.add_command(label='粘贴',accelerator='Ctrl + V',command=paste)
edit.add_separator()
edit.add_command(label='查找',accelerator='Ctrl + F',command=search)
edit.add_command(label='全选',accelerator='Ctrl + A',command=selectAll)
menubar.add_cascade(label='编辑',menu = edit)

about = Menu(menubar)
about.add_command(label='作者' ,command=author)
about.add_command(label='版权',command=banquan)
menubar.add_cascade(label='关于',menu = about)

toolbar = Frame(root, height=22,bg='light sea green')
shortButton = Button(toolbar,text='打开',command=openfile)
shortButton.pack(side=LEFT,padx=8,pady=8)

shortButton = Button(toolbar,text='保存',command=save)
shortButton.pack(side=LEFT,padx=8,pady=8)
toolbar.pack(expand=NO,fill=X)

#Status Bar
status = Label(root,text='ln20',bd=1,relief=SUNKEN,anchor=W)
status.pack(side=BOTTOM,fill=X)

#linenumber&text
lnlabel = Label(root, width=2,bg='antique white')
lnlabel.pack(side=LEFT,fill=Y)

textPad = Text(root, undo=True)
textPad.pack(expand=YES,fill=BOTH)

scroll = Scrollbar(textPad)
textPad.config(yscrollcommand= scroll.set)
scroll.config(command =textPad.yview)
scroll.pack(side=RIGHT,fill = Y)


root.mainloop()

