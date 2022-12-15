X = [l.strip() for l in open("2022/day2/input.txt")]
p1 = 0

for x in X:
    # A rock B paper C scissors
    # X rock Y paper Z scissors
    # A wins against Z
    # B wins against X
    # C wins against Y
    op, me = x.split()
    p1 += {"X": 1, "Y": 2, "Z": 3}[me]

    p1 += {
        ("A","X"):3, ("A","Y"):0, ("A","Z"):6, 
        ("B","X"):6, ("B","Y"):3, ("B","Z"):0, 
        ("C","X"):0, ("C","Y"):6, ("C","Z"):3
        }[op, me]

print(p1)