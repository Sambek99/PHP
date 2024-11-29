import tkinter as tk
from tkinter import filedialog, scrolledtext
from tkinter import ttk  # Importar ttk para widgets con estilo
import sys
import io
from datetime import datetime
import lexico as lx
import main as smt


analizadorLexico = lx.getAnalizadorLexico()
analizadorSintactico = smt.getAnalizadorSintactico()


# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Editor de Código")
ventana.geometry("800x600")

# Configuración de estilo
style = ttk.Style()
style.configure("TButton", font=("Arial", 12), padding=10, relief="flat", background="#4CAF50", foreground="white")
style.map("TButton", background=[("active", "#45a049")])

style.configure("TFrame", background="#f4f4f9")
style.configure("TText", font=("Consolas", 12), background="#f8f8f8", foreground="#333333")

# Crear un archivo de logs (solo para ejemplo)
logs_file = open("logs.txt", "a")

# Función para abrir archivos
def abrir_archivo():
    ruta = filedialog.askopenfilename(filetypes=[("Archivos Python", "*.py"), ("Todos los archivos", "*.*")])
    if ruta:
        with open(ruta, "r") as archivo:
            editor.delete("1.0", tk.END)
            editor.insert("1.0", archivo.read())
        consola.insert(tk.END, f"Archivo '{ruta}' cargado.\n")

# Función para guardar archivos
def guardar_archivo():
    ruta = filedialog.asksaveasfilename(defaultextension=".py", filetypes=[("Archivos Python", "*.py")])
    if ruta:
        with open(ruta, "w") as archivo:
            archivo.write(editor.get("1.0", tk.END))
        consola.insert(tk.END, f"Archivo guardado en '{ruta}'.\n")

# Función para correr el código
def correr_codigo():
    codigo = editor.get("1.0", tk.END)
    consola.delete("1.0", tk.END)
    try:
        old_stdout = sys.stdout
        old_stderr = sys.stderr
        sys.stdout = io.StringIO()
        sys.stderr = io.StringIO()

        exec(codigo)

        consola.insert(tk.END, sys.stdout.getvalue())
        consola.insert(tk.END, sys.stderr.getvalue())
    except Exception as e:
        consola.insert(tk.END, f"Error: {e}\n")
    finally:
        sys.stdout = old_stdout
        sys.stderr = old_stderr

# Función para análisis léxico
def lexico():
    codigo = editor.get("1.0", tk.END)
    logs_file.write(datetime.now().strftime("%m/%d/%Y, %H:%M:%S") + "\n")
    logs_file.write("Entrada:" + "\n" + codigo + "\n")
    consola.configure(state='normal')
    consola.delete("1.0", tk.END)

    lista_tokens = []
    analizadorLexico.input(codigo)
    lx.getListaTokens(analizadorLexico, lista_tokens)
    logs_file.write("Salida:" + "\n")

    for i, token in enumerate(lista_tokens):
        logs_file.write(str(token) + "\n")
        consola.insert(float(i + 1), str(token) + "\n")

    consola.configure(state='disabled')

def sintatico():
    codigo = editor.get("1.0", tk.END)
    logs_file.write(datetime.now().strftime("%m/%d/%Y, %H:%M:%S") + "\n")
    logs_file.write("Entrada:" + "\n" + codigo + "\n")
    consola.configure(state='normal')
    consola.delete("1.0", tk.END)

    logs_file.write("Salida:" + "\n")
    analisis = str(analizadorSintactico.parse(codigo))

    if smt.errores_sintacticos:
        for i, error in enumerate(smt.errores_sintacticos):
            logs_file.write(str(error) + "\n")
            consola.insert(float(i + 1), str(error) + "\n")
        smt.errores_sintacticos.clear()
    else:
        consola.insert("1.0", "Ingreso Válido")

    consola.configure(state='disabled')


# Función para limpiar la consola
def limpiar_consola():
    consola.configure(state='normal')
    consola.delete("1.0", tk.END)
    consola.configure(state='disabled')

# Marco para los botones
frame_botones = ttk.Frame(ventana)
frame_botones.pack(side=tk.TOP, fill=tk.X, padx=10, pady=5)

# Botones
btn_abrir = ttk.Button(frame_botones, text="Open", command=abrir_archivo)
btn_abrir.pack(side=tk.LEFT, padx=5)

btn_guardar = ttk.Button(frame_botones, text="Save", command=guardar_archivo)
btn_guardar.pack(side=tk.LEFT, padx=5)

btn_correr = ttk.Button(frame_botones, text="Sintactico", command=correr_codigo)
btn_correr.pack(side=tk.LEFT, padx=5)

btn_lexico = ttk.Button(frame_botones, text="Lexico", command=lexico)
btn_lexico.pack(side=tk.LEFT, padx=5)

# Botón para limpiar la consola
btn_clean = ttk.Button(frame_botones, text="Clean", command=limpiar_consola)
btn_clean.pack(side=tk.LEFT, padx=5)

# Área de texto para el editor
editor = scrolledtext.ScrolledText(ventana, wrap=tk.WORD, font=("Consolas", 12), height=20)
editor.pack(fill=tk.BOTH, expand=True, padx=10, pady=(0, 10))

# Área de texto para la consola (para mostrar el resultado del análisis léxico)
consola = scrolledtext.ScrolledText(ventana, wrap=tk.WORD, font=("Consolas", 10), height=10, bg="#f0f0f0")
consola.pack(fill=tk.BOTH, expand=True, padx=10, pady=(0, 10))

# Ejecutar la ventana
ventana.mainloop()

# No olvides cerrar el archivo de logs al final (en una aplicación real, esto se haría con un `finally`)
logs_file.close()
