# Karl Paju IS22
numbrid = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
paaris = 0
paaritu = 0

for num in numbrid:
    if num % 2 == 0:
        paaris += 1
    else:
        paaritu += 1

print("Paaris arvud: ", paaris)
print("Paaritu arvud: ", paaritu)
