#!/usr/bin/env python3

# fold dots according to the axis, 'x' or 'y', and the distance d
def fold(dots, instructions):
    for axis, d in instructions:
        folded = []
        for x,y in dots:
            if axis == 'x' and x > d:
                x = 2*d - x
            if axis == 'y' and y > d:
                y = 2*d - y
            if (x,y) not in folded:
                folded.append((x,y))
        dots = folded
    return dots

# print the dots
def print_dots(dots):
    dots = sorted(dots) # sort by x first
    xmax = dots[-1][0]
    dots.sort(key=lambda dots: dots[1]) # sort by y
    ymax = dots[-1][1]

    for y in range(ymax + 1):
        for x in range(xmax + 1):
            if dots and dots[0] == (x,y):
                print('#', end='')
                dots.pop(0)
            else:
                print(' ', end='')
        print()

if __name__ == "__main__":
    dots = [] # list of dot tuples, e.g. (2,23)
    instructions = [] # folding instructions, e.g. ('x', 15)

    with open("day13_input") as fh:
        line = fh.readline()
        while line != '':
            p = line.strip().split(',')
            if len(p) == 2:
                dots.append(tuple(map(int, p)))
            else:
                q = line.strip().split()
                if len(q) == 3:
                    r = q[2].split('=')
                    instructions.append( (r[0], int(r[1])) )
            line = fh.readline()

    # Part 1: fold once
    dots = fold(dots, instructions[:1])
    print(f"Part 1: number of dots after first fold: {len(dots)}")

    # Part 2: perform the remaining foldings
    print("Part 2: eight capital letters code:")
    print_dots(fold(dots, instructions[1:]))
