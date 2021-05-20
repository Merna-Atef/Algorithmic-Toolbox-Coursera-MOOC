#Uses python3
import sys
import math

def calc_dist(points):
    return euclid_dist(points[0],points[1])

def euclid_dist(p1, p2):
    return math.sqrt((p1[0]-p2[0])**2+(p1[1]-p2[1])**2)

def brute_force_closest_pair(points):
    min_d = euclid_dist(points[0],points[1])
    closest = {}
    closest['p1'] = points[0]
    closest['p2'] = points[1]
    closest['d'] = min_d
    for i in range(1, len(points)):
        for j in range(i+1,len(points)):
            d = euclid_dist(points[i], points[j])
            if d <= min_d:
                closest['p1'] = points[i]
                closest['p2'] = points[j]
                closest['d'] = d
    return closest


def closest_pair_across(slice, mid,d):
    min_d = d
    j = 0
    for i in range(len(slice)):
        j = i + 1
        while abs(i-j) < 7 and j < len(slice):
            if (slice[i][0] <= mid and slice[j][0] >= mid) or (slice[i][0] >= mid and slice[j][0] <= mid):
                d = euclid_dist(slice[i],slice[j])
                if d <= min_d:
                    min_d = d
            j = j+1
    return min_d


def closest_pair(points_x, points_y):
    n = len(points_x)
    if n <= 3:
        closest = brute_force_closest_pair(points_x)
        return closest['d']
    mid = n//2
    L = points_x[mid][0]
    left_x = points_x[0:mid]
    right_x = points_x[mid:n]
    left_y = []
    right_y = []
    for i in range(len(points_y)):
        if points_y[i][0] <= L:
            left_y.append(points_y[i])
        else:
            right_y.append(points_y[i])
    
    d_left = closest_pair(left_x, left_y)
    d_right = closest_pair(right_x, right_y)
    d = min(d_left, d_right)
    slice = []

    for point in points_y:
        if abs(point[0]-L) < d:
            slice.append(point)
    d_across = closest_pair_across(slice, L,d)
    d_min = min(d,d_across)
    return d_min


def minimum_distance(x, y):
    points = list(zip(x, y))
    sorted_x = sorted(points, key = lambda x: x[0])
    sorted_y = sorted(points, key = lambda x: x[1])
    #sorted_x = merge_sort_by(points, x)
    #sorted_y = merge_sort_by(points, y)
    d = closest_pair(sorted_x, sorted_y)
    return d

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    x = data[1::2]
    y = data[2::2]
    print("{0:.9f}".format(minimum_distance(x, y)))
    #print(minimum_distance(x, y))
