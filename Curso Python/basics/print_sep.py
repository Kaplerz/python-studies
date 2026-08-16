# \r\n -> CLRF é o padrão do Windows e serve para indicar o final de uma linha
# \n -> LF é o padrão do Linux e do Mac e serve para indicar o final de uma linha

print(12, 34, 333, sep="-", end='##\n')  # separador = "-" e end = "##" (final da linha)
print(56, 78, 211, sep="-", end='\n') # separador = "-" e end = "\n" (final da linha)
print(10, 46, 763, sep="-", end='\n') # separador = "-" e end = "\n" (final da linha)









