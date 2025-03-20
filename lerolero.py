"""
gerador de lero lero

gera frases de efeito sem sentido
"""
import random

parte1 = ["O sitema em desenvolvimento",
          "O novo protocolo de comunicação",
          "O algoritimo de otimizações"]
parte2 = ["oferece garantias de precisão acima da média"
        "possui excelente desenpenho",
        "preenche uma lacuna significativa"]
parte3 = ["nas aplicações em que se destina",
          "em relação as demais opções do mercado",
          ".Promovendo ampla vantagem competitiva"]

lingua = int(input("Escolha a lingua: 1 - portugues , 2 - ingles\n")) 

if lingua == 2:
    parte1 = []
    parte2 = []
    parte3 = []


print(random.choice(parte1),random.choice(parte2),random.choice(parte3))
