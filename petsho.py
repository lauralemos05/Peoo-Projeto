import tkinter as tk
from tkinter import messagebox

class Pet:
    def __init__(self, nome, especie, idade):
        self.nome = nome
        self.especie = especie
        self.idade = idade

class PetShopApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Pet Shop")
        
        self.pets = []

        self.create_widgets()

    def create_widgets(self):
        self.label_nome = tk.Label(self.master, text="Nome:")
        self.label_nome.grid(row=0, column=0, sticky="e")

        self.entry_nome = tk.Entry(self.master)
        self.entry_nome.grid(row=0, column=1)

        self.label_especie = tk.Label(self.master, text="Espécie:")
        self.label_especie.grid(row=1, column=0, sticky="e")

        self.entry_especie = tk.Entry(self.master)
        self.entry_especie.grid(row=1, column=1)

        self.label_idade = tk.Label(self.master, text="Idade:")
        self.label_idade.grid(row=2, column=0, sticky="e")

        self.entry_idade = tk.Entry(self.master)
        self.entry_idade.grid(row=2, column=1)

        self.button_adicionar = tk.Button(self.master, text="Adicionar Pet", command=self.adicionar_pet)
        self.button_adicionar.grid(row=3, column=0, columnspan=2, pady=10)

        self.listbox_pets = tk.Listbox(self.master)
        self.listbox_pets.grid(row=4, column=0, columnspan=2, pady=10)

        self.button_excluir = tk.Button(self.master, text="Excluir Pet", command=self.excluir_pet)
        self.button_excluir.grid(row=5, column=0, columnspan=2, pady=10)

    def adicionar_pet(self):
        nome = self.entry_nome.get()
        especie = self.entry_especie.get()
        idade = self.entry_idade.get()

        if nome and especie and idade:
            pet = Pet(nome, especie, idade)
            self.pets.append(pet)
            self.listbox_pets.insert(tk.END, f"{pet.nome} - {pet.especie} - {pet.idade} anos")
        else:
            messagebox.showwarning("Campos vazios", "Por favor, preencha todos os campos.")

    def excluir_pet(self):
        selected_index = self.listbox_pets.curselection()

        if selected_index:
            pet = self.pets.pop(selected_index[0])
            self.listbox_pets.delete(selected_index)
            messagebox.showinfo("Pet removido", f"{pet.nome} removido com sucesso.")
        else:
            messagebox.showwarning("Nenhum pet selecionado", "Por favor, selecione um pet para remover.")

if __name__ == "__main__":
    root = tk.Tk()
    app = PetShopApp(root)
    root.mainloop()



