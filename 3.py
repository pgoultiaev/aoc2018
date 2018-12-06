from util import readinput, vector
from collections import Counter

all_coords = []


def parse(line):
    v = vector(line, sep=' ')
    claim_id = v[0]
    l, t = vector(v[2].rstrip(':'), sep=',')
    w, h = vector(v[3], sep='x')
    return claim_id, l, t, w, h


def get_coords(claim_id, l, t, w, h):
    return claim_id, list(
        [(x, y) for y in range(t, t + h) for x in range(l, l + w)])


def solve1(data):
    for line in data:
        _, coords = get_coords(*parse(line))
        all_coords.extend(coords)
    overlaps = {c for c, count in Counter(all_coords).items() if count >= 2}
    return len(overlaps)


def solve2(data):
    claim_dict = {}
    for line in data:
        claim_id, coords = get_coords(*parse(line))
        claim_dict[claim_id] = coords

    all_coords_counted = Counter(all_coords)
    for claim_id, coords in claim_dict.items():
        if all([all_coords_counted[c] == 1 for c in coords]):
            return claim_id


print(solve1(readinput(3)))
print(solve2(readinput(3)))
