from tkinter import *
from tkinter import ttk

# ---------cores -----------

co0 = '#ffffff' #white
co1 = '#89cbd1' #cian
co2 = '#2b5985' #blue

janela = Tk()
janela.title("")
janela.geometry('295x230')
janela.configure(bg=co0)

# ---- dividindo a janela em duas partes.-------

frame_cima = Frame(janela, width=295, height=50, bg=co0, pady=0, padx=0, relief='flat')
frame_cima.grid(row=0, column=0, sticky=NSEW)

frame_baixo = Frame(janela, width=295, height=180, bg=co0, pady=0, padx=0, relief='flat')
frame_baixo.grid(row=1, column=0, sticky=NSEW)

# ----- configurando frame cima -------
txt1 = 'Calculadora de IMC'

app_nome = Label(frame_cima, text =txt1, width=23, height=1, padx=0, relief='flat', anchor='center', font=('Ivy 16 bold'), bg=co0, fg=co2 )
app_nome.place(x=0, y=0)

app_linha = Label(frame_cima, text ='', width=400, height=1, padx=0, relief='flat', anchor='center', font=('Ivy 1'), bg=co1 )
app_linha.place(x=0, y=35)

# ----------- calculos --------------

def calcular():
    peso = float(e_peso.get())
    altura = float(e_altura.get())

    imc = peso / altura**2

    if imc < 18.5:
        e_resultado_texto['text'] ='Seu IMC é: abaixo do peso.'
    elif imc >= 18.5 and imc < 25:
        e_resultado_texto['text'] ='Seu IMC é: normal.'
    elif imc >= 25 and imc < 30:
       e_resultado_texto['text'] ='Seu IMC é: sobrepeso.'
    else:
        e_resultado_texto['text'] = 'Sei IMC é: obeso'

    l_resultado['text'] = "{:.{}f}".format(imc, 2)

# ----- configurando frame baixo -------

txt2 = 'Insira seu peso'
txt3 = 'Insira sua altura'
txt4 = '---'
txt6 = 'Calcular'

l_peso = Label(frame_baixo, text =txt2, height=1, padx=0, relief='flat', anchor='center', font=('Ivy 10 bold'), bg=co0, fg=co2 )
l_peso.grid(row=0, column=0, sticky=NSEW, pady=10, padx=3)
e_peso = Entry(frame_baixo, width=5, relief='solid', font=('Ivy 10 bold'), justify='center')
e_peso.grid(row=0, column=1, sticky=NSEW, pady=10, padx=3)

l_altura = Label(frame_baixo, text =txt3, height=1, padx=0, relief='flat', anchor='center', font=('Ivy 10 bold'), bg=co0, fg=co2 )
l_altura.grid(row=1, column=0, sticky=NSEW, pady=10, padx=3)
e_altura = Entry(frame_baixo, width=5, relief='solid', font=('Ivy 10 bold'), justify='center')
e_altura.grid(row=1, column=1, sticky=NSEW, pady=10, padx=3)

l_resultado = Label(frame_baixo, text =txt4, width=5, height=1, padx=6, pady=12,  relief='flat', anchor='center', font=('Ivy 24 bold'), bg=co2, fg=co0 )
l_resultado.place(x=175, y=10)

e_resultado_texto = Label(frame_baixo, text ='', width=37, height=1, padx=0, pady=12,  relief='flat', anchor='center', font=('Ivy 10 bold'), bg=co0, fg=co2 )
e_resultado_texto.place(x=0, y=85)

e_calcular = Button(frame_baixo, command=calcular, text =txt6, width=34, overrelief=SOLID, height=1, relief='raised', anchor='center', font=('Ivy 10 bold'), bg=co2, fg=co0 )
e_calcular.grid(row=4, column=0, sticky=NSEW, pady=60, padx=5, columnspan=30)

janela.mainloop()
