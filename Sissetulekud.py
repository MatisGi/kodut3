# Matis Maamets ITT20
# 28.02.2021
# Kodutöö3
fail = open("konto.txt", encoding="UTF-8")
sissetulekud = []
for rida in fail:
    sissetulekud.append(rida)
    rida = float(rida)
    if rida > 0:
        print (rida)
fail.close()
