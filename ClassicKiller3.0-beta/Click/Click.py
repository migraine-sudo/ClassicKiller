#coding=utf-8
# 封装这个网页内部的一些点击操作

def Click_Submit(browser): #单击提交
    btn_submit=browser.btn_submit=browser.find_element_by_class_name("submit")
    btn_submit.click()

def Click_Test(browser,paperid): #单击测试
    #browser.find_element_by_link_text("测试").click()
    #testid=1+3*(int(paperid)-1)#before 2019.6
    testid = 2+3*(int(paperid)-1)
    browser.find_elements_by_class_name('btn')[testid].click()
    #browser.find_element_by_partial_link_text("测试").click()
    #browser.find_element_by_class_name("btn btn-defualt btn-sm")[1].click()

def Click_Next(browser): #单击下一题
    browser.find_element_by_xpath("//*[contains(text(),'下一题')]").click()

def Click_Value(browser,value):
    browser.find_element("id",value).click() #因为源码中id和value值相同
