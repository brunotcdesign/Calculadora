import tkinter as tk

def calcular():
    num1 = float(entrada_num1.get())
    num2 = float(entrada_num2.get())
    num3 = float(entrada_num3.get())
    num4 = float(entrada_num4.get())
    num5 = float(entrada_num5.get())

    operacao = operacao_var.get()

    if operacao == "Adição":
        resultado = num1 + num2 + num3 + num4 + num5
    elif operacao == "Subtração":
        resultado = num1 - num2 - num3 - num4 - num5
    elif operacao == "Multiplicação":
        resultado = num1 * num2 * num3 * num4 * num5
    elif operacao == "Divisão":
        resultado = num1 / num2 / num3 / num4 / num5
    else:
        resultado = "Erro"

    resultado_label.config(text=f"Resultado: {resultado}")

root = tk.Tk()
root.title("Calculadora com 5 Entradas")

entrada_num1 = tk.Entry(root)
entrada_num1.pack()

entrada_num2 = tk.Entry(root)
entrada_num2.pack()

entrada_num3 = tk.Entry(root)
entrada_num3.pack()

entrada_num4 = tk.Entry(root)
entrada_num4.pack()

entrada_num5 = tk.Entry(root)
entrada_num5.pack()

operacoes = ["Adição", "Subtração", "Multiplicação", "Divisão"]
operacao_var = tk.StringVar(root)
operacao_var.set(operacoes[0])
operacao_menu = tk.OptionMenu(root, operacao_var, *operacoes)
operacao_menu.pack()

calcular_botao = tk.Button(root, text="Calcular", command=calcular)
calcular_botao.pack()

resultado_label = tk.Label(root, text="")
resultado_label.pack()

root.mainloop()