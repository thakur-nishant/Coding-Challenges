def closestLocations(totalCrates, allLocations, truckCapacity):
    all_distances = {}
    for i in range(len(allLocations)):
        temp_dist = getDistance(allLocations[i])
        all_distances[temp_dist] = allLocations[i]

    sorted_distances = sorted(all_distances.keys())

    result = []
    for i in range(truckCapacity):
        result.append(all_distances[sorted_distances[i]])
    print(all_distances)
    return result


def getDistance(point):
    return (point[0] ** 2 + point[1] ** 2) ** (1 / 2)


print(closestLocations(3, [[1, -3], [1, 2], [3, 4]], 1))
