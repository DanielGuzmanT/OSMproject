'''
Función str_num(cadena):
    Variables de entrada: String tratada como lista de caracteres
    Retorna el número casteado que representa la cadena de caracteres
'''

def str_num(cadena):
    i = 0
    punto = False
    numero = 0
    signo = 1
    for c in cadena:
        assert c in ['0','1','2','3','4','5','6','7','8','9','0','.','-'], "error en casting"
        if c == '-':
            signo = -1
            continue
        elif c == '.':
            punto = True
            continue   
        elif not punto:
            numero *= 10
            numero += int(c)
        else:
            i += 1
            numero += int(c) / (10 ** i)

    return numero*signo
