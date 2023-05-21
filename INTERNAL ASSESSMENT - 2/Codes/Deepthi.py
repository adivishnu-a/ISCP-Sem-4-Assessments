from fractions import Fraction

a, b, c = map(int, input().split(":"))
d, e, f = map(int, input().split(":"))
unit = input()
r1 = 0
r2 = 0
r3 = 0

if d > a:
    r1 = d - a
    r2 = e - b
    r3 = f - c
elif d == a:
    r1 = 0
    if e > b:
        r2 = e - b
        r3 = f - c
    elif e == b:
        r2 = 0
        r3 = abs(f - c)
    else:
        r2 = b - e
        r3 = c - f
else:
    r1 = a - d
    r2 = b - e
    r3 = c - f

if unit == 's' or unit == 'S':
    diff = r1 * 3600 + r2 * 60 + r3
    print(diff, "Seconds")
elif unit == 'm' or unit == 'M':
    diff = r1 * 60 + r2
    fr = Fraction(r3, 60)
    if diff!=0:
        print(diff, fr, "Minutes")
    else:
        print(fr, "Minutes")
elif unit == 'h' or unit == 'H':
    diff = r1
    se = r2 * 60 + r3
    fr = Fraction(se, 3600)
    if diff!=0:
        print(diff, fr, "Hours")
    else:
        print(fr, "Hours")
