import requests
from tkinter import messagebox
import tkinter as tk
import webbrowser,sys
root=tk.Tk()
root.destroy()
banben='v1.2.4'
url = 'https://gitcode.net/xingjiahao200910/xgj/-/raw/master/index.html'
res = requests.get(url).text
if res[0:-1] != banben:
      url='https://gitcode.net/xingjiahao200910/xgj/-/raw/master/public/index.html'
      res1 = requests.get(url).text
      result = messagebox.askquestion('询问', '检测到新版本'+res+'是否更新？\n\n'+res1)
      if result == 'yes':
            url = 'https://gitcode.net/xingjiahao200910/xgj/-/raw/master/%E9%82%A2%E6%B0%8F%E5%B0%8F%E5%B7%A5%E5%85%B7'+res+'.exe?inline=false'
            webbrowser.open(url, new=0, autoraise=True)
            messagebox.showinfo(root,title = '更新提示',message='请查看您的电脑默认浏览器')
sys.exit()
