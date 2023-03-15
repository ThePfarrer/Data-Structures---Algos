def dfs_traverse(vertex, visited_vertices={}):
    visited_vertices[vertex.value] = True

    print(vertex.value)

    for adjacent_vertex in vertex.adjacent_vertices:
        if adjacent_vertex.value in visited_vertices:
            continue

        dfs_traverse(adjacent_vertex, visited_vertices)


def dfs(vertex, search_value, visited_vertices={}):

    if search_value == vertex.value:
        return vertex

    visited_vertices[vertex.value] = True

    print(vertex.value)

    for adjacent_vertex in vertex.adjacent_vertices:
        if adjacent_vertex.value in visited_vertices:
            continue

        if adjacent_vertex.value == search_value:
            return adjacent_vertex

        vertex_were_searching_for = dfs(adjacent_vertex, search_value, visited_vertices)

        if vertex_were_searching_for:
            return vertex_were_searching_for

    return None
