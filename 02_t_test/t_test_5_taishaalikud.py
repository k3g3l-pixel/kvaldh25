from scipy.stats import ttest_ind
lause1="Kui Arno isaga koolimajja jõudis olid tunnid juba alanud Kooliõpetaja kutsus mõlemad oma tuppa kõneles nendega  natuke aega, käskis Arnol hoolas ja korralik ja seadis ta siis pinki ühe pikkade juustega poisi kõrvale istuma"
lause2="Mu isamaa mu õnn ja rõõm kui kaunis oled sa Ei leia mina iial tääl see suure laia ilma pääl"

th="aeiouöäõü"
print(lause1.lower())
print([t for t in "koolimajja" if t in th])
print(len([t for t in "koolimajja" if t in th]))

def t_arv(sona):
    return len([t for t in sona if t in th])

print(t_arv("kalamaja"))
arvud1=[t_arv(sona) for sona in lause1.lower().split()]
print(arvud1)
#Kuva ka teise teksti iga sõna täishäälikute arv, kontrolli pisteliselt
arvud2=[t_arv(sona) for sona in lause2.lower().split()]
print(arvud2)
#Võrdle nende arvude aritmeetilisi keskmisi t-testiga
print(ttest_ind(arvud1, arvud2))
#Kuva kummagi arvujada aritmeetiline keskmine välja
def keskmine(m):
    return sum(m)/len(m)

print(keskmine(arvud1), keskmine(arvud2))

def t_osa(sona):
     return len([t for t in sona if t in th])/len(sona)

osakaalud1=[t_osa(sona) for sona in lause1.lower().split()]
osakaalud2=[t_osa(sona) for sona in lause2.lower().split()]
print(osakaalud1)
print(keskmine(osakaalud1), keskmine(osakaalud2))
#Leidke täishäälikute osakaalud ja nende keskmine hümni tekstis
#Võrrelge t-testiga kahe teksti sõnade täishäälikute osakaale
print(ttest_ind(osakaalud1, osakaalud2))


import statsmodels.stats.api as sms
cm = sms.CompareMeans(sms.DescrStatsW(osakaalud1), sms.DescrStatsW(osakaalud2))
print(cm.tconfint_diff(usevar='unequal'))
