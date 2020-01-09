'''
Given a list of points as a tuple (x, y) and an integer k, find the k closest points to the origin (0, 0).

'''

def distance_from_origin(a, b):
    return math.sqrt(a**2 + b**2)


def closest_points(points, k):
    
    distances = [distance_from_origin(a, b) for (a,b) in points]
    pairs = {distance:i for i, distance in enumerate(distances)}
    res = []
    distances.sort()
    
    for i in range(k):
        res.append(tuples[pairs[distances[i]]])
    
    return res
    
    
tuples = [(0, 0), (1, 2), (-3, 4), (3, 1)]
k = 2

print(closest_points(tuples, k))
