class Graph:
    
    class Node:
        def __init__(self, 
                     uid = None, 
                     value = None, 
                     prior = None):
            self.uid = uid
            self.value = value
            self.priority = prior
            
        def __str__(self):
            s = ""
            s += "ID: " + str(self.uid) + "\n"
            s += "Value: " + str(self.value) + "\n"
            if self.priority != None:
                s += "Priority: " + str(self.priority) + "\n"
            
            return s
        
        
        def __add__(self, y):
            self.value += y
            
        def __sub__(self, y):
            self.value -= y
            
        def __mul__(self, y):
            self.value *= y
            
        def __neg__(self):
            self.value *= -1
            
            
    class Edge:
        def __init__(self, 
                     source = None,
                     dest = None,
                     weigth = 0):
            self.source = source #uid
            self.dest = dest #uid
            self.weigth = weigth
            
        def __str__(self):
            s = str(self.source) + " -- " + str(self.weigth) + " -> " + str(self.dest)
            return s
            
    
    def __init__(self):
        self.__nodes = [] # Node
        self.__edges = {} # Node:[Edge]
        
        self.__conexions = {} #Node:set(uid)
        self.__uids = {} #uid:Node
        
        
    def GetNodes(self):
        """Return the list of nodes"""
        return self.__nodes
    
    def GetEdges(self):
        """Return the list of edges"""
        return self.__edges
    
    def GetNodeUID(self, nuid) -> Node:
        """Return the node that correspond to that uid"""
        return self.__uids[nuid]
    
    def Size(self):
        """Return the quantity of nodes in the graph"""
        return len(self.__nodes)
    
    
    def NewNode(self, uid, value, prior = None):
        """
        Make a new node and automatically appends it
        to the graph

        Parameters
        ----------
        uid : TYPE
            The id of the new node.
        value : TYPE
            The value of the new node.
        prior : TYPE, optional
            The priority of the new node. 
            The default is None.
        """
        new = Graph.Node(uid, value, prior)
        self.__nodes.append(new)
        self.__edges[new] = []
        self.__conexions[new] = set()
        self.__uids[uid] = new
        
        
    def Append(self, nod:Node):
        """
        Appends a node to the graph

        Parameters
        ----------
        nod : Node
            A node already created.
        """
        self.__nodes.append(nod)
        self.__edges[nod] = []
        self.__conexions[nod] = set()
        self.__uids[nod.uid] = nod
        
    
    def Remove(self, nod:Node):
        """
        Remove the node from the graph and 
        automatically destroy every conection with
        this graph

        Parameters
        ----------
        nod : Node
            The node we want to destroy.
        """
        if nod in self.__nodes:
            self.__nodes.remove(nod)
            del self.__edges[nod]
            del self.__conexions[nod]
            del self.__uids[nod.uid]
            
        for i in self.__nodes:
            if nod.uid in self.__conexions[i]:
                self.__conexions[i].remove(nod.uid)
                j = 0
                while j < len(self.__edges[i]):
                    if self.__edges[i][j].dest == nod.uid:
                        self.__edges[i].pop(j)
                        j -= 1
                    
                    j += 1
                
        
    def ReplaceWeigth(self, fr_node:Node, to_node:Node, 
                      new_weigth = 0, old_weigth = None):
        """
        Create a bow between two nodes, and if it 
        already exist, change its weigth

        Parameters
        ----------
        fr_node : Node
            The node where the bow start.
        to_node : Node
            The node where the bow is addresed.
        new_weigth : TYPE, optional
            The new weigth, that will replace the 
            weigth of the bow.
            The default is 0.
        old_weigth : TYPE, optional
            If it's used, search the bow that connect 
            the two nodes and has this weigth, 
            in order to change this weigth. 
            The default is None.
        """
        if old_weigth == None:
            if to_node.uid in self.__conexions[fr_node]:
                changed = False
                i = 0
                while not changed:
                    if self.__edges[fr_node][i].dest == to_node.uid:
                        self.__edges[fr_node][i].weigth = new_weigth
                        changed = True
                    i+=1
            else:
                new_con = Graph.Edge(fr_node.uid, to_node.uid, new_weigth)
                self.__edges[fr_node].append(new_con)
                self.__conexions[fr_node].add(to_node.uid)
                
        else:
            for n in self.__edges[fr_node]:
                if n.dest == to_node.uid and n.weigth == old_weigth:
                    n.weigth = new_weigth
            
            
    def Conect(self, fr_node:Node, to_node:Node, weigth = 0, directed = True):
        """
        Conect a bow between two nodes

        Parameters
        ----------
        fr_node : Node
            The node where the bow starts.
        to_node : Node
            The node where the bow ends.
        weigth : TYPE, optional
            The weigth of the bow. 
            The default is 0.
        directed : bool, optional
            If the bow is directed or not.
            If it's not directed, it creates two bows
            with the same weigth in both directions
            The default is True.
        """
        new_con = Graph.Edge(fr_node.uid, to_node.uid, weigth)
        self.__edges[fr_node].append(new_con)
        self.__conexions[fr_node].add(to_node.uid)
            
        if not directed and to_node != fr_node:
            con_new = Graph.Edge(to_node.uid, fr_node.uid, weigth)
            self.__edges[to_node].append(con_new)
            self.__conexions[to_node].add(fr_node.uid)
            
            
    def Disconnect(self, fr_node:Node, to_node:Node, weigth = None):
        """
        Destroys all bows between 2 nodes

        Parameters
        ----------
        fr_node : Node
            The node where the bow starts.
        to_node : Node
            The node where the bow ends.
        weigth : TYPE, optional
            The weight of the bow. If we want to specify 
            a bow by it's weigth
            The default is None.
        """
        if weigth == None:
            if to_node.uid in self.__conexions[fr_node]:
                self.__conexions[fr_node].remove(to_node.uid)
                
                i = 0
                while i < len(self.__edges[fr_node]):
                    if self.__edges[fr_node][i].dest == to_node.uid:
                        self.__edges[fr_node].pop(i)
                        
                        i -= 1
                    
                    i += 1
                    
                    
        else:
            if to_node.uid in self.__conexions[fr_node]:
                
                i = 0
                while i < len(self.__edges[fr_node]):
                    if self.__edges[fr_node][i].dest == to_node.uid and \
                        self.__edges[fr_node][i].weigth == weigth:
                        self.__edges[fr_node].pop(i)
                        self.__conexions[fr_node].remove(to_node.uid)
                        i -= 1
                    
                    i += 1
                    
                    
    def Isolated(self):
        """
        Return the nodes that have no conexion with
        the rest of the nodes
        """
        
        isol = []
        for node in self.__nodes:
            if len(self.__conexions[node]) == 0:
                likely = True
                n = 0
                while n < len(self.__nodes) and likely:
                    nnode = self.__nodes[n]
                    if node.uid in self.__conexions[nnode]:
                        likely = False
                    n += 1
                        
                if likely:
                    isol.append(node)
                
        return isol
    
    
    def Separate(self, nod:Node):
        """
        Destroys all kinds of conexions with
        one node
        """
        self.__edges[nod] = []
        self.__conexions[nod] = set()
        
        for i in self.__nodes:
            if nod.uid in self.__conexions[i]:
                self.__conexions[i].remove(nod.uid)
                j = 0
                while j < len(self.__edges[i]):
                    if self.__edges[i][j].dest == nod.uid:
                        self.__edges[i].pop(j)
                        j -= 1
                    
                    j += 1
                    

    def Loops(self) -> list:
        """
        Return all nodes that have at least one loop,
        namely, that has a bow that reference himself
        """
        loop = []
        for node in self.__conexions.keys():
            if node.uid in self.__conexions[node]:
                loop.append(node)
                
        return loop
    
    
    def ValueLoops(self) -> list:
        """
        Return the loops (the edges that starts at the 
        same point as ends
        """
        loop = []
        for node in self.__edges.keys():
            if node.uid in self.__conexions[node]:
                for edge in self.__edges[node]:
                    if edge.source == edge.dest:
                        loop.append(edge)
                
        return loop
    
    
    def Adjacent(self, a:Node, b:Node, directed = True) -> bool:
        """
        Return if two nodes are adjacents or not.
        If there is a bow that conect both

        Parameters
        ----------
        fr_node : Node
            The node where the bow starts.
        to_node : Node
            The node where the bow ends.
        directed : bool, optional
            If we consider one or both directions 
            in order to say that two nodes are adjacents. 
            The default is True.

        Returns
        -------
        bool
            If the nodes are or not adjacents.

        """
        if b.uid in self.__conexions[a]:return True
        if not directed:
            if a.uid in self.__conexions[b]:return True            
            
        return False
    
    
    def Incident(self, a:Node, b:Node, directed = True) -> bool:
        """
        The same function as Adjacent but in the other 
        direction
        If directed is True, i has exactly the same 
        function
        """
        if a.uid in self.__conexions[b]:return True
        if not directed:
            if b.uid in self.__conexions[a]:return True            
            
        return False
    
    
    def PrintAdjacencyMatrix(self, values = False):
        """
        Prints the Adjacency Matrix of the graph
        without calculating it

        Parameters
        ----------
        values : bool, optional
            If values is False it prints the number of 
            adjacencies between each graph. And set a 
            '.' if there isn't any adjcence.
            If values is True it prints the values of
            each bow, or the sum of them if there
            are more than one bow. If there isn't any bow
            it set a 0
            The default is False.
        """
        
        def __Values(self):
            s = "    "
            for index in self.__nodes:
                idxui = str(index.uid)
                s += idxui + " " + " " * (3 - len(idxui))
                
            s += "\n"
            for i in self.__nodes:
                iuid = str(i.uid)
                s += iuid + " " + " " * (3 - len(iuid))
                for j in self.__nodes:
                    if j.uid in self.__conexions[i]:
                        #s += "#   "
                        dist = 0
                        for k in self.__edges[i]:
                            if k.dest == j.uid:
                                dist += k.weigth
                        distance = str(dist)
                        s += distance + " " + " " * (3 - len(distance))
                    else:
                        s += "0   "
                        
                s += "\n\n"
                                        
            return s
        
        def __NotValues(self):
            s = "    "
            for index in self.__nodes:
                idxui = str(index.uid)
                s += idxui + " " + " " * (3 - len(idxui))
                
            s += "\n"
            for i in self.__nodes:
                iuid = str(i.uid)
                s += iuid + " " + " " * (3 - len(iuid))
                for j in self.__nodes:
                    if j.uid in self.__conexions[i]:
                        #s += "#   "
                        dist = 0
                        for k in self.__edges[i]:
                            if k.dest == j.uid:
                                dist += 1
                        distance = str(dist)
                        s += distance + " " + " " * (3 - len(distance))
                    else:
                        s += ".   "
                        
                s += "\n\n"
                                        
            return s
        
        if values: print(__Values(self))
        else: print(__NotValues(self))
        
        
    def AdjacencyMatrix(self, values = False) -> list: #matrix
        """
        It calculates and return the Adjacency Matrix 
        of the graph

        Parameters
        ----------
        values : bool, optional
            If values is False it count the number of 
            adjacencies between each graph. And set a 
            '.' if there isn't any adjcence.
            If values is True it count the values of
            each bow, or the sum of them if there
            are more than one bow. If there isn't any bow
            it set a 0
            The default is False.
            
        Returns
        -------
        m : list (matrix)
            The adjacence matrix.

        """
        def __Values(self):
            m = []
            for i in self.__nodes:
                r = []
                for j in self.__nodes:
                    if j.uid in self.__conexions[i]:
                        #s += "#   "
                        dist = 0
                        for k in self.__edges[i]:
                            if k.dest == j.uid:
                                dist += k.weigth
                        r.append(dist)
                    else:
                        r.append(0)
                        
                m.append(r)
                                        
            return m
        
        def __NotValues(self):
            
            m = []
            for i in self.__nodes:
                r = []
                for j in self.__nodes:
                    if j.uid in self.__conexions[i]:
                        #s += "#   "
                        dist = 0
                        for k in self.__edges[i]:
                            if k.dest == j.uid:
                                dist += 1
                        r.append(str(dist))
                    else:
                        r.append(".")
                        
                m.append(r)
                                        
            return m
        
        if values: return __Values(self) 
        else: return __NotValues(self)
    
    
    def IncidenceMatrix(self) -> list: #matrix
        """Return the Incidence Matrix of the Graph"""
        
        rows = {n.uid:[] for n in self.__nodes}
        i = 0
        for i in self.__nodes:
            for j in self.__edges[i]:
                if j.source == j.dest:
                    for h in rows.keys():
                        if h != i.uid:
                            rows[h].append(0)
                        else:
                            rows[h].append(2)
                else:
                    for k in rows.keys():
                        if k == i.uid or k == j.dest:
                            rows[k].append(1)
                            
                        else:
                            rows[k].append(0)
             
        matrix = []
        for r in rows.keys():
            matrix.append(rows[r])
        
        return matrix
    
    
    def PrintIncidenceMatrix(self):
        """Print the Incidence Matrix of the Graph"""
        
        m = self.IncidenceMatrix()
        
        s = "     "
        for u in range(len(m[0])):
            s += str(u + 1) + "   "
        s += "\n"
    
        for r in range(len(m)):
            n = str(self.__nodes[r].uid)
            s += n + " " * (5 - len(n))
            for c in m[r]:
                if c != 0:
                    s += str(c) + "   "
                else:
                    s += ".   "
                
            s += "\n\n"
        
        print(s)
        
    
    def Undirected(self):
        """
        Convert all directed nodes in the graph to 
        undirected with the same weigth
        """
        next_append = []
        for n in self.__nodes:
            for e in self.__edges[n]:
                find = False
                ndest = self.__uids[e.dest]
                for d in self.__edges[ndest]:
                    if e.source == d.dest and e.weigth == d.weigth:
                        find = True
                        
                if not find:
                    next_append.append(e)
                    
        for napp in next_append:
            
            new_con = Graph.Edge(napp.dest, napp.source, napp.weigth)
            self.__edges[self.__uids[napp.dest]].append(new_con)
            self.__conexions[self.__uids[napp.dest]].add(napp.source)
            
    
    def __str__(self) -> str:
        s = ""
        for i in self.__nodes:
            s += str(i.uid) + "\n"
            for j in self.__edges[i]:
                s += "\t" + str(j.source) + " -- " + str(j.weigth) + " -> " + str(j.dest)
                s += "\n"
            
        return s
    
    
    def Complete(self, weigth = 0):
        """
        Add an indirected bow between each node of 
        the graph in order to make the graph complete.
        You can decide the weigth of all the edges with
        weigth
        """
        for m in self.__nodes:
            for n in self.__nodes:
                if m != n:
                    self.Conect(m, n, weigth)
                    
                
    def AdjacentNodes(self, nod:Node) -> list:
        """
        Return a list with the adjacent nodes from a node.
        Namely, every node where wou can arrive from 
        the main node.
        """
        adj = []
        for nuid in self.__conexions[nod]:
            adj.append(self.GetNodeUID(nuid))
            
        return adj
    
    
    def IncidentNodes(self, nod:Node) -> list:
        """
        Return a list with the incident nodes from a node.
        Namely, every node which have a bow that 
        connect with te main node.
        """
        inc = []
        for n in self.__nodes:
            if nod.uid in self.__conexions[n]:
                inc.append(n)
                
        return inc
    
    
    def Conex(self, nod:Node = None) -> bool:
        """
        Return if the graph is conex or not.
        Namely, you can reach to any node independently
        of where you have started
        
        If nod is not None, then the function looks if 
        the graph is conex starting from that point.
        In other case, it check if the graph is strongly
        conex
        """
        def __Visit(nod, vis, con):
            con.update(self.__conexions[nod])
            for nuid in self.__conexions[nod]:
                if len(con) < self.Size():
                    if nuid not in vis:
                        vis.add(nuid)
                        newnode = self.GetNodeUID(nuid)
                        __Visit(newnode, vis, con)
                      
                        
        if nod != None:
            visited = set()
            conected = set()
            __Visit(nod, visited, conected)
            
            return len(conected) == self.Size()
        
        else:
            conex = True
            for n in self.__nodes:
                visited = set()
                conected = set()
                __Visit(n, visited, conected)
                conex = conex and len(conected) == self.Size()
                
            return conex
        
        
    def Conected(self, fr_node, to_node) -> bool:
        """
        Check if two nodes are or not conected.
        Namely, you can reach to the second node from the 
        first one (but not necessary in the other way)

        Parameters
        ----------
        fr_node : TYPE
            The starting node.
        to_node : TYPE
            The node that we want to know if is conected.

        Returns
        -------
        bool
            If the nodes are or not connected.

        """
        def __Search(fr_nod, to_node, vis):
            if to_node.uid not in self.__conexions[fr_nod]:
                find = False
                for nuid in self.__conexions[fr_nod]:
                    if nuid not in vis:
                        vis.add(nuid)
                        newnode = self.GetNodeUID(nuid)
                        find = __Search(newnode, to_node, vis)
                        
                return find
                        
            else:
                return True
        
        visited = set()
        return __Search(fr_node, to_node, visited)
    
    
    def Export(self, file:str = None):
        """
        This function creates (or modificate) a file
        creating an interpretative graph. 
        This can be used to move a graph from one place 
        to another and keep all information

        Parameters
        ----------
        file : str, optional
            The name of the file. We can expecify it or
            the function will create an automatic name
            with the uids of the firts nodes.
            The default is None.
        """
        if file is None:
            file = ""
            for nod in range(4):
                file += str(self.__nodes[nod].uid)
            file += "graph.txt"
        
        with open(file,'w',encoding = 'UTF-8') as g:
            for i in self.__nodes:
                g.write(str(i.uid) + " " + str(i.value))
                if i.priority != None:
                    g.write(" " + str(i.priority))
                g.write("\n")
                for j in self.__edges[i]:
                    g.write("\t" + str(j.source) + " -- " + str(j.weigth))
                    g.write(" -> " + str(j.dest) + "\n")
                    
                    
    def __ChangeKey(self, d:dict, k, nk):
        d[nk] = d[k]
        del d[k]
        
        
    def __IntUID(self):
        for nod in self.__nodes:

            aux_n = self.Node(nod.uid, nod.value, nod.priority)
            nod.uid = int(nod.uid)
            self.__uids[aux_n.uid].uid = int(nod.uid)

            for con in self.__conexions[nod]:
                self.__conexions[nod].add(int(con))
                self.__conexions[nod].discard(str(con))
                
            for ed in self.__edges[nod]:
                ed.source = int(ed.source)
                ed.dest = int(ed.dest)
                
            self.__ChangeKey(self.__uids, aux_n.uid, int(nod.uid))
            
            
    def __FloatValue(self):
        for nod in self.__nodes:
            aux_n = self.Node(nod.uid, nod.value, nod.priority)
            nod.value = float(nod.value)
            
            self.__uids[aux_n.uid].value = float(nod.value)

            
    def __IntPrior(self):
        for nod in self.__nodes:
            if nod.priority != None:
                aux_n = self.Node(nod.uid, nod.value, nod.priority)
                nod.priority = int(nod.priority)
                
                self.__uids[aux_n.uid].priority = int(nod.priority)
            
            
    def __FloatWeigth(self):
        for nod in self.__nodes:
            for ed in self.__edges[nod]:
                ed.weigth = float(ed.weigth)
                
                
    def Import(self, file:str, 
               int_uid:bool = False,
               flt_value:bool = False,
               int_priority:bool = False,
               flt_weigth:bool = False,
               num_default:bool = True):
        """
        Opposite function to export, that import a graph
        from a file.
        You can decide the type of the data that the graph
        will storage. It will be integers for uid and 
        priority and float for value and weigth for default.
        But you can change it

        Parameters
        ----------
        file : str
            The name of the file.
        int_uid : bool, optional
            If the uid will be imported as integer or not. 
            The default is False.
        flt_value : bool, optional
            If the value will be imported as float or not.
            The default is False.
        int_priority : bool, optional
            If the priority will be imported as integer or not.
            The default is False.
        flt_weigth : bool, optional
            If the priority will be imported as float or not. 
            The default is False.
        num_default : bool, optional
            If we want that all data be imported as numbers
            (int or float). 
            The default is True.
        """
        
        def __Importstr(self):

            f = open(file, "r", encoding = "UTF-8")
            l = f.readline()
            l_edges = []
            while l != "":
                #print(l)
                if l[0] != "\t":
                    nod = l.strip().split()
                    if len(nod) == 3:
                        self.NewNode(nod[0], nod[1], nod[2])
                    else:
                        self.NewNode(nod[0], nod[1])
                else:
                    l_edges.append(l.strip().split())

                l = f.readline()
                
            f.close()
            
            for ed in l_edges:
                self.Conect(
                    self.GetNodeUID(ed[0]),
                    self.GetNodeUID(ed[4]),
                    ed[2])
                
            return 
        
        
        def __DefInteger(self):
            f = open(file, "r", encoding = "UTF-8")
            l = f.readline()
            l_edges = []
            while l != "":
                #print(l)
                if l[0] != "\t":
                    nod = l.strip().split()
                    if len(nod) == 3:
                        self.NewNode(int(nod[0]), 
                                     float(nod[1]), 
                                     int(nod[2]))
                    else:
                        self.NewNode(int(nod[0]), 
                                     float(nod[1]))
                else:
                    l_edges.append(l.strip().split())

                l = f.readline()
                
            f.close()
            
            for ed in l_edges:
                self.Conect(
                    self.GetNodeUID(int(ed[0])),
                    self.GetNodeUID(int(ed[4])),
                    float(ed[2]))
            
            return
        
        if num_default:__DefInteger(self)
        else:
            self.__Importstr()
            if int_uid:
                self.__IntUID()
            if flt_value:
                self.__IntValue()
            if int_priority:
                self.__IntPrior()
            if flt_weigth:
                self.__IntWeigth()
        
    
    def DefaultNumbers(self):
        """Convert all data into numbers"""
        self.__IntUID()
        self.__FloatValue()
        self.__IntPrior()
        self.__FloatWeigth()