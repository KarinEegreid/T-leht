import random
r = random.randint(1,10)
nimekiri = []
f = open("nimekiri_10it.txt", encoding = "utf-8")
for rida in f:
    nimekiri.append(rida.strip())
f.close()
suvaline = r.randint(0,len(nimekiri) -1)
print(nimekiri[suvaline])