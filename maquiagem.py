import tkinter as tk
from tkinter import messagebox

class Cliente:
    def __init__(self, nome, horario, dia):
        self.nome = nome
        self.horario = horario
        self.dia = dia

class MaquiadoraApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Agendamento Maquiagem")
        
        self.clientes = []

        self.create_widgets()

    def create_widgets(self):
        self.label_nome = tk.Label(self.master, text="Nome do Cliente:")
        self.label_nome.grid(row=0, column=0, sticky="e")

        self.entry_nome = tk.Entry(self.master)
        self.entry_nome.grid(row=0, column=1)

        self.label_horario = tk.Label(self.master, text="Horário:")
        self.label_horario.grid(row=1, column=0, sticky="e")

        self.entry_horario = tk.Entry(self.master)
        self.entry_horario.grid(row=1, column=1)

        self.label_dia = tk.Label(self.master, text="Dia da Maquiagem:")
        self.label_dia.grid(row=2, column=0, sticky="e")

        self.entry_dia = tk.Entry(self.master)
        self.entry_dia.grid(row=2, column=1)

        self.button_agendar = tk.Button(self.master, text="Agendar Maquiagem", command=self.agendar_maquiagem)
        self.button_agendar.grid(row=3, column=0, columnspan=2, pady=10)

        self.listbox_clientes = tk.Listbox(self.master, height=10, width=50)  # Ajuste o tamanho aqui
        self.listbox_clientes.grid(row=4, column=0, columnspan=2, pady=10)

        self.button_cancelar = tk.Button(self.master, text="Cancelar Agendamento", command=self.cancelar_agendamento)
        self.button_cancelar.grid(row=5, column=0, columnspan=2, pady=10)

    def agendar_maquiagem(self):
        nome = self.entry_nome.get()
        horario = self.entry_horario.get()
        dia = self.entry_dia.get()

        if nome and horario and dia:
            cliente = Cliente(nome, horario, dia)
            self.clientes.append(cliente)
            self.listbox_clientes.insert(tk.END, f"{cliente.nome} - Dia: {cliente.dia} - Horário: {cliente.horario}")
        else:
            messagebox.showwarning("Campos vazios", "Por favor, preencha todos os campos.")

    def cancelar_agendamento(self):
        selected_index = self.listbox_clientes.curselection()

        if selected_index:
            cliente = self.clientes.pop(selected_index[0])
            self.listbox_clientes.delete(selected_index)
            messagebox.showinfo("Agendamento cancelado", f"{cliente.nome} teve o agendamento cancelado.")
        else:
            messagebox.showwarning("Nenhum agendamento selecionado", "Por favor, selecione um agendamento para cancelar.")

if __name__ == "__main__":
    root = tk.Tk()
    app = MaquiadoraApp(root)
    root.mainloop()
