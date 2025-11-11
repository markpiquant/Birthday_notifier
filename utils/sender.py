import json
import time
import pywhatkit
import tkinter      as tk
from tkinter        import messagebox
from pathlib        import Path

PATH = Path('C:\\Users\\markp\\Desktop\\VSC\\Birthday_Notifier\\Birthday_notifier')
DATAPATH = PATH / "data"

with open(DATAPATH / "phone_numbers.json", "r") as file:
    phone_numbers = json.load(file)

def send_notif_date(persons_list: list):
    """
    Affiche une notification pop-up si la liste des personnes 
    n'est pas vide.
    
    Args:
        persons_list (list): La liste des noms renvoyée par 
                             get_persons_celebtrating().
    """
    
    # 1. Ne rien faire si la liste est vide

    if not persons_list or persons_list == []:
        # 3. Initialisation et masquage de la fenêtre Tkinter
        root = tk.Tk()
        root.withdraw()  # Masquer la fenêtre principale

        # 4. Afficher la notification
        messagebox.showinfo("Birthday Notifier", 'Nothing to celebrate today')
        
        # 5. Détruire la fenêtre après utilisation
        # (Important pour que le script se termine)
        root.destroy()

        return

    # 2. Formater le message en fonction du nombre de personnes
    if len(persons_list) == 1:
        # Cas 1: Une seule personne
        names = persons_list[0]
        message = f"Aujourd'hui, c'est l'anniversaire de {names} !"
    
    elif len(persons_list) == 2:
        # Cas 2: Deux personnes
        names = f"{persons_list[0]} et {persons_list[1]}"
        message = f"Aujourd'hui, c'est l'anniversaire de {names} !"
    
    else:
        # Cas 3: Plus de deux personnes
        # Ex: "A, B, et C"
        names = ", ".join(persons_list[:-1]) + f", et {persons_list[-1]}"
        message = f"Aujourd'hui, c'est l'anniversaire de {names} !"

    # 3. Initialisation et masquage de la fenêtre Tkinter
    root = tk.Tk()
    root.withdraw()  # Masquer la fenêtre principale

    # 4. Afficher la notification
    messagebox.showinfo("🎉 Anniversaire 🎉", message)
    
    # 5. Détruire la fenêtre après utilisation
    # (Important pour que le script se termine)
    root.destroy()

def send_birthday_message(name: str, message: str):
    """
    Ouvre WhatsApp et ENVOIE automatiquement le message.
    """
    if name in phone_numbers:
        phone_number = phone_numbers[name]

        try:
            print(f"Tentative d'envoi à {name}...")

            # Ouvre WhatsApp (Web ou Desktop) et appuie sur "Entrée"
            # wait_time=15 : Laisse 15s à WhatsApp pour s'ouvrir avant d'appuyer sur Entrée
            # tab_close=True : Ferme l'onglet du navigateur après l'envoi
            pywhatkit.sendwhatmsg_instantly(
                phone_no=phone_number, 
                message=message,
                wait_time=15, 
                tab_close=True 
            )

            print(f"Message pour {name} envoyé (ou en cours d'envoi) !")
            # Ajoute un délai pour laisser le temps à la première fenêtre de se gérer
            time.sleep(10) 

        except Exception as e:
            print(f"Erreur lors de l'envoi à {name}: {e}")

    else:
        print(f"Erreur : Le nom '{name}' n'est pas dans le dictionnaire.")
