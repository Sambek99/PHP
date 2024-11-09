import ply.lex as lex

# List of token names.   This is always required
# GAONA DEFINICION DE TOKENS PARA POSTERIOR DEFINICION DE REGLAS
reserved = {
    "if": "IF",
    "else": "ELSE",
    "elseif": "ELSEIF",
    "while": "WHILE",
    "do": "DO",
    "for": "FOR",
    "foreach": "FOREACH",
    "switch": "SWITCH",
    "case": "CASE",
    "default": "DEFAULT",
    "function": "FUNCTION",
    "class": "CLASS",
    "public": "PUBLIC",
    "private": "PRIVATE",
    "protected": "PROTECTED",
    "try": "TRY",
    "catch": "CATCH",
    "finally": "FINALLY",
    "include": "INCLUDE",
    "require": "REQUIRE",
    "include_once": "INCLUDE_ONCE",
    "require_once": "REQUIRE_ONCE",
    "static": "STATIC",
    "return": "RETURN",
    "%": "MOD",
    "&&": "AND",
    "||": "OR",
    "!": "NOT"
}

# Definición de los tokens, incluyendo las palabras reservadas
tokens = (
    'FLOAT',
    'INTEGER',
    'PLUS',
    'MINUS',
    'STRING',
    'BOOLEAN',
    'ARRAY',
    'OBJECT',
    'TUPLE',
    'TIMES',
    'DIVIDE',
    'SIMPLE_ASSIGNMENT',
    'ADDITION_ASSIGNMENT',
    'SUBTRACTION_ASSIGNMENT',
    'LPAREN',
    'RPAREN',
    'VARIABLE',
    'COMA',
    'LCOR',
    'RCOR',
    'LBRACE',
    'RBRACE',
    'PUNTOYCOMA',
    'COMMENT'
) + tuple(reserved.values())  # GAONA INICIO DE DEFINICION DE TOKENS

# Regular expression rules for simple tokens
# GAONA INICIO
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_COMA = r','
t_LCOR = r'\['
t_RCOR = r'\]'
t_LBRACE = r'\{'
t_RBRACE = r'\}'
t_PUNTOYCOMA = r';'

# Expresiones para los operadores compuestos (prioridad alta)
t_OR = r'\|\|'  # || operador OR
t_AND = r'&&'   # && operador AND
t_MOD = r'%'    # % operador MOD
# GAONA FIN

# GAONA INICIO
# Revisar primero si es palabra reservada
def t_RESERVED(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'  # Expresión regular para palabras que empiezan con letra
    t.type = reserved.get(t.value, 'VARIABLE')  # Si es palabra reservada, se asigna el tipo adecuado
    return t

def t_STRING(t):
    r'"[^\n]*"'  # Expresión regular corregida para cadenas
    t.value = t.value[1:-1]  # Eliminar las comillas
    return t

def t_VARIABLE(t):
    r'\$[a-zA-Z_\x80-\xff][a-zA-Z0-9_\x80-\xff]*'  # Expresión regular corregida para variables
    t.type = reserved.get(t.value, 'VARIABLE')  # Si es palabra reservada, asigna el tipo adecuado
    return t

def t_FLOAT(t):
    r'-?\d+\.\d*([eE][+-]?\d+)?'  # Expresión regular corregida para flotantes
    t.value = float(t.value)
    return t

def t_INTEGER(t):
    r'-?\d+'  # Expresión regular corregida para enteros
    t.value = int(t.value)
    return t

def t_BOOLEAN(t):
    r'(true|false)'  # Expresión regular corregida para booleanos
    t.value = t.value.lower() == 'true'  # Convierte el valor a booleano
    return t

# Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Ignorar espacios y saltos de línea
t_ignore = r' \t\n'

# Error handling rule
def t_error(t):
    print(f"Illegal character '{t.value[0]}'")  # Manejo de errores más detallado
    t.lexer.skip(1)
# GAONA FIN


# Construir el lexer
lexer = lex.lex()

# Test it out
data = '''
3 + 4 * 10 if || % &&
  + -20 *2 3.5 2 {} , ; $hola "HOla" 4%5
'''

# Darle al lexer una entrada
lexer.input(data)

# Tokenizar
while True:
    tok = lexer.token()
    if not tok:
        break  # No hay más entrada
    print(tok)  # Muestra los tokens
