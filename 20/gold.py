from math import trunc

numbers = []
with open("vstup.txt") as vstup:
    for i, line in enumerate(vstup):
        sline = int(line.rstrip())
        numbers.append((i, sline * 811589153))
        if sline == 0:
            tvar_nuly = (i, sline)
for _ in range(10):
    for index in range(len(numbers)):
        for i, (order, num) in enumerate(numbers):
            if index == order:
                numbers.pop(i)  # toto je jedna z moznych implementaci ktora zkracuje zapis inaksie by boli vsetky len
                # zapisane ako len-1 lebo posuvane cislo vkladam do mezdier a
                if num > 0:
                    new_i = (i + num % len(numbers))
                    if new_i > len(numbers):
                        new_i -= len(numbers)
                if num < 0:
                    new_i = i + (num - trunc(num / len(numbers)) * len(numbers))
                    if new_i < 0:
                        new_i += len(numbers)
                if num == 0:
                    numbers.insert(i, (order, num))
                    break

                numbers.insert(new_i, (order, num))
                break

nula = numbers.index(tvar_nuly)
print(numbers[(nula + 1000) % len(numbers)][1] + numbers[(nula + 2000) % len(numbers)][1] +
      numbers[(nula + 3000) % len(numbers)][1])
