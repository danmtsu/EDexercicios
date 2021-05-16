from listaencadeada.node import Node

class NodeList:
    def __init__(self):
        self.__first = None
        self.__last = None

    @property
    def first(self):
        return self.__first

    @first.setter
    def first(self,newfirst:Node):
        newfirst.nxt_node = self.__first
        self.__first = newfirst

    @property
    def last(self):
        return self.__last

    @last.setter
    def last(self,newlast):
        self.__last = newlast

    def insere_elementos(self,elemento:int):
        if self.__first == None:
            self.__first = Node(elemento)
            self.__last = Node(elemento)
        elif self.__first.nxt_node == None:
            newNode = Node(elemento)
            self.__first.nxt_node = newNode
            self.__last = newNode
        else:
            newNode = Node(elemento)
            self.__last.nxt_node = newNode
            self.__last = newNode

    def junta_lista(self,other_list): #juntando uma lista com a posterior, assim criando uma apenas para a busca acho que o certo talvez fosse criar uma nova lista para não alterar nenhuma delas
        self.__last.nxt_node = other_list.first
        self.__last = other_list.last

    def buscaProExercicio(self,indice:int,list,list2): #algoritmo de busca, mas sem criar uma nova lista(o que provavelmente não está 100% certo)
        self.junta_lista(list)
        self.junta_lista(list2)
        buscado = self.__first
        for i in range(1,indice):
            buscado = buscado.nxt_node
        return str(buscado.node)
