import ply.yacc as yacc
from lexico import tokens  

# Diccionario para almacenar variables
variables_declaradas = {}

### Reglas Sintácticas ###


def p_parametros(p):
    '''
    parametros : VARIABLE
               | VARIABLE COMA parametros
    '''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = [p[1]] + p[3]

def p_cases(p):
    '''
    cases : CASE expresion COLON programa
          | CASE expresion COLON programa cases
    '''
    if len(p) == 5:
        p[0] = [(p[2], p[4])]
    else:
        p[0] = [(p[2], p[4])] + p[5]

def p_pares(p):
    '''
    pares : STRING COLON expresion
          | STRING COLON expresion COMA pares
    '''
    if len(p) == 4:
        p[0] = {p[1]: p[3]}
    else:
        p[0] = {p[1]: p[3], **p[5]}

def p_llamada_funcion(p):
    '''
    llamada_funcion : VARIABLE LPAREN parametros RPAREN
    '''
    p[0] = f"Llamada a función {p[1]} con parámetros {p[3]}"

# Programa principal
def p_statement(p):
    '''
    statement : asignacion
              | impresion
              | solicitud_datos
              | expresion_aritmetica
              | declaracion_estructura
              | condicion
    '''
    p[0] = p[1]

def p_programa(p):
    '''
    programa : statement programa
             | statement
    '''
    if len(p) == 3:
        p[0] = [p[1]] + p[2]
    else:
        p[0] = [p[1]]


########################################## REQUERIMIENTOS BASICOS ##########################################

# *Impresión con cero, uno o más argumentos*
def p_impresion(p):
    '''
    impresion : ECHO expresiones PUNTOYCOMA
              | ECHO PUNTOYCOMA
    '''
    if len(p) == 3:  # Sin argumentos
        print("")
    else:  # Con argumentos
        print(" ".join(map(str, p[2])))

def p_expresiones(p):
    '''
    expresiones : expresion
                | expresion COMA expresiones
    '''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = [p[1]] + p[3]


# *Solicitud de datos por teclado*
def p_solicitud_datos(p):
    '''
    solicitud_datos : VARIABLE SIMPLE_ASSIGNMENT INPUT LPAREN STRING RPAREN PUNTOYCOMA
    '''
    variable = p[1]
    mensaje = p[5]
    valor = input(mensaje)  # Solicita datos al usuario
    variables_declaradas[variable] = valor
    print(f"Variable '{variable}' asignada con el valor ingresado: {valor}")


# *Expresiones aritméticas con uno o más operadores*
def p_expresion_aritmetica(p):
    '''
    expresion_aritmetica : expresion_aritmetica operador term
                         | term
    '''
    if len(p) == 4:
        operador = p[2]
        if operador == '+':
            p[0] = p[1] + p[3]
        elif operador == '-':
            p[0] = p[1] - p[3]
        elif operador == '*':
            p[0] = p[1] * p[3]
        elif operador == '/':
            if p[3] == 0:
                print("Error: división entre cero.")
                p[0] = None
            else:
                p[0] = p[1] / p[3]
        elif operador == '%':
            p[0] = p[1] % p[3]
    else:
        p[0] = p[1]

def p_term(p):
    '''
    term : term operador factor
         | factor
    '''
    if len(p) == 4:
        p[0] = eval(f"{p[1]} {p[2]} {p[3]}")
    else:
        p[0] = p[1]

def p_factor(p):
    '''
    factor : LPAREN expresion_aritmetica RPAREN
           | INTEGER
           | FLOAT
           | VARIABLE
    '''
    if len(p) == 4:
        p[0] = p[2]
    elif isinstance(p[1], str) and p.slice[1].type == 'VARIABLE':
        variable = p[1]
        if variable in variables_declaradas:
            p[0] = variables_declaradas[variable]
        else:
            print(f"Error: Variable '{variable}' no declarada.")
            p[0] = None
    else:
        p[0] = p[1]

def p_operador(p):
    '''
    operador : PLUS
             | MINUS
             | TIMES
             | DIVIDE
             | MOD
    '''


# *Condiciones con uno o más conectores*
def p_condicion(p):
    '''
    condicion : IF LPAREN expresion RPAREN LBRACE programa RBRACE
              | IF LPAREN expresion RPAREN LBRACE programa RBRACE ELSE LBRACE programa RBRACE
    '''
    if len(p) == 8:  # Solo IF
        if p[3]:
            p[0] = p[6]
    elif len(p) == 12:  # IF-ELSE
        p[0] = p[6] if p[3] else p[10]


# *Definición de variables con tipos y almacenamiento de resultados*


def p_asignacion(p):
    '''
    asignacion : VARIABLE SIMPLE_ASSIGNMENT expresion PUNTOYCOMA
    '''
    variable = p[1]
    valor = p[3]
    variables_declaradas[variable] = valor
    print(f"Variable '{variable}' asignada con valor: {valor}")


# *Declaración de estructuras de datos*
def p_declaracion_estructura(p):
    '''
    declaracion_estructura : VARIABLE SIMPLE_ASSIGNMENT LCOR lista_elementos RCOR PUNTOYCOMA
                           | VARIABLE SIMPLE_ASSIGNMENT LCOR RCOR PUNTOYCOMA
    '''
    variable = p[1]
    if len(p) == 7:  # Estructura con elementos
        variables_declaradas[variable] = p[4]
    else:  # Estructura vacía
        variables_declaradas[variable] = []
    print(f"Estructura '{variable}' declarada con valor: {variables_declaradas[variable]}")

def p_lista_elementos(p):
    '''
    lista_elementos : expresion
                    | expresion COMA lista_elementos
    '''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = [p[1]] + p[3]


########################################## ESTRUCTURAS DE DATOS ##########################################

# ** COLAS
def p_declarar_cola(p):
    '''
    declarar_cola : VARIABLE SIMPLE_ASSIGNMENT QUEUE LPAREN RPAREN
    '''
    variables_declaradas[p[1]] = []
    print(f"Cola {p[1]} declarada vacía.")


# ** PILAS
def p_declarar_pila(p):
    '''
    declarar_pila : VARIABLE SIMPLE_ASSIGNMENT STACK LPAREN RPAREN
    '''
    variables_declaradas[p[1]] = []
    print(f"Pila {p[1]} declarada vacía.")


# ** MAPA
def p_declarar_mapa(p):
    '''
    declarar_mapa : VARIABLE SIMPLE_ASSIGNMENT MAP LPAREN RPAREN
    '''
    variables_declaradas[p[1]] = {}
    print(f"Mapa {p[1]} declarado vacío.")


# ** GRAFO
def p_declarar_grafo(p):
    '''
    declarar_grafo : VARIABLE SIMPLE_ASSIGNMENT GRAPH LPAREN RPAREN
    '''
    variables_declaradas[p[1]] = {"nodes": [], "edges": []}
    print(f"Grafo {p[1]} declarado vacío.")


# ** CONJUNTOS
def p_declarar_conjunto(p):
    '''
    declarar_conjunto : VARIABLE SIMPLE_ASSIGNMENT SET LPAREN RPAREN
    '''
    variables_declaradas[p[1]] = set()
    print(f"Conjunto {p[1]} declarado vacío.")


# ** DICCIONARIOS
def p_declarar_diccionario_valores(p):
    '''
    declarar_diccionario_valores : VARIABLE SIMPLE_ASSIGNMENT LBRACE pares RBRACE
    '''
    variables_declaradas[p[1]] = p[3]
    print(f"Diccionario {p[1]} declarado con valores: {p[3]}.")


########################################## ESTRUCTURA DE CONTROL ##########################################

# ** SWITCH-CASE
def p_switch_case(p):
    '''
    switch_case : SWITCH LPAREN expresion RPAREN LBRACE cases DEFAULT COLON programa RBRACE
                | SWITCH LPAREN expresion RPAREN LBRACE cases RBRACE
    '''
    if len(p) == 11:  # SWITCH con default
        p[0] = {'cases': p[6], 'default': p[8]}
    else:
        p[0] = {'cases': p[6]}


# ** BREAK
def p_break(p):
    '''
    break : BREAK PUNTOYCOMA
    '''
    p[0] = "break"
    print("Break ejecutado.")


# ** FOR-EACH
def p_for_each(p):
    '''
    for_each : FOR LPAREN VARIABLE IN VARIABLE RPAREN LBRACE programa RBRACE
    '''
    for item in variables_declaradas.get(p[4], []):
        parser.parse(p[7])


# ** DO-WHILE
def p_do_while(p):
    '''
    do_while : DO LBRACE programa RBRACE WHILE LPAREN expresion RPAREN PUNTOYCOMA
    '''
    while True:
        parser.parse(p[3])
        if not p[7]:
            break


# ** SWITCH CASE DEFAULT
def p_switch_case_default(p):
    '''
    switch_case_default : SWITCH LPAREN expresion RPAREN LBRACE cases DEFAULT COLON programa RBRACE
    '''
    p[0] = "Switch con casos y default ejecutado."


# ** CONTINUE
def p_continue(p):
    '''
    continue : CONTINUE PUNTOYCOMA
    '''
    p[0] = "continue"
    print("Continue ejecutado.")


########################################## ESTRUCTURA DE FUNCION ##########################################

# ** FUNCION PARAMETROS OPCIONALES 
def p_funcion_parametros_opcionales(p):
    '''
    funcion_parametros_opcionales : FUNCTION VARIABLE LPAREN parametros RPAREN LBRACE programa RBRACE
                                  | FUNCTION VARIABLE LPAREN RPAREN LBRACE programa RBRACE
    '''
    if len(p) == 9:  # Con parámetros
        p[0] = {'name': p[2], 'params': p[4], 'body': p[7]}
    else:  # Sin parámetros
        p[0] = {'name': p[2], 'params': [], 'body': p[6]}

        
# ** FUNCION LAMBDA
def p_funcion_lambda(p):
    '''
    funcion_lambda : VARIABLE SIMPLE_ASSIGNMENT LAMBDA LPAREN parametros RPAREN COLON expresion
    '''
    p[0] = f"Función lambda {p[1]} declarada con parámetros {p[5]}."


# ** FUNCION RECURSIVA
def p_funcion_recursiva(p):
    '''
    funcion_recursiva : FUNCTION VARIABLE LPAREN parametros RPAREN LBRACE llamada_funcion RBRACE
    '''
    p[0] = f"Función recursiva {p[2]} declarada."


# ** FUNCION CON RETORNO
def p_funcion_con_retorno(p):
    '''
    funcion_con_retorno : FUNCTION VARIABLE LPAREN parametros RPAREN LBRACE RETURN expresion PUNTOYCOMA RBRACE
    '''
    p[0] = f"Función {p[2]} declarada con retorno {p[8]}."


# ** FUNCION CON RETORNOS MULTIPLES
def p_funcion_multiples_retornos(p):
    '''
    funcion_multiples_retornos : FUNCTION VARIABLE LPAREN parametros RPAREN LBRACE RETURN LCOR expresiones RCOR PUNTOYCOMA RBRACE
    '''
    p[0] = f"Función {p[2]} declarada con múltiples retornos {p[8]}."


# ** FUNCION CON SOBRECARGA
def p_funcion_sobrecarga(p):
    '''
    funcion_sobrecarga : FUNCTION VARIABLE LPAREN parametros RPAREN LBRACE programa RBRACE
                       | FUNCTION VARIABLE LPAREN RPAREN LBRACE programa RBRACE
    '''
    p[0] = f"Función {p[2]} sobrecargada con o sin parámetros."



########################################## - ##########################################

# *Expresiones generales*
def p_expresion(p):
    '''
    expresion : STRING
              | INTEGER
              | FLOAT
              | VARIABLE
    '''
    if p.slice[1].type == 'VARIABLE':
        variable = p[1]
        if variable in variables_declaradas:
            p[0] = variables_declaradas[variable]
        else:
            print(f"Error: Variable '{variable}' no declarada.")
            p[0] = None
    else:
        p[0] = p[1]

# Manejo de errores
def t_error(t):
    print(f"Illegal character '{t.value[0]}' at line {t.lineno}, position {t.lexpos}")
    t.lexer.skip(1)  # Salta el carácter no reconocido


# Regla para vacío
def p_empty(p):
    'empty :'
    pass

# Construcción del parser

parser = yacc.yacc(debug=True, write_tables=False)
def getAnalizadorSintactico():
    return yacc.yacc()

"""
# Bucle principal para probar el parser
while True:
    try:
        s = input('calc > ')
    except EOFError:
        break
    if not s:
        continue
    result = parser.parse(s)
    print(result)
"""
