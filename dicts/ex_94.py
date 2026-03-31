pessoa = dict()
galera = list()
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
    media += 1
    galera.append(pessoa.copy())

    while True:   
        continuar = str(input("Deseja continuar: ")).upper()[0] 
        if continuar in 'SN':
            break
        print("Digite uma opção valida!")
    if continuar == 'N':
        break

print("-=" *30)

print(f"Ao todo temos o total de {len(galera)} pessoas cadastradas.")

print(f"A Media das idades é {soma / media}")