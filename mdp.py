import re

def verifier_mot_de_passe(mdp):
    score = 0
    erreurs = []

    if len(mdp) >= 8:
        score += 20
    else:
        erreurs.append("• Trop court (8 caractères minimum)")

    if re.search(r"[A-Z]", mdp):
        score += 20
    else:
        erreurs.append("• Aucune majuscule")

    if re.search(r"[a-z]", mdp):
        score += 20
    else:
        erreurs.append("• Aucune minuscule")

    if re.search(r"[0-9]", mdp):
        score += 20
    else:
        erreurs.append("• Aucun chiffre")

    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", mdp):
        score += 20
    else:
        erreurs.append("• Aucun caractère spécial")

    return score, erreurs

while True:
    mot_de_passe = input("Entre un mot de passe : ")
    score, erreurs = verifier_mot_de_passe(mot_de_passe)

    print(f"Sécurité du mot de passe : {score}%")

    if erreurs:
        print("Erreurs :")
        for erreur in erreurs:
            print(erreur)

    if score == 100:
        print("Mot de passe parfait !")
        break
