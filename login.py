

from tkinter import *

class GUI_Login(Tk):
    userName = ""
    password = ""

    def __init__(self, master=None):
        Tk.__init__(self, master)

        self.fontePadrao = ("Arial", "12")
        self.geometry("300x240+150+100")#("1920x1080+0+0")
        self.title("ADMSuper: Login")

        # Label Nome da Empresa
        self.Lb_empresa = Label(self, text="SJ Super", font=self.fontePadrao)#, bg="red", fg="white")
        self.Lb_empresa.place(x=30, y=30, width=240, height=30)
        # Label Nome:
        self.Lb_userName = Label(self, text="Nome:", font=self.fontePadrao)#, bg="yellow", fg="black")
        self.Lb_userName.place(x=30, y=70, width=70, height=25)
        # Entry Nome:
        self.Et_userName = Entry(self, font=self.fontePadrao)#, bg="green", fg="white")
        self.Et_userName.place(x=100, y=70, width=170, height=25)
        # Label Senha:
        self.Lb_password = Label(self, text="Senha:", font=self.fontePadrao)#, bg="yellow", fg="black")
        self.Lb_password.place(x=30, y=105, width=70, height=25)
        # Entry Senha:
        self.Et_password = Entry(self, font=self.fontePadrao, show='*')#, bg="green", fg="white")
        self.Et_password.place(x=100, y=105, width=170, height=25)
        # Botão Login:
        self.Bt_login = Button(self, text="LOGIN", font=self.fontePadrao)#, bg="green", fg="white")
        self.Bt_login.place(x=30, y=140, width=100, height=30)
        self.Bt_login["command"] = self.verificacao()
        #self.Bt_login["state"] =  "disabled"
        # Botão Sair:
        self.Bt_sair = Button(self, text="SAIR", font=self.fontePadrao)#, bg="green", fg="white")
        self.Bt_sair.place(x=170, y=140, width=100, height=30)
        self.Bt_sair["command"] = self.sair
        #self.Bt_sair["state"] =  "disabled"
        # Label Mensagem:
        self.Lb_mensagem = Label(self, text="", font=self.fontePadrao)#, bg="yellow", fg="black")
        self.Lb_mensagem.place(x=30, y=180, width=240, height=25)




    # Método verificar senha
    def verificacao(self):
        userName = self.Et_userName.get()
        password = self.Et_password.get()
        if userName == "fausto" and password == "fausto":
            print("Autenticado")
            self.Lb_mensagem["text"] = "Autenticado"
            return "Autenticado"
        else:
            print("Não Autenticado")
            self.Lb_mensagem["text"] = "Erro na Autenticado"
            return "Erro na autenticação"

    def sair(self):
        self.quit()



if __name__ == '__main__':
    root = GUI_Login()
    mainloop()


def Name():
     Na = 'guilherme'
     return Na

def Senha():
     se = 'e10adc3949ba59abbe56e057f20f883e'
     return se