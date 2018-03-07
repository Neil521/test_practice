from tkinter import *
import tkinter.simpledialog as dl
import tkinter.messagebox as mb

#设置GUI
root=Tk()
w=Label(root,text='Guess Nunber Game')
w.pack()

#欢迎界面
mb.showinfo('Welcome','Welcome to Guess Number Game!')
guess=dl.askinteger('Numeber','Enter a number')

#设置答案
answer=60

#游戏开始
while True:
    guess=dl.askinteger('Number','Enter a number:')

    if guess==answer:
        output='Bingo!You are celver'
        mb.showinfo('Hint:',output)
        break
    elif guess<answer:
        output = '您输入的数字太小了'
        mb.showinfo('Hint:', output)
    else:
        output = '您输入的数字太大了'
        mb.showinfo('Hint:', output)
#游戏结束
print('Done')
