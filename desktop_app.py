import tkinter.messagebox as mb
answer=mb.askyesno('質問','ラーメンは好きです？')
if answer==True:
    mb.showinfo('同意','僕も好きです。')
else:
    mb.showinfo('本当','まさか、ラーメンが嫌いだなんて！')
