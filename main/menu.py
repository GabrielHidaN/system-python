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
  secao1 =' (1)Manipulação de Dados\n (2)Automações\n (3)Games\n (4)IA\n (5)Buscador de Vagas\n (0)ajuda\n (Esc)Sair'


  print(secao1)

  print(ASCII_NAME_HIDANX)

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
