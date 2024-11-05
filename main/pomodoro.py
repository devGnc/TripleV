import tkinter as tk


class PomodoroWindow:
    def __init__(self, root):
        self.root = tk.Toplevel(root)  # Crée une nouvelle fenêtre
        self.root.title("Pomodoro Timer")
        self.root.geometry("1280x720")

        # Titre de la fenêtre
        title_label = tk.Label(self.root, text="Pomodoro Timer", font=("Arial", 36, "bold"))
        title_label.pack(pady=40)

        # Bouton "Retour" pour revenir à la page d'accueil (en bas à droite)
        back_button = tk.Button(self.root, text="Retour à l'accueil", font=("Arial", 16),
                                command=self.return_to_home)
        back_button.pack(anchor="se", padx=20, pady=20)

        self.main_root = root  # Référence à la fenêtre principale

    def return_to_home(self):
        self.root.destroy()  # Ferme la fenêtre Pomodoro
        self.main_root.deiconify()  # Restaure la fenêtre principale