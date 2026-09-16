nomes = 'Guilherme, Thomas, Predes'

nomes = nomes.split(',')
nomes_limpos = []


for nome in nomes:
    print(nome.strip())    
    nomes_limpos.append(nome.strip())


print(nomes_limpos)
