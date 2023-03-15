from collections import deque

def bfs_traverse(starting_vertex):
    queue = deque()
    visited_vertices = {}
    visited_vertices[starting_vertex.value] = True

    queue.append(starting_vertex)

    while queue:
        current_vertex = queue.popleft()

        print(current_vertex.value)

        for adjacent_vertex in current_vertex.adjacent_vertices:
            if not adjacent_vertex.value in visited_vertices:
                visited_vertices[adjacent_vertex.value] = True
            
            queue.append(adjacent_vertex)


def breath_first_search(vertex, visited_vertices={}):
    visited_vertices[vertex.value] = True

    print(vertex.value)

    for adjacent_vertex in vertex.adjacent_vertices:
        queue = deque()
        if adjacent_vertex.value in visited_vertices:
            continue


        breath_first_search(adjacent_vertex, visited_vertices)