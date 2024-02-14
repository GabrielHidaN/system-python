import os
import sys
from menu import*

nome_login = ''
def loginFunc():
  password = '0'
  tentative = 5
  while tentative >= 1:
     login = input('Digite a senha de acesso: \n')
     if login == password:
         os.system('cls')
         nome_login = input('Olá sejá bem vindo! Para facilitar acomunicação digite  seu nome: \n')
         os.system('cls')
         print(f' Olá {nome_login}')
         menu()
         exit()

     elif login != password:
        tentative = tentative -1
        if tentative >= 2:
            print('Senha Errada\n')
            print(f'Você ainda tem {tentative} tentativas')
        elif tentative > 0:
           print('Senha Errada\n')
           print(f'você não tem mais {tentative} tentativa!')
        elif tentative <= 0:
           print('Senha Errada\n')
           print('Não resta mais nenhuma tentativa!')
