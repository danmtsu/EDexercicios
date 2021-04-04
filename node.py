class Node:
    def __init__(self, item,prioridade:int):
        self.item = item
        self.nxt = None
        self.bfr = None
        self.ind = int()
        self.prio = prioridade

    def __str__(self):
        return str(self.item)

