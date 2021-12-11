"""
Faça um Programa que peça um número e então mostre a mensagem: O número informado foi [número].
"""
def ex002():
  print("{:*^50}".format(" Ex002 "))
  print()
  
  num = int(input("Digite um número inteiro: "))
  
  print()
  print("O número informado foi [{}].".format(num))
  print()
  
  print("{:*^50}".format(" Fim do programa "))
  
if __name__ == "__main__":
  ex002()
  