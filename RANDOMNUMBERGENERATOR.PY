import random
from this import s 
from tkinter import*
from tkinter import messagebox
text= "0123456789" 
window=Tk()
window.title("PASSWORD GENERATOR")
window.geometry("800x350")
captcha =StringVar()
user_input =StringVar()
def set_captcha():
   s =random.choices(text,k=4) 
   captcha.set(''.join(s))
Label (window, textvariable =captcha,   
    font ="Arial 100 bold").pack()
set_captcha() 
window.mainloop()