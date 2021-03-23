from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from arquivo import *

arquivo = 'lista_perfis.txt'

if not existe_arquivo(arquivo):
    criar_arquivo(arquivo)


class BotInstagram:
    def __init__(self, usuario, senha):
        self.usuario = usuario
        self.senha = senha
        self.driver = webdriver.Chrome(executable_path=r"C:\Users\User\Documents\chrome_driver\chromedriver.exe")

    def login(self, hashtag, mensagem):
        navegador = self.driver
        navegador.get('https://www.instagram.com')
        sleep(3)
        navegador.maximize_window()
        sleep(2)
        campo_usuario = navegador.find_element_by_xpath('//input[@name="username"]')
        campo_usuario.click()
        campo_usuario.clear()
        campo_usuario.send_keys(self.usuario)
        sleep(1)
        campo_senha = navegador.find_element_by_xpath('//input[@name="password"]')
        campo_senha.click()
        campo_senha.clear()
        campo_senha.send_keys(self.senha)
        campo_senha.send_keys(Keys.RETURN)
        sleep(5)
        try:
            agoraNao = navegador.find_element_by_xpath('//button[@class="sqdOP yWX7d    y3zKF     "]')
            agoraNao.click()
        except:
            print('Ocorreu um erro')
        sleep(2)
        agora_nao = navegador.find_element_by_xpath('//button[@class="aOOlW   HoLwm "]')
        agora_nao.click()
        sleep(1)
        self.pesquisar(hashtag, mensagem)

    def pesquisar(self, hashtag, mensagem):
        navegador = self.driver
        navegador.get('https://www.instagram.com/explore/tags/' + hashtag + '/')
        sleep(3)
        for i in range(0, 3):
            navegador.execute_script('window.scrollTo(0, document.body.scrollHeight);')
            sleep(5)

        hrefs = navegador.find_elements_by_tag_name('a')
        pic_hrefs = [elem.get_attribute('href') for elem in hrefs]
        [href for href in pic_hrefs if hashtag in href]
        contador = 1

        for pic_href in pic_hrefs:
            sleep(2)
            navegador.get(pic_href)
            perfil = navegador.find_element_by_xpath('//div[@class="e1e1d"]')
            perfil.click()
            sleep(8)
            try:
                nome_perfil = navegador.find_element_by_xpath('//h2[@class="_7UhW9       fKFbl yUEEX   KV-D4              fDxYl     "]').text
            except:
                nome_perfil = navegador.find_element_by_xpath('//h1[@class="_7UhW9       fKFbl yUEEX   KV-D4              fDxYl     "]').text
            condicao = ler_arquivo(arquivo, nome_perfil)
            if condicao:
                cadastrar_perfil(arquivo, nome_perfil)
                sleep(5)
                botao_seguir = navegador.find_element_by_xpath('//button[@class="_5f5mN       jIbKX  _6VtSN     yZn4P   "]')
                botao_seguir.click()
                sleep(3)
                enviar_mensagem = navegador.find_element_by_xpath('//button[@class="sqdOP  L3NKy _4pI4F   _8A5w5    "]')
                enviar_mensagem.click()
                sleep(5)
                campo_mensagem = navegador.find_element_by_tag_name('textarea')
                campo_mensagem.click()
                sleep(2)
                campo_mensagem.send_keys(mensagem)
                sleep(2)
                campo_mensagem.send_keys(Keys.RETURN)
                sleep(2)
                navegador.back()
                sleep(2)
                parar_seguir = navegador.find_element_by_xpath('//button[@class="_5f5mN    -fzfL     _6VtSN     yZn4P   "]')
                parar_seguir.click()
                sleep(2)
                unfollow = navegador.find_element_by_xpath('//button[@class="aOOlW -Cab_   "]')
                unfollow.click()
                sleep(1)
                contador += 1
                if contador > 10:
                    navegador.quit()
                    break
            else:
                continue
