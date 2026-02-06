from scipy.stats import ttest_ind
Renner="Tallinna mereröovlite laevad olid kaua paigal seisnud sest polnud tuult Seejärel tungisid nad Venemaale ühe Orešeki nimelise lossi lähedal röövisid seal kokku suure saagi niipalju kui laevadel jaksasid viia sest rahvas oli kõik ära põgenenud põletasid ka palju külasid maha võtsid ka sellel ajal ära kaks Lübecki laeva kaubaga mis Narva purjetasid ja vaenlase varustamisega tegelesid Sest ka inglased vedasid venelastele terveid laevatäisi soomussärke ja tulepüsse kusjuures ka mitmed põhja läksid"
Russow="Selsamal varakevadel tulid Danzigi piraadid kaheteistkümne laevaga hästi varustatult Tallinna alla ja heitsid Naissaare taga ankrusse et Poola kuninga nimel sulustada sõitu nii Tallinna kui ka Narva poole Need piraadid nõudsid Tallinna käest põletamise ähvardusel kontributsiooni kui nende nõudmisi ei täidetud Kui nad nüüd poole suve läbi Tallinna ees pidutsenud olid ning lõppeks teada said et Rootsi kuninga laevad olevat lähenemas taandusid nad jälle tagasi Danzigi poole"
sõnad1=Renner.split( )
print(sõnad1)
sõnad2=Russow.split( )
print(sõnad2)
print(len(sõnad1))
print(len(sõnad2))
#Renneril 71 sõna, Russowil 67
sõnapikkused1=[len(sõna) for sõna in sõnad1]
sõnapikkused2=[len(sõna) for sõna in sõnad2]
print(sõnapikkused1)
print(sõnapikkused2)
print(ttest_ind(sõnapikkused1, sõnapikkused2))
#P value 0.8450656399430174
def keskmine(m):
    return sum(m)/len(m)
print(keskmine(sõnapikkused1), keskmine(sõnapikkused2))
#Renneri ja Russowi sõnade pikkused on üpris lähedased (Renner = 6.014084507042254) (Russow = 6.104477611940299)
th="aeuioüõöä" #täishäälikute arv nende sõnades
def t_arv(sõna):
    return len([t for t in sõna if t in th])
nr1=[t_arv(sõna) for sõna in Renner.lower().split()]
nr2=[t_arv(sõna) for sõna in Russow.lower().split()]
print(ttest_ind(nr1, nr2))   #P value 0.7784720880445436
print(keskmine(nr1), keskmine(nr2))   #Renner = 2.76056338028169    Russow = 2.8208955223880596 aritmeetiline kesk
def t_osa(sõna):
    return len([t for t in sõna if t in th])/len(sõna)
osakaal1=[t_osa(sõna) for sõna in Renner.lower().split()]
osakaal2=[t_osa(sõna) for sõna in Russow.lower().split()]
print(keskmine(osakaal1), keskmine(osakaal2)) #Renneri arit. kesk. = 0.46567173046046284   Russowi = 0.4810579138937348
print(ttest_ind(osakaal1, osakaal2)) #P value 0.42554413198696545

import statsmodels.stats.api as sms
cm= sms.CompareMeans(sms.DescrStatsW(osakaal1), sms.DescrStatsW(osakaal2))
print(cm.tconfint_diff(usevar='unequal')) #osakaal1 = -0.053463134124227214   osakaal2 = 0.022690767257683493