


#Modul importing
from distutils.command.build import build
from logging import root
from time import sleep
from tkinter import *
from tkinter import messagebox
from turtle import clear
from typing_extensions import Self
from urllib.parse import uses_relative
#Modul importing end



#Kivy code begin


import kivy
from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.button import MDFlatButton
from kivymd.uix.dialog import MDDialog
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.app import App



class LoginLayout(Screen):
    pass


class MainApp(MDApp):




    def build(self):
        sm=ScreenManager()
        sm.add_widget(LoginLayout(name='login'))
        return sm

        self.theme_cls.theme_style = 'Dark'
        self.theme_cls.primary_palette = 'Blue'
    def login(self):
        if self.root.ids.user.text == "1" and self.root.ids.password.text == "1":
            self.root.ids.welcome_label.text = "Welcome " + self.root.ids.user.text
            self.root.ids.user.text = ""
            self.root.ids.password.text = ""
            sleep (1)
        else:
            self.root.ids.welcome_label.text = "Wrong username or password"
            self.root.ids.user.text = ""
            self.root.ids.password.text = ""
            self.manager.current = 'AfterLogin'
    def clear(self):
        self.root.ids.welcome_label.text = "welcome"
        self.root.ids.user.text = ""
        self.root.ids.password.text = ""
    def after_login(self):
        self.theme_cls.theme_style = 'Dark'
        self.theme_cls.primary_palette = 'Blue'
        return Builder.unload_file('login.kv')
    
    def logout(self):
        self.root.ids.welcome_label.text = "welcome"
        self.root.ids.user.text = ""
        self.root.ids.password.text = ""
        return self.build()

    def show_alert_dialog(self):
        if not self.dialog:
            self.dialog = MDDialog(
                text="Wrong Password!",
                buttons=[
                    MDFlatButton(
                        text="OK",
                        theme_text_color="Custom",
                        text_color=[0, 0, 0, 1],
                        pos_hint={'center_x': 0.5},
                        on_release=self.dialog.dismiss
                    )
                ]
            )
            self.dialog.open()
        else:
            self.dialog.open()
MainApp().run()








#Kivy code end

# definitionen
"""
def GetUUID():
   cmd = 'wmic csproduct get uuid'
   uuid = str(subprocess.check_output(cmd))
   pos1 = uuid.find("\\n")+2
   uuid = uuid[pos1:-15]
   return uuid

print(GetUUID())

def showmessagebox():
    if messagebox.askyesno("Wahr Oder Falsch", "Ist monte ein Rentner"):
        messagebox.showinfo("Richtig", "Er ist ein Rentner")
    else:
        messagebox.showinfo("Falsch", "Er ist ein Rentner")

def copy_button():
    clip = Tk()
    clip.withdraw()
    clip.clipboard_clear()
    clip.clipboard_append(GetUUID())  # Change INFO_TO_COPY to the name of your data source
    clip.destroy()

def Hwid():
      if GetUUID == "03C00218-044D-05DB-A406-090700080009":
            return True
        else:
            return False


def usr():
    usr = (username.get())
    pwd = (password.get())
    id = (GetUUID())
    if usr == "123" and pwd == "123" and Hwid():
        messagebox.showinfo("Login","Login war erfolgreich")
    else:
        messagebox.showerror("Login","Login ist fehlgeschlagen")


#Definitionen Ende

#arrays

Hwid3 = ["03C00218-044D-05DB-A406-090700080009"]

#arrays Ende

# Begin GUI 
root = Tk()
root.geometry("350x150")
root.title("Login")
root.resizable(0,0)

username = Label(master=root, bg="black", fg= "#d9a64f", text="Username")
username.place(x=0, y=0, width=100, height=30)

username = Entry(root)
username.place(x=140, y=0, width=200, height=30)

password = Label(master=root, bg="black", fg= "#d9a64f", text="Password")
password.place(x=0, y=40, width=100, height=30)

password = Entry(root)
password = Entry(master= root, show = '*')
password.place(x=140, y=40, width=200, height=30)

hardware = Button(master=root, bg="black", fg= "#d9a64f", text="HWID", command=lambda: copy_button())
hardware.place(x=0, y=80, width=100, height=30)

login = Button(master=root, bg="black", fg= "#d9a64f", text="Login", command=lambda: usr())
login.place(x=140, y=80, width=100, height=30)

# End GUI


#@copyright (c) 2023 by Thomas Schneider
root.mainloop()







"""