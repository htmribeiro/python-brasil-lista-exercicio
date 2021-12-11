"""
Faça um Programa que peça dois números e imprima a soma.
"""
def ex003():
  print()
  print("{:*^50}".format(" Ex003 - Imprime a soma de dois números. "))
  print()
  
  num1 = int(input("Digite o primeiro número: "))
  num2 = int(input("Digite o segundo número: "))
  
  print()
  print(f"O resultado da soma é: {num1 + num2}.")
  print()
  
  
  print("{:*^50}".format(" Fim do programa "))
  
if __name__ == "__main__":
  ex003()