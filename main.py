from tkinter import *
import sqlite3
import os
global resultado
global expression_debug
#criando um banco de dados
def CriarDB():
    conn = sqlite3.connect('banco_de_dados.sql')
    cursor = conn.cursor()
    print("db feito")


    cursor.execute("""
                CREATE TABLE IF NOT EXISTS Historico (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                operacao VARCHAR (255) NOT NULL,
                resultado_final VARCHAR(255) NOT NULL
                )
                """)
    conn.commit()
    conn.close()
CriarDB()
pass





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

def calcular_operacao(operacao):
    try:
        global expression
        if operacao == "dividir":
            expression += " / "
        elif operacao == "multiplicar":
            expression += " * "
        else:
            resultado = str(eval(expression))  
            equacao.set(resultado)
            expression = resultado 
            adicionar_o_db(expression, resultado)
    except:
        equacao.set("Erro")
        expression = "" 
        
        
        
def adicionar_o_db(expression, resultado):
    if os.path.exists('banco_de_dados.sql'):
        conn = sqlite3.connect('banco_de_dados.sql')
        cursor = conn.cursor()
        query = """
            INSERT INTO Historico (operacao, resultado_final) VALUES (?,?)
        """
        cursor.execute(query, (int(expression), resultado))
        conn.commit()
        conn.close()

def pegarresultadodebug():
    expression_debug = expression
    print(expression_debug)


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
    igual = Button(janela, text=' = ', fg='black', bg='white', command=lambda: calcular_operacao("igual"),COMMAND=pegarresultadodebug(),  height=1, width=7)
    
    igual.grid(row=1, column=4,)
    
    
    #dividir
    dividir_button = Button(janela, text="/", command=lambda: calcular_operacao("dividir"),height=1, width=7)
    dividir_button.grid(row=3, column=4)
    
    #multiplicar
    multiplicar_button = Button(janela, text="*", command=lambda: calcular_operacao("multiplicar"),height=1, width=7)
    multiplicar_button.grid(row=3, column=5)
    
    
    
        

        
        
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    









    
    








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
