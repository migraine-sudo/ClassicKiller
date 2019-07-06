#coding=utf-8
from output.printf import printf
from Login.Login import Login
from GetAnswer.GetAnswer import Answer
from Information.Information import PrintInformation
import thread
import time
from Tkinter import *

def logo():
    printf( '''
        _________ .__                       .__        ____  __.__.__  .__                
        \_   ___ \|  | _____    ______ _____|__| ____ |    |/ _|__|  | |  |   ___________ 
        /    \  \/|  | \__  \  /  ___//  ___/  |/ ___\|      < |  |  | |  | _/ __ \_  __ \ 
        \     \___|  |__/ __ \_\___ \ \___ \|  \  \___|    |  \|  |  |_|  |_\  ___/|  | \/
        \______  /____(____  /____  >____  >__|\___  >____|__ \__|____/____/\___  >__|   
                \/          \/     \/     \/        \/        \/                 \/       
                                                            Editor:Migraine-sudo
                                                            2019.7  
    ''',"purple")

def Model():
    printf("\n-------------Models-------------","yellow")
    printf("\t1.Classic Model","blue")
    printf("\t2.Super Model","blue")
    printf("\t3.Settings", "blue")
    printf("\t4.About","blue")
    printf("\t5.Exit","red")
    printf("--------------------------------", "yellow")
    Model=raw_input("Please Choice Model<<")
    return Model



#GUI
global username;
global password;

def Login_GUI():

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
        label3 = Label(fm1, text="选择试卷", fg="black", font=("黑体", 10))
        label3.pack(side=TOP, fill=X, pady=40, padx=5)

        #创建容器2，靠左靠着容器1
        global entry1
        global entry2
        fm2=Frame()
        fm2.pack(side=LEFT,padx=10,fill=Y,expand=YES)
        entry1=Entry(fm2)
        entry1.pack(side=TOP,pady=20)
        entry2=Entry(fm2,show="*")
        entry2.pack(side=TOP,pady=5)
        global entry_paper
        entry_paper=Entry(fm2,width=10)
        entry_paper.pack(side=TOP,pady=40)

        #创建容器3
        fm3=Frame()
        fm3.pack(side=LEFT,padx=10,fill=Y,expand=YES)
        Button(fm3,text="登陆",height=1,width=7,command=GetUser).pack(side=TOP,pady=40)
        Button2=Button(fm3, text="开始做题", height=1, width=7, command=GetPaper).pack(side=TOP, pady=10)
        #循环
        win.mainloop()


def GetUser():  # call back
    # 调用登陆模块
    username = entry1.get()
    password = entry2.get()
    print "Hello " + username + "!"
    printf("Setting Browser...Please Wait", "purple")

    try:
        browser = Login(username, password)
    except:
        BaseException
        print("Wrong password!")

def GetPaper():

        # 多线程2019.7.5
        try:
            thread.start_new_thread(ModelOne,("argc","argv"))
            printf("The Thread is Working ...")
            time.sleep(1)
        except:
            printf("Thread Error:unable to start thread", "red")





def ModelOne(argc,argv):
    # 调用登陆模块
    username = entry1.get()
    password = entry2.get()
    print "Hello " + username + "!"
    printf("Setting Browser...Please Wait", "purple")

    try:
        browser = Login(username, password)
    except:
        BaseException
        print("Wrong password!")

    x = entry_paper.get()
    paperid = int(x)

    A = Answer()
    A.GetAnswer(browser, paperid)


def main():
    # 打印Logo
    logo()
    Login_GUI()



if __name__=='__main__':
    main()

