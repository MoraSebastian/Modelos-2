

#Definición árbol n-ario
class Nario:
    def __init__(self,valor,hijos=[]):
        self.valor = valor
        self.hijos = hijos

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

def sumaPuntos(lista1,lista2):
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
    if mapa[cabeza[0]][cabeza[1]]=='1' or mapa[cabeza[0]][cabeza[1]]=='3'  :
        return Nario(cabeza,[])
        
    if mapa[cabeza[0]][cabeza[1]]=='x':
        print(impMap(mapa))
        return Nario(cabeza,[])

    return Nario(cabeza,[armarNario(sumarCoordenada(cabeza,[0,1]),modificarCoor(mapa, cabeza)),armarNario(sumarCoordenada(cabeza,[1,0]),modificarCoor(mapa, cabeza)) ,armarNario(sumarCoordenada(cabeza,[0,-1]),modificarCoor(mapa, cabeza)),armarNario(sumarCoordenada(cabeza,[-1,0]),modificarCoor(mapa, cabeza))  ])
    
def modificarCoor(mapa, coor):
    if coor[0]==0 and coor[1]==0:
        return [['3']+mapa[0][1:]]+mapa[1:]
    if coor[0]!=0:
        return [mapa[0]] + modificarCoor(mapa[1:],sumarCoordenada(coor, [-1,0]))
    return [[mapa[0][0]]+modificarCoor([mapa[0][1:]], sumarCoordenada(coor, [0,-1]))[0]] + mapa[1:]


    

def impMap(mapa):
   
    if(len(mapa)==0):
        return " "
    if(len(mapa[0])==0):
        return "\n"+impMap(mapa[1:])
    return mapa[0][0]+" "+impMap([(mapa[0])[1:]]+mapa[1:]) 


def impArbol(arbol):
    
    if(arbol.hijos==[]):
        return [[arbol.valor]]
    if len(arbol.hijos)==1:
        return conbinacion(arbol.valor,impArbol(arbol.hijos[0]))
        
    return conbinacion(arbol.valor,impArbol(arbol.hijos[0])) +impArbol (Nario(arbol.valor,arbol.hijos[1:]))

def conbinacion(valor, hijos):
    if len(hijos)==0:
        return [[]]
    if len(hijos)==1:
        return [[valor]+hijos[0]]
    return [[valor]+hijos[0]]+conbinacion(valor,hijos[1:])

def limpiar(lista):
    if len(lista)==0:
        return []
    if len(lista[0])==0:
        return limpiar(lista[1:])
    if ultimoVal(lista[0]):
        return [lista[0]]+limpiar(limpiar(lista[1:]))



def eliminarCaminos(lista,mapa):
 
    if lista==[]:
        return []
    if mapa[lista[0][len(lista[0])-1][0]][lista[0][len(lista[0])-1][1]]=='x':
        return [lista[0]]+eliminarCaminos(lista[1:],mapa)
    else:
        return eliminarCaminos(lista[1:],mapa)
    

print(eliminarCaminos(impArbol(armarNario(buscarY(generarMap()), generarMap())),generarMap()))
