from node import Node

class Fila:
    def __init__(self):
        self.start_list = None
        self.tamanho = 0


    def entrarNaFila(self,data,prioridade):
        if self.start_list is None:
            new_node = Node(data,prioridade)
            self.start_list = new_node
            new_node.ind = 0
            self.tamanho += 1
            return
        else:
            n = self.start_list
            new_code = Node(data,prioridade)
            while n.nxt is not None:
                if n.prio > prioridade:
                    if n.bfr is None:
                        n.bfr = new_code
                        new_code.nxt = n
                        self.start_list = new_code
                    else:
                        n.bfr.nxt = new_code
                        new_code.bfr = n.bfr
                        new_code.nxt = n
                        n.bfr = new_code
                elif n.nxt.prio > prioridade:
                    n.nxt.bfr = new_code
                    new_code.nxt = n.nxt
                    n.nxt = new_code
                    new_code.bfr = n
                return
            if n.nxt is None:
                if n.prio > prioridade:
                    new_code.nxt = n
                    n.bfr = new_code
                    self.start_list = new_code
                    return
                else:
                    n.nxt = new_code
                    new_code.bfr = n
                    return


    def delete_start(self):
        if self.start_list is None:
            print('list is empty')
        else:
            if self.start_list.nxt is None:
                self.start_list = None
                self.tamanho -= 1
                return

            else:
                self.start_list = self.start_list.nxt
                self.start_list.bfr = None
                self.tamanho -= 1
                n = self.start_list
                while n is not None:
                    n.ind -= 1
                    n = n.nxt
                return

    def __str__(self):
        n = self.start_list
        list = str(n)
        while n.nxt is not None:
            list += "," + str(n.nxt)
            n = n.nxt
        return list

d = Fila()
d.entrarNaFila(5,3)
d.entrarNaFila(4,1)
d.entrarNaFila(3,2)
d.entrarNaFila(7,1)
d.delete_start()

print(d)


''' new_node = Node(data,prioridade)
 new_node.bfr = n
 new_node.nxt = n.nxt
 new_node.ind = n.ind +1
 if n.nxt is not None:
     n.nxt.prev = new_node
 n.next = new_node
 self.tamanho +=1'''