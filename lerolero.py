"""
gerador de lero lero

gera frases de efeito sem sentido
"""
import random

parte1 = []
parte2 = []
parte3 = []

lingua = int(input("Escolha a lingua: 1 - portugues , 2 - ingles\n")) 

if lingua == 2:
    parte1 = []
    parte2 = []
    parte3 = []


print(random.choice(parte1),random.choice(parte2),random.choice(parte3))
