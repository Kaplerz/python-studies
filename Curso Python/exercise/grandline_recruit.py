candidatos = {
    'Zoro': ['Espadachim', 'Haki', 'Força'],
    'Sanji': ['Cozinheiro', 'Haki', 'Footwork'],
    'Nami': ['Navegador', 'Médico', 'Clima'], 
    'Usopp': ['Atirador', 'Engenharia'],
    'Franky': ['Engenharia', 'Força', 'Mecânico']
    
}

def encontrar_especialistas(candidatos, habilidade):
    especialistas = []
    for nome, habilidades in candidatos.items():
        if habilidade in habilidades:
            especialistas.append(nome)
    return especialistas
        
resultado = encontrar_especialistas(candidatos, 'Engenharia')
print(f'Os candidatos que tem a habilidade "Engenharia" são: {resultado}')