def multiplicar(*args):
    resultado = 1
    
    for numero in args:
        resultado = resultado * numero
        
    return resultado

def par_ou_impar(numero):
    if numero % 2 == 0:
        return 'Par'
    else:
        return 'Ímpar'
    
resultado = multiplicar(2, 3, 4, 5)

print(resultado)
print(par_ou_impar(resultado)) 