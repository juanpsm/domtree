[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)
# domtree 
[![Run on Repl.it](https://repl.it/badge/github/pibytes/domtree)](https://repl.it/github/pibytes/domtree)
[![GitHub issues](https://img.shields.io/github/issues/pibytes/domtree?style=plastic)](https://github.com/pibytes/domtree/issues)
[![GitHub contributors](https://img.shields.io/github/contributors/pibytes/domtree.svg?style=plastic)](https://github.com/pibytes/domtree/graphs/contributors)
[![GitHub last commit](https://img.shields.io/github/last-commit/pibytes/domtree.svg?style=plastic)](https://github.com/pibytes/domtree/commits/master)
[![Codeship Status for pibytes/domtree](https://app.codeship.com/projects/049ce370-de97-0138-495c-02045832bc80/status?branch=master)](https://app.codeship.com/projects/409630)
[![HitCount](http://hits.dwyl.com/pibytes/domtree.svg)](http://hits.dwyl.com/pibytes/domtree)
## Introducción
Desafío propuesto por la cátedra de Redes y Comunicaciones de la Facultad de Informática de la Universidad Nacional de La Plata
### Desafío
Hacer un programa que lea un archivo que contiene n dominios; uno por linea.
Consideramos que hay un "." (root) siempre, deben armar el árbol que
representa ese conjunto de datos.
Ejecutando ese código podremos ayudar a comprender mejor el DNS y lo
usaremos como materia de apoyo en la materia!

Ejemplo: `Input.txt`
```
www.unlp.edu.ar
www.info.unlp.edu.ar
www.uba.ar
nic.ar
www. motorola.com
pypi.org
stackoverflow.com
```
### Operaciones a implementar:
- **create:** Permite crear un árbol a partir de una lista de dominios contenidos en
un archivo.
- **query:** Permite consultar si un dominio si existe buscando en el árbol.
- **add:** Permite agregar un nodo.
### Premisas:
- Los nodos solo tienen los ID de sus hijos y no tiene información de sus
padres!!
- Pueden usar cualquier lenguaje, pero sin usar un cañón para matar
hormigas!!

## Dependencias

### Instalar las dependencias usando el [requirements.txt](https://medium.com/@boscacci/why-and-how-to-make-a-requirements-txt-f329c685181e)

`pip install -r requirements.txt`

## Clonar de github:
```console
git clone https://github.com/pibytes/domtree
cd domtree
```
## Correr _domtree.py_ 
`python domtree.py [OPCIONES]`

### Opciones:
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
                Genera un diccionario en forma de arbol y lo muestra en pantalla
## _test.py_
En este archivo se pueden ver algunos ejemplos del uso de las funciones más importantes
```python
from domtree import create, query, add, pprintTree

tree = create()

query(tree, "www.unlp.edu.ar")

add(tree, 'w.w.w.w.w')

# tree = create("test-data/opendns-top-domains.txt")
```
## _test-data_
distintos archivos para probar
