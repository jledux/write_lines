"""Entrer les des phrases itératives dans un fichier."""
import os


def main():
    """Fonction principale."""
    while True:
        print("Le r�pertoire contient les éléments suivants :")
        print(os.listdir())
        phrase = input("Entrez la phrase voulue : ")
        numero = input("Entrez le nombre d'itérations : ")
        print("Vous avez entr� la phrase '{}' avec le nombre d'it�ration {}.\n"
              .format(phrase, numero))
        fichier = open("fichier.txt", "w")
        for i in range(int(numero)):
            fichier.write("{} {}\n".format(phrase, i+1))
        fichier.close()
        fichier = open("fichier.txt", "r")
        print("Voici le contenu du fichier :\n")
        print(fichier.read())
        fichier.close()
        # to DELETE the text file.
        # print("Suppression du fichier...\n")
        # os.remove("fichier.txt")
        print("Voici le contenu du répertoire :")
        print(os.listdir())
        answer = input("Appuyer sur Entrée si vous voulez" +
                       " recommencer ou 'n' pour arr�ter : ")
        if answer.lower() == "n":
            break


if __name__ == "__main__":
    main()
