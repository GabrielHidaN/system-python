import os
import sys

def digit_pass():
   login = input('Digite a senha de acesso: \n')
nome_login = ''
def login_signed():
  password = '0'
  login = input('Digite a senha de acesso: \n')
  if  login == password:
    os.system('cls')
    nome_login = input('Olá sejá bem vindo! Para facilitar a comunicação  digite  seu nome: \n')
    os.system('cls')
    print(f'É um prazer ter você aqui conosco {nome_login}! ')
  else:
      tentativas = 5
      while login != password:
          tentativas = tentativas -1
          print(tentativas)
          if tentativas > 0:
             digit_pass()
          else:
             print('Você não tem mais tentativas!')
             exit()
