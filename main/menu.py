from init import*
from config import*
from name_ascii import*
from init import*
import keyboard


def menu_init():
  print('')

  print(paragrafo1)

  print(ASCII_ART_MENU)

  print(paragrafo_menu)

  print('')


  OPCOES = ['0','1','2','3','4','5']
  secao1 =' (1)Manipulação de Dados\n (2)Automações\n (3)Games\n (4)IA\n (5)Buscador de Vagas\n (6)...  \n (7)...\n (8)...\n (9)...\n (0)voltar\n'

  print(secao1)

  print(ASCII_NAME_HIDANX)
  secao1 = input()
  if('0' in OPCOES):
    print('deu certo')

#resolver o keyboard no input
