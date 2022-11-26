from GRAPH_CLASS import Graph


g = Graph()
ga = g.Node(1,3)
gb = g.Node(2,5)
gc = g.Node(3,9)
gd = g.Node(4,12)

g.Append(ga)
g.Append(gb)
g.Append(gc)
g.Append(gd)
g.NewNode(5, 6)

g.Conect(ga,ga,8)
g.Conect(gd, g.GetNodes()[g.Size() - 1])
g.Conect(ga, gb, 6)
g.Conect(ga, gb, 5)
g.Conect(gc, gb, 6)
ge = g.GetNodes()[g.Size() - 1]
g.Conect(gb, ge, 11, directed = False)
g.Conect(g.GetNodes()[g.Size() - 1], 
         g.GetNodes()[g.Size() - 1], 
         directed = False)
for i in [ga, gb, gc, gd]:
    g.Conect(gd, i, gd.value + i.value)
print(g)
print(g.AdjacencyMatrix(values = True))
print(g.AdjacencyMatrix())

g.PrintAdjacencyMatrix(values = True)
g.PrintAdjacencyMatrix()

for i in g.Loops():
    print(i)
for i in g.ValueLoops():
    print(i)
    
print(g.Adjacent(ga, gb))
print(g.Adjacent(gb, ga))
print(g.Adjacent(gb, ga, directed = False))

print(g)
g.PrintIncidenceMatrix()

g.PrintAdjacencyMatrix(values = True)
#print(g)
g.Undirected()
#print(g)
g.PrintAdjacencyMatrix(values = True)
#g.PrintAdjacencyMatrix(values = False)

print(g)
g.PrintAdjacencyMatrix()

g.Disconnect(ga, gd)
g.Disconnect(gd, gb)
g.Disconnect(gd, ge)
g.Disconnect(ge, gb)
g.Disconnect(ge, ge)
g.Disconnect(ge, gd)

for i in g.Isolated():
    print(i)
print(g)
g.Remove(gc)
print(g)
g.PrintAdjacencyMatrix()

g.Undirected()
g.PrintAdjacencyMatrix()

print(ga,gb,ge)
i = 0
while i <= 2:
    ga - 4
    gb + 2
    ge * 1.5
    i += 1
    
print(ga, gb, ge)