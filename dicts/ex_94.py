pessoa = dict()
galera = list()
acima_media = list()
soma = media = 0

while True:
    
    pessoa['nome'] = str(input("Nome: ")) 
    
    while True: 
        pessoa['sexo'] = str(input("Sexo: [M/F] ")).upper() [0] 
        if(pessoa['sexo'] in 'MF'):
            break
        print("Valor errado, apenas M ou F.")
    
    pessoa['idade'] = int(input("Idade: "))
    soma += pessoa['idade']
    galera.append(pessoa.copy())

    while True:   
        continuar = str(input("Deseja continuar: ")).upper()[0] 
        if continuar in 'SN':
            break
        print("Digite uma opção valida!")
    if continuar == 'N':
        break

print(f"soma: {soma}")
print(f"quantidade: {len(galera)}")

media = soma / len(galera)
print("-=" *30)

print(f"Ao todo temos o total de {len(galera)} pessoas cadastradas.")

print(f"A Media das idades é {media:5.2f}")

print(f"As mulheres cadastradas foram: ", end='')

for p in galera:
    if(p['sexo'] == 'F'):
        print(f"{p["nome"]}", end =' ') 
print()

print(f"Pessoas com idade acima da média: ") 

for p in galera: #P = Array pessoas, este for percorre cara array 
    if ( p['idade'] >= media):
        for k, v in p.items():
            print(f"{k}: {v}")

