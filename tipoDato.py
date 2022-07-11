
from itertools import permutations
from math import inf

class DataType(object):
    def __init__(self, name, size, align):
        self.name = name
        self.size = size
        self.align = align


    def __repr__(self):
        return "nombre: {}\ntamaño:{}\nalineacion:{}".format(self.name,self.size,self.align)

    def __str__(self):
        return "nombre: {}\ntamaño:{}\nalineacion:{}".format(self.name,self.size,self.align)

class Struct(DataType):
    def __init__(self, name, types):
        self.types = types
        size = sum([t.size for t in types])
        align = types[0].align

        DataType.__init__(self, name, size, align)

        self.calcWaste()


    def calcWaste(self):
        unpackedSize = self.calcSize(self.types)
        self.unpackedWaste = unpackedSize - self.size

        minSize = inf
        for p in list(permutations(self.types)):
            size = self.calcSize(p)
            if size < minSize: minSize = size
        self.minWaste = minSize - self.size


    def calcSize(self, types):
        i = 0
        for t in types:
            m = i % t.align
            if m != 0: i += t.align - m
            i += t.size
        return i

    def __repr__(self):
        return "nombre: {}\ndefinicion: struct {}\ntamaño:{}\nalineacion:{}\ndesperdicio sin empaquetar: {}\ndesperdicio reordenacion optima: {}".format(self.name, " ".join([t.name for t in self.types]), self.size,self.align, self.unpackedWaste, self.minWaste)

    def __str__(self):
        return "nombre: {}\ndefinicion: struct {}\ntamaño:{}\nalineacion:{}\ndesperdicio sin empaquetar: {}\ndesperdicio reordenacion optima: {}".format(self.name, " ".join([t.name for t in self.types]), self.size,self.align, self.unpackedWaste, self.minWaste)

class Union(DataType):
    def __init__(self, name, types):
        self.types = types
        size = 10
        align = 10
        DataType.__init__(self, name, size, align)

    def calcWaste(self):
        unpackedSize = self.calcSize(self.types)
        self.unpackedWaste = unpackedSize - self.size

        minSize = inf
        for p in list(permutations(self.types)):
            size = self.calcSize(p)
            if size < minSize: minSize = size
        self.minWaste = minSize - self.size


    def calcSize(self, types):
        i = 0
        for t in types:
            m = i % t.align
            if m != 0: i += t.align - m
            i += t.size
        return i

    def __repr__(self):
        return "nombre: {}\ndefinicion: struct {}\ntamaño:{}\nalineacion:{}\ndesperdicio sin empaquetar: {}\ndesperdicio reordenacion optima: {}".format(self.name, " ".join([t.name for t in self.types]), self.size,self.align, self.unpackedWaste, self.minWaste)

    def __str__(self):
        return "nombre: {}\ndefinicion: struct {}\ntamaño:{}\nalineacion:{}\ndesperdicio sin empaquetar: {}\ndesperdicio reordenacion optima: {}".format(self.name, " ".join([t.name for t in self.types]), self.size,self.align, self.unpackedWaste, self.minWaste)


class DataTypeSystem(object):

    dataTypes = {}

    def newAtom(self,name, size, align):
        try: 
            self.dataTypes[name]
            return False
        except:
            self.dataTypes[name] = DataType(name, size, align)
            return True

    def newComposite(self, name, typeNames, dataType):
        try: 
            self.dataTypes[name]
            return False
        except:
            types = []
            for t in typeNames:
                try:types.append(self.dataTypes[t])
                except: return t
            self.dataTypes[name] = dataType(name, types)
            return True

    def describe(self, name):
        try: 
            t = self.dataTypes[name]
        except:
            return False

        print(t)

        return True

dts = DataTypeSystem()
while True:

    command = input(">").strip().split(" ")
    l = len(command)

    if command[0] == "": continue

    if command[0] == "ATOMICO":

        if l == 1:
            print("Error: no fue provisto <nombre>")
            continue
        if l == 2:
            print("Error: no fue provisto <representacion>")
            continue
        if l == 3:
            print("Error: no fue provisto <alineacion>")
            continue
        
        if not command[2].isnumeric():
            print("Error: dato invalido para <representacion>")
            continue

        if not command[3].isnumeric():
            print("Error: dato invalido para <alineacion>")
            continue

        if not dts.newAtom(command[1], int(command[2]), int(command[3])):
            print("ya existe tipo " + command[1])

    elif command[0] in ["STRUCT", "UNION"]:

        if l == 1:
            print("Error: no fue provisto <nombre>")
            continue
        if l == 2:
            print("Error: no fue provisto [<tipo>]")
            continue
        
        dataType = Struct
        if command[0] == "UNION":
            dataType = Union

        res = dts.newComposite(command[1], command[2:], dataType)
        if res == False:
            print("ya existe tipo " + command[1])
        elif res != True:
            print("tipo " + res + " no encontrado")

    
    elif command[0] == "DESCRIBIR":

        if l == 1:
            print("Error: no fue provisto <nombre>")
            continue
        if l != 2:
            print("Error: argumento no valido " + command[2])
            continue
        
        if not dts.describe(command[1]):
            print("tipo " + res + " no encontrado")



    elif command[0] == "SALIR": exit()
    else: print("comando invalido")