import tkinter as tk
from tkinter import messagebox

def send_notif_date(persons_list: list):
    """
    Affiche une notification pop-up si la liste des personnes 
    n'est pas vide.
    
    Args:
        persons_list (list): La liste des noms renvoyée par 
                             get_persons_celebtrating().
    """
    
    # 1. Ne rien faire si la liste est vide
    if not persons_list:
        print("Aucun anniversaire à notifier aujourd'hui.")
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

