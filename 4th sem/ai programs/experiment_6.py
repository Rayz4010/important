def nearest_neighbour(distance):
    num_cities=len(distance)
    unvisited_cities=list(range(num_cities))
    current_city=0
    tour=[current_city]
    total_distance=0
    while unvisited_cities:
        nearest_city=min(unvisited_cities,key=lambda city:distance[current_city][city])
        total_distance+=distance[current_city][nearest_city]
        current_city=nearest_city
        unvisited_cities.remove(nearest_city)
        tour.append(current_city)
    total_distance+=distance[current_city][tour[0]]
    tour.append(0)
    return tour, total_distance


distance=[
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

tour, total_distance = nearest_neighbour(distance)
print("Neqrest Neighbour TSP solution:")
print("Tour:",tour,"\nTotal Distance:",total_distance)
