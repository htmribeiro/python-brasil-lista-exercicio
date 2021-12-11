"""
Faça um Programa que peça as 4 notas bimestrais e mostre a média.
"""
def ex004():
  print()
  print("{:*^50}".format(" Ex004 - Media das notas bimestrais "))
  print()
  
  n1 = float(input("Informe a N1: "))
  n2 = float(input("Informe a N2: "))
  n3 = float(input("Informe a N3: "))
  n4 = float(input("Informe a N4: "))
  
  notas = n1 + n2 + n3 + n4
  media_bimenstral = notas/4
  
  print()
  print("A média bimestral do Aluno é: {:.2F}".format(media_bimenstral))
  
  print()
  print("{:*^50}".format(" Fim do programa "))

if __name__ == "__main__":
  ex004()