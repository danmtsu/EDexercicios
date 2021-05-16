from listaencadeada.listaEncadeada import NodeList

l1 = NodeList()
l2 = NodeList()
l3 = NodeList()

l1.insere_elementos(3)
l1.insere_elementos(7)
l1.insere_elementos(9)
l1.insere_elementos(11)
l2.insere_elementos(18)
l2.insere_elementos(20)
l2.insere_elementos(21)
l2.insere_elementos(25)
l2.insere_elementos(27)
l3.insere_elementos(34)
l3.insere_elementos(35)
l3.insere_elementos(38)
l3.insere_elementos(42)
l3.insere_elementos(50)
l3.insere_elementos(51)

buscado = l1.buscaProExercicio(11,l2,l3)
print(buscado)