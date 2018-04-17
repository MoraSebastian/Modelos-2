#Definición árbol n-ario
class Nario:
    def __init__(self,valor,hijos=[]):
        self.valor = valor
        self.hijos = hijos

nodo= Nario(25,[Nario(22,[Nario(13),Nario(17)]),Nario(89)])
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


def imp_hijos(lista):
    if lista == []:
        return []
    return [imp(lista[0])+imp_hijos(lista[1:])]        
def imp(arbol):
    return [arbol.valor]+["h"]+imp_hijos(arbol.hijos)
##print(buscar(nodo,89))
"""
1 1 1 1 1 1 1
1 0 0 0 1 0 1
1 1 x 0 0 0 1
1 1 1 1 0 0 1
1 y 0 0 0 0 1
1 1 1 1 1 1 1
"""
def impBakcTracking(arbol):
    if len(arbol.hijos)==0:
        return [[arbol.valor]]
    if len(arbol.hijos)==1:
        return [[arbol.valor]+impBakcTracking(arbol.hijos[0])]
    if len(arbol.hijos)>1:
        return [[arbol.valor]+impBakcTracking(arbol.hijos[0])]+ impBakcTracking(Nario(arbol.valor,arbol.hijos[1:]))
def sumaPuntos(lista1,lista2):
    ##print (lista1 ,"  ")
    ##print (lista2 ,"\n")
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
      
    if mapa[0][0]=='y':
        return [0,0]
    if len(mapa[0])==1:

        return sumarCoordenada(sumarCoordenada([1,0],buscarY(mapa[1:]) ),[0,-(len(mapa[1])-1)])
    if mapa[0]!=[] :

        return  sumarCoordenada ([0,1],buscarY([mapa[0][1:]]+mapa[1:]))    
    else:
        return [0,0]
    
def sumarCoordenada(coor1,coor2):
    return [coor1[0]+coor2[0],coor1[1]+coor2[1]]

def armarNario(cabeza,mapa):
    
    if mapa[cabeza[0]][cabeza[1]]=='1' or mapa[cabeza[0]][cabeza[1]]=='x':
        
        return Nario(cabeza,[])
    
    return Nario(cabeza,[armarNario(sumarCoordenada(cabeza,[1,0]),modificarCoor(mapa, cabeza)),armarNario(sumarCoordenada(cabeza,[0,1]),modificarCoor(mapa, cabeza))])  

def modificarCoor(mapa, coor):
  
    if coor[0]==0 and coor[1]==0:
        return [[1]+mapa[0][1:]]+mapa[1:]
    if coor[0]!=0:
        return [mapa[0]] + modificarCoor(mapa[1:],sumarCoordenada(coor, [-1,0]))
    return [[mapa[0][0]]+modificarCoor([mapa[0][1:]], sumarCoordenada(coor, [0,-1]))[0]] + mapa[1:]

def imprimirArbol(arbol):
    if len(arbol.hijos):
        [arbol.valor]+imprimirArbol()
    else:
        return [arbol.valor]

    print (arbol[0].valor,"[")
    if(len(arbol[0].hijos)!=0):
        imprimirArbol (arbol[0].hijos)
    if len(arbol)>1:
        imprimirArbol(arbol[1:])
    
    
        
mapa=generarMap()
##print(mapa)
##print(mostrarCoordenada(mapa,[2,2]))
##print(buscarY(mapa))
##print(modificarCoor( mapa,[4,4-3]))
##imprimirArbol([armarNario(buscarY(mapa), mapa)])
##print(imp(armarNario(buscarY(mapa), mapa)))
print (impBakcTracking(nodo))
##print(posX(mapa))
##print(sumarCoordenada([1,0],[0,1]))
