# Matis Maamets ITT20
# 28.02.2021
# Kodutöö3
failinimi = input("Palun sisestage failinimi: ")
fail = open(failinimi, encoding="UTF-8")
number = 0
laulud = []
for rida in fail:
    laulud.append(rida)
    number=number+1
    print (number,". ",rida)
fail.close()
