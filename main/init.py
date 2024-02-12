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
  elif login != password:
      tentativas = 5
      while tentativas >=1:
         print(f'Senha errada , você tem mais {tentativas} tentativas.')
         tentativas = tentativas -1
         digit_pass()
      print('Todas suas tentativas foram esgotadas!')
login_signed()

"""
tratar do  bug de login 
"""
