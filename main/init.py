import os
import sys

nome_login = ''
def login_signed():
  password = str('0')
  login = input('Digite a senha de acesso: \n')
  if login == password:
    os.system('cls')
    nome_login = input('Olá sejá bem vindo! Para facilitar a comunicação digite seu nome: \n')
    os.system('cls')
    print(f'É um prazer ter você aqui conosco {nome_login}! ')

  else:
    attempts = 5
    while login != password:
      print('Você digitou a senha errada!')
      tentativ = f'voce so tem mais {attempts -1} tentativa'
      print(tentativ)
      login_signed()
      if attempts <= 0:
        print('acabou suas tentativas')
        sys.exit()

"""
Resolver:
Bug do while -1
"""
