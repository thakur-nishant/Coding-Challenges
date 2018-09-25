#
# Complete the 'minArea' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY x
#  2. INTEGER_ARRAY y
#  3. INTEGER k
#


def minArea(x, y, k):
    new_x, new_y = closest_k_points(x, y, k)

    length = max(new_x) - min(new_x) + 2
    height = max(new_y) - min(new_y) + 2

    return max(length, height) ** 2

def closest_k_points(x, y, k):
    centroid_x = sum(x)/len(x)
    centroid_y = sum(y)/len(y)

    distance = {}
    for i in range(len(x)):
        distance[tuple([x[i], y[i]])] = euclidean_distance([x[i], y[i]], [centroid_x, centroid_y])

    closest_k_points = sorted(distance, key=distance.__getitem__)[:k]

    new_x = []
    new_y = []

    for i in range(len(closest_k_points)):
        new_x.append(closest_k_points[i][0])
        new_y.append(closest_k_points[i][1])

    return new_x,new_y

def euclidean_distance(x, y):
    sum = 0
    for i in range(len(x)):
        sum += (float(x[i]) - float(y[i]))**2
    return sum ** 0.5


x = [1, 1, 50, 100]
y = [1, 2, 50, 100]
k = 2
soln = minArea(x, y, k)
print(soln)
