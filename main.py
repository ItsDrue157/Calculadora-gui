from tkinter import *
import os
#op de limpar o campo de expressao
def clear():
    global expression
    expression = ""
    equacao.set("")
#adicionando ao campo de expressao
def adicionar(num):
    global expression
    expression = expression + str(num)
    equacao.set(expression)
#op de calcular

def calcular():
    try:
        global expression
        resultado = str(eval(expression))  
        equacao.set(resultado)
        expression = resultado   
    except:
        equacao.set("Erro")
        expression = "" 
#op de divisao
def dividir():
    try:
        global expression
        resultado = str(eval(expression))  
        equacao.set(resultado)
        expression = resultado   
    except:
        equacao.set("Erro")
        expression = "" 
#op de multiplicacao

def multiplicar():
    try:
        global expression
        resultado = str(eval(expression))  
        equacao.set(resultado)
        expression = resultado   
    except:
        equacao.set("Erro")
        expression = "" 

if __name__ == "__main__":
    janela = Tk()
    janela.configure(background="light green")
    janela.title("Calculadora")
    janela.geometry("450x400")

    # variavel para armazenar a expressao digitada
    expression = ""
    equacao = StringVar()

    # Campo de entrada para a expressão
    expression_field = Entry(janela, textvariable=equacao)
    expression_field.grid(row=0, column=0, columnspan=4, ipadx=70)
    
    
    #botoes
    button1 = Button(janela, text=' 1 ', fg='black', bg='white', command=lambda: press('1'), height=1, width=7)
    button1.grid(row=1, column=0, padx=10, pady=10)
    #botao2
    button2 = Button(janela, text='2', fg='black', bg='white', command=lambda: press('2'), height=1, width=7)
    button2.grid(row=1, column=1, padx=10, pady=10)
    #botao3
    button3 = Button(janela, text='3', fg='black', bg='white', command=lambda: press('3'), height=1, width=7)
    button3.grid(row=1, column=2, padx=10, pady=10)
    
    button4 = Button(janela, text='4', fg='black', bg='white',command=lambda: press('4'), height=1, width=7 )
    button4.grid(row=2, column=0, padx=10, pady=10 )
    
    button5 = Button(janela, text='5', fg='black', bg='white',command=lambda: press('5'), height=1, width=7 )
    button5.grid(row=2, column=1, padx=10, pady=10 )

    button6 = Button(janela, text='6', fg='black', bg='white',command=lambda: press('6'), height=1, width=7 )
    button6.grid(row=2, column=2, padx=10, pady=10 )

    button7 = Button(janela, text='7', fg='black', bg='white',command=lambda: press('7'), height=1, width=7 )
    button7.grid(row=3, column=0, padx=10, pady=10 )
    
    button8 = Button(janela, text='8', fg='black', bg='white',command=lambda: press('8'), height=1, width=7 )
    button8.grid(row=3, column=1, padx=10, pady=10 )
    
    button9 = Button(janela, text='9', fg='black', bg='white',command=lambda: press('9'), height=1, width=7 )
    button9.grid(row=3, column=2, padx=10, pady=10 )
    
    #limpar o campo das expressoes
    limpar = Button(janela, text='Limpar', fg='black', bg='white', command=clear, height=1, width=7)
    limpar.grid(row=2, column=5)
    
    #adicao
    adicionar = Button(janela, text='+', fg='black', bg='white', command=lambda: press('+'), height=1, width=7, )
    adicionar.grid(row=1, column= 5, padx=(15))
    #botoes de acao:
    menos = Button(janela, text=' - ', fg='black', bg='white', command=lambda: press('-'), height=1, width=7 ) 
    menos.grid(row=2, column=4)
    
    #calcular
    igual = Button(janela, text=' = ', fg='black', bg='white', command=calcular, height=1, width=7)
    igual.grid(row=1, column=4,)
    
    #dividir
    divide = Button(janela, text='/', fg='black', bg='white', command=lambda: press('/'), height=1, width=7)
    divide.grid(row=3, column=4)
    
    #multiplicar
    multiplica = Button(janela, text='*', fg='black', bg='white', command=lambda: press('*'), height=1, width=7)
    multiplica.grid(row=3, column=5)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    









    
    








#fazer botoes
def press(num):
    global expression
    expression= expression + str(num)
    equacao.set(expression) 
def clear(): 
    global expression 
    expression = "" 
    equacao.set("") 

    
    







#manter a janela aberta 
janela.mainloop()
