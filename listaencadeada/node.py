class Node:
    def __init__(self,node):
        self.__node = node
        self.__nxt_node = None

    @property
    def node(self):
        return self.__node

    @node.setter
    def node(self,newNode):
        self.__node = newNode

    @property
    def nxt_node(self):
        return self.__nxt_node

    @nxt_node.setter
    def nxt_node(self,new_next):
        self.__nxt_node = new_next
