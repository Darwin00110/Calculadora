import tkinter as tk
import os
class Calculadora:
    def __init__(self, visor):
        self.visor = visor
        self.valorInicial = None
        self.valorFinal = None
        self.operador = None
        self.jaClicado = False

    def config(self, valor):
        if self.jaClicado:
            if self.valorFinal is None:
                self.valorFinal = str(valor)
            else:
                self.valorFinal += str(valor)
            self.visor.delete(0, tk.END)
            self.visor.insert(0, f"{self.valorInicial} {self.operador} {self.valorFinal}")
        else:
            if self.valorInicial is None:
                self.valorInicial = str(valor)
            else:
                self.valorInicial += str(valor)
            self.visor.delete(0, tk.END)
            self.visor.insert(0, self.valorInicial)

    def operadores(self, operador):
        if self.valorInicial is not None:
            self.jaClicado = True
            self.operador = operador
            self.visor.delete(0, tk.END)
            self.visor.insert(0, f"{self.valorInicial} {self.operador}")

    def Resultado(self):
        if self.valorInicial is None or self.valorFinal is None or self.operador is None:
            self.visor.delete(0, tk.END)
            self.visor.insert(0, "Operação inválida!")
            self.visor.config(fg="red")
            return

        a = int(self.valorInicial)
        b = int(self.valorFinal)
        resultado = 0

        try:
            if self.operador == "+":
                resultado = a + b
            elif self.operador == "-":
                resultado = a - b
            elif self.operador == "x":
                resultado = a * b
            elif self.operador == "/":
                resultado = a / b

            self.visor.delete(0, tk.END)
            self.visor.insert(0, f"{a} {self.operador} {b} = {resultado}")
            self.visor.config(fg="black")

        except Exception as e:
            self.visor.delete(0, tk.END)
            self.visor.insert(0, f"Erro: {str(e)}")
            self.visor.config(fg="red")

    def limparVisor(self):
        self.jaClicado = False
        self.valorInicial = None
        self.valorFinal = None
        self.operador = None
        self.visor.delete(0, tk.END)
        self.visor.config(fg="black")

tela = tk.Tk()
tela.geometry("300x300")
tela.title("Calculadora")
tela.config(bg="#0D1B2A")

molde = tk.Frame(tela, bg="#1B263B")
molde.place(rely=0.2, relwidth=1.0, relheight=0.8)

molde_visor = tk.Frame(tela, bg="#092A48")
molde_visor.place(x=0, y=0, relwidth=1.0, relheight=0.2)

visor = tk.Entry(molde_visor, font=("Arial", 14))
visor.place(relwidth=0.95, relheight=0.6, relx=0.02, rely=0.18)

calculadora = Calculadora(visor)

for i in range(4): molde.grid_columnconfigure(i, weight=1)
for j in range(4): molde.grid_rowconfigure(j, weight=1)

botoes = [
    ("7", 0, 0), ("8", 0, 1), ("9", 0, 2), ("+", 0, 3),
    ("4", 1, 0), ("5", 1, 1), ("6", 1, 2), ("-", 1, 3),
    ("1", 2, 0), ("2", 2, 1), ("3", 2, 2), ("x", 2, 3),
    ("0", 3, 0), ("C", 3, 1), ("=", 3, 2), ("/", 3, 3)
]

for (txt, r, c) in botoes:
    if txt.isdigit():
        cmd = lambda x=txt: calculadora.config(int(x))
    elif txt == "C":
        cmd = calculadora.limparVisor
    elif txt == "=":
        cmd = calculadora.Resultado
    else:
        cmd = lambda x=txt: calculadora.operadores(x)

    tk.Button(molde, text=txt, bg="#778DA9", fg="white", font=("Arial", 12), bd=3, relief="raised",
              command=cmd).grid(row=r, column=c, padx=5, pady=5, sticky="nsew")

caminhoIcon = os.path.join("Calculadora", "Calculadora", "calculadora.ico")
caminhoAbsoluto = os.path.abspath(caminhoIcon)
if os.path.exists(caminhoAbsoluto):
    tela.iconbitmap(caminhoAbsoluto)
else:
    print("o caminho solicitado não existe", caminhoAbsoluto)

tela.mainloop()