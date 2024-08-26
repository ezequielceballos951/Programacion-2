import tkinter as tk

def validar_numeros(char):
    return char.isdigit() or char == ""

def calcular_resultado(operacion):
    try:
        num1 = int(entrada_numero1.get())
        num2 = int(entrada_numero2.get())
        
        if operacion == "+":
            resultado = num1 + num2
        elif operacion == "-":
            resultado = num1 - num2
        elif operacion == "*":
            resultado = num1 * num2
        elif operacion == "/":
            if num2 != 0:
                resultado = num1 / num2
            else:
                resultado = "Error"
        elif operacion == "%":
            if num2 != 0:
                resultado = num1 % num2
            else:
                resultado = "Error"
        elif operacion == "Reset":
            resultado = 0
            entrada_numero1.delete(0, tk.END)
            entrada_numero2.delete(0, tk.END)
        else:
            resultado = "Error"

        entrada_resultado.config(state=tk.NORMAL)  
        entrada_resultado.delete(0, tk.END) 
        entrada_resultado.insert(0, str(resultado))  
        entrada_resultado.config(state='readonly')  
    except ValueError:
        entrada_resultado.config(state=tk.NORMAL)  
        entrada_resultado.delete(0, tk.END) 
        entrada_resultado.insert(0, "Error")  
        entrada_resultado.config(state='readonly')  

def clear_campos():
    entrada_numero1.delete(0, tk.END)
    entrada_numero2.delete(0, tk.END)
    entrada_resultado.config(state=tk.NORMAL)  
    entrada_resultado.delete(0, tk.END)  
    entrada_resultado.config(state='readonly')  


root = tk.Tk()
root.title("Calculadora")

marco = tk.Frame(root, bg="lightblue", padx=10, pady=10)
marco.pack(padx=20, pady=20, fill=tk.BOTH, expand=True)

etiqueta_numero1 = tk.Label(marco, text="Primer Número", font=("Arial", 16), bg="lightblue")
etiqueta_numero1.grid(row=0, column=0, padx=10, pady=5)  

etiqueta_numero2 = tk.Label(marco, text="Segundo Número", font=("Arial", 16), bg="lightblue")
etiqueta_numero2.grid(row=1, column=0, padx=10, pady=5)  

etiqueta_resultado = tk.Label(marco, text="Resultado", font=("Arial", 16), bg="lightblue")
etiqueta_resultado.grid(row=2, column=0, padx=10, pady=5)  


validar_cmd = root.register(validar_numeros)
entrada_numero1 = tk.Entry(marco, font=("Arial", 16), bg="white", validate="key", validatecommand=(validar_cmd, "%S"))
entrada_numero1.grid(row=0, column=1, padx=10, pady=5)  

entrada_numero2 = tk.Entry(marco, font=("Arial", 16), bg="white", validate="key", validatecommand=(validar_cmd, "%S"))
entrada_numero2.grid(row=1, column=1, padx=10, pady=5) 

entrada_resultado = tk.Entry(marco, font=("Arial", 16), bg="white", state='readonly')  
entrada_resultado.grid(row=2, column=1, padx=10, pady=5)  

botones = {
    "+": (0, 2),
    "-": (1, 2),
    "*": (0, 3),
    "/": (1, 3),
    "%": (0, 4),
    "Reset": (1, 4),
    "Clear": (2, 4)
}

for texto, (fila, columna) in botones.items():
    if texto == "Clear":
        boton = tk.Button(marco, text=texto, font=("Arial", 16), command=clear_campos)
    else:
        boton = tk.Button(marco, text=texto, font=("Arial", 16), command=lambda t=texto: calcular_resultado(t))
    boton.grid(row=fila, column=columna, padx=10, pady=10)

root.mainloop()