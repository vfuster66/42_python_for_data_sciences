import string


def count_characters(text: str) -> dict:
    """
    Compte les majuscules, minuscules, ponctuations,
    chiffres et espaces dans le texte fourni.
    """
    counts = {
        "upper": 0,
        "lower": 0,
        "punctuation": 0,
        "digits": 0,
        "spaces": 0
    }

    for char in text:
        if char.isupper():
            counts["upper"] += 1
        elif char.islower():
            counts["lower"] += 1
        elif char in string.punctuation:
            counts["punctuation"] += 1
        elif char.isdigit():
            counts["digits"] += 1
        elif char.isspace():
            counts["spaces"] += 1

    return counts
