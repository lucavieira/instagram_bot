from bibliotecas import *

usuario = str(input('Digite o seu usuario: '))
senha = str(input('Digite sua senha: '))
mensagem = str(input('Digite a mensagem que deseja enviar: '))
perfil = str(input('Tema do perfil que deseja enviar mensagem: '))

bot = BotInstagram(usuario, senha)
bot.login(perfil, mensagem)
