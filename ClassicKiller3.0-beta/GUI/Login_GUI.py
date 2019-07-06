#coding=utf-8
#2019.7.5 Update
from Tkinter import *

#GUI

def Login():
        global username
        global password
        win=Tk()
        win.title("ClassicKiller")
        win.geometry("400x400+200+50")

        #创建容器
        fm_top=Frame()
        fm_top.pack(side=TOP,fill=X)
        label_TOP=Label(fm_top,text="ClassicKiller",fg="purple",font=("微软雅黑",20)).pack(side=TOP,fill=X)

        fm_bottom = Frame()
        fm_bottom.pack(side=BOTTOM, fill=X)
        label_buttom = Label(fm_bottom, text="Powered by Migraine-sudo", fg="black", font=("黑体", 8)).pack(expand=YES)


        #创建容器1，靠左
        fm1=Frame()
        fm1.pack(side=LEFT,fill=BOTH)

        label1=Label(fm1,text="用户名",fg="black",font=("黑体",10))
        label1.pack(side=TOP,fill=X,pady=20,padx=10)
        label2=Label(fm1,text="密码",fg="black",font=("黑体",10))
        label2.pack(side=TOP,fill=X,pady=5,padx=5)

        #创建容器2，靠左靠着容器1
        global entry1
        global entry2
        fm2=Frame()
        fm2.pack(side=LEFT,padx=10,fill=Y,expand=YES)
        entry1=Entry(fm2)
        entry1.pack(side=TOP,pady=20)
        entry2=Entry(fm2,show="*")
        entry2.pack(side=TOP,pady=5)

        #创建容器3
        fm3=Frame()
        fm3.pack(side=LEFT,padx=10,fill=Y,expand=YES)
        Button(fm3,text="登陆",height=2,width=7,command=GetUser).pack(side=TOP,pady=50)

        win.mainloop()


def GetUser(): #call back
        username=entry1.get()
        password=entry2.get()
        print "Hello "+username+"!"


if __name__=='__main__':
        x=Login()
        print x