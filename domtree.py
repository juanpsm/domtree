CREDITS = '''
    Juan Pablo Sanchez Magariños, UNLP
'''
from anytree import Node, RenderTree, find, AsciiStyle
import json, sys

DOC = sys.argv[0]+''' v0.1 escrito para Python 3.8.1
Opciones:
        -h, --help 
                Muestra éste texto de ayuda

        -c, --create <route/to/file.txt>
                Crea un arbol según la lista de dominios (por ejemplo 'www.qq.com')
                Sin esta opción busca el archivo 'Input.txt' en la carpera donde
                se encuentra el script. Imprime el arbol generado.

        -q, --query <dominio> (por ejemplo www.qq.com)
                Busca que se encuentre el dominio en el arbol (ya sea este creado
                con el archivo por defecto o con la opción -c), responde si no lo 
                encuentra y también si lo hace total o parcialmente.

        -a, --add <dominio>
                Agrega el dominio al arbol (creado por defecto o con la opción -c)
                Los subdominios que ya estén no se repiten. 

        -d, --dict
                Genera un diccionario en forma de arbol y lo muestra en pantalla.
'''
HELP = '-h' in sys.argv or '--help' in sys.argv
CREATE = '-c' if ('-c' in sys.argv) else ('--create' if '--create' in sys.argv else False)
DICT = '-d' in sys.argv or '--dict' in sys.argv
QUERY = '-q' if ('-q' in sys.argv) else ('--query' if '--query' in sys.argv else False)
ADD = '-a' if ('-a' in sys.argv) else ('--add' if '--add' in sys.argv else False)
OPCIONES = ('-h', '--help', '-c', '--create', '-d', '--dict', '-q', '--query', '-a', '--add')
TOOMANY = len(sys.argv) > 9
FILEIN ='Input.txt'
ROOT = '.'

def separarCadena(cadena):
    '''Cada cadena la divido por '.' (filtrando los blancos), y luego armo 
    una lista de listas con ellos, eliminando nuevamente los conjuntos vacíos'''
    return list(filter(None,cadena.split('.')))

def listarDominios(domfile):
    '''Desde un archivo de texto con un dominio en cada linea, se genera una lista de
    listas de las partes de cada dominio'''

    # Armar lista de dominios desde archivo, quitando los saltos de linea
    try:
        listaStrings = [line.rstrip('\n') for line in open(domfile)]
    except FileNotFoundError:
        if domfile != FILEIN:
            print(f"No existe el archivo especificado: {domfile}")
            exit(6)
        else:
            print(f"No se encuentra el archivo {FILEIN}")
            exit(7)
    
    # Remover strings vacíos
    while("" in listaStrings) :
        listaStrings.remove("")
    
    # Armo una lista de listas con ellos, eliminando nuevamente los conjuntos vacíos
    listaSeparada = list(filter(None, [separarCadena(dom) for dom in listaStrings]))

    return listaSeparada

def dictFromListOfLists(domList):
    '''Crear y devolver un diccionario en forma de árbol, desde una lista de listas'''
    tree = {}
    for item in domList: 
        currTree = tree # recordar que todo lo que haga en curr se hará en tree
        for key in item[::-1]: #recorre item en reverso
            if key not in currTree: 
                currTree[key] = {}
            currTree = currTree[key]
    return tree

def treeFromListOfLists(domList):
    '''Crear y devolver un arbol de anytree, desde una lista de listas'''
    tree = Node(ROOT)
    for item in domList: 
        currTree = tree
        for subitem in item[::-1]:
            if subitem not in list(map(lambda x: x.name, currTree.children)):
                child = Node(subitem)
                child.parent = currTree
            else:
                child = findChildren(currTree, subitem) 
            currTree = child
    return tree

def create(filename = FILEIN):
    '''Crear y devolver un arbol de anytree, desde un archivo especificado o 'Input.txt' por defecto'''
    domList = listarDominios(filename)
    domTree = treeFromListOfLists(domList)
    pprintTree(domTree)
    return domTree

def findChildren(tree, nombre):
    '''Devuelve, si existe, el Nodo de los hijos del arbol que tenga ese nombre'''
    hijos = list(map(lambda x: x.name, tree.children))
    if nombre in hijos:
        for child in hijos:
            candidato = tree.children[hijos.index(child)]
            if candidato.name == nombre:
                return candidato 

def pprintTree(tree):
    '''Forma más limpia de imprimir los arboles que print(RenderTree(tree)). Uso
    AsciiStyle ya que los otros levantan la excepción UnicodeEncodeError en
    algunos shell'''
    for pre, _ , node in RenderTree(tree, style=AsciiStyle()):
        print(f"{pre}{node.name}")

def query(tree,cadena):
    '''Buscar cierto dominio en el arbol. Retorna un diccionario con las claves
    'exito' que es true o false según si lo encontró o no.
    'ultimoCoincidente' el nodo del último pedazo de dominio que coincidio con 
    la búsqueda (la raiz del árbol si no encontró nada)'''

    cadenaSeparada = separarCadena(cadena)[::-1]
    resultado = {}
    print(f"\n Buscando '{cadena}' en el arbol...")
    largo = len(cadenaSeparada)
    # altura = tree.height # quito esto porque nos interesa recorrerlo igual para obtener el ultimoCoincidente
    # if largo > altura:
    #     print(f"No se encuentra (es muy larga)")
    #     return False
    currTree = tree
    porcentajeExito = 0
    for part in cadenaSeparada:
        if part in list(map(lambda nodo: nodo.name, currTree.children)):
            currTree = findChildren(currTree, part) 
            porcentajeExito += (1/largo)
            print(f" -> {currTree.name}", end='')
        else:
            print(f" -x-> {part}", end='')
            if porcentajeExito > 0:
                print(f"\n Casi ({round(porcentajeExito*100, 2)} %)... pero no se encuentra en el arbol")
            else:
                print(f"\n No se encuentra en el arbol")
            resultado["exito"] = False
            resultado["ultimoCoincidente"] = currTree
            return resultado
    print("\nEncontrado!")
    # assert porcentajeExito == 1
    resultado["exito"] = True
    resultado["ultimoCoincidente"] = currTree
    return resultado

def add(tree, dominio):
    '''Agrega los elementos del dominio que no estén en el árbol, retornando el arbol modificado'''
    print(f"\nAgregar'{dominio}' al arbol...")
    dominioSeparado = separarCadena(dominio)
    busqueda = query(tree, dominio)
    ultimo = busqueda["ultimoCoincidente"]
    # Saco de la lista los que ya estén en el árbol, a menos que lo haya enconrtado
    if ultimo.name != ROOT:
        dominioSeparado = dominioSeparado[:dominioSeparado.index(ultimo.name)]
    if len(dominioSeparado) > 0:
        # Si queda algo para agregar
        # Crear arbol con la lista de partes (dentro de otra lista), y tomamos el primer (y unico) hijo
        branch = treeFromListOfLists([dominioSeparado]).children[0]
        print("\nAgregaremos el siguiente arbol:")
        pprintTree(branch)
        print("\nResultado:")
        # Enlazar el nuevo arbol al ultimo que ya existe en el original
        branch.parent = ultimo
        pprintTree(tree)
    return tree

if __name__ == "__main__":
    if HELP:
        print(DOC)
        exit(0)
    elif TOOMANY:
        print("Demasiados argumentos, intenta con '--help'")
        exit(1)
    elif len(sys.argv)>1 and sys.argv[1] not in OPCIONES:
        print("No se reconoce esa opción, intenta con '--help'")
        exit(2)
    else:
        if CREATE:
            try:
                filename = sys.argv[sys.argv.index(CREATE)+1]
            except IndexError:
                print("Debes indicar el nombre o ruta del archivo (Ayuda '-h')")
                exit(3)
        else:
            filename = FILEIN
        
        if DICT:
            domList = listarDominios(filename)
            domDict = dictFromListOfLists(domList)
            # print("\ndomDict: ", domDict)
            print(json.dumps(domDict, indent=2))

        # Crear arbol
        domTree = create(filename)
        
        if ADD:
            try:
                dominio = sys.argv[sys.argv.index(ADD)+1]
            except IndexError:
                print(f"Debes indicar el dominio (Ayuda '-h')")
                exit(4)
            else:
                domTree = add(domTree, dominio)

        if QUERY:
            try:
                cadena = sys.argv[sys.argv.index(QUERY)+1]
            except IndexError:
                print(f"Debes indicar el dominio a buscar (Ayuda '-h')")
                exit(5)
            query(domTree, cadena)