from bibliotecas import *
from tkinter import *


class InterfaceGrafica:
    def __init__(self, master=None):
        image_button = PhotoImage(file='c:/Users/User/Pictures/Image_Projects/Instagram_Bot/send-button.png')

        self.fontePadrao = ('Arial', '10')

        self.primeiroContainer = Frame(master)
        self.primeiroContainer['pady'] = 10
        self.primeiroContainer.pack()

        self.segundoContainer = Frame(master)
        self.segundoContainer['pady'] = 5
        self.segundoContainer.pack()

        self.terceiroContainer = Frame(master)
        self.terceiroContainer['pady'] = 5
        self.terceiroContainer.pack()

        self.quartoContainer = Frame(master)
        self.quartoContainer['pady'] = 5
        self.quartoContainer.pack()

        self.quintoContainer = Frame(master)
        self.quintoContainer['pady'] = 10
        self.quintoContainer.pack()

        self.sextoContainer = Frame(master)
        self.sextoContainer['pady'] = 10
        self.sextoContainer.pack()

        self.titulo = Label(self.primeiroContainer, text='Bot Instagram')
        self.titulo['font'] = ('Comic Sans MS', '25')
        self.titulo.pack()

        self.usuario = Label(self.segundoContainer, text='Usuario:', font=self.fontePadrao)
        self.usuario.pack(side=LEFT)

        self.campo_usuario = Entry(self.segundoContainer)
        self.campo_usuario['width'] = 20
        self.campo_usuario['font'] = self.fontePadrao
        self.campo_usuario.pack(side=LEFT)

        self.senha = Label(self.terceiroContainer, text='Senha:  ', font=self.fontePadrao)
        self.senha.pack(side=LEFT)

        self.campo_senha = Entry(self.terceiroContainer)
        self.campo_senha['width'] = 20
        self.campo_senha['font'] = self.fontePadrao
        self.campo_senha['show'] = '*'
        self.campo_senha.pack(side=LEFT)

        self.nicho = Label(self.quartoContainer, text='Nicho:  ', font=self.fontePadrao)
        self.nicho.pack(side=LEFT)

        self.campo_nicho = Entry(self.quartoContainer)
        self.campo_nicho['width'] = 20
        self.campo_nicho['font'] = self.fontePadrao
        self.campo_nicho.pack(side=LEFT)

        self.mensagem = Label(self.quintoContainer, text='Mensagem: ', font=self.fontePadrao)
        self.mensagem.pack()

        self.campo_mensagem = Text(self.quintoContainer)
        self.campo_mensagem['width'] = 30
        self.campo_mensagem['height'] = 5
        self.campo_mensagem['font'] = self.fontePadrao
        self.campo_mensagem.pack()

        self.iniciar = Button(self.sextoContainer)
        self.iniciar['text'] = 'Iniciar Bot'
        self.iniciar['width'] = 15
        self.iniciar['command'] = self.enviar
        self.iniciar.pack()

    def enviar(self):
        usuario = str(self.campo_usuario.get())
        senha = str(self.campo_senha.get())
        print(senha)
        mensagem = str(self.campo_mensagem.get('1.0', 'end-1c'))
        print(mensagem)
        nicho = str(self.campo_nicho.get())
        bot = BotInstagram(usuario, senha)
        bot.login(nicho, mensagem)


root = Tk()
InterfaceGrafica(root)
root.geometry('500x500')
root.mainloop()
