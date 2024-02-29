from init import*
from config import*
from name_ascii import*
from init import*
import keyboard


def MENU_INIT():

  OPCOES = ['0','1','2','3','4','5']
  secao1 =f'''
{paragrafo1}

{ASCII_ART_MENU}

{paragrafo_menu}

  (1)Manipulação de Dados

  (2)Automações

  (3)Games

  (4)IA

  (5)Buscador de Vagas

  (0)ajuda

  (Esc)Sair

{ASCII_NAME_HIDANX}
  '''

  print(secao1)

  INPUT_MENU = str(keyboard.read_key())

  if INPUT_MENU in OPCOES:
    if INPUT_MENU == '0':
      ...
    elif INPUT_MENU == '1':
      ...
    elif INPUT_MENU == '2':
      ...
    elif INPUT_MENU == '3':
      ...
    elif INPUT_MENU == '4':
      ...
    elif INPUT_MENU == '5':
      ...
  elif INPUT_MENU == 'esc':
      sys.exit("Programa finalizado")

  else:
    print('ele nao esta')

#resolver o keyboard no input
