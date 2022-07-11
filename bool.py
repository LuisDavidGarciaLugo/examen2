def evalBool(exp, i, post, p = None):
    try:
        el = exp[i[0]]
    except:
        return None
    if el in ["|", "&", "=>"]:
        i[0] +=1
        arg1 = evalBool(exp, i, post)
        i[0] +=1
        arg2 = evalBool(exp, i, post)

        if arg1 == None or arg2 == None: return None

        if el == "|":
            val = arg1 or arg2
        elif el == "&":
            val = arg1 and arg2
        elif el == "=>":
            if post:
                val = arg1 or (not arg2)
            else:
                val = (not arg1) or arg2

    elif el == "^":
        i[0] +=1
        arg = evalBool(exp, i, post)
        if arg == None: return None
        val = not arg
    
    elif el == "true": val = True
    elif el == "false": val = False

    else: return None


    return val

#En esta implementacion en las expresiones POST las conjunciones
#y disyunciones se muestran en
#sentido contrario, por ejemplo para
#   MOSTRAR POST false true |
#el programa imprime
#   true | false
#en lugar de
#   false | true
#por reflexividad las expresiones emitidas son equivalentes
#a las indicadas en el enunciado
prec = {"^": 3, "&": 2, "|":2, "=>":1, None:0}
def mostrar(exp, i, post, parent = None, side = None):
    try:
        el = exp[i[0]]
    except:
        return None
    if el in ["|", "&", "=>"]:
        i[0] +=1
        arg1 = mostrar(exp, i, post, el, "left")
        i[0] +=1
        arg2 = mostrar(exp, i, post, el, "right")

        if arg1 == None or arg2 == None: return None

        if post == True and el == "=>":
            s = arg1
            arg1 = arg2
            arg2 = s

        if prec[el] < prec[parent] or (prec[el] == prec[parent] and ((prec[el] == 1 and side =="left") or (prec[el] == 2 and side =="right"))):
            val = "({} {} {})".format(arg1, el, arg2)
        else: val = "{} {} {}".format(arg1, el, arg2)

    elif el == "^":
        i[0] +=1
        arg = mostrar(exp, i, post, el)
        if arg == None: return None
        val = "{} {}".format(el, arg)
    
    elif el == "true": val = "true"
    elif el == "false": val = "false"

    else: return None


    return val

while True:

    command = input(">").strip().split(" ")
    l = len(command)

    if command[0] == "": continue

    if command[0] in ["EVAL", "MOSTRAR"]:

        if l == 1:
            print("Error: no fue provisto <orden>")
            continue
        if l == 2:
            print("Error: no fue provisto <expr>")
            continue
        

        if command[1] not in ["PRE", "POST"]:
            if l < 4:
                print("Error: valor no reconocido para <orden>: " + command[1])
                continue

        exp = command[2:]

        post = False
        if command[1] == "POST": 
            exp.reverse()
            post = True



        i = [0]
        if command[0] == "EVAL":
            evalBool(exp, i, post)
        else:
            res = mostrar(exp, i, post, None, None)

        if res == None or i[0] +1 != len(exp):
            print("Error: valor para exp invalido")
            continue

        print(res)



    elif command[0] == "SALIR": exit()
    else: print("comando invalido")
