sides = [3, 2, 4, 7, 5, 12, 11, 13, 15, 16, 14, 14]

sides = sorted(sides, reverse=True)

smax = 0
for i in range(len(sides)):
    for j in range(i + i, len(sides)):
        for k in range(j + i, len(sides)):
            a = sides[i]
            b = sides[j]
            c = sides[k]
            if a + b > c and a + c > b and b + c > a:
                p = (a + b + c) / 2
                s = (p * (p - a) * (p - b) * (p - c)) ** (1 / 2)
                if s > smax:
                    smax = s

print("Maximalnaya ploschad ravna", smax)
