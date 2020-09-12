"""Entrer les des phrases itératives dans un fichier."""
import os

def main():
    """Fonction principale."""
    while True:
        print("Le répertoire contient les éléments suivants :")
        print(os.listdir())
        phrase = input("Entrez la phrase voulue : ")
        numero = input("Entrez le nombre d'itérations : ")
        print("Vous avez entré la phrase '{}' avec le nombre d'itération {}.\n"
              .format(phrase, numero))
        fichier = open("fichier.txt", "a")
        for i in range(int(numero)):
            fichier.write("{} {}\n".format(phrase, i+1))
        fichier.close()
        fichier = open("fichier.txt", "r")
        print("Voici le contenu du fichier :\n")
        print(fichier.read())
        fichier.close()
        print("Voici le contenu du répertoire :")
        print(os.listdir())
        print("Suppression du fichier...\n")
        os.remove("fichier.txt")
        print("Voici le contenu du répertoire :")
        print(os.listdir())
        answer = input("Appuyer sur Entrée si vous voulez"+
                       " arrêter ou 'n' pour arrêter : ")
        if answer.lower() == "n":
            break


if __name__ == "__main__":
    main()
