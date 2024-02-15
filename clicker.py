from tkinter import *
from tkinter import ttk
import pyautogui
import time
import keyboard
print("essa")
root = Tk()
style = ttk.Style()
root.title("Clicker")

root.geometry("500x500")
root.resizable(False, False)
bgcolor = "#16151f"
fgcolor = "#6856b3"
root.configure(bg=bgcolor)

def destroy(event):
    root.destroy()

Label(root, text="Clicker", font=("System", 30), fg=fgcolor, bg=bgcolor).pack()

key = Entry(root, font=("System", 20), fg=fgcolor, bg=bgcolor, width=10, insertbackground="White", selectbackground="Gray", highlightthickness=1, highlightbackground="White")
key.place(x=170, y=150)

def check(*args):
    if combobox.get() == 'Key':
        label1 = Label(root, text="Key: ", font=("System", 16), fg=fgcolor, bg=bgcolor)
        label1.place(x=170, y=128)
        key.delete(first=0, last=999)
        key.insert(0, 'leftmouse')
    if combobox.get() == 'Text':
        label2 = Label(root, text="Text: ", font=("System", 16), fg=fgcolor, bg=bgcolor)
        label2.place(x=170, y=128)
        key.delete(first=0, last=999)
        key.insert(0, 'Text example')

current_var = StringVar()
current_var.trace('w', callback=check)
combobox = ttk.Combobox(root, textvariable=current_var, state="readonly", width=7)
combobox['values'] = ['Key','Text']
combobox.current(0)

style.theme_create('combostyle', parent='alt',
                         settings = {'TCombobox':
                                     {'configure':
                                      {'selectbackground': 'none',
                                       'fieldbackground': '#16151f',
                                       'background': '#6856b3',
                                       'foreground': 'White'
                                       }}}
                    )
combobox.configure(font=("System", 20))
combobox.place(x=20, y=150)
style.theme_use('combostyle')

Label(root, text="Pause time:", font=("System", 16), fg=fgcolor, bg=bgcolor).place(x=170, y=203)
pause = Entry(root, font=("System", 20), fg=fgcolor, bg=bgcolor, width=10, insertbackground="White", selectbackground="Gray", highlightthickness=1, highlightbackground="White")
pause.place(x=170, y=225)
pause.insert(0, "0.1")

Label(root, text="Key to stop:", font=("System", 16), fg=fgcolor, bg=bgcolor).place(x=170, y=278)
keystop = Entry(root, font=("System", 20), fg=fgcolor, bg=bgcolor, width=10, insertbackground="White", selectbackground="Gray", highlightthickness=1, highlightbackground="White")
keystop.place(x=170, y=300)
keystop.insert(0, "q")

enteroption = IntVar()
cb = Checkbutton(root, text='Enable clicking\n enter after every\n text output (only\n works in the\n "Text" mode)', bg=bgcolor, fg=fgcolor, font=("System", 10),border=0, variable=enteroption, onvalue=1, offvalue=0)
cb.place(x=20, y=200)

def click():
    time.sleep(3)
    if combobox.get() == 'Key':
        if key.get() == "leftmouse":
            while True:
                pyautogui.click()
                if keyboard.is_pressed(keystop.get()):
                    destroy()
        if key.get() == "rightmouse":
            while True:
                pyautogui.click(button='right')
                if keyboard.is_pressed(keystop.get()):
                    destroy()
        else:
            while True:
                pyautogui.press(key.get())
                if keyboard.is_pressed(keystop.get()):
                    destroy()
    if combobox.get() == 'Text':
        while True:
            pyautogui.write(key.get())
            if enteroption.get() == 1:
                pyautogui.press('enter')
            if keyboard.is_pressed(keystop.get()):
                    destroy()
def start():
    pyautogui.PAUSE = float(pause.get())
    if float(pause.get()) < 0.01:
        root2 = Tk()
        root2.geometry("300x200")
        root2.resizable(False, False)
        root2.title("Warning")
        root2.configure(bg=bgcolor)
        def nofunc():
            root2.destroy()
        def yesfunc():
            root2.destroy()
            click()
        Label(root2, text="Are you sure you\nwant to start with this\n little pause time?", font=("System", 20), fg=fgcolor, bg=bgcolor).pack()
        no = Button(root2, text="No", font=("System", 20), fg=fgcolor, bg=bgcolor, command=nofunc)
        no.place(x=50, y=130)
        yes = Button(root2, text="Yes", font=("System", 20), fg=fgcolor, bg=bgcolor, command=yesfunc)
        yes.place(x=175, y=130)
        root2.mainloop()
    else:
        click()
    
Button(root, text="START", font=("System", 20), fg=fgcolor, bg=bgcolor, command=start).place(x=200, y=375)
root.mainloop()