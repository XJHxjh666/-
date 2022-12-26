import tkinter as tkinte
import tkinter
import tkinter as tk
import tkinter.messagebox
from tkinter import simpledialog
import tkinter.ttk
import requests
import turtle
import json
import datetime
import os
import time
from tkinter import colorchooser
import webbrowser
import pygame
from pygame.locals import *
import random
import urllib.request
import ctypes
from PIL import Image, ImageTk
import io
import pygame.gfxdraw
from collections import namedtuple
import subprocess
import sys
import shutil
import stat
import threading
import tkinter as tk
from tkinter import ttk, END
from time import sleep
from tkinter.filedialog import askdirectory
from typing import Tuple
from tkinter import filedialog
import base64
import turtle

TIME1 = time.strftime("%H")
ds=1
banben='v1.2.4'
def update():
      #tk.messagebox.showinfo(title = '提示',message='检查更新可能较慢，程序可能会未响应，请耐心等待...')
      url = 'https://gitcode.net/xingjiahao200910/xgj/-/raw/master/index.html'
      try:
            res = requests.get(url).text
            if res[0:-1] != banben:
                  url='https://gitcode.net/xingjiahao200910/xgj/-/raw/master/public/index.html'
                  res1 = requests.get(url).text
                  result = tkinter.messagebox.askquestion('询问', '检测到新版本'+res+'是否更新？\n\n'+res1)
                  if result == 'yes':
                        url = 'https://gitcode.net/xingjiahao200910/xgj/-/raw/master/%E9%82%A2%E6%B0%8F%E5%B0%8F%E5%B7%A5%E5%85%B7'+res+'.exe?inline=false'
                        #tk.messagebox.showinfo(title = '更新提示',message='请访问 https://xjhxjh666.github.io/'+res+'.exe')
                        webbrowser.open(url, new=0, autoraise=True)
                        tk.messagebox.showinfo(title = '更新提示',message='请查看您的电脑默认浏览器')
                        '''
                        content = requests.get(url).content
                        exe='邢氏小工具'+res[0:-2]+'.exe'
                        with open(exe, 'wb') as file:
                              file.write(content)'''
            else:
                  tk.messagebox.showinfo(title = '提示',message='当前已是最新版')
      except:
            tkinter.messagebox.showerror(title = '出错了',message='请检查网络后重试')
def gettime():
      TIME = time.strftime("%H:%M:%S")
      var.set(time.strftime("%H:%M:%S"))   # 获取当前时间
      root.after(1000,gettime)

def delete():
      result = tkinter.messagebox.askquestion('询问', '您真的要卸载吗？')
      if result == 'yes':
            try:
                  subprocess.Popen("uninst.exe")
                  sys.exit()
            except:
                  tk.messagebox.showinfo(title = '提示',message='卸载失败\n请联系软件开发者')

def bg2():
    color=tkinte.colorchooser.askcolor()
    if color != (None, None):
          print(color)
          colorstr=str(color)
          root.config(background=colorstr[-9:-2])

def fankui():
      webbrowser.open('https://xjhxjh666.github.io/xgj/', new=0, autoraise=True)
def setting():
      root1 = tk.Toplevel(root)
      root1.title('设置')#标题
      root1.geometry('200x300')  
      root1.resizable(False, False)#固定窗体
      root1.config(background="#6fb705")
      yu=tkinte.Button(root1, text='自定义背景',command=bg2,width=10, height=1)
      yu.pack()
      yu.place(x=50,y=30)
      yu2=tkinte.Button(root1, text='检查更新',command=update,width=10, height=1)
      yu2.pack()
      yu2.place(x=50,y=90)
      yu3=tkinte.Button(root1, text='卸载软件',command=delete,width=10, height=1)
      yu3.pack()
      yu3.place(x=50,y=150)
      yu4=tkinte.Button(root1, text='意见反馈',command=fankui,width=10, height=1)
      yu4.pack()
      yu4.place(x=50,y=210)
      
      
def tianqi():
    s = simpledialog.askstring('天气查询', '请输入城市：', initialvalue='')
    if s != '' and s != None:
        root1 = tk.Toplevel(root)
        root1.title('天气-'+s)#标题
        root1.geometry('350x350') 
        def callback():
             print('')
        
        try:
            url = 'https://api.vvhan.com/api/weather?city='+s+'&type=week'
            headers = {'Content-Type': 'application/json;charset=UTF-8'}
            r = requests.request("POST", url, headers=headers)
            a = r.json()
            if 'message' in a:
                tk.Label(root1,text=a['message']).pack(fill='x')
            elif a['data'][0]['date'] == None:
                tk.Label(root1,text='未知错误：可能暂不支持该城市').pack(fill='x')
            else:
                b= a['data']
                c = b[0]
                d = b[1]#当日
                e = b[2]#次日
                g = b[3]
                city = s

                date = d['date']
                week = d['week']
                tianqi = d['type']
                high = d['high']
                low = d['low']
                fengxiang = d['fengxiang']
                fengli = d['fengli']

                date1 = e['date']
                week1 = e['week']
                tianqi1 = e['type']
                high1 = e['high']
                low1= e['low']
                fengxiang1 = e['fengxiang']
                fengli1 = e['fengli']

                date2 = g['date']
                week2 = g['week']
                tianqi2 = g['type']
                high2 = g['high']
                low2= g['low']
                fengxiang2 = g['fengxiang']
                fengli2 = g['fengli']

                f = city+':\n'+'\n'+date+' '+week+'\n'+tianqi+'\n'+high+'\n'+low+'\n'+fengxiang+'\n'+fengli+'\n'+'\n'+date1+''+week1+'\n'+tianqi1+'\n'+high1+'\n'+low1+'\n'+fengxiang1+'\n'+fengli1+'\n''\n'+date2+''+week2+'\n'+tianqi2+'\n'+high2+'\n'+low2+'\n'+fengxiang2+'\n'+fengli2  
                qw=tk.Label(root1,text=city+'：')
                qw.pack()
                qw.place(x=0,y=0)

                qw=tk.Label(root1,text=date)
                qw.pack()
                qw.place(x=0,y=40)
                
                qw=tk.Label(root1,text=tianqi)
                qw.pack()
                qw.place(x=0,y=60)

                qw=tk.Label(root1,text=fengxiang+'，'+fengli)
                qw.pack()
                qw.place(x=0,y=80)
                
                qw=tk.Label(root1,text=high+'，'+low)
                qw.pack()
                qw.place(x=0,y=100)

                qw=tk.Label(root1,text=date1)
                qw.pack()
                qw.place(x=0,y=140)
                
                qw=tk.Label(root1,text=tianqi1)
                qw.pack()
                qw.place(x=0,y=160)

                qw=tk.Label(root1,text=fengxiang1+'，'+fengli1)
                qw.pack()
                qw.place(x=0,y=180)
                
                qw=tk.Label(root1,text=high1+'，'+low1)
                qw.pack()
                qw.place(x=0,y=200)

                qw=tk.Label(root1,text=date2)
                qw.pack()
                qw.place(x=0,y=240)
                
                qw=tk.Label(root1,text=tianqi2)
                qw.pack()
                qw.place(x=0,y=260)

                qw=tk.Label(root1,text=fengxiang2+'，'+fengli2)
                qw.pack()
                qw.place(x=0,y=280)
                
                qw=tk.Label(root1,text=high2+'，'+low2)
                qw.pack()
                qw.place(x=0,y=300)

                if '阴' in tianqi:
                    url = "https://codingcdn.gaotu100.com/prod%2Fpython%2Ffile%2F%E9%98%B4_c4c4b80c-b5aa-4493-8e52-18e4d0c60ee2.png"
                    image_bytes = requests.get(url).content
                    data_stream = io.BytesIO(image_bytes)
                    pil_image = Image.open(data_stream)
                    w, h = pil_image.size
                    fname = url.split('/')[-1]
                    sf = "{} ({}x{})".format(fname, w, h)
                    tk_image = ImageTk.PhotoImage(pil_image)
                    label = tk.Label(root1, image=tk_image)
                    label.pack()
                    label.place(x=200,y=50)

                if '云' in tianqi:
                    url = "https://codingcdn.gaotu100.com/prod%2Fpython%2Ffile%2F%E5%A4%9A%E4%BA%91_76a74712-bd0c-4f00-85ca-82ce13a7e815.png"
                    image_bytes = requests.get(url).content
                    data_stream = io.BytesIO(image_bytes)
                    pil_image = Image.open(data_stream)
                    w, h = pil_image.size
                    fname = url.split('/')[-1]
                    sf = "{} ({}x{})".format(fname, w, h)
                    tk_image = ImageTk.PhotoImage(pil_image)
                    label = tk.Label(root1, image=tk_image)
                    label.pack(padx=5, pady=5)
                    label.place(x=200,y=50)
                if '晴' in tianqi:
                    url = "https://codingcdn.gaotu100.com/prod%2Fpython%2Ffile%2F%E6%99%B4_a99f6b0c-ae06-421b-9875-20595757b90d.png"
                    image_bytes = requests.get(url).content
                    data_stream = io.BytesIO(image_bytes)
                    pil_image = Image.open(data_stream)
                    w, h = pil_image.size
                    fname = url.split('/')[-1]
                    sf = "{} ({}x{})".format(fname, w, h)
                    tk_image = ImageTk.PhotoImage(pil_image)
                    label = tk.Label(root1, image=tk_image)
                    label.pack(padx=5, pady=5)
                    label.place(x=200,y=50)
                if '雪' in tianqi:
                    url = "https://codingcdn.gaotu100.com/prod%2Fpython%2Ffile%2F%E9%9B%AA_96cc26aa-27d7-4faa-bc8f-3969950d06ba.png"
                    image_bytes = requests.get(url).content
                    data_stream = io.BytesIO(image_bytes)
                    pil_image = Image.open(data_stream)
                    w, h = pil_image.size
                    fname = url.split('/')[-1]
                    sf = "{} ({}x{})".format(fname, w, h)
                    tk_image = ImageTk.PhotoImage(pil_image)
                    label = tk.Label(root1, image=tk_image)
                    label.pack(padx=5, pady=5)
                    label.place(x=200,y=50)

                if '阴' in tianqi1:
                    url = "https://codingcdn.gaotu100.com/prod%2Fpython%2Ffile%2F%E9%98%B4_c4c4b80c-b5aa-4493-8e52-18e4d0c60ee2.png"
                    image_bytes = requests.get(url).content
                    data_stream = io.BytesIO(image_bytes)
                    pil_image = Image.open(data_stream)
                    w, h = pil_image.size
                    fname = url.split('/')[-1]
                    sf = "{} ({}x{})".format(fname, w, h)
                    tk_image = ImageTk.PhotoImage(pil_image)
                    label1 = tk.Label(root1, image=tk_image)
                    label1.pack()
                    label1.place(x=200,y=150)
                if '云' in tianqi1:
                    url = "https://codingcdn.gaotu100.com/prod%2Fpython%2Ffile%2F%E5%A4%9A%E4%BA%91_76a74712-bd0c-4f00-85ca-82ce13a7e815.png"
                    image_bytes = requests.get(url).content
                    data_stream = io.BytesIO(image_bytes)
                    pil_image = Image.open(data_stream)
                    w, h = pil_image.size
                    fname = url.split('/')[-1]
                    sf = "{} ({}x{})".format(fname, w, h)
                    tk_image = ImageTk.PhotoImage(pil_image)
                    label = tk.Label(root1, image=tk_image)
                    label.pack(padx=5, pady=5)
                    label.place(x=200,y=150)
                if '晴' in tianqi1:
                    url = "https://codingcdn.gaotu100.com/prod%2Fpython%2Ffile%2F%E6%99%B4_a99f6b0c-ae06-421b-9875-20595757b90d.png"
                    image_bytes = requests.get(url).content
                    data_stream = io.BytesIO(image_bytes)
                    pil_image = Image.open(data_stream)
                    w, h = pil_image.size
                    fname = url.split('/')[-1]
                    sf = "{} ({}x{})".format(fname, w, h)
                    tk_image = ImageTk.PhotoImage(pil_image)
                    label = tk.Label(root1, image=tk_image)
                    label.pack(padx=5, pady=5)
                    label.place(x=200,y=150)
                if '雪' in tianqi1:
                    url = "https://codingcdn.gaotu100.com/prod%2Fpython%2Ffile%2F%E9%9B%AA_96cc26aa-27d7-4faa-bc8f-3969950d06ba.png"
                    image_bytes = requests.get(url).content
                    data_stream = io.BytesIO(image_bytes)
                    pil_image = Image.open(data_stream)
                    w, h = pil_image.size
                    fname = url.split('/')[-1]
                    sf = "{} ({}x{})".format(fname, w, h)
                    tk_image = ImageTk.PhotoImage(pil_image)
                    label = tk.Label(root1, image=tk_image)
                    label.pack(padx=5, pady=5)
                    label.place(x=200,y=150)

                if '阴' in tianqi2:
                    url = "https://codingcdn.gaotu100.com/prod%2Fpython%2Ffile%2F%E9%98%B4_c4c4b80c-b5aa-4493-8e52-18e4d0c60ee2.png"
                    image_bytes = requests.get(url).content
                    data_stream = io.BytesIO(image_bytes)
                    pil_image = Image.open(data_stream)
                    w, h = pil_image.size
                    fname = url.split('/')[-1]
                    sf = "{} ({}x{})".format(fname, w, h)
                    tk_image = ImageTk.PhotoImage(pil_image)
                    label1 = tk.Label(root1, image=tk_image)
                    label1.pack()
                    label1.place(x=200,y=250)
                if '云' in tianqi2:
                    url = "https://codingcdn.gaotu100.com/prod%2Fpython%2Ffile%2F%E5%A4%9A%E4%BA%91_76a74712-bd0c-4f00-85ca-82ce13a7e815.png"
                    image_bytes = requests.get(url).content
                    data_stream = io.BytesIO(image_bytes)
                    pil_image = Image.open(data_stream)
                    w, h = pil_image.size
                    fname = url.split('/')[-1]
                    sf = "{} ({}x{})".format(fname, w, h)
                    tk_image = ImageTk.PhotoImage(pil_image)
                    label = tk.Label(root1, image=tk_image)
                    label.pack(padx=5, pady=5)
                    label.place(x=200,y=250)
                if '晴' in tianqi2:
                    url = "https://codingcdn.gaotu100.com/prod%2Fpython%2Ffile%2F%E6%99%B4_a99f6b0c-ae06-421b-9875-20595757b90d.png"
                    image_bytes = requests.get(url).content
                    data_stream = io.BytesIO(image_bytes)
                    pil_image = Image.open(data_stream)
                    w, h = pil_image.size
                    fname = url.split('/')[-1]
                    sf = "{} ({}x{})".format(fname, w, h)
                    tk_image = ImageTk.PhotoImage(pil_image)
                    label = tk.Label(root1, image=tk_image)
                    label.pack(padx=5, pady=5)
                    label.place(x=200,y=250)
                if '雪' in tianqi2:
                    url = "https://codingcdn.gaotu100.com/prod%2Fpython%2Ffile%2F%E9%9B%AA_96cc26aa-27d7-4faa-bc8f-3969950d06ba.png"
                    image_bytes = requests.get(url).content
                    data_stream = io.BytesIO(image_bytes)
                    pil_image = Image.open(data_stream)
                    w, h = pil_image.size
                    fname = url.split('/')[-1]
                    sf = "{} ({}x{})".format(fname, w, h)
                    tk_image = ImageTk.PhotoImage(pil_image)
                    label = tk.Label(root1, image=tk_image)
                    label.pack(padx=5, pady=5)
                    label.place(x=200,y=250)
                    
        except:
            tkinter.messagebox.showerror(title = '出错了',message='网络错误或该功能正在维护')
     
def wuliu():
    s = simpledialog.askstring('物流查询', '请输入物流单号：', initialvalue='')
    if s != '' and s != None:
        root1 = tk.Toplevel(root)
        root1.title('物流-'+s)#标题
        def callback():
             print('')
        
        try:
            url = "https://v2.alapi.cn/api/kd"
            payload = "token=fPzdCy22nysKhDF6&number="+s+"&com=&order=asc"
            headers = {'Content-Type': "application/x-www-form-urlencoded"}

            response = requests.request("POST", url, data=payload, headers=headers)

            a = response.text
            a=json.loads(a)
            d = '查询结果\n'
            if a['code'] == 200:
                b=a['data']
                c = b['info']
                for i in c:
                    time = '时间：'+i['time']
                    zhuangtai = '状态：'+i['content']
                    d = d+time+'\n'+zhuangtai+'\n'
                tk.Label(root1,text=d).pack(fill='x')
            else:
                tk.Label(root1,text='请填写正确的快递编号或不支持该物流公司').pack(fill='x')
        except:
            tkinter.messagebox.showerror(title = '出错了',message='网络错误或该功能正在维护')

def chengyu():
    s = simpledialog.askstring('成语查询', '请输入您要查询的成语：', initialvalue='')
    if s != '' and s != None:
        root1 = tk.Toplevel(root)
        root1.title('成语-'+s)#标题
        tk.messagebox.showinfo(title = '提示',message='请稍后...')
        def callback():
             print('')
        try:
            url = 'http://api.qingyunke.com/api.php?key=free&appid=0&msg=成语'+s        
            headers = {'Content-Type': 'application/json;charset=UTF-8'}
            r = requests.request("POST", url,  headers=headers)
            a = r.json()
            b = a['content']
            if '{br}' in b:
                b = b.replace('{br}','\n')
            tk.Label(root1,text=b).pack(fill='x')
        except:
            tkinter.messagebox.showerror(title = '出错了',message='网络错误或该功能正在维护')

def xiaohua():
    if 1==1:
        root1 = tk.Toplevel(root)
        root1.title('笑话')#标题
        tk.messagebox.showinfo(title = '提示',message='请稍后...')
        def callback():
            print('')
        try:
            url = 'http://api.qingyunke.com/api.php?key=free&appid=0&msg=笑话'        
            headers = {'Content-Type': 'application/json;charset=UTF-8'}
            r = requests.request("POST", url, headers=headers)
            a = r.json()
            b = a['content']
            b = b.replace('{br}','\n')
            b = b.replace('\n提示：按分类看笑话请发送“笑话分类”',' ')
            tk.Label(root1,text=b).pack(fill='x')
        except:
            tkinter.messagebox.showerror(title = '出错了',message='网络错误或该功能正在维护')

def xinwen():
    if 1==1:
        root1 = tk.Toplevel(root)
        root1.title('新闻')#标题
        '''
        root1.geometry('500x500')  
        root1.resizable(False, False)#固定窗体
        sb = tk.Scrollbar(root1)               # 创建Scrollbar组件
        sb.pack(side='right', fill='y')      # 右对齐，填满整个y轴
        lb = tk.Listbox(root, xscrollcommand=sb.set)  # 滚动listbox里面内容，滚动条跟着移动'''


        #tk.messagebox.showinfo(title = '提示',message='请稍后...')
        def callback():
             print('')
        
        try:
            url = 'https://api.vvhan.com/api/60s?type=json'
            headers = {'Content-Type': 'application/json;charset=UTF-8'}
            r = requests.request("POST",url,headers=headers)
            a = r.json()
            if a['success'] == False:
                tk.Label(root1,text='网络错误').pack(fill='x')
            else:
                b = a['name']+'\n'
                time = a['time']
                day = time[0]+'  '
                day_1 = time[1]+'  '
                week = time[2]+'\n'
                c = a['data']
                d = '1.'+c[0]+'\n'
                e = '2.'+c[1]+'\n'
                f = '3.'+c[2]+'\n'
                f1 = '4.'+c[3]+'\n'
                f2 = '5.'+c[4]+'\n'
                f3 = '6.'+c[5]+'\n'
                f4 = '7.'+c[6]+'\n'
                f5 = '8.'+c[7]+'\n'
                a1 = b+day+day_1+week+d+e+f
                tk.Label(root1,text=a1).pack(fill='x')
                
                #gh=tk.Label(root1,text=d)
                #gh.pack(fill='x')
                #gh.place(x=0,y=60)
                
                #sb.config(command=lb.xview) 
                
        except:
            tkinter.messagebox.showerror(title = '出错了',message='网络错误或该功能正在维护')

def fanyi():
    s = simpledialog.askstring('翻译', '请输入您要翻译的文本：', initialvalue='')
    if s != '' and s != None:
        root1 = tk.Toplevel(root)
        root1.title('翻译-'+s)#标题
        #tk.messagebox.showinfo(title = '提示',message='请稍后...')
        def callback():
             print('')
        
        try:
            url = 'https://api.vvhan.com/api/fy?text='+s                          
            headers = {'Content-Type': 'application/json;charset=UTF-8',}
            r = requests.request("POST", url, headers=headers)
            a = r.json()
            print(a)
            b = a['data']
            c = b['fanyi']
            print(c)
            tk.Label(root1,text=c).pack(fill='x')
        except:
            tkinter.messagebox.showerror(title = '出错了',message='网络错误或该功能正在维护')

def lishi():
     if 1==1:
        root1 = tk.Toplevel(root)
        root1.title('历史上的今天')#标题
        #tk.messagebox.showinfo(title = '提示',message='请稍后...')
        def callback():
             print('')
        
        try:
            url = 'https://api.vvhan.com/api/hotlist?type=history'
            headers = {'Content-Type': 'application/json;charset=UTF-8'}
            r = requests.request("POST", url, headers=headers)
            a = r.json()
            if a['success'] == False:
                tk.Label(root1,text='网络错误').pack(fill='x')  
            else:
                b = a['title']+'\n'
                c = a['update_time']+'\n'
                d = a['data']
                d = d[0]
                e = d['title']+'\n'
                f = d['desc']+'\n'
                f_c = len(f)
                f_c1 = f_c//100+1
                d = []
                r = 0
                for i in range(f_c1):
                    d.append(f[r:r+100])
                    r+=100

                    #print(f[r:f_c])
                a1=b+c+e
                for i in d:
                    a1 += i+'\n'
                tk.Label(root1,text=a1).pack(fill='x')     
        except:
            tkinter.messagebox.showerror(title = '出错了',message='网络错误或该功能正在维护')

def guanji():
    root1 = tk.Toplevel(root)
    root1.title('系统计划')#标题
    root1.geometry('300x200')  
    root1.resizable(False, False)
    root1.config(background="#6fb799")
    def close():
        root2 = tk.Toplevel(root1)
        root2.geometry('300x150')  
        root2.resizable(False, False)
        root2.config(background="#6fb799")
        def minon():
              s = simpledialog.askstring('关机', '几分钟后关机(输入整数)', initialvalue='')
              try:
                  if s != None:
                        s=int(s)
                        g=1
              except:
                  tkinter.messagebox.showerror(title = '出错了',message='输入有误(输入范例:30)')
                  g = 2
              if g != 2:
                  s = s*60
                  os.system("shutdown -s -t  "+str(s))
                  tkinter.messagebox.showwarning(title = '关机',message='windows将在'+str(s//60)+'分钟后被关闭')
                  g=1
        def time2():
              s = simpledialog.askstring('关机', '请输入时间(例:19:20:00)', initialvalue='')
              try:
                   if s != None:
                         if '：' in s:
                             s = s.replace('：',':')
                         TIME=time.strftime("%H:%M:%S")
                         start_time = TIME
                         end_time = s
                         start_time1 = datetime.datetime.strptime(start_time , "%H:%M:%S")
                         end_time1 = datetime.datetime.strptime(end_time , "%H:%M:%S")
                         seconds = (end_time1 - start_time1).seconds
                         g=1
              except:
                    tkinter.messagebox.showerror(title = '出错了',message='输入有误(输入范例: 19:30:00)')
                    g = 2
              if g != 2:
                  os.system("shutdown -s -t  "+str(seconds))
                  tkinter.messagebox.showwarning(title = '关机',message='windows将在'+s+'被关闭')
                  g=1

        button_1 = tkinte.Button(root2, text='输入x分钟后',command=minon,width=10, height=1)
        button_1.pack()
        button_1.place(x=25, y=50)
        button_2 = tkinte.Button(root2, text='输入具体时间',command=time2,width=10, height=1)
        button_2.pack()
        button_2.place(x=175, y=50)
        
    
    def chexiao():
        os.system("shutdown -a")
        tkinter.messagebox.showwarning(title = '关机',message='计划的关机被取消')

    def close2():
        root2 = tk.Toplevel(root1)
        root2.geometry('300x150')  
        root2.resizable(False, False)
        root2.config(background="#6fb799")
        def minon():
              s = simpledialog.askstring('重启', '几分钟后重启(输入整数)', initialvalue='')
              try:
                  if s != None:
                        s=int(s)
                        g=1
              except:
                  tkinter.messagebox.showerror(title = '出错了',message='输入有误(输入范例:30)')
                  g = 2
              if g != 2:
                  s = s*60
                  os.system("shutdown -r -t  "+str(s))
                  tkinter.messagebox.showwarning(title = '重启',message='windows将在'+str(s//60)+'分钟后被重启')
                  g=1
        def time2():
              s = simpledialog.askstring('重启', '请输入时间(例:19:20:00)', initialvalue='')
              print(s)
              try:
                   if s != None:
                         if '：' in s:
                             s = s.replace('：',':')
                         TIME=time.strftime("%H:%M:%S")
                         start_time = TIME
                         end_time = s
                   
                         start_time1 = datetime.datetime.strptime(start_time , "%H:%M:%S")
                         end_time1 = datetime.datetime.strptime(end_time , "%H:%M:%S")
                   
                         seconds = (end_time1 - start_time1).seconds
                         g2=1
              except:
                    tkinter.messagebox.showerror(title = '出错了',message='输入有误(输入范例: 19:30:00)')
                    g2 = 2
              if g2 != 2:
                  os.system("shutdown -r -t  "+str(seconds))
                  tkinter.messagebox.showwarning(title = '重启',message='windows将在'+s+'被重启')
                  g2=1

        button_3 = tkinte.Button(root2, text='输入x分钟后',command=minon,width=10, height=1)
        button_3.pack()
        button_3.place(x=25, y=50)
        button_3 = tkinte.Button(root2, text='输入具体时间',command=time2,width=10, height=1)
        button_3.pack()
        button_3.place(x=175, y=50)
    def chexiao2():
        os.system("shutdown -a")
        tkinter.messagebox.showwarning(title = '重启',message='计划的重启被取消')  
    button_3 = tkinte.Button(root1, text='定时关机',command=close,width=10, height=1)
    button_3.pack()
    button_3.place(x=25, y=50)
    button_3 = tkinte.Button(root1, text='撤销关机指令',command=chexiao,width=10, height=1)
    button_3.pack()
    button_3.place(x=175, y=50)
    button_3 = tkinte.Button(root1, text='定时重启',command=close2,width=10, height=1)
    button_3.pack()
    button_3.place(x=25, y=130)
    button_3 = tkinte.Button(root1, text='撤销重启指令',command=chexiao2,width=10, height=1)
    button_3.pack()
    button_3.place(x=175, y=130)


def jishi():
    os.system("notepad")
    
def jisuan():
    os.system("calc")

def games():
      root1 = tk.Toplevel(root)
      root1.title('邢氏小工具-休闲小游戏')#标题
      root1.geometry('300x200')  
      root1.resizable(False, False)
      root1.config(background="#6fb799")
      def tanchishe():
            # 定义颜色变量
            ds=1
            redColour = pygame.Color(255,0,0)
            blackColour = pygame.Color(0,0,0)
            whiteColour = pygame.Color(255,255,255)
            greyColour = pygame.Color(150,150,150)

            # 定义gameOver函数
            def gameOver(playSurface):
                gameOverFont = pygame.font.Font('arial.ttf',72)
                gameOverSurf = gameOverFont.render('Game Over', True, greyColour)
                gameOverRect = gameOverSurf.get_rect()
                gameOverRect.midtop = (320, 10)
                playSurface.blit(gameOverSurf, gameOverRect)
                pygame.display.flip()
                time.sleep(5)
                pygame.quit()
                sys.exit()

            # 定义main函数
            def main():
                # 初始化pygame
                pygame.init()
                fpsClock = pygame.time.Clock()
                # 创建pygame显示层
                playSurface = pygame.display.set_mode((640,480))
                pygame.display.set_caption('贪吃蛇')

                # 初始化变量
                snakePosition = [100,100]
                snakeSegments = [[100,100],[80,100],[60,100]]
                raspberryPosition = [300,300]
                raspberrySpawned = 1
                direction = 'right'
                changeDirection = direction
                while True:
                    # 检测例如按键等pygame事件
                    for event in pygame.event.get():
                        if event.type == QUIT:
                            pygame.quit()
                        elif event.type == KEYDOWN:
                            # 判断键盘事件
                            if event.key == K_RIGHT or event.key == ord('d'):
                                changeDirection = 'right'
                            if event.key == K_LEFT or event.key == ord('a'):
                                changeDirection = 'left'
                            if event.key == K_UP or event.key == ord('w'):
                                changeDirection = 'up'
                            if event.key == K_DOWN or event.key == ord('s'):
                                changeDirection = 'down'
                            if event.key == K_ESCAPE:
                                pygame.event.post(pygame.event.Event(QUIT))
                    # 判断是否输入了反方向
                    if changeDirection == 'right' and not direction == 'left':
                        direction = changeDirection
                    if changeDirection == 'left' and not direction == 'right':
                        direction = changeDirection
                    if changeDirection == 'up' and not direction == 'down':
                        direction = changeDirection
                    if changeDirection == 'down' and not direction == 'up':
                        direction = changeDirection
                    # 根据方向移动蛇头的坐标
                    if direction == 'right':
                        snakePosition[0] += 20
                    if direction == 'left':
                        snakePosition[0] -= 20
                    if direction == 'up':
                        snakePosition[1] -= 20
                    if direction == 'down':
                        snakePosition[1] += 20
                    # 增加蛇的长度
                    snakeSegments.insert(0,list(snakePosition))
                    # 判断是否吃掉了树莓
                    if snakePosition[0] == raspberryPosition[0] and snakePosition[1] == raspberryPosition[1]:
                        raspberrySpawned = 0
                    else:
                        snakeSegments.pop()
                    # 如果吃掉树莓，则重新生成树莓
                    if raspberrySpawned == 0:
                        x = random.randrange(1,32)
                        y = random.randrange(1,24)
                        raspberryPosition = [int(x*20),int(y*20)]
                        raspberrySpawned = 1
                    # 绘制pygame显示层
                    playSurface.fill(blackColour)
                    for position in snakeSegments:
                        pygame.draw.rect(playSurface,whiteColour,Rect(position[0],position[1],20,20))
                        pygame.draw.rect(playSurface,redColour,Rect(raspberryPosition[0], raspberryPosition[1],20,20))

                    # 刷新pygame显示层
                    pygame.display.flip()
                    # 判断是否死亡
                    if snakePosition[0] > 620 or snakePosition[0] < 0:
                        global ds
                        if ds==1:
                              tk.messagebox.showinfo(title = '提示',message='你输了！')
                              ds=0
                    if snakePosition[1] > 460 or snakePosition[1] < 0:
                        for snakeBody in snakeSegments[1:]:
                            if snakePosition[0] == snakeBody[0] and snakePosition[1] == snakeBody[1]:
                                 if ds==1:
                                       tk.messagebox.showinfo(title = '提示',message='你输了！')
                                       ds=0
                    # 控制游戏速度
                    fpsClock.tick(4.5)

            if __name__ == "__main__":
                main()

 

      def eluosi():
            class Block:
                blk_color = [(255, 255, 255),(255, 255, 0),(255, 0, 255),(0, 255, 255),(255, 0, 0),(0, 255, 0),(0, 0, 255),(32,32,32)]
                BLANK = 7
                type_coord=[[[-1,0],[0,0],[1,0],[2,0]]\
                    ,[[-1,0],[0,0],[1,0],[0,1]]\
                    ,[[-1,0],[0,0],[-1,1],[0,1]]\
                    ,[[-1,0],[0,0],[0,1],[1,1]]\
                    ,[[0,0],[1,0],[-1,1],[0,1]]\
                    ,[[-1,0],[0,0],[1,0],[1,1]]\
                    ,[[-1,0],[0,0],[1,0],[-1,1]]]
                type_rotate = []
                
                def __init__(self,x,y,blk,angle):
                    self.x = x
                    self.y = y
                    self.blk = blk
                    self.angle = angle
                    
                @staticmethod
                def rotate(no):
                    rt_all = []
                    rt = Block.type_coord[no][:]
                    cx,cy=0,0
                    for b in range(4):
                        rt[b][0],rt[b][1] = rt[b][0]*4,rt[b][1]*4
                        cx += rt[b][0]
                        cy += rt[b][1]
                    cx = (cx)//8*2 if no !=6 else (cx+4)//8*2
                    cy = (cy)//8*2 if no !=6 else (cy-4)//8*2
                    rt_all.append(rt)
                    for r in range(3):
                        rt_new = []
                        for b in range(4):
                            rt_new.append([cx + (cy-rt[b][1]),cy-(cx-rt[b][0])])
                        rt_all.append(rt_new)
                        rt = rt_new
                    for r in range(4):
                        for b in range(4):
                            rt_all[r][b][0] //= 4
                            rt_all[r][b][1] //= 4
                    return rt_all
                @staticmethod
                def init_rotate():
                    for r in range(7):
                        Block.type_rotate.append(Block.rotate(r))

            class TRS:
                screen = None
                map = [[Block.BLANK]*10 for i in range(20)]
                STATUS = 0
                cbk = None

                def __init__(self,screen):
                    TRS.screen = screen

                @staticmethod
                def action(key_pressed):
                    if(key_pressed[K_LEFT] and TRS.check_action(TRS.cbk.x-1,TRS.cbk.y,TRS.cbk.blk,TRS.cbk.angle)):
                        TRS.cbk.x -= 1
                    elif (key_pressed[K_RIGHT] and TRS.check_action(TRS.cbk.x+1,TRS.cbk.y,TRS.cbk.blk,TRS.cbk.angle)):
                        TRS.cbk.x += 1
                    elif (key_pressed[K_UP] and TRS.check_action(TRS.cbk.x,TRS.cbk.y,TRS.cbk.blk,TRS.cbk.angle+1)):
                        TRS.cbk.angle += 1
                    elif (key_pressed[K_DOWN] and TRS.check_action(TRS.cbk.x,TRS.cbk.y+1,TRS.cbk.blk,TRS.cbk.angle)):
                        TRS.cbk.y += 1
                        
                @staticmethod
                def new_blk():
                    TRS.cbk = Block(5,0,random.randint(0,6),0)
                @staticmethod
                def check_action(x,y,blk,angle):
                    tr = Block.type_rotate[blk][angle%4]
                    for b in range(4):
                        bx,by = x + tr[b][0],y + tr[b][1]
                        if(bx<0 or bx>9 or by <0 or by>19 or TRS.map[by][bx]!=Block.BLANK):
                            return False
                    return True
                @staticmethod
                def check_drop():
                    if TRS.check_action(TRS.cbk.x,TRS.cbk.y+1,TRS.cbk.blk,TRS.cbk.angle):
                        TRS.cbk.y += 1
                    else:
                        TRS.STATUS = 2
                        
                @staticmethod
                def check_clear():
                    blk = Block.type_rotate[TRS.cbk.blk][TRS.cbk.angle%4]
                    row = list({TRS.cbk.y + blk[i][1] for i in range(4)})
                    row.sort()
                    row.reverse()
                    for b in range(4):
                        TRS.map[TRS.cbk.y + blk[b][1]][TRS.cbk.x + blk[b][0]] = TRS.cbk.blk
                    del_rows = 0
                    for r in row:
                        if not (Block.BLANK in TRS.map[r]):
                            TRS.map.pop(r)
                            del_rows += 1
                    for d in range(del_rows):
                        TRS.map.insert(0,[Block.BLANK for i in range(10)])
                        
                @staticmethod
                def print_game():
                    TRS.screen.fill((0, 0, 0))
                    for row in range(20):
                        for col in range(10):
                            pygame.draw.rect(TRS.screen, Block.blk_color[TRS.map[row][col]], ((col*21,row*21), (20, 20)), 0)
                    blk = Block.type_rotate[TRS.cbk.blk][TRS.cbk.angle%4]
                    for b in range(4):
                        pygame.draw.rect(TRS.screen, Block.blk_color[TRS.cbk.blk], (((TRS.cbk.x+blk[b][0])*21,(TRS.cbk.y+blk[b][1])*21), (20, 20)), 0)
            class App:
                def __init__(self):
                    pygame.init()
                    screen = pygame.display.set_mode((300,430))
                    Block.init_rotate()
                    TRS(screen)
                    
                def main(self):
                    clock = pygame.time.Clock()   # 创建游戏时钟
                    count = 1
                    # 进入游戏循环
                    while True:
                        # 设置刷新帧率
                        clock.tick(15)
                     
                        # 事件检测
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:   # 退出事件
                                  pygame.display.flip()
                                  pygame.quit()
                                
                        if TRS.STATUS == 0:
                            TRS.new_blk()
                            if TRS.check_action(TRS.cbk.x,TRS.cbk.y,TRS.cbk.blk,TRS.cbk.angle):
                                TRS.STATUS = 1
                            else:
                                TRS.STATUS = 3
                                tk.messagebox.showinfo(title = '提示',message='你输了！')
                        elif TRS.STATUS == 1:
                            TRS.action(pygame.key.get_pressed())
                            if count % 10 == 0:
                                TRS.check_drop()
                        elif TRS.STATUS == 2:
                            TRS.check_clear()
                            TRS.STATUS = 0

                        TRS.print_game()
                        pygame.display.update()   #刷新屏幕
                        count += 1
             
            App().main()
      def wuziqi():
             
            Chessman = namedtuple('Chessman', 'Name Value Color')
            Point = namedtuple('Point', 'X Y')
             
            BLACK_CHESSMAN = Chessman('黑子', 1, (45, 45, 45))
            WHITE_CHESSMAN = Chessman('白子', 2, (219, 219, 219))
             
            offset = [(1, 0), (0, 1), (1, 1), (1, -1)]
             
             
            class Checkerboard:
                def __init__(self, line_points):
                    self._line_points = line_points
                    self._checkerboard = [[0] * line_points for _ in range(line_points)]
             
                def _get_checkerboard(self):
                    return self._checkerboard
             
                checkerboard = property(_get_checkerboard)
             
                # 判断是否可落子
                def can_drop(self, point):
                    return self._checkerboard[point.Y][point.X] == 0
             
                def drop(self, chessman, point):
                    """
                    落子
                    :param chessman:
                    :param point:落子位置
                    :return:若该子落下之后即可获胜，则返回获胜方，否则返回 None
                    """
                    # 把黑棋/白棋落子的坐标打印出来
                    print(f'{chessman.Name} ({point.X}, {point.Y})')
                    self._checkerboard[point.Y][point.X] = chessman.Value
             
                    # 打印获胜方出来
                    if self._win(point):
                        print(f'{chessman.Name}获胜')
                        return chessman
             
                # 判断是否赢了
                def _win(self, point):
                    cur_value = self._checkerboard[point.Y][point.X]
                    for os in offset:
                        if self._get_count_on_direction(point, cur_value, os[0], os[1]):
                            return True
             
                # 判断是否赢了的代码，从这里往上看，代码都是正着写，反着看，写代码思路缺什么补什么，所以从这里开始看
                # 声明一个函数，按方向数数，数满5个就获胜。
                # 一个二维坐标上，判断上下、左右、两个45度直线，是否有五个相同的直连棋子，只要满足五颗子，则游戏结束:
                def _get_count_on_direction(self, point, value, x_offset, y_offset):
                    count = 1
                    for step in range(1, 5):
                        x = point.X + step * x_offset
                        y = point.Y + step * y_offset
                        if 0 <= x < self._line_points and 0 <= y < self._line_points and self._checkerboard[y][x] == value:
                            count += 1
                        else:
                            break
                    for step in range(1, 5):
                        x = point.X - step * x_offset
                        y = point.Y - step * y_offset
                        if 0 <= x < self._line_points and 0 <= y < self._line_points and self._checkerboard[y][x] == value:
                            count += 1
                        else:
                            break
             
                    return count >= 5
             
             
            SIZE = 30  # 棋盘每个点时间的间隔
            Line_Points = 19  # 棋盘每行/每列点数
            Outer_Width = 20  # 棋盘外宽度
            Border_Width = 4  # 边框宽度
            Inside_Width = 4  # 边框跟实际的棋盘之间的间隔
            Border_Length = SIZE * (Line_Points - 1) + Inside_Width * 2 + Border_Width  # 边框线的长度
            Start_X = Start_Y = Outer_Width + int(Border_Width / 2) + Inside_Width  # 网格线起点（左上角）坐标
            SCREEN_HEIGHT = SIZE * (Line_Points - 1) + Outer_Width * 2 + Border_Width + Inside_Width * 2  # 游戏屏幕的高
            SCREEN_WIDTH = SCREEN_HEIGHT + 200  # 游戏屏幕的宽
             
            Stone_Radius = SIZE // 2 - 3  # 棋子半径
            Stone_Radius2 = SIZE // 2 + 3
            Checkerboard_Color = (0xE3, 0x92, 0x65)  # 棋盘颜色，0x是16进制表示哦
            BLACK_COLOR = (0, 0, 0)
            WHITE_COLOR = (255, 255, 255)
            RED_COLOR = (200, 30, 30)
            BLUE_COLOR = (30, 30, 200)
             
            RIGHT_INFO_POS_X = SCREEN_HEIGHT + Stone_Radius2 * 2 + 10
             
             
            def print_text(screen, font, x, y, text, fcolor=(255, 255, 255)):
                imgText = font.render(text, True, fcolor)
                screen.blit(imgText, (x, y))
             
             
            def main():
                pygame.init()
                screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
                pygame.display.set_caption('五子棋')
             
                font1 = pygame.font.SysFont('SimHei', 32)  # 字体：黑体，32号
                font2 = pygame.font.SysFont('SimHei', 72)  # 字体：黑体，72号
                fwidth, fheight = font2.size('黑方获胜')
             
                checkerboard = Checkerboard(Line_Points)
                cur_runner = BLACK_CHESSMAN
                winner = None
                computer = AI(Line_Points, WHITE_CHESSMAN)
             
                # 设置黑白双方初始连子为0
                black_win_count = 0
                white_win_count = 0
             
                while True:
                    for event in pygame.event.get():
                        if event.type == QUIT:
                            pygame.display.flip()
                            pygame.quit()
                        elif event.type == KEYDOWN:
                            if event.key == K_RETURN:
                                if winner is not None:
                                    winner = None
                                    cur_runner = BLACK_CHESSMAN
                                    checkerboard = Checkerboard(Line_Points)
                                    computer = AI(Line_Points, WHITE_CHESSMAN)
                        elif event.type == MOUSEBUTTONDOWN:  # 检测鼠标落下
                            if winner is None:  # 检测是否有一方胜出
                                pressed_array = pygame.mouse.get_pressed()
                                if pressed_array[0]:
                                    mouse_pos = pygame.mouse.get_pos()
                                    click_point = _get_clickpoint(mouse_pos)
                                    if click_point is not None:  # 检测鼠标是否在棋盘内点击
                                        if checkerboard.can_drop(click_point):
                                            winner = checkerboard.drop(cur_runner, click_point)
                                            if winner is None:  # 再次判断是否有胜出
                                                # 一个循环内检测两次，意思就是人出一次检测一下，电脑出一次检测一下。
                                                cur_runner = _get_next(cur_runner)
                                                computer.get_opponent_drop(click_point)
                                                AI_point = computer.AI_drop()
                                                winner = checkerboard.drop(cur_runner, AI_point)
                                                if winner is not None:
                                                    white_win_count += 1
                                                cur_runner = _get_next(cur_runner)
                                            else:
                                                black_win_count += 1
                                    else:
                                        print('超出棋盘区域')
             
                    # 画棋盘
                    _draw_checkerboard(screen)
             
                    # 画棋盘上已有的棋子
                    for i, row in enumerate(checkerboard.checkerboard):
                        for j, cell in enumerate(row):
                            if cell == BLACK_CHESSMAN.Value:
                                _draw_chessman(screen, Point(j, i), BLACK_CHESSMAN.Color)
                            elif cell == WHITE_CHESSMAN.Value:
                                _draw_chessman(screen, Point(j, i), WHITE_CHESSMAN.Color)
             
                    _draw_left_info(screen, font1, cur_runner, black_win_count, white_win_count)
             
                    if winner:
                        print_text(screen, font2, (SCREEN_WIDTH - fwidth) // 2, (SCREEN_HEIGHT - fheight) // 2, winner.Name + '获胜',
                                   RED_COLOR)
             
                    pygame.display.flip()
             
             
            def _get_next(cur_runner):
                if cur_runner == BLACK_CHESSMAN:
                    return WHITE_CHESSMAN
                else:
                    return BLACK_CHESSMAN
             
             
            # 画棋盘
            def _draw_checkerboard(screen):
                # 填充棋盘背景色
                screen.fill(Checkerboard_Color)
                # 画棋盘网格线外的边框
                pygame.draw.rect(screen, BLACK_COLOR, (Outer_Width, Outer_Width, Border_Length, Border_Length), Border_Width)
                # 画网格线
                for i in range(Line_Points):
                    pygame.draw.line(screen, BLACK_COLOR,
                                     (Start_Y, Start_Y + SIZE * i),
                                     (Start_Y + SIZE * (Line_Points - 1), Start_Y + SIZE * i),
                                     1)
                for j in range(Line_Points):
                    pygame.draw.line(screen, BLACK_COLOR,
                                     (Start_X + SIZE * j, Start_X),
                                     (Start_X + SIZE * j, Start_X + SIZE * (Line_Points - 1)),
                                     1)
                # 画星位和天元
                for i in (3, 9, 15):
                    for j in (3, 9, 15):
                        if i == j == 9:
                            radius = 5
                        else:
                            radius = 3
                        # pygame.draw.circle(screen, BLACK, (Start_X + SIZE * i, Start_Y + SIZE * j), radius)
                        pygame.gfxdraw.aacircle(screen, Start_X + SIZE * i, Start_Y + SIZE * j, radius, BLACK_COLOR)
                        pygame.gfxdraw.filled_circle(screen, Start_X + SIZE * i, Start_Y + SIZE * j, radius, BLACK_COLOR)
             
             
            # 画棋子
            def _draw_chessman(screen, point, stone_color):
                # pygame.draw.circle(screen, stone_color, (Start_X + SIZE * point.X, Start_Y + SIZE * point.Y), Stone_Radius)
                pygame.gfxdraw.aacircle(screen, Start_X + SIZE * point.X, Start_Y + SIZE * point.Y, Stone_Radius, stone_color)
                pygame.gfxdraw.filled_circle(screen, Start_X + SIZE * point.X, Start_Y + SIZE * point.Y, Stone_Radius, stone_color)
             
             
            # 画右侧信息显示
            def _draw_left_info(screen, font, cur_runner, black_win_count, white_win_count):
                _draw_chessman_pos(screen, (SCREEN_HEIGHT + Stone_Radius2, Start_X + Stone_Radius2), BLACK_CHESSMAN.Color)
                _draw_chessman_pos(screen, (SCREEN_HEIGHT + Stone_Radius2, Start_X + Stone_Radius2 * 4), WHITE_CHESSMAN.Color)
             
                print_text(screen, font, RIGHT_INFO_POS_X, Start_X + 3, '玩家', BLUE_COLOR)
                print_text(screen, font, RIGHT_INFO_POS_X, Start_X + Stone_Radius2 * 3 + 3, '电脑', BLUE_COLOR)
             
                print_text(screen, font, SCREEN_HEIGHT, SCREEN_HEIGHT - Stone_Radius2 * 8, '战况：', BLUE_COLOR)
                _draw_chessman_pos(screen, (SCREEN_HEIGHT + Stone_Radius2, SCREEN_HEIGHT - int(Stone_Radius2 * 4.5)),
                                   BLACK_CHESSMAN.Color)
                _draw_chessman_pos(screen, (SCREEN_HEIGHT + Stone_Radius2, SCREEN_HEIGHT - Stone_Radius2 * 2), WHITE_CHESSMAN.Color)
                print_text(screen, font, RIGHT_INFO_POS_X, SCREEN_HEIGHT - int(Stone_Radius2 * 5.5) + 3, f'{black_win_count} 胜',
                           BLUE_COLOR)
                print_text(screen, font, RIGHT_INFO_POS_X, SCREEN_HEIGHT - Stone_Radius2 * 3 + 3, f'{white_win_count} 胜',
                           BLUE_COLOR)
             
             
            def _draw_chessman_pos(screen, pos, stone_color):
                pygame.gfxdraw.aacircle(screen, pos[0], pos[1], Stone_Radius2, stone_color)
                pygame.gfxdraw.filled_circle(screen, pos[0], pos[1], Stone_Radius2, stone_color)
             
             
            # 根据鼠标点击位置，返回游戏区坐标
            def _get_clickpoint(click_pos):
                pos_x = click_pos[0] - Start_X
                pos_y = click_pos[1] - Start_Y
                if pos_x < -Inside_Width or pos_y < -Inside_Width:
                    return None
                x = pos_x // SIZE
                y = pos_y // SIZE
                if pos_x % SIZE > Stone_Radius:
                    x += 1
                if pos_y % SIZE > Stone_Radius:
                    y += 1
                if x >= Line_Points or y >= Line_Points:
                    return None
             
                return Point(x, y)
             
             
            class AI:
                def __init__(self, line_points, chessman):
                    self._line_points = line_points
                    self._my = chessman
                    self._opponent = BLACK_CHESSMAN if chessman == WHITE_CHESSMAN else WHITE_CHESSMAN
                    self._checkerboard = [[0] * line_points for _ in range(line_points)]
             
                def get_opponent_drop(self, point):
                    self._checkerboard[point.Y][point.X] = self._opponent.Value
             
                def AI_drop(self):
                    point = None
                    score = 0
                    for i in range(self._line_points):
                        for j in range(self._line_points):
                            if self._checkerboard[j][i] == 0:
                                _score = self._get_point_score(Point(i, j))
                                if _score > score:
                                    score = _score
                                    point = Point(i, j)
                                elif _score == score and _score > 0:
                                    r = random.randint(0, 100)
                                    if r % 2 == 0:
                                        point = Point(i, j)
                    self._checkerboard[point.Y][point.X] = self._my.Value
                    return point
             
                def _get_point_score(self, point):
                    score = 0
                    for os in offset:
                        score += self._get_direction_score(point, os[0], os[1])
                    return score
             
                def _get_direction_score(self, point, x_offset, y_offset):
                    count = 0  # 落子处我方连续子数
                    _count = 0  # 落子处对方连续子数
                    space = None  # 我方连续子中有无空格
                    _space = None  # 对方连续子中有无空格
                    both = 0  # 我方连续子两端有无阻挡
                    _both = 0  # 对方连续子两端有无阻挡
             
                    # 如果是 1 表示是边上是我方子，2 表示敌方子
                    flag = self._get_stone_color(point, x_offset, y_offset, True)
                    if flag != 0:
                        for step in range(1, 6):
                            x = point.X + step * x_offset
                            y = point.Y + step * y_offset
                            if 0 <= x < self._line_points and 0 <= y < self._line_points:
                                if flag == 1:
                                    if self._checkerboard[y][x] == self._my.Value:
                                        count += 1
                                        if space is False:
                                            space = True
                                    elif self._checkerboard[y][x] == self._opponent.Value:
                                        _both += 1
                                        break
                                    else:
                                        if space is None:
                                            space = False
                                        else:
                                            break  # 遇到第二个空格退出
                                elif flag == 2:
                                    if self._checkerboard[y][x] == self._my.Value:
                                        _both += 1
                                        break
                                    elif self._checkerboard[y][x] == self._opponent.Value:
                                        _count += 1
                                        if _space is False:
                                            _space = True
                                    else:
                                        if _space is None:
                                            _space = False
                                        else:
                                            break
                            else:
                                # 遇到边也就是阻挡
                                if flag == 1:
                                    both += 1
                                elif flag == 2:
                                    _both += 1
             
                    if space is False:
                        space = None
                    if _space is False:
                        _space = None
             
                    _flag = self._get_stone_color(point, -x_offset, -y_offset, True)
                    if _flag != 0:
                        for step in range(1, 6):
                            x = point.X - step * x_offset
                            y = point.Y - step * y_offset
                            if 0 <= x < self._line_points and 0 <= y < self._line_points:
                                if _flag == 1:
                                    if self._checkerboard[y][x] == self._my.Value:
                                        count += 1
                                        if space is False:
                                            space = True
                                    elif self._checkerboard[y][x] == self._opponent.Value:
                                        _both += 1
                                        break
                                    else:
                                        if space is None:
                                            space = False
                                        else:
                                            break  # 遇到第二个空格退出
                                elif _flag == 2:
                                    if self._checkerboard[y][x] == self._my.Value:
                                        _both += 1
                                        break
                                    elif self._checkerboard[y][x] == self._opponent.Value:
                                        _count += 1
                                        if _space is False:
                                            _space = True
                                    else:
                                        if _space is None:
                                            _space = False
                                        else:
                                            break
                            else:
                                # 遇到边也就是阻挡
                                if _flag == 1:
                                    both += 1
                                elif _flag == 2:
                                    _both += 1
             
                    # 下面这一串score（分数）的含义：评估棋格获胜分数。
                    # 使计算机计算获胜分值越高的棋格，就能确定能让自己的棋子最有可能达成联机的位置，也就是最佳进攻位置，
                    # 而一旦计算机能确定自己的最高分值的位置，计算机就具备了进攻能力。
                    # 同理，计算机能计算出玩家的最大分值位置，并抢先玩家获得该位置，这样计算机就具有了防御的能力。
             
                    # 在计算机下棋之前，会计算空白棋格上的获胜分数，根据分数高低获取最佳位置。
                    # 计算机会将棋子下在获胜分数最高的地方。
                    # 当已放置4颗棋子时，必须在第五个空棋格上设置绝对高的分值。也就是10000
                    # 当获胜组合上有部分位置已被对手的棋格占据而无法连成五子时，获胜组合上空棋格的获胜分数会直接设置为0。（四颗棋子，你把中间断了）
                    # 当有两组及其以上的获胜组合位置交叉时，对该位置的分数进行叠加，形成分数比周围位置明显高。（五子棋中三三相连）
             
                    score = 0
                    if count == 4:
                        score = 10000
                    elif _count == 4:
                        score = 9000
                    elif count == 3:
                        if both == 0:
                            score = 1000
                        elif both == 1:
                            score = 100
                        else:
                            score = 0
                    elif _count == 3:
                        if _both == 0:
                            score = 900
                        elif _both == 1:
                            score = 90
                        else:
                            score = 0
                    elif count == 2:
                        if both == 0:
                            score = 100
                        elif both == 1:
                            score = 10
                        else:
                            score = 0
                    elif _count == 2:
                        if _both == 0:
                            score = 90
                        elif _both == 1:
                            score = 9
                        else:
                            score = 0
                    elif count == 1:
                        score = 10
                    elif _count == 1:
                        score = 9
                    else:
                        score = 0
             
                    if space or _space:
                        score /= 2
             
                    return score
             
                # 判断指定位置处在指定方向上是我方子、对方子、空
                def _get_stone_color(self, point, x_offset, y_offset, next):
                    x = point.X + x_offset
                    y = point.Y + y_offset
                    if 0 <= x < self._line_points and 0 <= y < self._line_points:
                        if self._checkerboard[y][x] == self._my.Value:
                            return 1
                        elif self._checkerboard[y][x] == self._opponent.Value:
                            return 2
                        else:
                            if next:
                                return self._get_stone_color(Point(x, y), x_offset, y_offset, False)
                            else:
                                return 0
                    else:
                        return 0
             
             
            if __name__ == '__main__':
                main()
                
      def bird():
        subprocess.Popen("flybird//bird.exe")

      button_1 = tkinte.Button(root1, text='贪吃蛇',command=tanchishe,width=10, height=1)
      button_1.pack()
      button_1.place(x=25, y=50)
      button_2 = tkinte.Button(root1, text='俄罗斯方块',command=eluosi,width=10, height=1)
      button_2.pack()
      button_2.place(x=175, y=50)
      button_3 = tkinte.Button(root1, text='五子棋',command=wuziqi,width=10, height=1)
      button_3.pack()
      button_3.place(x=25, y=120)
      button_3 = tkinte.Button(root1, text='飞翔小鸟',command=bird,width=10, height=1)
      button_3.pack()
      button_3.place(x=175, y=120)

def caozuo():
      root1 = tk.Toplevel(root)
      root1.title('系统操作')#标题
      root1.geometry('400x300')  
      root1.resizable(False, False)
      root1.config(background="#6fb799")
      def cmd():
            os.system('cmd')
      def mspaint():
            os.system('mspaint')
      def explorer():
            os.system('explorer')
      def diskmgmt_msc():
            os.system('diskmgmt.msc')
      def control():
            os.system('control')
      def bizhi():
            try:
                  #tk.messagebox.showinfo(title = '提示',message='请等待几秒')
                  '''
                  url = 'https://tuapi.eees.cc/api.php?category=fengjing&type=json'
                  headers = {'Content-Type': 'application/json;charset=UTF-8'}
                  r = requests.request("GET", url, headers=headers)
                  a = r.json()
                  url = a['img']'''
                  url='https://tu.ltyuanfang.cn/api/fengjing.php'
                  rsp=urllib.request.urlopen(url)
                  img=rsp.read()
                  sd='C://1.jpg'
                  with open(sd,'wb') as f:
                      f.write(img)
                  ctypes.windll.user32.SystemParametersInfoW(20, 0, sd, 0)
                  tk.messagebox.showinfo(title = '更新提示',message='已完成')
            except:
                  tkinter.messagebox.showerror(title = '出错了',message='请检查网络后重试')
      button_1 = tkinte.Button(root1, text='打开cmd',command=cmd,width=10, height=1)
      button_1.pack()
      button_1.place(x=25, y=70)
      
      button_2 = tkinte.Button(root1, text='画画',command=mspaint,width=10, height=1)
      button_2.pack()
      button_2.place(x=155, y=70)

      button_3 = tkinte.Button(root1, text='打开\'此电脑\'',command=explorer,width=10, height=1)
      button_3.pack()
      button_3.place(x=285, y=70)

      button_4 = tkinte.Button(root1, text='磁盘管理',command=diskmgmt_msc,width=10, height=1)
      button_4.pack()
      button_4.place(x=25, y=180)

      button_5 = tkinte.Button(root1, text='控制面板',command=control,width=10, height=1)
      button_5.pack()
      button_5.place(x=155, y=180)

      button_6 = tkinte.Button(root1, text='一键换壁纸',command=bizhi,width=10, height=1)
      button_6.pack()
      button_6.place(x=285, y=180)
      
def zhuanhuan():
      webbrowser.open('https://onlineconvertfree.com/zh/', new=0, autoraise=True)
      tk.messagebox.showinfo(title = '提示',message='请查看您的电脑默认浏览器')

def xiangji():
      subprocess.Popen("camera//amcap.exe")

def laji():
      def laji1():
            tkinter.messagebox.showwarning(title = '警告',message='强力清理通常会误删非垃圾文件，请谨慎使用\n（作者的忠告：用安全清理吧，强理清理技术不成熟）')
            # Temp-临时文件
            path_data1 = "C:\\Windows\\Temp"
            # Prefetch-访问记录
            path_data2 = "C:\\Windows\\Prefetch"
            # Download-系统更新时下载的补丁和一些安装包等
            path_data3 = "C:\\Windows\\SoftwareDistribution\\Download"
            # LogFiles-系统日志及操作记录
            path_data4 = "C:\\Windows\\System32\\LogFiles"
            path_data_diy = ""


            # python删除文件的方法 os.remove(path)path指的是文件的绝对路径,如：
            # os.remove(r"E:\code\practice\data\1.py")#删除文件
            # os.rmdir(r"E:\code\practice\data\2")#删除文件夹（只能删除空文件夹）
            # shutil.rmtree(r"E:\code\practice\data\2")#删除文件夹
            # path_data = "E:\code\practice\data"#


            def thread_it(func, *args):
                """将函数打包进线程"""
                # 创建
                t = threading.Thread(target=func, args=args)
                # 守护 !!!
                t.setDaemon(True)
                # 启动
                t.start()
                # 阻塞--卡死界面！
                # t.join()


            class GUI:

                def __init__(self):
                    self.root1 = tk.Tk()
                    self.root1.title("邢氏小工具-垃圾清理")
                    self.root1.configure(bg='#2c3038')
                    self.root1.option_add('*Font', '楷体')
                    # self.root.geometry("500x200+1100+150")
                    # 程序运行时在屏幕中间打开
                    sw = self.root1.winfo_screenwidth()
                    sh = self.root1.winfo_screenheight()
                    ww = 1055
                    wh = 550
                    x = (sw - ww) / 2
                    y = (sh - wh) / 2
                    self.root1.geometry("%dx%d+%d+%d" % (ww, wh, x, y))
                    self.root1.resizable(False, False)
                    self.root1.update()
                    self.root1.wm_attributes('-topmost', 1)
                    self.interface()

                def interface(self):
                    self.CheckVar1 = tk.IntVar()
                    self.CheckVar2 = tk.IntVar()
                    self.CheckVar3 = tk.IntVar()
                    self.CheckVar4 = tk.IntVar()
                    self.C1 = tk.Checkbutton(self.root1, text="Temp-临时文件", variable=self.CheckVar1, onvalue=1, offvalue=0,
                                             fg='#d9f5ff', bg='#2c3038', selectcolor='#2c3344', activebackground='#2c3038',
                                             activeforeground='#60b6fc')
                    self.C2 = tk.Checkbutton(self.root1, text="Prefetch-访问记录", variable=self.CheckVar2, onvalue=1, offvalue=0,
                                             fg='#d9f5ff', bg='#2c3038', selectcolor='#2c3344', activebackground='#2c3038',
                                             activeforeground='#60b6fc')
                    self.C3 = tk.Checkbutton(self.root1, text="Download-系统更新补丁", variable=self.CheckVar3, onvalue=1, offvalue=0,
                                             fg='#d9f5ff', bg='#2c3038', selectcolor='#2c3344', activebackground='#2c3038',
                                             activeforeground='#60b6fc')
                    self.C4 = tk.Checkbutton(self.root1, text="LogFiles-系统日志", variable=self.CheckVar4, onvalue=1, offvalue=0,
                                             fg='#d9f5ff', bg='#2c3038', selectcolor='#2c3344', activebackground='#2c3038',
                                             activeforeground='#60b6fc')

                    self.C1.select()
                    self.C2.select()
                    self.C3.select()
                    self.C4.select()
                    self.C1.grid(row=0, column=0, ipadx=10, ipady=10, padx=3, pady=10)
                    self.C2.grid(row=0, column=1, ipadx=10, ipady=10, padx=3, pady=10)
                    self.C3.grid(row=0, column=2, ipadx=10, ipady=10, padx=3, pady=10)
                    self.C4.grid(row=0, column=3, ipadx=10, ipady=10, padx=3, pady=10)
                    self.Button0 = tk.Button(self.root1, text="清理基本C盘垃圾", command=lambda: thread_it(self.event_清理基本C盘垃圾), width=10,
                                             bg='#4a8e53', fg='#d9f5ff', activebackground='#4d535f', activeforeground='#fdfdfd')
                    self.Button0.grid(row=0, column=4, ipadx=20, ipady=10, padx=5, pady=10)
                    self.w1 = tk.Entry(self.root1, textvariable='请输入目标路径', bg='#25272c', fg='#b2b2b2')
                    self.w1.grid(row=1, column=0, columnspan=4, ipadx=290, ipady=8, padx=5, pady=10)
                    self.Button1 = tk.Button(self.root1, text="选择目标文件夹", command=lambda: thread_it(self.event_选择目标文件夹), width=10,
                                             bg='#4780ac', fg='#d9f5ff', activebackground='#4d535f', activeforeground='#fdfdfd')
                    self.Button1.grid(row=1, column=4, ipadx=20, ipady=10, padx=5, pady=10)
                    self.Button2 = tk.Button(self.root1, text="清理目标文件夹", command=lambda: thread_it(self.event_清理目标文件夹), width=10,
                                             bg='#4a8e53', fg='#d9f5ff', activebackground='#4d535f', activeforeground='#fdfdfd')
                    self.Button2.grid(row=1, column=5, ipadx=20, ipady=10, padx=5, pady=10)
                    self.Button3 = tk.Button(self.root1, text="清空输出信息", command=lambda: thread_it(self.event_清空输出信息), width=10,
                                             bg='#2c3038', fg='#d9f5ff', activebackground='#4d535f', activeforeground='#fdfdfd')
                    self.Button3.grid(row=0, column=5, ipadx=20, ipady=10, padx=5, pady=10)
                    self.text = tk.Text(self.root1, bg='#25272c', fg='#777c8a')
                    self.text.grid(row=2, column=0, columnspan=6, ipadx=195, padx=10, pady=10)
                    # 新建滚动条
                    self.scroll = tk.Scrollbar()
                    # 两个控件关联
                    self.scroll.config(command=self.text.yview)
                    self.text.config(yscrollcommand=self.scroll.set)

                def event_清理基本C盘垃圾(self):
                    try:
                        if self.CheckVar1.get() == 1:
                            self.routineCleanup1()
                        if self.CheckVar2.get() == 1:
                            self.routineCleanup2()
                        if self.CheckVar3.get() == 1:
                            self.routineCleanup3()
                        if self.CheckVar4.get() == 1:
                            self.routineCleanup4()
                    except Exception as e:
                        print(e)

                def event_选择目标文件夹(self):
                    path_ = askdirectory()  # 使用askdirectory()方法返回文件夹的路径
                    if path_ == "":
                        self.w1.get()  # 当打开文件路径选择框后点击"取消" 输入框会清空路径，所以使用get()方法再获取一次路径
                    else:
                        path_ = path_.replace("/", "\\")  # 实际在代码中执行的路径为“\“ 所以替换一下
                        print(path_)
                        self.w1.delete(0, END)
                        self.w1.insert(0, path_)

                def event_清理目标文件夹(self):
                    try:
                        data_path = self.w1.get()
                        if data_path is not None:
                            time1 = time.time()
                            current_time = time.strftime("%Y-%m-%d %H-%M-%S", time.localtime(time1))
                            self.text.insert(tk.INSERT, "正在清理目标文件" + data_path + current_time + '\n')
                            self.text.see(END)
                            self.del_file(data_path)
                            time2 = time.time()
                            self.text.insert(tk.INSERT, "清理用时" + str(round((time2 - time1), 2)) + 's' + '\n')
                            self.text.see(END)
                    except Exception as e:
                        self.text.insert(tk.INSERT, "   " + str(e) + '\n')
                        self.text.see(END)
                        print(e)

                def event_清空输出信息(self):
                    try:
                        self.text.delete('1.0', END)
                    except Exception as e:
                        print(e)
                        pass

                def del_file(self, path_data):
                    if len(os.listdir(path_data)) == 0:
                        self.text.insert(tk.INSERT, "  无垃圾可清理" + '\n')
                        self.text.see(END)
                        print("  无垃圾可清理")
                        return
                    n = 0
                    for i in os.listdir(path_data):  # os.listdir(path_data)#返回一个列表，里面是当前目录下面的所有东西的相对路径
                        # file_data = path_data + "\\" + i  # 当前文件夹的下面的所有东西的绝对路径
                        path = os.path.join(path_data, i)
                        if os.path.isdir(path):
                            try:
                                # 使用shutil模块
                                shutil.rmtree(path)
                            except Exception as error:
                                os.system('rd /s /q %s' % path)
                            self.text.insert(tk.INSERT, '  已清除文件夹 ' + path + '\n')
                            self.text.see(END)
                            print('  已清除文件夹 ' + path)
                        elif os.path.isfile(path):
                            try:
                                # 使用os模块删除
                                os.remove(path)
                            except Exception as error:
                                # 使用windows命令行强制删除
                                # os.system('del' + path + '/S')
                                os.system("del /f /q %s" % path)
                            self.text.insert(tk.INSERT, '  已清除文件 ' + path + '\n')
                            self.text.see(END)
                            print('  已清除文件 ' + path)
                        n += 1
                    if n > 0:
                        self.text.insert(tk.INSERT, '此路径共清除文件数： ' + str(n) + '\n')
                        self.text.see(END)

                def routineCleanup1(self):
                    try:
                        time1 = time.time()
                        current_time = time.strftime("%Y-%m-%d %H-%M-%S", time.localtime(time1))
                        self.text.insert(tk.INSERT, "正在清理Temp-临时文件的垃圾……" + current_time + '\n')
                        self.text.see(END)
                        print("正在清理Temp-临时文件的垃圾……" + current_time)
                        # 利用以下语言获得文件夹的写入权限
                        os.chmod(path_data1, stat.S_IRWXU)
                        self.del_file(path_data1)
                        time2 = time.time()
                        self.text.insert(tk.INSERT, "  清理用时" + str(round((time2 - time1), 2)) + 's' + '\n')
                        self.text.see(END)
                    except Exception as e:
                        self.text.insert(tk.INSERT, "   " + str(e) + '\n')
                        self.text.see(END)
                        print("   " + str(e))

                def routineCleanup2(self):
                    try:
                        time1 = time.time()
                        current_time = time.strftime("%Y-%m-%d %H-%M-%S", time.localtime(time1))
                        self.text.insert(tk.INSERT, "正在清理Prefetch-访问记录的垃圾……" + current_time + '\n')
                        self.text.see(END)
                        print("正在清理Prefetch-访问记录的垃圾……" + current_time)
                        os.chmod(path_data2, stat.S_IRWXU)
                        self.del_file(path_data2)
                        time2 = time.time()
                        self.text.insert(tk.INSERT, "  清理用时" + str(round((time2 - time1), 2)) + 's' + '\n')
                        self.text.see(END)
                    except Exception as e:
                        self.text.insert(tk.INSERT, "   " + str(e) + '\n')
                        self.text.see(END)
                        print("   " + str(e))

                def routineCleanup3(self):
                    try:
                        time1 = time.time()
                        current_time = time.strftime("%Y-%m-%d %H-%M-%S", time.localtime(time1))
                        self.text.insert(tk.INSERT, "正在清理Download-系统补丁的垃圾……" + current_time + '\n')
                        self.text.see(END)
                        print("正在清理Download-系统补丁的垃圾……" + current_time)
                        # 利用以下语言获得文件夹的写入权限
                        os.chmod(path_data3, stat.S_IRWXU)
                        self.del_file(path_data3)
                        time2 = time.time()
                        self.text.insert(tk.INSERT, "  清理用时" + str(round((time2 - time1), 2)) + 's' + '\n')
                        self.text.see(END)
                    except Exception as e:
                        self.text.insert(tk.INSERT, "   " + str(e) + '\n')
                        self.text.see(END)
                        print("   " + str(e))

                def routineCleanup4(self):
                    try:
                        time1 = time.time()
                        current_time = time.strftime("%Y-%m-%d %H-%M-%S", time.localtime(time1))
                        self.text.insert(tk.INSERT, "正在清理LogFiles-系统日志的垃圾……" + current_time + '\n')
                        self.text.see(END)
                        print("正在清理LogFiles-系统日志的垃圾……" + current_time)
                        # 利用以下语言获得文件夹的写入权限
                        os.chmod(path_data4, stat.S_IRWXU)
                        self.del_file(path_data4)
                        time2 = time.time()
                        self.text.insert(tk.INSERT, "  清理用时" + str(round((time2 - time1), 2)) + 's' + '\n')
                        self.text.see(END)
                    except Exception as e:
                        self.text.insert(tk.INSERT, "   " + str(e) + '\n')
                        self.text.see(END)
                        print("   " + str(e))


            if __name__ == "__main__":
                a = GUI()
                a.root1.mainloop()

      def laji2():
            subprocess.Popen("exe//clean.exe")

      root1 = tk.Toplevel(root)
      root1.title('垃圾清理')#标题
      root1.geometry('200x200')  
      root1.resizable(False, False)#固定窗体
      root1.config(background="#6fb705")
      yu=tkinte.Button(root1, text='安全清理',command=laji2,width=10, height=1)
      yu.pack()
      yu.place(x=50,y=30)
      yu2=tkinte.Button(root1, text='强力清理',command=laji1,width=10, height=1)
      yu2.pack()
      yu2.place(x=50,y=120)

def mu():
    root1 = tk.Toplevel(root)
    root1.title('邢氏音乐')#标题
    root1.geometry('400x400')  
    root1.resizable(False, False)#固定窗体
    root1.config(background="#6fb765")
    root1.iconbitmap('k.ico')#设置图片
    root1.config(background="#6fb705")
    pygame.init()
    def sousuo():
        s = simpledialog.askstring('邢氏音乐', '请输入歌名：', initialvalue='')
        def search(keyword: str) -> Tuple[int, str, str]:
            url = "https://music.163.com/api/cloudsearch/pc"
            params = {"s": keyword, "type": 1, "offset": 0, "limit": 1}
            global result1
            result1 = requests.post(url=url, params=params).json()
            result = requests.post(url=url, params=params).json()
            #print(result)
            if songs := result["result"]["songs"]:
                global imfortion
                global music_name
                music_name = songs[0]['name']
                music_id = songs[0]["id"]
                songer = songs[0]["ar"][0]['name']
                imfortion = '《'+music_name+'》—— '+songer
                
                return 1, f'https://music.163.com/song/media/outer/url?id={music_id}.mp3', music_name
            return 0, "网易云音乐中找不到相关的歌曲", ''

        def main():
            keyword = s
            result = search(keyword=keyword)
            if result[0]:
                headers = {
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                                'Chrome/101.0.4951.41 Safari/537.36 Edg/101.0.1210.32'}
                global file 
                file = requests.get(url=result[1], headers=headers).content
                if 'html' not in str(file):
                    if not os.path.exists('music'):
                        os.mkdir('music')
                    os.chdir('music')
                    with open(f'a.mp3', 'wb') as f:
                        f.write(file)
                        f.close()
                        print('下载完成！')
                        print(music_name)
                        pygame.mixer.music.load('a.mp3')
                        pygame.mixer.music.play()
                        url = result1['result']['songs'][0]['al']['picUrl']
                else:
                        tk.messagebox.showinfo(title = '提示',message='这首歌要付费呢')
            else:
                print(result[1])
        if __name__ == '__main__':
            main()

            t1 = tkinter.Label(root1, text=imfortion)
            t1.pack()
            t1.place(x=25, y=65)
            
    def zanting():
        pygame.mixer.music.pause()

    def bofang():
        pygame.mixer.music.unpause()

    def bofang2():
        pygame.mixer.music.rewind()

    def bofang3():
        pygame.mixer.music.stop()

    def dow():
        dr = os.path.join(os.path.expanduser('~'),"Desktop")+'\\'+music_name+'.mp3'
        with open(dr, 'wb') as f:
            f.write(file)
            f.close()
            print(music_name)
            tk.messagebox.showinfo(title = '提示',message='下载完成，已保存至桌面')

    b1 = tkinter.Button(root1, text='搜索音乐',command=sousuo,width=10, height=1)
    b1.pack()
    b1.place(x=145, y=25)

    b2 = tkinter.Button(root1, text='暂停',command=zanting,width=10, height=1)
    b2.pack()
    b2.place(x=20, y=300)

    b3 = tkinter.Button(root1, text='播放',command=bofang,width=10, height=1)
    b3.pack()
    b3.place(x=150, y=300)

    b4 = tkinter.Button(root1, text='重新播放',command=bofang2,width=10, height=1)
    b4.pack()
    b4.place(x=280, y=300)

    b5 = tkinter.Button(root1, text='停止播放',command=bofang3,width=10, height=1)
    b5.pack()
    b5.place(x=20, y=350)

    b5 = tkinter.Button(root1, text='下载歌曲',command=dow,width=10, height=1)
    b5.pack()
    b5.place(x=150, y=350)

def yanzhi():
      def getfile():
        file_path=filedialog.askopenfilename()
        fpath.set(file_path)

      def face_baidu():
          class BaiduPicIndentify:
              def __init__(self,img):
                  self.AK = "juqVLsljMBigcM4soXoVmMGr"
                  self.SK = "g5EgLoGOxEs3jogREqGVWUYl1e5tLkUL"
                  self.img_src = img
                  self.headers = {
                      "Content-Type": "application/json; charset=UTF-8"
                  }
       
              def get_accessToken(self):
                  host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=' + self.AK + '&client_secret=' + self.SK
                  response = requests.get(host, headers=self.headers)
                  json_result = json.loads(response.text)
                  return json_result['access_token']
       
              def img_to_BASE64(slef,path):
                  with open(path,'rb') as f:
                      base64_data = base64.b64encode(f.read())
                      return base64_data
       
              def detect_face(self):
                  # 人脸检测与属性分析
                  img_BASE64 = self.img_to_BASE64(self.img_src)
                  request_url = "https://aip.baidubce.com/rest/2.0/face/v3/detect"
                  post_data = {
                      "image": img_BASE64,
                      "image_type": "BASE64",
                      "face_field": "gender,age,beauty,gender,race,expression",
                      "face_type": "LIVE"
                  }
                  access_token = self.get_accessToken()
                  request_url = request_url + "?access_token=" + access_token
                  response = requests.post(url=request_url, data=post_data, headers=self.headers)
                  json_result = json.loads(response.text)
                  if json_result['error_msg']!='pic not has face':
                      print()
                      if json_result['result']['face_list'][0]['gender']['type'] == 'male':
                          gender= '男'
                      else:
                          gender= '女'
                          
                      if json_result['result']['face_list'][0]['race']['type'] == 'yellow':
                          race= '黄种人'
                      elif json_result['result']['face_list'][0]['race']['type'] == 'black':
                          race= '黑种人'
                      else:
                          race= '白种人'

                      if json_result['result']['face_list'][0]['expression']['type'] == None:
                          sd= '无'
                      else:
                          sd = json_result['result']['face_list'][0]['expression']['type']
                      t1 = tk.Label(win, text=json_result['result']['face_num']).grid(row=4,column=1)
                      t2 = tk.Label(win, text=json_result['result']['face_list'][0]['age']).grid(row=5,column=1)
                      t3 = tk.Label(win, text=str(json_result['result']['face_list'][0]['beauty'])+'（满分100）').grid(row=6,column=1)
                      t4 = tk.Label(win, text=gender).grid(row=7,column=1)
                      t5 = tk.Label(win, text=race).grid(row=8,column=1)
                      t6 = tk.Label(win, text=sd).grid(row=9,column=1)
       
          if __name__=='__main__':
              img_src=fpath.get()
              baiduDetect = BaiduPicIndentify(img_src)
              baiduDetect.detect_face()

      win = tk.Toplevel(root)
      win.title("颜值检测")
      win.geometry("600x300")
      fpath=tk.StringVar()

      l = tk.Label(win, text='邢氏颜值检测系统', bg='brown', font='黑体,20,bold',fg='white')
      l.grid(row=1,column=0)

      ttk.Button(win,text='选择人脸',command=getfile).grid(row=2,column=0)
      ttk.Entry(win,textvariable=fpath).grid(row=2,column=1)

      l1 = tk.Label(win, text='人脸数：')
      l1.grid(row=4,column=0)
      l2 = tk.Label(win, text='人物年龄：')
      l2.grid(row=5,column=0)
      l3 = tk.Label(win, text='人物颜值评分：')
      l3.grid(row=6,column=0)
      l4 = tk.Label(win, text='人物性别：')
      l4.grid(row=7,column=0)
      l5 = tk.Label(win, text='人物种族：')
      l5.grid(row=8,column=0)
      l6 = tk.Label(win, text='人物表情：')
      l6.grid(row=9,column=0)

      b=tk.Button(win,text="点击开始检测",width=15,height=2,command=face_baidu)
      b.grid(row=10,column=0)

def xspy():
      root1 = tk.Toplevel(root)
      root1.title('编程开发')#标题
      root1.geometry('200x200')  
      root1.resizable(False, False)#固定窗体
      root1.config(background="#6fb705")
      def py1():
            subprocess.Popen("exe//xspy.exe")
      def py2():
            subprocess.Popen("exe//xspy2.exe")
      yu=tkinte.Button(root1, text='pyhon编程',command=py1,width=15, height=1)
      yu.pack()
      yu.place(x=30,y=30)
      yu2=tkinte.Button(root1, text='pyhon交互模式',command=py2,width=15, height=1)
      yu2.pack()
      yu2.place(x=30,y=120)
root=tkinter.Tk()
root.title('邢氏小工具')#标题
root.geometry('500x500')  
root.resizable(False, False)#固定窗体
root.config(background="#6fb765")
root.iconbitmap('ico//k.ico')#设置图片

subprocess.Popen("update//update.exe")

if  os.path.exists('music'):
    shutil.rmtree('music')
if TIME1 == '06' or TIME1 == '07':
      gt = tkinte.Label(text='嗨!我们又见面了\n早上好',fg='red',font=("微软雅黑",9))
      gt.pack()
      gt.place(x=30,y=35)
elif TIME1 == '08' or TIME1 == '09' or TIME1 == '10':
      gt = label=tkinte.Label(text='嗨!\n新的一天\n元气满满',fg='red',font=("微软雅黑",9))
      gt.pack()
      gt.place(x=60,y=35)
elif TIME1 == '11' or TIME1 == '12':
      gt = label=tkinte.Label(text='嗨!中午好',fg='red',font=("微软雅黑",9))
      gt.pack()
      gt.place(x=60,y=55)
elif TIME1 == '13' or TIME1 == '14' or TIME1 == '15' or TIME1 == '16' or TIME1 == '17' or TIME1 == '18' :
      gt = label=tkinte.Label(text='嗨!下午好',fg='red',font=("微软雅黑",9))
      gt.pack()
      gt.place(x=60,y=55)
elif TIME1 == '19' or TIME1 == '20' or TIME1 == '21':
      gt = label=tkinte.Label(text='嗨!\n一天就要过去了\n准备迎接新一天的美好',fg='red',font=("微软雅黑",9))
      gt.pack()
      gt.place(x=10,y=35)
else:
      gt = label=tkinte.Label(text='夜深了\n请注意休息',fg='red',font=("微软雅黑",9))
      gt.pack()
      gt.place(x=50,y=45)
      
st = tkinte.Label(text='邢氏小工具v1.2.4',font=("微软雅黑",10))
st.pack()
st.place(x=175,y=25)

var=tkinter.StringVar()
lb = tkinter.Label(root,textvariable=var,fg='blue',font=("黑体",15))
lb.pack()
lb.place(x=190,y=65)
gettime()

button1 = tkinte.Button(root, text='天气查询',command=tianqi,width=10, height=1)
button1.pack()
button1.place(x=45, y=120)

button2 = tkinte.Button(root, text='物流查询',command=wuliu,width=10, height=1)
button2.pack()
button2.place(x=195, y=120)

button3= tkinte.Button(root, text='成语解释',command=chengyu,width=10, height=1)
button3.pack()
button3.place(x=345, y=120)

button4= tkinte.Button(root, text='计划任务',command=guanji,width=10, height=1)
button4.pack()
button4.place(x=45, y=180)

button5= tkinte.Button(root, text='笑话',command=xiaohua,width=10, height=1)
button5.pack()
button5.place(x=195, y=180)

button6= tkinte.Button(root, text='新闻',command=xinwen,width=10, height=1)
button6.pack()
button6.place(x=345, y=180)

button7= tkinte.Button(root, text='翻译',command=fanyi,width=10, height=1)
button7.pack()
button7.place(x=45, y=240)

button8= tkinte.Button(root, text='历史上的今天',command=lishi,width=10, height=1)
button8.pack()
button8.place(x=195, y=240)

button9= tkinte.Button(root, text='记事本',command=jishi,width=10, height=1)
button9.pack()
button9.place(x=345, y=240)

button10 = tkinte.Button(root, text='计算器',command=jisuan,width=10, height=1)
button10.pack()
button10.place(x=45, y=300)

button12 = tkinte.Button(root, text='休闲小游戏',command=games,width=10, height=1)
button12.pack()
button12.place(x=195, y=300)

button13 = tkinte.Button(root, text='系统操作',command=caozuo,width=10, height=1)
button13.pack()
button13.place(x=345, y=300)

button14 = tkinte.Button(root, text='万能格式转换',command=zhuanhuan,width=10, height=1)
button14.pack()
button14.place(x=45, y=360)

button15 = tkinte.Button(root, text='相机',command=xiangji,width=10, height=1)
button15.pack()
button15.place(x=195, y=360)

button16 = tkinte.Button(root, text='清理垃圾',command=laji,width=10, height=1)
button16.pack()
button16.place(x=345, y=360)

button16 = tkinte.Button(root, text='邢氏音乐',command=mu,width=10, height=1)
button16.pack()
button16.place(x=45, y=420)

button16 = tkinte.Button(root, text='颜值测试',command=yanzhi,width=10, height=1)
button16.pack()
button16.place(x=195, y=420)

button17 = tkinte.Button(root, text='编程开发',command=xspy,width=10, height=1)
button17.pack()
button17.place(x=345, y=420)

button11 = tkinte.Button(root, text='设置',command=setting,width=10, height=1)

button11.pack()
button11.place(x=345, y=40)

root.mainloop()


