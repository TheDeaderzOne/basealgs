import math 

class UnionFind:
    
    def __init__(self, nodenumber):
        self.parents = [int(x) for x in range(nodenumber)]
        self.sizes = [1] * len(self.parents)
        
    def UFFind(self,node):
        if node == self.parents[node]:
            return node
        self.parents[node]= self.UFFind(self.parents[node])
        return self.parents[node]

    def UFJoin(self,node1,node2):
        if self.parents[node1]!=self.parents[node2]: 
            parenta = self.UFFind(node1); parentb = self.UFFind(node2)
            # lol stop recalculating lmao 
            if self.sizes[parenta] > self.sizes[parentb]:
                self.sizes[parenta]+=self.sizes[parentb]
                self.parents[parentb]=parenta
            else:
                self.sizes[parentb] += self.sizes[parenta]
                self.parents[parenta]=parentb
                
    def UFDistinct(self,node1,node2):
        if self.UFFind(node1)==self.UFFind(node2):
            return False
        return True

# Kruskal's???

edges = [(0,1,3),(1,2,5),(2,3,9),(3,5,7),(0,4,5),(4,5,2),(1,4,6),(2,5,3)]
edges2 = [(0,1,4), (1,2,1), (2,3,2), (3,4,3), (0,4,6), (1,4,5), (2,4,7), (0,2,8)]
edges3 = [(0,1,2), (1,2,3), (2,3,1), (0,2,4), (0,3,5), (1,3,6)]
edges4 = [(4,5,2), (0,1,3), (3,5,3), (1,2,4), (5,6,4), (1,6,5), (3,4,5), (2,3,6), (2,5,6), 
          (0,2,7), (4,6,7), (1,3,8), (3,6,8), (2,4,9), (0,5,10)]
edges5 = [(0,1,1), (1,2,2), (2,3,3), (3,4,2), (4,5,1), (0,2,4), (1,3,5), (2,4,6), (3,5,4), (0,4,7),
(1,5,8), (2,5,9), (0,3,10), (1,4,3)]

def Kruskals(edgearr, vertexnum): 
    MSTlength = 0
    mst = UnionFind(vertexnum)
    edgearr.sort(key=lambda x:x[2])
    print(mst.parents, mst.sizes)
    # main algorithm start
    for x in edgearr: 
        if mst.UFDistinct(x[0],x[1]):
            MSTlength += x[2]
            mst.UFJoin(x[0],x[1])
    # main algorithm end
    print(mst.parents, mst.sizes)
    return MSTlength
    
print(Kruskals(edges, 6)) # 20
print(Kruskals(edges2, 5)) # 10
print(Kruskals(edges3, 4)) # 6 
print(Kruskals(edges4, 7)) # 21
print(Kruskals(edges5, 6)) # 9