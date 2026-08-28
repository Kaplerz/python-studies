for numero in range(1, 50 + 1):
    if (numero > 35) and (numero % 5 == 0):
        break
    
    if numero % 3 == 0:
        continue
    
    print(numero)