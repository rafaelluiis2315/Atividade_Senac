### DESENVOLVEDORES : RAFAEL LUÍS | IURI TORRES ###

# IMPORTAÇÕES

from ast import While
from operator import index
import os
from time import sleep
import datetime

from numpy import true_divide

# CÓDIGO
lista_nome = []
lista_idade = []
lista_sexo = []


while True:

    nome = input('Qual o seu nome? ')                                # Armazena nome

    lista_nome.append(nome)

    idade = int(input('Qual a sua idade? '))                         # Armazena idade

    lista_idade.append(idade)

    sexo = str(input('Qual o seu sexo? (M/F): ' ))                  # Armazena sexo1

    if sexo.strip('asc' and 'asculino').upper() == 'M':
       lista_sexo.append(sexo)
       
       print( lista_sexo)








# CONDIÇÃO DE EXIBIÇÃO DE NOME (SEXO MASCULINO COM MAIS DE 21 ANOS)

if idade1 and idade2 > 21 and sexo1 == 'M' and sexo2 == 'M':
    print('Nome: \n\n - {} \n - {}'.format(nome1, nome2))

elif idade1 > 21 and sexo1 != 'F':
    print('Nome: \n\n - {}'.format(nome1))

elif idade2 > 21 and sexo2 != 'F':
    print('Nome: \n\n - {}'.format(nome2))


