f = open("/Users/jacobtilly/Documents/GitHub/AdventOfCode-2020/day1/input.txt", "r")
input = f.read().split('\n')
for a in input:
  for b in input:
      if(2020-int(a)-int(b) == 0):
          print(int(a)*int(b))