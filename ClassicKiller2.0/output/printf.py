#coding:utf-8
"""
0  All attributes off 默认值
1  Bold (or Bright) 粗体 or 高亮
4  Underline 下划线
5  Blink 闪烁
7  Invert 反显
30 Black text
31 Red text
32 Green text
33 Yellow text
34 Blue text
35 Purple text
36 Cyan text
37 White text
40 Black background
41 Red background
42 Green background
43 Yellow background
44 Blue background
45 Purple background
46 Cyan background
47 White background
"""

def printf(t,c="n",b="n"):
    color={
        "red":"31","black":"30","green":"32","yellow":"33","blue":"34","white":"37",
        "bblack":"40","bred":"41","bgreen":"42","byellow":"43","bblue":"44","bwhite":"47","purple":"35",
        "n":"0"
    }
    print "\033[0;"+color[c]+";"+color[b]+"m"+t+"\033[0m"