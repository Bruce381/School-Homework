'''
2021   Bruce   取款机

'''

while True : #整体循环

    import random #导入随机
    import time #导入时间
    
    MONEY=1000000000 #我超有钱（笑）

    wrong=0
    password=123456

    while wrong < 3 : #三次错误跳出
        #peint("请输入账号")
        #name=input()
        
        print("请输入密码")
        key=int(input())
        
        if key == password :
            print("密码正确")
            
            num=random.randint(1000,10000) #生成验证码
            
            print("验证码为：",num)
            a=int(input("请输入验证码："))

            
            if a == num : #判断验证码
                
                print("验证码正确")
                
                while True : #操作循环
                    print("A.存钱 B.取钱 C.个人资料 D.退出")
                
                    b=str(input())

                    if b == 'A' or b == '存钱'  :
                        put=int(input("请输入存钱张数："))
                        MONEY=100*put+MONEY
                        #q=MONEY*(1+0.0125)
                        print("余额：",MONEY)#,"利息：",q)
                    
                    elif b == 'B' or b == '取钱' :
                        get=int(input("请输入取钱张数"))
                        MONEY=MONEY-100*get
                        #q=MONEY*(1+0.0125)
                        print("余额：",MONEY)#,"利息：",q)
                        
                    elif b == 'C' or b == '个人资料' :
                        my=str(input("A.更改密码 B.返回 "))

                        if my == 'A' or my =='更改密码' :
                            password=int(input("请输入新密码："))
                            print("密码修改成功")
                            
                        else :
                            continue

                    else :
                        break

            else :
                print("验证码错误请重新输入")

        else :
            wrong+=1
            print("密码错误")

    print("错误次数过多请稍后再试")
    time.sleep(5)
