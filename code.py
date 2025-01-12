#Etape 1 : Ouvrir le fichier en mode lecture
with open("document.txt", 'r', encoding='utf-8') as fichier:
    lignes = fichier.readlines()

# fonction qui Supprime les espaces inutiles et affiche chaque ligne
def afficher_lines_stripped(lignes):
  for ligne in lignes:
    return [ligne.strip() for ligne in lignes]
lines_stripped = afficher_lines_stripped(lignes)
print(lines_stripped)

#Etape 2 : Extraire les chiffres :
#fonction pour extraire les chiffres de chaque ligne :
def extraire_chiffres(ligne):
    return [c for c in ligne if c.isdigit()]
#création d'une liste contient tous les listes des chifres de chaque ligne
listes_chiffres = [extraire_chiffres(ligne) for ligne in lines_stripped]
print(listes_chiffres)
#Etape 3 
#Création d'une liste contient les chiffres combinés de chaque ligne
#Fonction pour combiner le premier et le dernier chiffre de chaque ligne :
def combiner_chiffres (L):
  if len(L) >=2 :
    return int(L[0]+ L[-1]) #convertir string en int 
  else :
    for n in L :
      return int(n + n)

chiffres_combinés = [combiner_chiffres(L) for L in listes_chiffres]
print (chiffres_combinés)
#Finalement 
#additionner les chiffres combinés
somme=sum(chiffres_combinés)
print(somme)
#resultat_obtenu = 53386 
