# Acertar o número sorteado
import random

i = random.randint(1, 10); #http://curso.grupysanca.com.br/pt/latest/input.html

j = int(input("Digite o valor que você acha que foi sorteado: "))

while(j != i):
  if (j > i):
    print("O número que você digitou é maior que o número sorteado.")
  elif(j < i):
    print("O número que você digitou é menor que o número sorteado")
  j = int(input("Digite o valor que você acha que foi sorteado: "))

if(j == i):
  print("PARABÉNS! Você acertou o número!")
