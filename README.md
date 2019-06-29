# ClassicKiller
###       --解决某理工学校 经-典-阅-读 做题困扰的方案

概述：基于python2.7的经典阅读刷题工具，基于seleuimn库，通过实现页面模拟人工点击来实现自动做题功能。

实验平台：windows10（x64）FireFox（32）

#### 该程序仅为验证技术实现请勿用于商业目的!

#### 注: 完整的步骤在[说明文档.docx](说明文档.doc )中

## 0x01环境配置

```
步骤
  1.安装python2.7
  2.安装pycharm
  3.安装seleuimn+BeautifulSoup
  4.安装FireFox和对应的驱动
  5.运行程序
```
1.安装python2.7
在官网上下载python2.7,下载到本地安装即可，略

2.安装pycharm（seleuimn+BeautifulSoup）
略

3.安装seleuimn+BeautifulSoup
在pycharm中Setting中找到Project Interpreter
选择python2.7，点击右边的绿色+号，添加seleuimn，BeatuifulSoup库（如果有遗漏，按照下图补充）

4.安装FireFox和对应的驱动
可以使用官网的安装器安装最新版的FireFox，但是出于稳定还是建议安装61.01版。
并且选择32位安装
#否则需要重新下载对应的驱动。

安装驱动
打开环境配置目录里的geckodriver-v0.24.0-win32，解压出来就是浏览器驱动，放入python27的根目录即可。#如果因为浏览器更新而无法使用，请到FireFox的github下载最新的驱动。

5.运行程序
PyCharm-Open在目录中找到解压好的Classic Killer2.0

在源码中找到ClassicKiller2.0.py文件，右击Run(设置Interpreter为python2.7)，运行成功，显示LOGO！


## 0x02使用说明
运行程序，主页面会打印出选项。只需要输入想要执行的序号，程序就会执行。
```
1.Classic Model 经典模式，程序会让你输入账号密码和选择的试卷（根据从上到下的排布，输入想要做的试卷序号即可）
2.Super Model 超级模式，全局刷题模式，一次性刷所有题目。#仍在测试阶段
3.Settings 设置
4.About 打印程序版本号，以及访问代码项目库
5.Exit 退出程序
```
选择经典模式，程序要求输入账号和密码
程序使用FireFox打开题目网页。悲惨世界排在第12个，于是在程序要求输入paperid的位置输入12。


程序自动将答案选填完毕之后，只需要等到可以交卷的时候点提交即可。#这是整个程序唯一需要直接对浏览器操作的地方#或者删掉源码中js限制提交的代码，就能直接交卷

交卷成功后，可以看到成功拿到了90.

## 0x03程序接口

### Click接口

程序封装了Click接口，将点击操作封装为方法。
实现了 ‘点击下一题’，‘点击选项’ 等功能的自动化

源码如下
```
#coding=utf-8
# 封装这个网页内部的一些点击操作

def Click_Submit(browser): #单击提交
    btn_submit=browser.btn_submit=browser.find_element_by_class_name("submit")
    btn_submit.click()

def Click_Test(browser,paperid): #单击测试
    #browser.find_element_by_link_text("测试").click()
    testid=1+3*(int(paperid)-1)
    browser.find_elements_by_class_name('btn')[testid].click()
    #browser.find_element_by_partial_link_text("测试").click()
    #browser.find_element_by_class_name("btn btn-defualt btn-sm")[1].click()

def Click_Next(browser): #单击下一题
    browser.find_element_by_xpath("//*[contains(text(),'下一题')]").click()

def Click_Value(browser,value):
browser.find_element("id",value).click() #因为源码中id和value值相同
```



## 0x04更新
### 2019.6.29
网站更新了之后，页面多了两个lo标签，导致程序查找选项出错。
修改get_option_name函数报错

修正了Click_Test函数查找按钮的偏差


### 未来展望
增加try catch部分，防止程序崩溃。
增加多选试卷模式。
