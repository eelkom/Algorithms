import sys

e, s, m = map(int, sys.stdin.readline().strip().split())
year = e

while year:
    if (year - s) % 28 == 0 and (year - m) % 19 == 0:
        break
    year += 15

print(year)