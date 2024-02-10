from random import *
from easygui import*
import time
import turtle
import os
def begin():
    a = os.path.exists("D:\\Desktop Manager运行根目录\\")
    if a == False:
        os.makedirs("D:\\Desktop Manager运行根目录")


l = 0


def clean():
    mj=buttonbox(msg="确定清除结果吗？",choices=["确定","取消"],title="Desktop Manager 5.0")
    if mj == "确定":
        a = os.listdir("D:\\Desktop Manager运行根目录\\")
        if a == []:
            msgbox("没有可以清除的文件",title="Desktop Manager 5.0")
        else:
            for i in a:
                os.remove("D:\\Desktop Manager运行根目录\\" + i)


def xuijishu():
    global l
    a = multenterbox(msg="请输入以下项",fields=["请输入随机数最小值","请输入随机数最大值","请输入生成数量"],title="Desktop Manager 5.0")

    w = a[0]
    v = a[1]
    x = a[2]

    w = int(w)
    v = int(v)
    x = int(x)
    a = []
    for i in range(x):
        a.append(str(randint(w, v)))
    b = ""
    nv = 1
    for i in a:
        b = b + i
        if nv != x:
            b = b + ","
            nv= nv+1
    msgbox(msg="结果为" + b, title="Desktop Manager 5.0")
    with open("D:\\Desktop Manager运行根目录\\"+str(time.time())+"随机数结果.txt", "w") as f:
        f.write("随机数结果为" + b)
    l = l+1

def dakai():
    global l
    g = enterbox("请输入文件路径", title="Desktop Manager 5.0")
    os.system(g)
    l += 1

def zhishupanduan():
    global l
    a = enterbox("请输入", title="Desktop Manager 5.0")
    a = int(a)
    b = 0
    c = []
    if a == 0 or a == 1:
        msgbox("本数不为质数或合数", title="Desktop Manager 5.0")
    else:
        for i in range(1, a + 1):
            if a % i == 0:
                b = b + 1
                c.append(i)

        if b == 2:
            msgbox("质数", title="Desktop Manager 5.0")
            msgbox("它的约数有" + str(c), title="Desktop Manager 5.0")
            with open("D:\\Desktop Manager运行根目录\\"+str(time.time())+"质数判断结果.txt", "w") as f:
                f.write(str(a) + "是质数，它的约数有" + str(c))
            l += 1
        else:
            msgbox("合数", title="Desktop Manager 5.0")
            msgbox("它的约数有" + str(c), title="Desktop Manager 5.0")
            with open("D:\\Desktop Manager运行根目录\\"+str(time.time())+"质数判断结果.txt", "w") as f:
                f.write(str(a) + "是合数，它的约数有" + str(c))
            l += 1

def jiamijiemi():
    global l
    a = buttonbox(msg="你需要加密还是解密", choices=["加密", "解密"], title="Desktop Manager 5.0")
    if a == "加密":
        b = enterbox("请输入要加密的内容", title="Desktop4.6")
        c = enterbox("请输入要加密的格数（输入数字即可，最大为9，最小为1）", title="Desktop Manager 5.0")
        c = int(c)
        d = ""
        for i in b:
            e = ord(i)
            e = e + c
            e = chr(e)
            d = d + e
        d = str(d)
        c = str(c)

        msgbox("加密结果为" + c + d, title="Desktop Manager 5.0")
        with open("D:\\Desktop Manager运行根目录\\"+str(time.time())+"加密结果.txt", "w",encoding="gbk") as f:
            f.write("加密结果为" + c+d)
        l += 1

    if a == "解密":
        b = enterbox("请输入要解密的内容", title="Desktop Manager 5.0")

        c = int(b[0])
        d = ""
        for i in range(len(b) - 1):
            e = ord(b[i + 1])
            e = e - c
            e = chr(e)
            d = d + e
            d = str(d)
        msgbox("解密结果为" + d, "Desktop Manager 5.0")
        with open("D:\\Desktop Manager运行根目录\\"+str(time.time())+"解密结果.txt", "w",encoding="gbk") as f:
            f.write("解密结果为" + d)
        l += 1
bn=""
def paoyingbi():
    global l,bn
    a = enterbox("输入抛硬币的次数", title="Desktop Manager 5.0")

    a = int(a)
    z = 0
    f = 0
    g = 0
    for i in range(a):
        bn=bn+"这是第" + str(i + 1) + "次模拟\r\n"
        c  = randint(0, 1)
        if c == 0:
            z = z + 1
            bn = bn+"本次结果为正\r\n"
        if c == 1:
            f = f + 1
            bn = bn + "本次结果为反\r\n"
    msgbox("正面有" + str(z) + "次" + "," + "反面有" + str(f) + "次", title="Desktop Manager 5.0")
    with open("D:\\Desktop Manager运行根目录\\"+str(time.time())+"抛硬币模拟器结果.txt", "w") as m:
        m.write(bn+"正面有" + str(z) + "次" + "," + "反面有" + str(f) + "次")
    l += 1

def wenjianjiashengcheng():
    global l
    a = enterbox("请输入需要生成文件夹的目录", title="Desktop Manager 5.0")
    b = enterbox("请输入需要生成文件夹的名称", title="Desktop Manager 5.0")
    os.chdir(a)
    os.makedirs(b)
    msgbox("完成", title="Desktop Manager 5.0")
    l += 1






def bqsm():
    turtle.setup(width=1000, height=1000)
    turtle.penup()
    turtle.goto(0, -50)
    turtle.pendown()
    turtle.speed("fastest")

    turtle.circle(100, 360)
    turtle.color("blue")
    turtle.circle(200, 360)
    turtle.left(90)
    turtle.fd(400)
    turtle.left(90)
    turtle.color("green")
    turtle.circle(100, 360)
    turtle.color("blue")
    turtle.circle(200, 90)
    turtle.left(90)
    turtle.color("purple")
    turtle.fd(400)
    turtle.left(90)
    turtle.circle(100, 360)
    turtle.color("blue")
    turtle.circle(200, 180)
    turtle.right(360)
    turtle.color("purple")
    turtle.circle(100, 360)
    turtle.color("orange")
    turtle.fd(200)
    turtle.left(90)
    turtle.fd(400)
    turtle.left(90)
    turtle.fd(400)
    turtle.left(90)
    turtle.fd(400)
    turtle.left(90)
    turtle.fd(200)

    turtle.penup()
    turtle.goto(0, -100)
    turtle.pendown()
    turtle.write(arg="北极星工作室软件部开发科python部出品", align="center", font=("宋体", 20, "normal"))
    turtle.hideturtle()


    turtle.mainloop()
def main():
    while True:
        begin()
        if l == 0:
            bqsm()

        msgbox("欢迎", title="Desktop Manager 5.0")
        n = choicebox(msg="请选择功能",
                      choices=["打开", "质数判断", "随机数", "加密解密", "抛硬币模拟器", "文件夹生成", "清除保存的结果",
                               "退出"], title="Desktop Manager 5.0")
        if n == "随机数":
            xuijishu()

        elif n == "打开":
            dakai()
        elif n == "质数判断":
            zhishupanduan()
        elif n == "加密解密":
            jiamijiemi()
        elif n == "抛硬币模拟器":
            paoyingbi()
        elif n == "文件夹生成":
            wenjianjiashengcheng()
        elif n == "清除保存的结果":
            clean()
        else:
            break


cv = os.path.exists("D:\\Desktop Manager权限申请结果保存.txt")
if cv == True:
    with open("D:\\Desktop Manager权限申请结果保存.txt","r")as b:
        g = b.read()
    if g =="path":

        main()

else:
    with open("D:\\Desktop Manager权限申请结果保存.txt","w")as b:
        mn = buttonbox(msg="Desktop Manager申请以下权限\r\n1.文件写入权\r\n2.文件调用权\r\n3.文件更改权",title="Desktop Manager 5.0",choices=["我同意","我不同意"])
        if mn == "我同意":
            b.write("path")

            main()


        else:
            os.remove("D:\\Desktop Manager权限申请结果保存.txt")


