M = float(input("digite uma distancia em metros :"))
KM = M / 1000
HM = M / 100
DAM = M / 10
DM = M * 10
CM = M * 100
MM = M * 1000
print('A medida de {} corresponde a \n{}km \n{}hm \n{}dam \n{:.0f}dm \n{:.0f}cm \n{:.0f}mm'.format(M,KM,HM,DAM,DM,CM,MM))
