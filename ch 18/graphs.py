class Vertex:
    def __init__(self, value):
        self.value = value
        self.adjacent_vertices = []

    def add_adjacent_vertex(self, vertex):
        if vertex in self.adjacent_vertices:
            return
        self.adjacent_vertices.append(vertex)
        vertex.add_adjacent_vertex(self)



alice = Vertex("Alice")
bob = Vertex("Bob")
cynthia = Vertex("Cynthia")
candy = Vertex("Candy")
fred = Vertex("Fred")
helen = Vertex("Helen")
irena = Vertex("Irena")
elaine = Vertex("Elaine")
derek = Vertex("Derek")
gina = Vertex("Gina")



alice.add_adjacent_vertex(bob)
alice.add_adjacent_vertex(candy)
alice.add_adjacent_vertex(derek)
alice.add_adjacent_vertex(elaine)
bob.add_adjacent_vertex(fred)
fred.add_adjacent_vertex(helen)
helen.add_adjacent_vertex(candy)
derek.add_adjacent_vertex(gina)
derek.add_adjacent_vertex(elaine)
gina.add_adjacent_vertex(irena)

