import os
import sys

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
         print(f'É um prazer ter você aqui conosco {nome_login}! ')
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

