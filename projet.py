import csv

def menu():
    print("Qui etes vous?\n")
    tryagain = True
    while tryagain == True:
        try:
            choix = int(input("Tapez:\n 1) si vous etes le directeur \n 2) si vous etes un simple utilisateur\n: "))
        except ValueError:
            print("Choix incorrect")
            continue
        if choix == 1:
            print(mot_de_passe())
            tryagain = False
        elif choix == 2:
            print(simple_utilisateur())
            tryagain = False
        else:
            print("Choix incorrect")


# Creation du fichier
def creation():
    file = open ("Name.csv","w")
    newrecord = "firstname ,Lastname ,poste ,username ,email \n"
    file.write(str(newrecord))
    file.close()
    return newrecord

# Ajouter un nouveau membre
def ajouter():
    file = open ("Name.csv","a")
    firstname = input("Enter the firstname: ")
    fname = firstname
    lastname = input("Enter the last name: ")
    lname = lastname
    poste = input("Enter your poste: ")
    firstname = firstname.lower()
    lastname = lastname.lower()
    fullname = firstname + lastname
    fullname = fullname.replace(" ", "")
    firstname = firstname[0]
    username = firstname + lastname
    email = fullname+"@coding.com"
    newrecord = fname + " ," + lname + " ,"+ poste + " ,"+ username + " ,"+ email +"\n"
    file.write(str(newrecord))
    file.close()
    return fname, lname, poste, username, email

# Chercher quelqu'un
def recherche():
    file = open ("Name.csv","r")
    search = input("Qui voulez-vous rechercher: ")
    reader = csv.reader(file)
    count  = 0
    for row in file:
        if search in str(row):
            print(row)
            count = count + 1
    if count == 0:
        print("Cette personne n'est pas dans la liste")
    file.close()

# Effacer un membre
def effacer ():
    file = open("Name.csv","r")
    x = 0
    tmplist = []
    for row in file:
        tmplist.append(row)
    file.close()
    for row in tmplist:
        print (x, row)
        x = x + 1
    rowtodelete = int (input ("Enter the row number to delete: "))
    del tmplist [rowtodelete]
    file = open("Name.csv","w")
    for row in tmplist: 
        file.write (row)
    file.close()
    
    
def modifier():
    file = list(csv.reader(open("Name.csv")))
    ensname = []
    for row in file:
        ensname.append(row)
        
    x = 0
    for row in ensname:
        display = x,ensname[x]
        print(display)
        x = x + 1
    alter = int(input("Entrer le numero de la ligne que vous voulez modifier: "))
    x = 0
    for row in ensname[alter]:
        display = x, ensname[alter][x]
        print(display)
        x = x + 1
    part = int(input("Quel parti voulez-vous changer? "))
    newdata = input("Entrer le nouveau mot: ")
    ensname[alter][part] = newdata
    
    file = open("Name.csv","w")
    x = 0
    for row in ensname:
        newrecord = ensname[x][0] + ", " + ensname[x][1] + ", " + ensname[x][2] + ", " + ensname[x][3] + ", " + ensname[x][4] + "\n" 
        file.write(str(newrecord))
        x = x + 1
    file.close()


# Lire la liste
def lecture():
    file = open ("Name.csv","r")
    for row in file:
        print(row)
    file.close()


# Mot de passe
def mot_de_passe():
    compteur = 1
    while compteur <= 3:
        mot_de_pass = "Directeur"
        password = input("Entrer votre mot de passe: ")
        if mot_de_pass == password:
            print(directeur())
            break
        else:
            print("Mot de passe incorrect")
            compteur = compteur + 1

# Pour ajouter quelqu'un d'autre            
def qqch_autre():
    verif = True
    while verif == True:
        qqch2 = input("Voulez-vous faire quelque chose d'autre? (y/n)\n: ")
        qqch2 = qqch2.lower()
        if qqch2 == "y":
            print(directeur())
        elif qqch2 == "n":
            print("Merci et au revoir")
            quit()
        else:
            print("Choix incorrect")
            
# Si c'est le directeur    
def directeur():
    print("Bonjour!\n Que voulez-vous faire? ")
    tryagain = True
    while tryagain == True:
        try:
            choisir = int(input("Tapez:\n 1) Si vous voulez creer le fichier\n 2) Si vous voulez ajouter un nouvel employer\n 3) Si voulez faire une recherche\n 4) si vous voulez effacer les informations d'un employer\n 5) Si vous voulez lire la liste\n 6) Si vous voulez modifier un nom\n 7) Si vous voulez quitter le programme\n: "))
        except ValueError:
            print("Choix incorrect")
            continue
        if choisir == 1:
            print(creation())
            print("Le ficher a ete cree avec succes.")
            tryagain = False
        elif choisir == 2: # Pour ajouter
            print(ajouter())
            encore = True
            while encore == True:
                autre = input("Voulez-vous ajouter quelqu'un d'autre (y/n): ")
                autre = autre.lower()
                if autre == "y":
                    print(ajouter()) # Pour ajouter
                elif autre == "n": 
                    break
                else:
                    print("Choix incorrect")
            tryagain = False
        elif choisir == 3: # Pour faire une recherche
            print(recherche())
            tryagain = False
        elif choisir == 4: # Pour effacer
            print(effacer())
            print(lecture())
            print("La ligne a ete supprime")
            encore = True
            while encore == True:
                autre = input("Voulez-vous effacer quelqu'un d'autre (y/n): ")
                autre = autre.lower()
                if autre == "y":
                    print(effacer())
                elif autre == "n":
                    break
                else:
                    print("Choix incorrect")
            tryagain = False
        elif choisir == 5: # Pour lire
            print(lecture())
            tryagain = False
        elif choisir == 6:
            print(modifier())
            print(lecture())
            print("La ligne a ete modifier")
            encore = True
            while encore == True:
                autre = input("Voulez-vous modifier quelque chose d'autre (y/n): ")
                autre = autre.lower()
                if autre == "y":
                    print(modifier())
                    print(lecture())
                    print("La ligne a ete modifier")
                elif autre == "n":
                    break  
                else:
                    print("Choix incorrect")
            tryagain = False
        elif choisir == 7:
            print("Merci et au revoir")
            quit()
        else:
            print("Choix incorrect")
    print(qqch_autre())


# Simple utilisateur
def simple_utilisateur():
    tryagain = True
    while tryagain == True:
        try:
            deux = int(input("Ecrivez\n 1) Si vous voulez ajouter votre nom\n 2) Si vous voulez quitter le programme\n :"))
        except ValueError:
            print("Choix incorrect")
            continue
        if deux == 1: 
            print("N.B: Regarder votre username et votre email attentivement\n", ajouter() )
            tryagain = False
        elif deux == 2:
            print("Merci et au revoir")
            quit()
        else:
            print("Choix incorrect")

            
def main():
    print(menu())
    
main()

print("Merci et au revoir")
