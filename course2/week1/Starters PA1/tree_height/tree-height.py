# python3

import sys, threading
sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**25)  # new thread will get stack of such size

class TreeHeight:
        def read(self):
                self.n = int(sys.stdin.readline())
                self.parent = list(map(int, sys.stdin.readline().split()))

        def fill_depth(self, i, depth):
                if depth[i] != 0:
                    return

                if self.parent[i] == -1:
                    depth[i] = 1
                    return

                if depth[self.parent[i]] == 0:
                    self.fill_depth(self.parent[i], depth)

                depth[i] = depth[self.parent[i]] + 1

        def compute_height(self):
                depth = [0 for i in range(self.n)]

                for i in range(self.n):
                    self.fill_depth(i, depth)

                ht = depth[0]
                for i in range(1, self.n):
                    ht = max(ht, depth[i])

                return ht

        

def main():
  tree = TreeHeight()
  tree.read()
  print(tree.compute_height())

threading.Thread(target=main).start()
