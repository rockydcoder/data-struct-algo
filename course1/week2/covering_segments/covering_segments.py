# Uses python3
import sys
from collections import namedtuple

Segment = namedtuple('Segment', 'start end')

def optimal_points(segments):
    points = []
    segments.sort(key = lambda tup: tup.end)
    pointer = 0
    while pointer < len(segments):
        seg = segments[pointer]
        points.append(seg.end)
        pointer += 1
        while pointer < len(segments) and (segments[pointer].start <= seg.end):
            pointer += 1

    return points

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *data = map(int, input.split())
    segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    points = optimal_points(segments)
    print(len(points))
    for p in points:
        print(p, end=' ')
