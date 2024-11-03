import tkinter as tk
from tkinter import messagebox


# Classe principale de l'application
class TripleVApp:
    def __init__(self, root):
        self.root = root
        self.root.title("TripleV : Veni, Vidi, Vici")
        self.root.geometry("720x480")
        self.root.resizable(False, False)

        # Affichage du nom de l'application en haut, centré
        title_label = tk.Label(self.root, text="TripleV : Veni, Vidi, Vici", font=("Arial", 16, "bold"))
        title_label.pack(pady=20)

        # Création des boutons
        self.create_buttons()

        # Gestion de la fermeture de la fenêtre
        self.root.protocol("WM_DELETE_WINDOW", self.quit_app)

    def create_buttons(self):
        # Bouton pour le Timer Pomodoro
        pomodoro_button = tk.Button(self.root, text="Timer Pomodoro", font=("Arial", 12), command=self.open_pomodoro)
        pomodoro_button.pack(pady=10)

        # Bouton pour l'Outil de Prise de Notes
        notes_button = tk.Button(self.root, text="Outil de Prise de Notes", font=("Arial", 12), command=self.open_notes)
        notes_button.pack(pady=10)

        # Bouton pour la To-Do List
        todo_button = tk.Button(self.root, text="To-Do List", font=("Arial", 12), command=self.open_todo)
        todo_button.pack(pady=10)

        # Bouton pour quitter l'application
        quit_button = tk.Button(self.root, text="Quitter", font=("Arial", 12), command=self.quit_app)
        quit_button.pack(pady=20)

    def open_pomodoro(self):
        pomodoro = Pomodoro()
        pomodoro.show()

    def open_notes(self):
        notes = Notes()
        notes.show()

    def open_todo(self):
        todo = ToDo()
        todo.show()

    def quit_app(self):
        self.root.quit()


# Classe pour la fonctionnalité Timer Pomodoro
class Pomodoro:
    def show(self):
        messagebox.showinfo("Pomodoro", "Ouverture du timer Pomodoro...")


# Classe pour la fonctionnalité de Prise de Notes
class Notes:
    def show(self):
        messagebox.showinfo("Notes", "Ouverture de l'outil de prise de notes...")


# Classe pour la fonctionnalité To-Do List
class ToDo:
    def show(self):
        messagebox.showinfo("To-Do List", "Ouverture de la To-Do List...")


# Point d'entrée de l'application
if __name__ == "__main__":
    root = tk.Tk()
    app = TripleVApp(root)
    root.mainloop()