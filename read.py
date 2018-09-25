# -*- coding:utf-8 -*-


import os
import pyperclip
files = os.listdir()
print(len(files))
c = ''
d = input("d?")
d = int(d)
while c == '' or c == '1':
    flag = 0
    t1 = 0
    t2 = 0
    print(files[d]+'('+str(d)+')')
    f2 = open("reading.txt", 'w' , encoding = "utf-8")
    if (files[d])[-3:] == 'yml':
        with open(files[d], 'r' , encoding = "utf-8") as f1:
            print(os.path.getsize('./'+files[d]))
            text = f1.read()
            for i in range(0,len(text)):
                if text[i] == '\"' and flag == 0:
                    flag = 1
                    t1 = i
                elif text[i] == '\"' and flag == 1:
                    t2 = i
                    flag = 0
                    f2.write(text[t1:t2+1]+'\n')
            f2.close()
            f2 = open("reading.txt",'r',encoding = "utf-8")
            text2 = f2.read()
            pyperclip.copy(text2)
            
    f2.close()
    c = input("继续？")
    if c == '1':
        d = d + 1
        continue
    if c == '0':
        break
    f2 = open("reading.txt",'r',encoding = "utf-8")
    text2 = f2.read()
    tran_list = text2.split('\n\n')
    t1 = 0
    t2 = 0
    s = 0
    flag = 0
    with open(files[d], 'w' , encoding = "utf-8") as f1:
        for i in range(0,len(text)):
            if text[i] == '\"':
                if flag == 0:
                    t1 = i
                    flag = 1
                    u1 = 0
                    u2 = tran_list[s][-1]
                    if tran_list[s][0] == "“" or tran_list[s][0] == "”" or tran_list[s][0] == "\"":
                            u1 = 1
                    if tran_list[s][-1] == "“" or tran_list[s][-1] == "”" or tran_list[s][-1] == "\"":
                            u2 = ''
                    f1.write(text[t2:t1+1]+tran_list[s][u1:-1].replace(' ','')+u2)
                    s = s + 1
                elif flag == 1:
                    t2 = i
                    flag =0
        f1.write(text[t2:])
    f2.close()
    d = d+1
