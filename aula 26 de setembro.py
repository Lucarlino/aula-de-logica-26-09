import os 
os.system ('cls')

# (ex01) Informando números até 50
print(f'\n Exercício 1')

for x in range (1,51):
   print (x)

# (ex02) Todos os anos em que ocorreram a copa do mundo 
print(f'\n Exercício 2')

for x in range (1930,2026,4):
   print (x)
print('Ainda vai haver muitas copas do mundo em breve')

#(ex03) Sistema para gerar todos os números da quina
print(f'\n Exercício 3')

import random
for x in range (5):
   num = random.randint(1,80)
   print(num)

