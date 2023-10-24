from tkinter import *

def user():
    Accound=a_entry.get()#获取用户名
    Password=b_entry.get()#获取密码
    a_len = len(Accound)#获取用户名长度
    b_len = len(Password)#获取密码长度
    if Accound == 'bruce' and Password == '123' :
        msg_label["text"] = "登陆成功"
        
    elif Accound == 'bruce' and Password != '123' :
        msg_label["text"] = "密码错误"
        b_entry.delete(0,b_len)#清除区域
        
    else :
        msg_label["text"] = "用户名或密码错误"
        a_entry.delete(0,a_len)#清除区域
        b_entry.delete(0,b_len)#清除区域

root=Tk()
root.title('登录/注册')#标题
root.geometry('230x100')#窗口大小

#用户
a_label = Label(root,text='用户名:')
a_label.grid(row=0,column=0,sticky=W)
a_entry = Entry(root)
a_entry.grid(row=0,column=1,sticky=E)

#密码
b_label = Label(root,text="密码:")
b_label.grid(row=1,column=0,sticky=W)
b_entry = Entry(root)
b_entry["show"] = "*" #显示*
b_entry.grid(row=2,column=1,sticky=E)

#按钮
btn = Button(root,text="登录",command=user)
btn.grid(row=2,column=1,sticky=E)

#提示
msg_label = Label(root,text="")
msg_label.grid(row=3)


root.mainloop()#执行
