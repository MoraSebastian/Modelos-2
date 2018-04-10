#Definición árbol n-ario
class Nario:
    def __init__(self,valor,hijos=[]):
        self.valor = valor
        self.hijos = hijos

nodo= Nario(25,[Nario(22),Nario(89)])
#25
#10 100
#

def buscar_hijos(lista,valor):
    if lista == []:
        return False
    return (buscar(lista[0],valor) or buscar_hijos(lista[1:],valor))
        
def buscar(arbol,valor):
    if arbol.valor == valor:
        return True
    else:
        return buscar_hijos(arbol.hijos,valor)

##print(buscar(nodo,89))
"""
1 1 1 1 1 1 1
1 0 0 0 1 0 1
1 1 x 0 0 0 1
1 1 1 1 0 0 1
1 y 0 0 0 0 1
1 1 1 1 1 1 1
"""
def sumaPuntos(lista1,lista2):
    print (lista1 ,"  ")
    print (lista2 ,"\n")
    if len(lista2)>len(lista1):
        return sumaPuntos(lista2,lista1)
    if lista2==[]:
        return lista1
    return lista1[0]+lista2[0] + sumaPuntos(lista1[1:],lista2[1:])
def separar_lista(lista):
    if lista==[]:
        return []
    return [lista[0].split(" ")]+separar_lista(lista[1:])

def generarMap():
    return separar_lista([y.strip("\n") for y in open("hello.txt", "r").readlines()])


def mostrarCoordenada(mapa,coordenada):
    return mapa [coordenada[0]][coordenada[1]]

def buscarY(mapa):
    print(mapa)
      
    if mapa[0][0]=='y':
        print("Se encontro")
        return [0,0]
    if len(mapa[0])==1:
        print("Se quita fila")
        return sumarCoordenada(sumarCoordenada([1,0],buscarY(mapa[1:]) ),[0,-(len(mapa[1])-1)])
    if mapa[0]!=[] :
        print("Se corta elemento de fila")
        return  sumarCoordenada ([0,1],buscarY([mapa[0][1:]]+mapa[1:]))    
    else:
        return [0,0]
    
def sumarCoordenada(coor1,coor2):
    return [coor1[0]+coor2[0],coor1[1]+coor2[1]]

def armarNario(cabeza,mapa):
    if mapa[cabeza[0]][cabeza[1]]=='1' or buscar(:
        return None
    return Nario(cabeza,[armarNario(sumarCoordenada(cabeza,[0,1]),mapa)]   

def modificarCoor(coor,mapa):
    if coor

























                 
mapa=generarMap()
print(mapa)
print(mostrarCoordenada(mapa,[2,2]))
print(buscarY(mapa))
##print(posX(mapa))
##print(sumarCoordenada([1,0],[0,1]))
