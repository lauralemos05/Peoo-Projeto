import tkinter as tk
from tkinter import messagebox
import random

class JogoDaForca:
    def __init__(self, root):
        self.root = root
        self.root.title("Jogo da Forca")

        self.palavras = ["PYTHON", "CASA", "JAVASCRIPT", "HTML", "CSS", "GITHUB", "PROGRAMACAO"]

        self.palavra_secreta = ""
        self.palavra_descoberta = []

        self.tentativas_maximas = 6
        self.tentativas_atuais = 0

        self.inicializar_jogo()

    def inicializar_jogo(self):
        self.palavra_secreta = random.choice(self.palavras).upper()
        self.palavra_descoberta = ["_"] * len(self.palavra_secreta)
        self.tentativas_atuais = 0

        self.criar_interface()

    def criar_interface(self):
        self.label_palavra = tk.Label(self.root, text=" ".join(self.palavra_descoberta), font=("Helvetica", 16))
        self.label_palavra.pack(pady=10)

        self.entry_letra = tk.Entry(self.root, font=("Helvetica", 14))
        self.entry_letra.pack(pady=10)

        self.botao_tentar = tk.Button(self.root, text="Tentar", command=self.verificar_tentativa)
        self.botao_tentar.pack(pady=10)

        self.botao_reiniciar = tk.Button(self.root, text="Reiniciar Jogo", command=self.inicializar_jogo)
        self.botao_reiniciar.pack(pady=10)

    def verificar_tentativa(self):
        letra = self.entry_letra.get().upper()

        if letra.isalpha() and len(letra) == 1:
            if letra in self.palavra_secreta:
                for i in range(len(self.palavra_secreta)):
                    if self.palavra_secreta[i] == letra:
                        self.palavra_descoberta[i] = letra

                self.label_palavra.config(text=" ".join(self.palavra_descoberta))

                if "_" not in self.palavra_descoberta:
                    messagebox.showinfo("Parabéns!", "Você ganhou!\nA palavra era: {}".format(self.palavra_secreta))
                    self.inicializar_jogo()
            else:
                self.tentativas_atuais += 1
                self.atualizar_forca()

                if self.tentativas_atuais == self.tentativas_maximas:
                    messagebox.showinfo("Fim de Jogo", "Você perdeu!\nA palavra era: {}".format(self.palavra_secreta))
                    self.inicializar_jogo()
        else:
            messagebox.showwarning("Aviso", "Digite uma letra válida.")

    def atualizar_forca(self):
        if self.tentativas_atuais == 1:
            self.desenhar_cabeca()
        elif self.tentativas_atuais == 2:
            self.desenhar_tronco()
        elif self.tentativas_atuais == 3:
            self.desenhar_braco_esquerdo()
        elif self.tentativas_atuais == 4:
            self.desenhar_braco_direito()
        elif self.tentativas_atuais == 5:
            self.desenhar_perna_esquerda()
        elif self.tentativas_atuais == 6:
            self.desenhar_perna_direita()
            messagebox.showinfo("Fim de Jogo", "Você perdeu!\nA palavra era: {}".format(self.palavra_secreta))
            self.inicializar_jogo()

    def desenhar_cabeca(self):
        messagebox.showinfo("Erro", "Cabeça")

    def desenhar_tronco(self):
        messagebox.showinfo("Erro", "Tronco")

    def desenhar_braco_esquerdo(self):
        messagebox.showinfo("Erro", "Braço Esquerdo")

    def desenhar_braco_direito(self):
        messagebox.showinfo("Erro", "Braço Direito")

    def desenhar_perna_esquerda(self):
        messagebox.showinfo("Erro", "Perna Esquerda")

    def desenhar_perna_direita(self):
        messagebox.showinfo("Erro", "Perna Direita")


if __name__ == "__main__":
    root = tk.Tk()
    jogo = JogoDaForca(root)
    root.mainloop()