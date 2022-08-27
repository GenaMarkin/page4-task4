kilo = []
i = 1
while i > - 0:
    i = float(input('enter kilo: '))
    if i > 0:
        kilo.append(i)
kilo.sort()
print('first: ', kilo[len(kilo) - 1])
print('second: ', kilo[len(kilo) - 2])
