import ply.yacc as yacc
from lexico import tokens
import time
import os

variables_declaradas = {}

def p_programa(p):
    '''
    programa : statement programa
             | statement 
    '''
    
def p_statement(p):
    '''
    statement : asignacion
              | impresion
              | expresion_aritmetica
              | declarar_array
              
    '''  

def p_asignacion(p):
    '''
    asignacion : VARIABLE SIMPLE_ASSIGNMENT expresion PUNTOYCOMA
                
    '''
    


    # impresión con cero, uno o más argumentos
    
def p_impresion(p):
    '''
    impresion : ECHO expresiones 
              | ECHO
    '''
    if len(p) == 2:
        print("")  # Imprimir vacío
    else:
        print(p[2])  # Imprimir el/los argumentos


def p_expresiones(p):
    '''
    expresiones : expresion 
                | expresion COMA expresiones
    '''
    # Combina los elementos para imprimirlos
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = f"{p[1]} {p[3]}"  # Concatenar con un espacio


def p_expresion(p):
    '''
    expresion : STRING
              | INTEGER 
              | FLOAT
              | VARIABLE
              | expresion_aritmetica
    '''
    if p.slice[1].type == 'VARIABLE':
        variable = p[1]
        if variable not in variables_declaradas:
            print(f"Error: la variable {variable} no ha sido declarada.")
            p[0] = None
        else:
            p[0] = variables_declaradas[variable]
    else:
        p[0] = p[1]
        
        
    # solicitud de datos por teclado
    
    # expresiones aritméticas con uno o más operadores
def p_expresion_aritmetica(p):
    '''
    expresion_aritmetica : expresion_aritmetica operador term
                         | term
    '''
    if len(p) == 4:
        p[0] = eval(f"{p[1]} {p[2]} {p[3]}")  # Realiza la operación
    else:
        p[0] = p[1]

def p_term(p):
    '''
    term : term operador factor
         | factor
    '''
    if len(p) == 4:
        p[0] = eval(f"{p[1]} {p[2]} {p[3]}")  # Realiza la operación
    else:
        p[0] = p[1]

def p_factor(p):
    '''
    factor : LPAREN expresion_aritmetica RPAREN
           | INTEGER
           | FLOAT
           | VARIABLE
    '''
    if len(p) == 4:  # Caso de paréntesis
        p[0] = p[2]
    elif isinstance(p[1], str) and p.slice[1].type == 'VARIABLE':
        variable = p[1]
        if variable in variables_declaradas:
            p[0] = variables_declaradas[variable]
        else:
            print(f"Error: Variable {variable} no declarada")
            p[0] = None
    else:
        p[0] = p[1]  # Devuelve el número25 + 3 * 2;


def p_operador(p):
    ''' 
    operador : PLUS 
            | MINUS
            | TIMES
            | DIVIDE
            | MOD 
    '''  

    
    # condiciones con uno o más conectores
    
    # declarar estructuras de datos
def p_declarar_array(p):
    '''
    declarar_array :  VARIABLE SIMPLE_ASSIGNMENT ARRAY LPAREN RPAREN
                    | VARIABLE SIMPLE_ASSIGNMENT ARRAY LPAREN lista_elementos RPAREN
                    | VARIABLE SIMPLE_ASSIGNMENT LCOR RCOR
                    | VARIABLE SIMPLE_ASSIGNMENT LCOR lista_elementos RCOR

    '''
    variable = p[1]
    valores = [] if len(p) in [5, 6] else p[5]  # Manejo de arrays vacíos
    variables_declaradas[variable] = valores
    print(f"Array {variable} declarado con valores: {valores}")

def p_lista_elementos(p):
    '''
    lista_elementos : empty
                    | expresion
                    | expresion COMA lista_elementos
    '''
    if len(p) == 1:  # Lista vacía
        p[0] = []
    elif len(p) == 2:  # Un solo elemento
        p[0] = [p[1]]
    else:  # Lista de elementos separados por comas
        p[0] = [p[1]] + p[3]

# ------------------------
    
# Error rule for syntax errors
def p_error(p):
    if p:
        print(f"Error de sintaxis en la línea {p.lineno}, columna {find_column(p)}, token inesperado: {p.value}")


def find_column(token):
    input = token.lexer.lexdata
    line_start = input.rfind('\n', 0, token.lexpos) + 1
    return (token.lexpos - line_start) + 1

# Build the parser
def p_empty(p):
    'empty :'
    pass

parser = yacc.yacc()

while True:
   try:
       s = input('calc > ')
   except EOFError:
       break
   if not s: continue
   result = parser.parse(s)
   print(result)
   if (s == "STOP"):
        # Generar el nombre del archivo de log
        usuario_git = input("Ingrese el usuario") # <---- Cambiar este usuario
        fecha_hora = time.strftime("%d%m%Y-%Hh%M")
        log_filename = f"sintactico-{usuario_git}-{fecha_hora}.txt"

        # Obtener el directorio actual  
        current_directory = os.path.dirname(os.path.abspath(__file__))

        # Crear las carpetas "algoritmos" y "logs" si no existen
        algoritmos_directory = os.path.join(current_directory, "algoritmos")
        logs_directory = os.path.join(current_directory, "logs")
        os.makedirs(algoritmos_directory, exist_ok=True)
        os.makedirs(logs_directory, exist_ok=True)

        # Ruta completa para el archivo de log en la carpeta "logs"
        log_filepath = os.path.join(logs_directory, log_filename)

        # Abrir el archivo de log en modo escritura
        with open(log_filepath, "w") as log_file:

                # Aquí se añadirían las líneas del código donde se registran los eventos
                # Ejemplo de cómo se registran eventos
                log_file.write("Generación de log iniciada.\n")

                # En cada acción relevante en tu código, puedes añadir algo como:
                # Log para impresión
                log_file.write(s+"\n")

                # Log para declaración de variables
                log_file.write(str(result)+"\n")
        break
       
   
   


