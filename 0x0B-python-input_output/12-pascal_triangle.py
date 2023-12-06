#!/usr/bin/python3
'''A pascal triangle implementation'''


def pascal_triangle(n):
    '''
    Returns a list of integers representing the pascal's triangle
    Args:
        n(int) : An integer
    '''
    if n <= 0:
        return []
    
    triangles = [[1]]
    while len(triangles) != n:
        tri = triangles[-1]
        temp = [1]
        for i in range(len(tri) - 1):
            temp.append(tri[i] + tri[i + 1])
        temp.append(1)
        triangles.append(temp)
    return triangles
