from utils import fatorial, dobro, triplo
num = int(input("Digite um número: "))
fat = fatorial(num)
dob = dobro(num)
tri = triplo(num)
print(f"O fatorial de {num} é {fat}.")  
print(f"O dobro de {num} é {dob}.")
print(f"O triplo de {num} é {tri}.")