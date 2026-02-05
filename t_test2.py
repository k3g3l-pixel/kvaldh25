from scipy.stats import ttest_ind
lause1="Kui Arno isaga koolimajja jõudis olid tunnid juba alanud Kooliõpetaja kutsus mõlemad oma ette"
lause2="Mu isamaa mu õnn ja rõõm kui kaunis oled sa ei leia mina iial tea"
sonad1=lause1.split( )
print(sonad1)
print(sonad1[3])
print(len(sonad1[3]))
print(len(sonad1))
sonapikkused1=[len(sona) for sona in sonad1]
print(sonapikkused1)

sonad2=lause2.split( )
print(sonad2)
print(sonad2[3])
print(len(sonad2[3]))
print(len(sonad2))
sonapikkused2=[len(sona) for sona in sonad2]
print(sonapikkused2)
print(sum(sonapikkused1)/len(sonapikkused1))
#print(ttest_ind(sonapikkused1, sonapikkused2))
print(ttest_ind(sonapikkused1, sonapikkused2))
#git add .
#git push
th="aeiouõäöü"
print(lause1.lower())
print([t for t in "koolimajja" if t in th])
print(len([t for t in "koolimajja" if t in th]))
def t_arv(sona):
    return len([t for t in sona if t in th])
print(t_arv("kalamaja"))
arvud1=[t_arv(sona) for sona in lause1.lower().split()]
print(arvud1)
print(lause2.lower())
arvud2=[t_arv(sona) for sona in lause2.lower().split()]
print(arvud2)
print(ttest_ind(arvud1, arvud2))