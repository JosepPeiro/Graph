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


    
g.Separate(ge)
print(g.Isolated())
for i in g.Isolated():
    print(i)
g.PrintAdjacencyMatrix()

print(g)
g.ReplaceWeigth(ga, ga, 12)
g.ReplaceWeigth(ga, gb, 20, 5)
g.ReplaceWeigth(gb, ga, 20)
print(g)
g.Disconnect(ga, gb)
g.Separate(gd)
g.Conect(ga, ge, 5)

for i in g.Isolated():
    print(i)

print(g)
g.ReplaceWeigth(ga, gb, 14)
g.ReplaceWeigth(gd, ge, 6)
g.Conect(ge,gd,11)
g.Conect(gb, gb,1, directed = False)
g.PrintAdjacencyMatrix(values = 1)
g.PrintIncidenceMatrix()

g.Complete(1)
g.PrintAdjacencyMatrix(values = 1)
g.PrintIncidenceMatrix()

j = Graph()
nn = 30
while nn <= 45:
    j.NewNode(nn, 99)
    nn += 1
j.PrintAdjacencyMatrix()
j.Complete(weigth=66666)
j.PrintAdjacencyMatrix(values = 1)
g.PrintAdjacencyMatrix(values = 1)

j.PrintAdjacencyMatrix(values = 0)
g.PrintAdjacencyMatrix(values = 0)

for i in j.AdjacentNodes(j.GetNodes()[0]):
    print(i)
    
g.Conect(ge, ge,2)
g.Separate(ge)
print(g)
for i in g.IncidentNodes(ga):
    print(i)
    
g.Conect(ge, ge,11)
#g.Conect(ge,ga,22)
g.Conect(ga, ge,4)
g.Disconnect(ga, gb)
print(g)
g.PrintAdjacencyMatrix()
print(g.Conex(ga))
#g.Separate(ga)
print(g.Conex(ge))
g.PrintAdjacencyMatrix()
g.Complete()
g.PrintAdjacencyMatrix()
print(g.Conex())
g.Separate(ga)
g.Conect(ge,ga,22)
print(g.Conex())
print(g.Conex(ge))

g.PrintIncidenceMatrix()
print(666,g.Conected(gb, ga))
print(g.Conected(ga,gb))
print(g.Conected(gb,gd))
g.Disconnect(gb, ge)
g.Disconnect(gd, ge)
g.PrintAdjacencyMatrix()
print(g.Conected(gb,ge))

print(ga,gb,ge)
i = 0
while i <= 2:
    ga - 5*i**2
    print(ga)
    gb + 2
    ge * 1.5
    i += 1
    -ga
print(ga,gb,ge)
