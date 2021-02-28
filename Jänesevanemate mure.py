# Matis Maamets ITT20
# 28.02.2021
# Kodutöö3
ringid = int(input("Sisestage ringide arv: "))
x = range(1,ringid+1)
porgand = int(0)
for ring in x:    
    if (ring % 2) == 0:
     porgand = porgand + ring
     
print("Saadavate porgandite koguarv on 12. ",porgand)