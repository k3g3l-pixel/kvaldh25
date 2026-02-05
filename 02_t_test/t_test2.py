lause1="Kui Arno isaga koolimajja jõudis olid tunnid juba alanud"
lause2="Mu isamaa mu õnn ja rõõm kui kaunis oled sa"

#Leia T-testi abil, kas nende lausete sõnade keskmine pikkus erineb üldistatavalt
sonad1=lause1.split()
print(sonad1)
print(sonad1[3])
print(len("tere"))
#Kuva sõna nr 3 tähtede arv
print(len(sonad1[3]))
print(len(sonad1)) #Sõnu lauses kokku
sonapikkused1=[len(sona) for sona in sonad1]
print(sonapikkused1)

