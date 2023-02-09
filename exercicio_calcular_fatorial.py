# Calcular o fatorial de um número
y = numero = int(input("Digite o número: "))

if(numero > -1):
  while(numero > 1):
    y = y * (numero - 1)
    numero = numero - 1
  print("O fatorial é " + str(y))
else:
  print("O número deve ser positivo!")
