from tkinter import *

def log_in():
    user={'admin':123456}

    usr=str(input(e1.get()))
    pw=str(input(e2.get()))
    
    if usr in user :
        
        pw1=user.get(usr)
        
        if pw == pw1 :
            msg_Message2["text"]="登录成功"
    else:
        msg_Message1["text"]="无该用户"
        e1.delete(0,END)
        e2.delete(0,END)
        

#初始化tk
app = Tk()

app.title("HELLO")
app.geometry('650x450')
app.resizable(width=False,height=False)

#标题
Label(app,text='welcome to wrold',font=("Arial",20),width=30,height=1,bg='pink').pack()

#标题
Label(app,text='用户名:',font=('黑体',10)).place(x=90,y=90,anchor=NW)
Label(app,text='密  码:',font=('黑体',10)).place(x=90,y=130,anchor=NW)

#输入框
e1=Entry(app)
e1.place(x=150,y=90,anchor=NW)

e2=Entry(app,show="*")
e2.place(x=150,y=130,anchor=NW)

#按钮
b1=Button(app,text='登录',font=('黑体',10),relief='flat')
b1.place(x=220,y=160,anchor=NW)

b2=Button(app,text='注册',font=('黑体',10),relief='flat')
b2.place(x=140,y=160,anchor=NW)



app.mainloop()
