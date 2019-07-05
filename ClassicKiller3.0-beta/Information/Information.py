from output.printf import printf
from selenium import webdriver
def PrintInformation():
    Information='''
    Version:v1.00-beta
    Date:2019.7
    Github:Migraine-sudo
    Welcome to My Github,to make our world better!   
    Enter M to For More...'''
    printf("\n"+Information,'purple')
    URL = 'https://github.com/migraine-sudo/ClassicKiller'
    ifForMore=raw_input()
    if ifForMore=='M':
        printf("visiting "+URL,'blue')
        browser = webdriver.Firefox()
        browser.get(URL)

    raw_input("Enter to continue...\n\n\n\n\n")

