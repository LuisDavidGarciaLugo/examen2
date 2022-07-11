#15-10540
X = 5
Y = 4
Z = 0

alpha = ((X+Y) % 5) + 3
beta = ((Y+Z) % 5) + 3

def F_Recursiva(n):
    if 0 <= n < alpha*beta : return n

    res = 0
    for i in range(1, alpha+1):
        res += F_Recursiva(n-beta*i) 

    return res


def F_Cola(n):
    if 0 <= n < alpha*beta : return n

    #valores iniciales
    f0 = n % (alpha*beta)
    fup = f0
    fdown = f0 - beta
    initVals = []

    while fup < alpha*beta:
        initVals.append(fup)
        fup += beta

    while fdown >= 0:
        initVals.insert(0, fdown)
        fdown -= beta
   # print(initVals)
    return F_Cola_Rec(n, initVals)

def F_Cola_Rec(n, vals):
        
        #condicion de salida de recursion
        if n < alpha*(beta+1): 
            return sum(vals)

        #obtener nuevo valor para la recursion actual
        newVal = sum(vals)

        for i in range(alpha-1):
            vals[i] = vals[i+1]

        vals[-1] = newVal

        return F_Cola_Rec(n-beta, vals)


def F_Iter(n):
    if 0 <= n < alpha*beta : return n

    #valores iniciales
    f0 = n % (alpha*beta)
    fup = f0
    fdown = f0 - beta
    vals = []

    while fup < alpha*beta:
        vals.append(fup)
        fup += beta

    while fdown >= 0:
        vals.insert(0, fdown)
        fdown -= beta

    #condicion de salida de iteracion
    while n >= alpha*(beta+1):

        #obtener nuevo valor para la iteracion actual
        newVal = sum(vals)

        for i in range(alpha-1):
            vals[i] = vals[i+1]

        vals[-1] = newVal

        n -= beta

    return sum(vals)




