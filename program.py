REMOVE = [',', ' ']
#----------------------------------------
def conversao(x,y,v):
    while x > 0:
        z = x % v  
        x = x // v
        if v == 16 or 20:
            if z == 10:
                z = 'A'
            if z == 11:
                z = 'B'
            if z == 12:
                z = 'C'
            if z == 13:
                z = 'D'
            if z == 14:
                z = 'E'
            if z == 15:
                z = 'F'
        if v == 20:
            if z == 16:
                z = 'G'
            if z == 17:
                z = 'H'
            if z == 18:
                z = 'I'
            if z == 19:
                z = 'J'
        y.append(z)
    y.reverse()
    y = [str(a) for a in y]
    a = y
    char = set(REMOVE)
    res = ' '.join(filter(lambda x: x not in char, a))
    y = res
    if v == 2:
        print('Binario:')
    elif v == 4:
        print('Quaternário:')
    elif v == 8:
        print('Octal:')
    elif v == 16:
        print('Hexadecimal:')
    elif v == 20:
        print('Vigesimal:')
    print(y,'\n')
#----------------------------------------

while True:
    print('===' * 7)
    x = int(input("Valor para converter: "))
    valor = x
    base = [2,4,8,16,20]  
    for i in base:
    #Binario
        x = valor
        y = []
        v = i
        conversao(x,y,v)
    print('===' * 7)
    print(' ')
    continuar = str(input("Deseja continuar? [S/N]: "))
    if continuar == 'S' or continuar == 's':
        pass
    elif continuar == 'N' or continuar == 'n':
        print('Encerrando...')
        break;