#coding=utf-8
from output.printf import printf
from time import sleep
from Click.Click import *
from bs4 import BeautifulSoup
import base64
import re
import csv
import codecs

class Answer:
    def __int__(self):
        self.browser=""
        self.page_source=""
        self.soup=''

    #获取页面源码
    def getPaper(self,paperid):
        sleep(1)
        Click_Test(self.browser,paperid)
        self.page_source=self.browser.page_source #获取页面源码


    #获取每道题的题目
    def get_question(self):

        self.soup=BeautifulSoup(self.page_source,'html.parser') #html.parser 而不是html，否则报错
        question_all=self.soup.find_all("h")

        question_list=[]
        for i in range(100):
            Question = "".join(question_all[i])
            #Question = base64.b64decode(Question) # base64转码
            Question=re.match(".*](.*)",Question).group(1) # 正则表达式去掉题号
            #Question=Question.decode("utf-8")
            question_list.append(Question) #添加到question List的结尾
       # for qu in question_list: #打印题目
        #    print qu
        return question_list

    def get_option_name(self):
        self.soup = BeautifulSoup(self.page_source, 'html.parser')
        option=self.soup.find_all("ol")
        #print option
        option_name_list=[]
        for i in range(2,102): #因为网页源码多了两个 ol标签，导致所有的标签需要往后移动两个（2019.6）
            #print "option=" + str(option[1])
            #option_name = re.search('name="(.*)" type', str(option[i])).group(1) before 2019.6
            option_name = re.search('name="(.*)" type', str(option[i])).group(1)
            #print "option_name="+str(option_name)
            option_name_list.append(option_name)
       # for name in option_name_list:
       #     print "name="+name
        return option_name_list

    def get_option_value(self):
        self.soup = BeautifulSoup(self.page_source, 'html.parser')
        option=self.soup.find_all("ol")

        option_value_list=[]
        for i in range(2,102): #2019.6
            option_value = re.search('<label for="(.*)"', str(option[i])).group(1)
            option_value_list.append(option_value)
       # for value in option_value_list:
       #     print "value="+value
        return option_value_list

    def get_answer(self,question_list,option_name_list,option_value_list):
        filename='answer.csv' #放在根目录
        csvFile=codecs.open(filename,'r','gbk')
        reader=csv.reader(csvFile)
        i=0
        answer=[]
        for qu in csvFile:
            answer.append(qu)
        checksum=0
        for i in range(100):#遍历题目
            for qu in answer:
                    if question_list[i] in qu:
                        print "match"+str(i)
                        checksum=0
                        for x in qu: #提取答案
                            if 'A'<=x and x<='E':
                                checksum=1
                                #print "i="+str(i)
                                print "name="+option_name_list[i]
                                if x == 'A':
                                    print "value="+option_value_list[i]
                                    Click_Value(self.browser,option_value_list[i])
                                if x == 'B':
                                    print "value=" + str(int(option_value_list[i])+1)
                                    Click_Value(self.browser,str(int(option_value_list[i])+1))
                                if x == 'C':
                                    print "value=" + str(int(option_value_list[i])+2)
                                    Click_Value(self.browser,str(int(option_value_list[i]) + 2))
                                if x == 'D':
                                    print "value=" + str(int(option_value_list[i])+3)
                                    Click_Value(self.browser,str(int(option_value_list[i]) + 3))
                                if x == 'E' and i>60:
                                    print "value=" + str(int(option_value_list[i])+4)
                                    Click_Value(self.browser,str(int(option_value_list[i]) + 4))
                                #selenium.common.exceptions.NoSuchElementException: Message: Unable to locate element: [id="143517"]

            if checksum==1 and i!=100:
                sleep(0.1)
                try:
                    Click_Next(self.browser)#下一题
                except:
                    BaseException
                #selenium.common.exceptions.ElementNotInteractableException: Message: Element <button class="btn btn-success next-btn"> could not be scrolled into view

            elif checksum==0 and i!=100:
                Click_Value(self.browser, str(int(option_value_list[i]) + 1))#如果没搜到答案，选B
                sleep(0.1)
                try:
                    Click_Next(self.browser)#下一题
                except:
                    BaseException
            else:
                printf ("finish!",'purple')





    #main()
    def GetAnswer(self,browser,paperid):
        self.browser=browser
        self.getPaper(paperid)
        question_list=self.get_question()
        option_name_list=self.get_option_name()
        option_value_list=self.get_option_value()

        self.get_answer(question_list,option_name_list,option_value_list)

        raw_input("请等待到交卷时间。。。\n Enter->继续做题")
        #browser.close()

