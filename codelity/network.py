# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(T):
    '''
    Specification:
        cities is integers in range(0, M-1)
        network is undirected graph
        network <- (cities, roads):
            nodes <- for city in cities
            edges <- for road in roads
            distance <- (node1, node2):
                shortest_path(node1, node2)
            capital <- min(nodes)
    Constrains:
        Each node has at most one edge.
    Statement:
        - Get table lookup of distance of each node from capital with format [distance, distance, distance, ...] where index if node.
    '''
    N = len(T)

    # Sanity check
    if N == 0:
        raise ValueError('Input must be not empty!')

    # Find the capital
    capital = None
    for node, city in zip(range(len(T)), T):
        if node == city:
            capital = city
            break

    # Sanity check
    if capital is None:
        raise ValueError('Capital not found!')
    else:
        print("Capital is", capital)

    # Distance index
    distanceFromCapital = []
    for node in T:
        if node == capital:
            continue
        distanceFromCapital.append(distance(T, node, capital))
    # logic here
    

    return distanceFromCapital


def distance(T, x, capital):
    cont = 0
    currNode = T[x]
    while currNode != capital:
        cont += 1
        currNode = T[currNode]
    return cont+1