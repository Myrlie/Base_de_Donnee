import csv

def menu():
    print("Qui etes vous?\n Tapez:\n")

menu()
choix = int(input("1) si vous etes le directeur \n 2) si vous etes un simple utilisateur\n: "))

# Creation du fichier
def creation():
    file = open ("Name.csv","w")
    newrecord = "firstname ,Lastname ,poste ,username ,email \n \n"
    file.write(str(newrecord))
    firstname = input("Enter your firstname: ")
    fname = firstname
    lastname = input("Enter your last name: ")
    lname = lastname
    poste = input("Enter your poste: ")
    firstname = firstname.lower()
    lastname = lastname.lower()
    fullname = firstname + lastname
    firstname = firstname[0]
    username = firstname + lastname
    email = fullname+"@coding.com"
    newrecord = fname + " ," + lname + " ,"+ poste + " ,"+ username + " ,"+ email +"\n"
    file.write(str(newrecord))
    file.close()
    return fname, lname, poste, username, email

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
    for row in file:
        if search in str(row):
            print(row)
        else:
            print("Cette personne n'est pas dans la liste")
    file.close()
    return row

# Effacer un membre
def delete():
    file = list(csv.reader(open("Name.csv")))
    ensname = []
    for row in file:
        ensname.append(row)
        
    x = 0
    for row in ensname:
        display = x,ensname[x]
        print(display)
        x = x + 1
    getrid = int(input("Entrer le numero de la ligne que vous voulez supprimer: "))
    del ensname[getrid]

    file = open("Name.csv", "w")
    x = 0    
    for row in ensname:
        newrecord = ensname[x][0]+ ", " + ensname[x][1]+ ", " + ensname[x][2] + ", " + ensname[x][3]+ ", " + ensname[x][4]+ ", "+ "\n"
        file.write(newrecord)
        x = x+1
    file.close()
    
    return newrecord

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
    
    file = open("Name.csv", "w")
    x = 0
    for row in ensname:
        newrecord = ensname[x][0]+ ", " + ensname[x][1]+ ", " + ensname[x][2] + ", " + ensname[x][3]+ ", " + ensname[x][4]+ ", "+ "\n"
        file.write(newrecord)
        x = x+1
    file.close()
    
    return ensname[alter]


# Lire la liste
def lecture():
    file = open ("Name.csv","r")
    for row in file:
        print(row)
    file.close()


# Si c'est le directeur

if choix == 1:
    compteur = 1
    while compteur <= 3:
        mot_de_passe = "Directeur"
        password = input("Entrer votre mot de passe: ")
        if mot_de_passe == password:
            print("Bonjour!\n Que voulez-vous faire? Tapez: ")
            choisir = int(input("1) Si vous voulez creer le fichier\n 2) Si vous voulez ajouter un nouvel employer\n 3) Si voulez faire une recherche\n 4) si vous voulez effaser les information d'un employer\n 5) Si vous voulez lire la liste\n 6) Si voulez modifier un nom\n: "))
            if choisir == 1:
                print(creation())
            elif choisir == 2: # Pour ajouter
                print(ajouter())
                autre = input("Voulez-vous ajouter quelqu'un d'autre (y/n): ")
                autre = autre.lower()
                if autre == "y":
                    print(ajouter())
                elif autre == "n": # Pour ajouter
                    print("Merci et au revoir!")
                else:
                    print("Choix incorrect")
                    break
            elif choisir == 3: # Pour faire une recherche
                print(recherche())
            elif choisir == 4: # Pour effacer
                print(delete())
                print("Cette ligne a ete supprime")
                autre = input("Voulez-vous effacer quelqu'un d'autre (y/n): ")
                autre = autre.lower()
                if autre == "y":
                    print(delete())
                elif autre == "n":
                    print("Merci et au revoir!")
                    print("Cette ligne a ete supprime")   
                else:
                    print("Choix incorrect")
                    break
            elif choisir == 5: # Pour lire
                print(lecture())
            elif choisir == 6:
                print(modifier())
                autre = input("Voulez-vous effacer quelqu'un d'autre (y/n): ")
                autre = autre.lower()
                if autre == "y":
                    print(delete())
                elif autre == "n":
                    print("Merci et au revoir!")
                    print("Cette ligne a ete supprime")   
                else:
                    print("Choix incorrect")
                    break                
            else:
                print("Choix incorrect")
                break
            break
        else:
            print("Mot de passe incorrect")
            compteur = compteur + 1
elif choix == 2: # Simple utilisateur
    print("N.B: Regarder votre username et votre email attentivement\n", ajouter() )
else:
    print("Choix incorrect")
    menu()
    choix = int(input("1) si vous etes le directeur \n 2) si vous etes un simple utilisateur\n: "))

print("Merci et au revoir")