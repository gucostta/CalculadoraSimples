import tkinter as tk
from tkinter import ttk

def adicionar_numero(numero):
    entry_numero.insert(tk.END, numero)

def adicionar_operacao(operacao):
    entry_numero.insert(tk.END, operacao)

def calcular():
    try:
        expressao = entry_numero.get()
        resultado = eval(expressao)
        label_resultado.config(text="Resultado: " + str(resultado))
    except Exception as e:
        label_resultado.config(text="Erro: " + str(e))

janela = tk.Tk()
janela.title("Calculadora Moderna")

# Define o ícone da janela
janela.iconphoto(True, tk.PhotoImage(file='keys.png'))

# Frame principal
frame_principal = ttk.Frame(janela)
frame_principal.grid(row=0, column=0, padx=20, pady=20)

# Entrada para a expressão
entry_numero = ttk.Entry(frame_principal, font=('Helvetica', 14))
entry_numero.grid(row=0, column=0, columnspan=4, padx=5, pady=5)

# Botões para números
for i in range(10):
    ttk.Button(frame_principal, text=str(i), command=lambda i=i: adicionar_numero(str(i))).grid(row=(i // 3) + 1, column=(i % 3), padx=5, pady=5)

# Botões para operações
operacoes = ["+", "-", "*", "/"]
for i, operacao in enumerate(operacoes):
    ttk.Button(frame_principal, text=operacao, command=lambda operacao=operacao: adicionar_operacao(operacao)).grid(row=i + 1, column=3, padx=5, pady=5)

# Botão de igual
ttk.Button(frame_principal, text="=", command=calcular).grid(row=4, column=0, columnspan=2, padx=5, pady=5)

# Botão de limpar
ttk.Button(frame_principal, text="C", command=lambda: entry_numero.delete(0, tk.END)).grid(row=4, column=2, columnspan=2, padx=5, pady=5)

# Label para o resultado
label_resultado = ttk.Label(frame_principal, text="Resultado: ", font=('Helvetica', 12))
label_resultado.grid(row=5, column=0, columnspan=4)

# Executar a janela
janela.mainloop()


