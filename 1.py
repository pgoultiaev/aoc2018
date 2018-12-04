from util import readinput

input = [int(x) for x in readinput(1)]


def solve2(data):
    visited = []
    number = 0
    curr = 0
    while True:
        if number in visited:
            return number
        else:
            visited.append(number)
            number = number + data[curr]
            curr = (curr + 1) % len(data)


print(sum(input))
print(solve2(input))
