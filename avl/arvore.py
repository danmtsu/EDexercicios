from node import Node


class avltree(object):

    def __init__(self):
        "Construct."

        # raiz da árvore.
        self.node = None
        # altura da árvore.
        self.height = -1
        # fator de balanceamento.
        self.balance = 0

    def insert(self, key):#inserção de um elemento
        # criando um node novo
        n = Node(key)

        # arvore inicial
        if not self.node:
            self.node = n
            self.node.left = avltree()
            self.node.right = avltree()
        # insere a chave do lado esquerdo da subarvore
        elif key < self.node.key:
            self.node.left.insert(key)
        # Insere a chave do lado direito da subarvore
        elif key > self.node.key:
            self.node.right.insert(key)

        # balanceamento da arvore
        self.rebalance()

    def rebalance(self):
        """
        após alterar a quantidade de itens na arvore, rebalanceia nas regras da AVL
        """

        # verifica se é preciso rebalancear a arvore
        # atualiza a altura
        # balanceia a arvore
        self.update_heights(recursive=False)
        self.update_balances(False)

        # verificação de nós
        # se self.balance for -1,0,+1 não precisa de rotação.
        while self.balance < -1 or self.balance > 1:
            # subárvore da esquerda é maior q a da direita
            if self.balance > 1:

                # rotação para a esquerda
                if self.node.left.balance < 0:
                    #     x               x
                    #    / \             / \
                    #   y   D           z   D
                    #  / \        ->   / \
                    # A   z           y   C
                    #    / \         / \
                    #   B   C       A   B
                    self.node.left.rotate_left()
                    self.update_heights()
                    self.update_balances()

                #rotação para a direita
                #       x                 z
                #      / \              /   \
                #     z   D            y     x
                #    / \         ->   / \   / \
                #   y   C            A   B C   D
                #  / \
                # A   B
                self.rotate_right()
                self.update_heights()
                self.update_balances()

            # subárvore da direita sendo maior que a da esquerda
            if self.balance < -1:

                # rotação das subarvores para a direita
                if self.node.right.balance > 0:
                    #     y               y
                    #    / \             / \
                    #   A   x           A   z
                    #      / \    ->       / \
                    #     z   D           B   x
                    #    / \                 / \
                    #   B   C               C   D
                    self.node.right.rotate_right()
                    self.update_heights()
                    self.update_balances()

                # rotação para a esquerda
                #       y                 z
                #      / \              /   \
                #     A   z            y     x
                #        / \     ->   / \   / \
                #       B   x        A   B C   D
                #          / \
                #         C   D
                self.rotate_left()
                self.update_heights()
                self.update_balances()

    def update_heights(self, recursive=True):
        """
        atualiza a altura da arvore
        """
        if self.node:
            if recursive:
                if self.node.left:
                    self.node.left.update_heights()
                if self.node.right:
                    self.node.right.update_heights()

            self.height = 1 + max(self.node.left.height, self.node.right.height)
        else:
            self.height = -1

    def update_balances(self, recursive=True):
        """
        atualiza o fator de balanceamento da árvore

        """
        if self.node:
            if recursive:
                if self.node.left:
                    self.node.left.update_balances()
                if self.node.right:
                    self.node.right.update_balances()

            self.balance = self.node.left.height - self.node.right.height
        else:
            self.balance = 0

    def rotate_right(self):
        new_root = self.node.left.node
        new_left_sub = new_root.right.node
        old_root = self.node

        self.node = new_root
        old_root.left.node = new_left_sub
        new_root.right.node = old_root

    def rotate_left(self):
        new_root = self.node.right.node
        new_left_sub = new_root.left.node
        old_root = self.node

        self.node = new_root
        old_root.right.node = new_left_sub
        new_root.left.node = old_root

    def delete(self, key):
        """
        Delete key from the tree

        Let node X be the node with the value we need to delete,
        and let node Y be a node in the tree we need to find to take node X's place,
        and let node Z be the actual node we take out of the tree.

        Steps to consider when deleting a node in an AVL tree are the following:

            * If node X is a leaf or has only one child, skip to step 5. (node Z will be node X)
                * Otherwise, determine node Y by finding the largest node in node X's left sub tree
                    (in-order predecessor) or the smallest in its right sub tree (in-order successor).
                * Replace node X with node Y (remember, tree structure doesn't change here, only the values).
                    In this step, node X is essentially deleted when its internal values were overwritten with node Y's.
                * Choose node Z to be the old node Y.
            * Attach node Z's subtree to its parent (if it has a subtree). If node Z's parent is null,
                update root. (node Z is currently root)
            * Delete node Z.
            * Retrace the path back up the tree (starting with node Z's parent) to the root,
                adjusting the balance factors as needed.
        """
        if self.node != None:
            if self.node.key == key:
                # Key found in leaf node, just erase it
                if not self.node.left.node and not self.node.right.node:
                    self.node = None
                # Node has only one subtree (right), replace root with that one
                elif not self.node.left.node:
                    self.node = self.node.right.node
                # Node has only one subtree (left), replace root with that one
                elif not self.node.right.node:
                    self.node = self.node.left.node
                else:
                    # Find  successor as smallest node in right subtree or
                    #       predecessor as largest node in left subtree
                    successor = self.node.right.node
                    while successor and successor.left.node:
                        successor = successor.left.node

                    if successor:
                        self.node.key = successor.key

                        # Delete successor from the replaced node right subree
                        self.node.right.delete(successor.key)

            elif key < self.node.key:
                self.node.left.delete(key)

            elif key > self.node.key:
                self.node.right.delete(key)

            # Rebalance tree
            self.rebalance()

    def inorder_traverse(self):
        """
        Inorder traversal of the tree
            Left subree + root + Right subtree
        """
        result = []

        if not self.node:
            return result

        result.extend(self.node.left.inorder_traverse())
        result.append(self.node.key)
        result.extend(self.node.right.inorder_traverse())

        return result

    def display(self, node=None, level=0):
        if not node:
            node = self.node

        if node.right.node:
            self.display(node.right.node, level + 1)
            print('\t' * level, '    /')

        print('\t' * level,'  ', node)

        if node.left.node:
            print('\t' * level, '    \\')
            self.display(node.left.node, level + 1)


