import json
from datetime import datetime

def get_persons_celebtrating(date: str = '2025-11-08') -> list:
    """
    Récupère les personnes qui fêtent leur anniversaire à une date donnée.
    
    Args:
        date (str): La date à vérifier, au format YYYY-MM-DD.
    """
    
    # 1. Chargement des données (ajout de l'encodage)
    try:
        with open("data/birthday_data.json", "r", encoding="utf-8") as file:
            birthday_data = json.load(file)
    except FileNotFoundError:
        print(f"Erreur: Le fichier 'birthday_data.json' n'a pas été trouvé.")
        return []
    except json.JSONDecodeError:
        print(f"Erreur: Le fichier 'birthday_data.json' n'est pas un JSON valide.")
        return []

    # 2. Analyse de la date d'entrée (au lieu de time.localtime())
    try:
        # Convertit la chaîne 'YYYY-MM-DD' en objet datetime
        date_obj = datetime.strptime(date, '%Y-%m-%d')
    except ValueError:
        print(f"Erreur: Le format de date '{date}' est invalide. "
              "Veuillez utiliser le format YYYY-MM-DD.")
        return []

    # 3. Extraction du jour et du mois au format du JSON
    # .strftime("%d") -> "08"
    # .strftime("%b") -> "Nov" (grâce à la locale 'C')
    target_day = date_obj.strftime("%d")
    target_month_abbr = date_obj.strftime("%b")

    # 4. Vérification et filtrage
    if target_month_abbr not in birthday_data:
        # Si le mois (ex: "Nov") n'existe pas comme clé dans le JSON
        return []

    # Récupère les noms (k) dans le sous-dict du mois (ex: birthday_data["Nov"])
    # où le jour (v) correspond au jour cible (target_day)
    persons_celebrating = [
        k for k, v in birthday_data[target_month_abbr].items() 
        if v == target_day
    ]
    
    return persons_celebrating

