[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)
# domtree 

[![GitHub issues](https://img.shields.io/github/issues/lossh/tpfinalpython.svg?style=plastic)](https://github.com/lossh/tpfinalpython/issues)
[![GitHub contributors](https://img.shields.io/github/contributors/lossh/tpfinalpython.svg?style=plastic)](https://github.com/lossh/tpfinalpython/graphs/contributors)
[![GitHub last commit](https://img.shields.io/github/last-commit/lossh/tpfinalpython.svg?style=plastic)](https://github.com/lossh/tpfinalpython/commits/master)
[![Codeship Status for lossh/tpfinalpython](https://app.codeship.com/projects/ffa22c30-7849-0137-fda4-6ae33c4945cb/status?branch=master)](https://app.codeship.com/projects/350185)
[![HitCount](http://hits.dwyl.io/lossh/tpfinalpython.svg?style=plastic)](http://hits.dwyl.io/lossh/tpfinalpython)[ [¿qué es esto?]](https://nitratine.net/blog/post/github-badges/)

## Introducción


## Dependencias

### Instalar las dependencias usando el [requirements.txt](https://medium.com/@boscacci/why-and-how-to-make-a-requirements-txt-f329c685181e)

`pip install -r requirements.txt`

## Clonar de github:
```console
git clone https://github.com/lossh/tpfinalpython
cd domtree
```
## Correr _domtree.py_ 
`python domtree.py`

### Opciones:
        -h, --help 
                Muestra éste texto de ayuda

        -c, --create <route/to/file.txt>
                Crea un arbol según la lista de dominios (por ejemplo 'www.qq.com')
                Sin esta opción busca el archivo 'Input.txt' en la carpera donde
                se encuentra el script.

        -q, --query <dominio> (por ejemplo www.qq.com)
                Busca que se encuentre el dominio en el arbol (ya sea este creado
                con el archivo por defecto o con la opción -c), responde si no lo 
                encuentra y también si lo hace total o parcialmente.

        -a, --add <dominio>
                Agrega el dominio al arbol (creado por defecto o con la opción -c)
                Los subdominios que ya estén no se repiten. 

        -d, --dict
                Genera un diccionario en forma de arbol y lo muestra en pantalla
                si se acompaña con la opción -p