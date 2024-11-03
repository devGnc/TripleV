import tkinter as tk
from tkinter import messagebox
import pomodoro
import notes
import todo


# Classe principale de l'application
class TripleVApp:
    def __init__(self, root):
        self.root = root
        self.root.title("TripleV : Veni, Vidi, Vici")
        self.root.geometry("1280x720")
        self.root.resizable(False, False)

        # Affichage du nom de l'application en haut, centré, en très grand
        title_label = tk.Label(self.root, text="TripleV : Veni, Vidi, Vici", font=("Arial", 36, "bold"))
        title_label.pack(pady=40)

        # Création des boutons et centrage
        self.create_buttons()

        # Gestion de la fermeture de la fenêtre avec sauvegarde
        self.root.protocol("WM_DELETE_WINDOW", self.quit_app)

    def create_buttons(self):
        # Cadre pour centrer les boutons horizontalement
        button_frame = tk.Frame(self.root)
        button_frame.pack(pady=100)

        # Bouton pour le Timer Pomodoro
        pomodoro_button = tk.Button(
            button_frame, text="Timer Pomodoro", font=("Arial", 20, "bold"),
            width=20, height=3, command=self.open_pomodoro
        )
        pomodoro_button.pack(pady=20)

        # Bouton pour l'Outil de Prise de Notes
        notes_button = tk.Button(
            button_frame, text="Outil de Prise de Notes", font=("Arial", 20, "bold"),
            width=20, height=3, command=self.open_notes
        )
        notes_button.pack(pady=20)

        # Bouton pour la To-Do List
        todo_button = tk.Button(
            button_frame, text="To-Do List", font=("Arial", 20, "bold"),
            width=20, height=3, command=self.open_todo
        )
        todo_button.pack(pady=20)

    def open_pomodoro(self):
        self.root.withdraw()  # Cache la fenêtre principale
        pomodoro.PomodoroWindow(self.root)  # Ouvre la fenêtre Pomodoro

    def open_notes(self):
        self.root.withdraw()
        notes.NotesWindow(self.root)  # Ouvre la fenêtre Notes

    def open_todo(self):
        self.root.withdraw()
        todo.ToDoWindow(self.root)  # Ouvre la fenêtre To-Do List

    def quit_app(self):
        # Action de sauvegarde (ajouter du code de sauvegarde ici si nécessaire)
        self.save_data()
        self.root.quit()

    def save_data(self):
        # Ici, on ajoute le code pour sauvegarder les données si nécessaire
        print("Données sauvegardées avec succès.")  # Exemple de retour pour vérifier la sauvegarde


# Point d'entrée de l'application
if __name__ == "__main__":
    root = tk.Tk()
    app = TripleVApp(root)
    root.mainloop()