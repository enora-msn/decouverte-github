"""Générateur aléatoire d'excuses."""

import random

QUI = [
    "Mon chat",
    "Le bus",
    "Un voisin",
    "Mon petit frère",
    "Le chien du voisin",
    "Ma grand-mère",
    "Un extraterrestre",
    "Le Wi-Fi",
]

ACTION = [
    "a mangé",
    "a caché",
    "a supprimé",
    "a cassé",
    "a perdu",
    "a renversé du café sur",
    "a emporté",
    "a effacé",
]

QUOI = [
    "mon ordinateur",
    "mes clés",
    "mon TD",
    "mon téléphone",
    "mon cahier",
    "mon devoir",
    "ma clé USB",
    "mon réveil",
]


def generer_excuse():
    """Retourne une excuse aléatoire composée de : qui + action + quoi."""
    qui = random.choice(QUI)
    action = random.choice(ACTION)
    quoi = random.choice(QUOI)
    return f"{qui} {action} {quoi}."


if __name__ == "__main__":
    print(generer_excuse())
