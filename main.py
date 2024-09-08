from tkinter import *
# configurações iniciais/ nome e tamanho do programa
root = Tk()
root.title('Calculadora python')
root.geometry('408x355')
root.minsize(408,355)
root.maxsize(408,355)

# variaveis 
numero1 = ''
divisao = False
multiplica = False
subtracao = False
adicao = False

root.configure(background='#1C1C1C')
# caixa de entrada para os numeros
ent = Entry(root, width=15, borderwidth=4, relief=FLAT, fg='#FFFFFF', bg='#363636', font=('futura', 25, 'bold'), justify=CENTER)
ent.grid(row=0,
        column=0,
        columnspan=4,
        pady=2)

# funções para realizar as operações
def botao_divide():
    global numero1
    global divisao
    divisao = TRUE
    numero1 = ent.get()
    ent.delete(0, END)

def botao_click(num):
    ent.insert(END, num)

def botao_multiplica():
    global numero1
    global multiplica
    multiplica = TRUE
    numero1 = ent.get()
    ent.delete(0, END)
    
def botao_subtracao():
    global numero1
    global subtracao
    subtracao = TRUE
    numero1 = ent.get()
    ent.delete(0, END)

def botao_adicao():
    global numero1
    global adicao
    adicao = TRUE
    numero1 = ent.get()
    ent.delete(0, END)

def botao_clear():
    ent.delete(0, END)

def botao_igualdade(): # botão de igualde com a lógica das operações
    global subtracao, adicao, multiplica, divisao
    numero2 = ent.get()
    ent.delete(0, END)
    if adicao == TRUE:
        ent.insert(0, int(numero1) + int(numero2))
        adicao = FALSE
    if multiplica == TRUE:
        ent.insert(0, int(numero1) * int(numero2))
        multiplica = FALSE
    if subtracao == TRUE:
        ent.insert(0, int(numero1) - int(numero2))
        subtracao = FALSE
    if divisao == TRUE:
        ent.insert(0, int(numero1) / int(numero2))
        divisao = FALSE
    

div = Button(root,text='÷', padx=40, pady=20, command=botao_divide, fg='#FFFFFF', activeforeground='#FFFFFF', bg='#2F4F4F', activebackground='#2F4F4F',relief=FLAT,font=('futura', 12,'bold'))
div.grid(row=0,column=4)

# elementos da linha 1 (numeros 1, 2, 3 e multiplicação)
um = Button(root,text='1', padx=40, pady=20, command=lambda: botao_click(1), fg='#FFFFFF', activeforeground='#FFFFFF', bg='#363636', activebackground='#363636',relief=FLAT,font=('futura', 12,'bold'))
um.grid(row=1,column=1)

dois = Button(root,text='2', padx=40, pady=20, command=lambda: botao_click(2), fg='#FFFFFF', activeforeground='#FFFFFF', bg='#363636', activebackground='#363636',relief=FLAT,font=('futura', 12,'bold'))
dois.grid(row=1,column=2)

tres = Button(root,text='3', padx=42, pady=20, command=lambda: botao_click(3), fg='#FFFFFF', activeforeground='#FFFFFF', bg='#363636', activebackground='#363636',relief=FLAT,font=('futura', 12,'bold'))
tres.grid(row=1, column=3)

mult = Button(root,text='x', padx=41, pady=20, command=botao_multiplica, fg='#FFFFFF', activeforeground='#FFFFFF', bg='#2F4F4F', activebackground='#2F4F4F',relief=FLAT,font=('futura', 12, 'bold'))
mult.grid(row=1, column=4)

# elementos da linha 2 (numeros 4, 5, 6 e subtração)

quatro =  Button(root,text='4', padx=40, pady=20, command=lambda: botao_click(4), fg='#FFFFFF', activeforeground='#FFFFFF', bg='#363636', activebackground='#363636',relief=FLAT,font=('futura', 12,'bold'))
quatro.grid(row=2,column=1)

cinco =  Button(root,text='5', padx=40, pady=20, command=lambda: botao_click(5), fg='#FFFFFF', activeforeground='#FFFFFF', bg='#363636', activebackground='#363636',relief=FLAT,font=('futura', 12,'bold'))
cinco.grid(row=2,column=2)

seis =  Button(root,text='6', padx=42, pady=20, command=lambda: botao_click(6), fg='#FFFFFF', activeforeground='#FFFFFF', bg='#363636', activebackground='#363636',relief=FLAT,font=('futura', 12,'bold'))
seis.grid(row=2,column=3)

sub = Button(root,text='-', padx=43, pady=20, command=botao_subtracao, fg='#FFFFFF', activeforeground='#FFFFFF', bg='#2F4F4F', activebackground='#2F4F4F',relief=FLAT,font=('futura', 12, 'bold'))
sub.grid(row=2,column=4)

# elementos da linha 3 (numeros 7, 8, 9 e adição)

sete = Button(root,text='7', padx=40, pady=20, command=lambda: botao_click(7), fg='#FFFFFF', activeforeground='#FFFFFF', bg='#363636', activebackground='#363636',relief=FLAT,font=('futura', 12,'bold'))
sete.grid(row=3,column=1)

oito = Button(root,text='8', padx=40, pady=20, command=lambda: botao_click(8), fg='#FFFFFF', activeforeground='#FFFFFF', bg='#363636', activebackground='#363636',relief=FLAT,font=('futura', 12,'bold'))
oito.grid(row=3,column=2)

nove = Button(root,text='9', padx=42, pady=20, command=lambda: botao_click(9), fg='#FFFFFF', activeforeground='#FFFFFF', bg='#363636', activebackground='#363636',relief=FLAT,font=('futura', 12,'bold'))
nove.grid(row=3,column=3)

adi = Button(root,text='+', padx=41, pady=20, command=botao_adicao, fg='#FFFFFF', activeforeground='#FFFFFF', bg='#2F4F4F', activebackground='#2F4F4F',relief=FLAT,font=('futura', 12, 'bold'))
adi.grid(row=3,column=4)

# elementos da linha 4 (numero 0, clear e igualdade)

zero = Button(root,text='0', padx=91, pady=20, command=lambda: botao_click(0), fg='#FFFFFF', activeforeground='#FFFFFF', bg='#363636', activebackground='#363636',relief=FLAT,font=('futura', 12,'bold'))
zero.grid(row=4,column=1, columnspan=2)

clear = Button(root,text='C', padx=40.2, pady=20, command=botao_clear, fg='#FFFFFF', activeforeground='#FFFFFF', bg='#FF8C00', activebackground='#FF8C00',relief=FLAT,font=('futura', 12, 'bold'))
clear.grid(row=4,column=3)

igualdade = Button(root,text='=', padx=41.2, pady=20, command=botao_igualdade, fg='#FFFFFF', activeforeground='#FFFFFF', bg='#2F4F4F', activebackground='#2F4F4F',relief=FLAT,font=('futura', 12, 'bold'))
igualdade.grid(row=4,column=4)

root.mainloop()
