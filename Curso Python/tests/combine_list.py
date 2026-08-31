produtos_a = ['Mouse', 'Teclado']
produtos_b = ['Monitor', 'Headset'] 
produtos_c = produtos_a + produtos_b
print(f'Primeira lista: {produtos_a}, Segunda lista: {produtos_b} \
Terceira lista: {produtos_c}')

legumes_1 = ['Cenoura', 'Pepino']
legumes_2 = ['Abóbora', 'Batata']
legumes_1.extend(legumes_2)
print(f'Opções de legumes: {legumes_1} e {legumes_2}')

relogios_1 = ['Cassio', 'G-Shock']
relogios_2 = ['Rolex', 'Patek']
relogios_1.append(relogios_2)
print(f'Os relógios disponíveis são: {relogios_1} e {relogios_2}')