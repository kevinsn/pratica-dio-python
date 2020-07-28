# COMANDOS Aula_8 Python Console
# import aula_7_televisao
from aula_7_televisao import Televisao
from aula_7_calculadora1 import Calculadora
from aula_8_contador_letras import contador_letras, teste

# Só executa quando for chamado dentro do main, se não não executa
import os
if __name__ == '__main__':
    print("Estou sendo chamado pelo próprio arquivo neste caminho: ", os.path.realpath(__file__))

    televisao = Televisao()
    print(televisao.ligada)
    televisao.power()
    print(televisao.ligada)

    calculadora = Calculadora(5, 10)
    print(calculadora.soma())

    lista = ['cachorro', 'gato', 'elefante']
    total_letras = contador_letras(lista)
    print('Total de letras por palavra: {}'.format(total_letras))
    print(teste())

