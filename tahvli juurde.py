# Matis Maamets ITT20
# 28.02.2021
# Kodutöö3
from datetime import *
failinimi = input("Palun sisestage failinimi: ")
fail = open(failinimi, encoding="UTF-8")
number = 0
nimed = []
päev = int(datetime.now().day)
võitja = 0

for rida in fail:
    nimed.append(rida)
    number=number+1
    print (number,". ",rida)
    if päev == number:
        võitja = rida 
fail.close()

print()
print ("Vastama tuleb: ",võitja)