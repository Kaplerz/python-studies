bando = {
    'Zoro': {'Espadachim', 'Haki', 'Força'},
    'Sanji': {'Cozinheiro', 'Footwork', 'Haki'},
    'Nami': {'Médico', 'Haki', 'Peituda'}
    
    
    
}

requisitos_navio = {'Navegador', 'Médico', 'Haki', 'Cozinheiro'}

def analisar_tripulacao(bando, requisitos):
    faltantes = requisitos.copy()
    maior_quantidade = 0
    tripulante_maior = None
    
    for nome, habilidades in bando.items():
        faltantes = faltantes - habilidades
        if len(habilidades) > maior_quantidade:
            maior_quantidade = len(habilidades)
            tripulante_maior = nome
    return faltantes, tripulante_maior

resultado = analisar_tripulacao(bando, requisitos_navio)
faltantes, tripulacao_maior = resultado
print(f'A habilidade faltante é: {faltantes}, e o tripulante com mais habilidades é: {tripulacao_maior}')