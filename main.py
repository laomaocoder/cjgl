import tkinter as tk
from tkinter import messagebox
import DataBase as db
from configparser import ConfigParser


username = ''
all_user_window = None;
listx = 20
listy = 20
def checkNumber(a):
    return a.isdigit()

def checkEmpty(a):
    if a == "":
        return False
    return True


# 登录界面
def main():
    def usr_login():
        usr_name = var_usr_name.get()
        usr_pwd = var_usr_pwd.get()
        if usr_name == "":
            is_sign_up = tk.messagebox.askyesno('欢迎', '你还没有注册，现在注册吗?')
            if is_sign_up:
                usr_sign_up()
            return
        try:
            conn = db.Database(host=cf.get('mysql', 'host'), user=cf.get('mysql', 'user'), password=cf.get('mysql', 'password'), db=cf.get('mysql', 'db'))
            sql = 'select * from user where username=%s'
            result = conn.select(sql, data=usr_name)
            if result == ():
                tk.messagebox.showerror(title="错误", message="账号不存在")
                return
            if result[0][2] ==  usr_pwd:
                global username
                username= usr_name
                print(username)
                window.destroy()
                index_page()
            else:
                tk.messagebox.showerror(title="密码错误", message="请确认你的密码是否正确")
        except Exception as e:
            tk.messagebox.showerror(title="错误",message=str(e))


    #设置当前窗口的标题
    window = tk.Tk()
    window.title('登录/注册')
    # 设置窗口大小和居中的代码
    winWidth = 440
    winHeight = 320
    screenWidth = window.winfo_screenwidth()
    screenHeight = window.winfo_screenheight()
    x = int((screenWidth - winWidth) / 2)
    y = int((screenHeight - winHeight) / 2)
    window.geometry("%sx%s+%s+%s" % (winWidth, winHeight, x, y))
    window.resizable(0,0)  #禁止窗口进行缩放

    # welcome image
    canvas = tk.Canvas(window, height=200, width=500)
    image_file = tk.PhotoImage(file='cjgl.png')
    image = canvas.create_image(0, 0, anchor='nw', image=image_file)
    canvas.pack(side='top')

    # user information
    tk.Label(window,font=("楷体", 12, "bold"), text='用户名: ').place(x=50, y=150)
    tk.Label(window,font=("楷体", 12, "bold"), text='密码: ').place(x=50, y=190)

    var_usr_name = tk.StringVar()
    entry_usr_name = tk.Entry(window, textvariable=var_usr_name)
    entry_usr_name.place(x=160, y=150,height=25)
    var_usr_pwd = tk.StringVar()
    entry_usr_pwd = tk.Entry(window, textvariable=var_usr_pwd, show='*')
    entry_usr_pwd.place(x=160, y=190,height=25)
    # login and sign up button
    btn_login = tk.Button(window, font=("楷体", 12, "bold"),text='登录',bg='#000000', fg='#ffffff', command=usr_login)
    btn_login.place(x=170, y=230)
    btn_sign_up = tk.Button(window,font=("楷体", 12, "bold"), text='注册',bg='#000000', fg='#ffffff', command=usr_sign_up)
    btn_sign_up.place(x=270, y=230)
    window.mainloop()
