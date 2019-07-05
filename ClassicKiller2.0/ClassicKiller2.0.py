#coding=utf-8
from output.printf import printf
from Login.Login import Login
from GetAnswer.GetAnswer import Answer
from Information.Information import PrintInformation




def logo():
    printf( '''
        _________ .__                       .__        ____  __.__.__  .__                
        \_   ___ \|  | _____    ______ _____|__| ____ |    |/ _|__|  | |  |   ___________ 
        /    \  \/|  | \__  \  /  ___//  ___/  |/ ___\|      < |  |  | |  | _/ __ \_  __ \ 
        \     \___|  |__/ __ \_\___ \ \___ \|  \  \___|    |  \|  |  |_|  |_\  ___/|  | \/
        \______  /____(____  /____  >____  >__|\___  >____|__ \__|____/____/\___  >__|   
                \/          \/     \/     \/        \/        \/                 \/       
                                                            Editor:Migraine-sudo
                                                            2019.5  
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


def main():
    # 打印Logo
    logo()
    ifContinue = True
    while ifContinue:
        model = Model()
        if model=='1':#常规模式
            #调用登陆模块
            username = raw_input("Please input your username<<")
            password = raw_input("password<<")
            while (True):
                printf("Setting Browser...Please Wait", "purple")
                try :
                    browser = Login(username,password)
                except :
                    BaseException
                    print("Wrong password!")
                    username = raw_input("Please reinput your username<<")
                    password = raw_input("password<<")
                    continue

                paperid = raw_input("Please input the ID of your paper(enter 0 to exit)<<")
                if paperid=='0':
                    break
                #创建解答模块的实例
                A=Answer()
                A.GetAnswer(browser,paperid)
        if model=='2':
            printf("Warning ,this models is still in test!")
            username = raw_input("Please input your username<<")
            password = raw_input("password<<")
            browser = Login(username,password)
            while (True):
                papers=raw_input("How many papers do you want to Kill<<")
                for i in range(1,papers):
                    A = Answer()
                    A.GetAnswer(browser, i)
        if model=='3':
            printf("\n\tSettings is not available now!\n\n",'blue')
        if model=='4':
            PrintInformation()
        if model=='5':
            ifContinue=False
            printf("Good Night!","purple")

if __name__=='__main__':
    main()

