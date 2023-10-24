# 破解凯撒加密

def jiema(m):
    for i in m:
        if i == ' ':
            return " "
        elif 97 + key <= ord(m) < 123 or 65 + key <= ord(m) < 92:
            m = chr(ord(m) - key)
            return m
        elif 97 <= ord(m) < 97 + key or 65 <= ord(m) < 65 + key:
            m = chr(ord(m) - key + 26)
            return m


m = input('请输入密文：')
out = ''
for key in range(1, 27):
    for n in list(map(jiema, m)):
        out = out + str(n)
    print('第%d个可能的结果是%s' % (key, out))
    out = ''
