from domtree import create, query, add, pprintTree

tree = create()

query(tree, "www.unlp.edu.ar")

add(tree, 'w.w.w.w.w')

tree = create("test-data/opendns-top-domains.txt")