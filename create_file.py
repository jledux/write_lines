"""Entrer les des phrases it√©ratives dans un fichier."""
import os


def main():
    """Fonction principale."""
    while True:
        print("Le rÈpertoire contient les √©l√©ments suivants :")
        print(os.listdir())
        phrase = input("Entrez la phrase voulue : ")
        numero = input("Entrez le nombre d'it√©rations : ")
        print("Vous avez entrÈ la phrase '{}' avec le nombre d'itÈration {}.\n"
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
        print("Voici le contenu du r√©pertoire :")
        print(os.listdir())
        answer = input("Appuyer sur Entr√©e si vous voulez" +
                       " recommencer ou 'n' pour arrÍter : ")
        if answer.lower() == "n":
            break


if __name__ == "__main__":
    main()
