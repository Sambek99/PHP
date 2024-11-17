import ply.yacc as yacc
from lexico import tokens

variables_declaradas = {}

    
# IMPRESION

def p_imprimir(p):
    'imprimir : impresion'

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
      
# SOLICITUD DE DATOS

"""
def p_solicitudDatos(p):
    '''solicitudDatos : INPUT LPAREN cadena RPAREN'''

def p_cadena(p):
    '''cadena : VARIABLE'''

"""

def p_asignacion(p):
    '''asignacion : DOLAR VARIABLE SIMPLE_ASSIGNMENT valor
                  | DOLAR VARIABLE SIMPLE_ASSIGNMENT valor_bool
                  | DOLAR VARIABLE SIMPLE_ASSIGNMENT operadorAritmetica'''
    variable = p[1]
    valor = p[3]
    variables_declaradas[variable] = valor
    print(f"{variable} = {valor}")

'''
def p_asignacion_EA (p):
    'asignacion : DOLAR VARIABLE SIMPLE_ASSIGNMENT operadorAritmetica'
'''
def p_valor(p):
    '''
    valor : INTEGER 
          | FLOAT
          | VARIABLE 
    '''
    p[0] = p[1]
    
def p_valor_bool(p): 
    '''
    valor : VERDADERO
          | FALSO 
    '''
    
def p_operadorAritmetica(p):
    '''
    operadorAritmetica : valor operador valor
    '''
    
def p_operador(p):
    ''' 
    operador : PLUS 
            | MINUS
            | TIMES
            | DIVIDE
            | MOD 
    '''  
    
# Error rule for syntax errors
def p_error(p):
    if p:
        print(f"Error de sintaxis en la línea {p.lineno}, token inesperado: {p.value}")
    else:
        print("Error de sintaxis: fin inesperado de la entrada")


# Build the parser
parser = yacc.yacc()

while True:
   try:
       s = input('calc > ')
   except EOFError:
       break
   if not s: continue
   result = parser.parse(s)
   print(result)