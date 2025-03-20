"""
gerador de lero lero

gera frases de efeito sem sentido
"""
import random

parte1 = ["O sitema em desenvolvimento",
          "O novo protocolo de comunicação",
          "O algoritimo otimizado"]
parte2 = ["oferece garantias de precisão acima da média"
        "possui excelente desenpenho",
        "preenche uma lacuna significativa"]
parte3 = ["nas aplicações em que se destina",
          "em relação as demais opções do mercado",
          ".Promovendo ampla vantagem competitiva"]

print(random.choice(parte1),random.choice(parte2),random.choice(parte3))