"""Module de vérification de palindromes avec nettoyage de chaîne."""

import unicodedata

def ispalindrome(p):
    """
    Vérifie si une chaîne est un palindrome après nettoyage :
    suppression des espaces, conversion en minuscules, suppression des accents.
    """
    p = p.replace(" ", "").lower()
    p = unicodedata.normalize('NFD', p)
    p = ''.join(c for c in p if unicodedata.category(c) != 'Mn')
    for i in range(len(p)):
        if p[i-1] != p[-i]:
            return False
    return True

def main():
    """
    Fonction principale : teste la fonction ispalindrome sur plusieurs exemples.
    """
    for s in ["radar", "kayak", "level", "rotor", "civique", "deifie"]:
        print(s, ispalindrome(s))

if __name__ == "__main__":
    main()
