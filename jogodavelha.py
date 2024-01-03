import tkinter as tk
from tkinter import messagebox

class JogoDaVelha:
    def __init__(self):
        self.janela = tk.Tk()
        self.janela.title("Jogo da Velha")
        self.iniciar_jogo()

    def iniciar_jogo(self):
        self.tabuleiro = [" "] * 9
        self.jogador_atual = "X"

        self.botoes = []
        for i in range(3):
            for j in range(3):
                botao = tk.Button(self.janela, text=" ", font=("Helvetica", 24), width=5, height=2,
                                  command=lambda row=i, col=j: self.clique_botao(row, col))
                botao.grid(row=i, column=j)
                self.botoes.append(botao)

    def clique_botao(self, row, col):
        index = 3 * row + col
        if self.tabuleiro[index] == " ":
            self.tabuleiro[index] = self.jogador_atual
            self.botoes[index]["text"] = self.jogador_atual

            if self.verificar_vitoria():
                messagebox.showinfo("Fim de Jogo", f"Jogador {self.jogador_atual} venceu!")
                self.resetar_jogo()
            elif " " not in self.tabuleiro:
                messagebox.showinfo("Fim de Jogo", "O jogo empatou!")
                self.resetar_jogo()
            else:
                self.jogador_atual = "O" if self.jogador_atual == "X" else "X"

    def verificar_vitoria(self):
        # Verifica linhas, colunas e diagonais
        for i in range(3):
            # Linhas
            if self.tabuleiro[i * 3] == self.tabuleiro[i * 3 + 1] == self.tabuleiro[i * 3 + 2] != " ":
                return True
            # Colunas
            if self.tabuleiro[i] == self.tabuleiro[i + 3] == self.tabuleiro[i + 6] != " ":
                return True
        # Diagonais
        if self.tabuleiro[0] == self.tabuleiro[4] == self.tabuleiro[8] != " ":
            return True
        if self.tabuleiro[2] == self.tabuleiro[4] == self.tabuleiro[6] != " ":
            return True
        return False

    def resetar_jogo(self):
        for i in range(9):
            self.tabuleiro[i] = " "
            self.botoes[i]["text"] = " "
        self.jogador_atual = "X"

if __name__ == "__main__":
    jogo = JogoDaVelha()
    jogo.janela.mainloop()
