from scipy.stats import ttest_ind
lause1="Kui Arno isaga koolimajja jõudis olid tunnid juba alanud"
lause2="Mu isamaa mu õnn ja rõõm kui kaunis oled sa"

#Leia T-testi abil, kas nende lausete sõnade keskmine pikkus erineb üldistatavalt
sonad1=lause1.split()
sonapikkused1=[len(sona) for sona in sonad1]
sonad2=lause2.split()
sonapikkused2=[len(sona) for sona in sonad2]
print(ttest_ind(sonapikkused1, sonapikkused2))
print(sum(sonapikkused1)/len(sonapikkused1))
