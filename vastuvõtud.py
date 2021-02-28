# Matis Maamets ITT20
# 28.02.2021
# Kodutöö3
fail = open("rebased.txt", encoding="UTF-8")
aasta = int(input("Palun sisestage, millise aasta andmeid vajate: "))
asukoht = aasta-2011
vastuvõetud = []
for rida in fail:
    vastuvõetud.append(int(rida))        
fail.close()
print (f"{aasta}. aastal oli vastuvõetuid {vastuvõetud[asukoht]}")