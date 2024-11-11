import ply.lex as lex
# List of token names.   This is always required
# GAONA Y STEVEN DEFINICION DE TOKENS PARA POSTERIOR DEFINICION DE REGLAS
reserved = {
    "if": "IF",
    "else": "ELSE",
    "elseif": "ELSEIF",
    "endif": "ENDIF",
    "while": "WHILE",
    "endwhile": "ENDWHILE",
    "do": "DO",
    "for": "FOR",
    "endfor": "ENDFOR",
    "foreach": "FOREACH",
    "endforeach": "ENDFOREACH",
    "switch": "SWITCH",
    "case": "CASE",
    "default": "DEFAULT",
    "endswitch": "ENDSWITCH",
    "function": "FUNCTION",
    "class": "CLASS",
    "interface": "INTERFACE",
    "trait": "TRAIT",
    "extends": "EXTENDS",
    "implements": "IMPLEMENTS",
    "abstract": "ABSTRACT",
    "final": "FINAL",
    "static": "STATIC",
    "public": "PUBLIC",
    "protected": "PROTECTED",
    "private": "PRIVATE",
    "const": "CONST",
    "try": "TRY",
    "catch": "CATCH",
    "finally": "FINALLY",
    "throw": "THROW",
    "array": "ARRAY",
    "callable": "CALLABLE",
    "bool": "BOOL",
    "int": "INT",
    "object": "OBJECT",
    "void": "VOID",
    "null": "NULL",
    "echo": "ECHO",
    "print": "PRINT",
    "include": "INCLUDE",
    "require": "REQUIRE",
    "include_once": "INCLUDE_ONCE",
    "require_once": "REQUIRE_ONCE",
    "return": "RETURN",
    "yield": "YIELD",
    "list": "LIST",
    "global": "GLOBAL",
    "var": "VAR",
    "unset": "UNSET",
    "isset": "ISSET",
    "empty": "EMPTY",
    "declare": "DECLARE",
    "namespace": "NAMESPACE",
    "use": "USE",
    "as": "AS",
    "new": "NEW",
    "clone": "CLONE",
    "instanceof": "INSTANCEOF",
    "exit": "EXIT",
    "die": "DIE",
    "goto": "GOTO"
}

# Definición de los tokens, incluyendo las palabras reservadas
tokens = (
    'FLOAT', 
    'INTEGER',
    'PLUS', 
    'MINUS',
    'STRING',
    'BOOLEAN', 
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
    'SIMPLE_COMMENT',
    'MULTIPLE_COMMENT',
# STEVEN INICIO
    'LT',
    'GT',
    'AND',
    'NOT',
    'OR',
    'MOD',
# STEVEN FIN  
# ARIANA INICIO
    'LE',
    'GE',
    'EQ', 
    'NEQ', 
    'IDENTICAL', 
    'NOT_IDENTICAL',
    'MULTIPLICATION_ASSIGNMENT', 
    'DIVISION_ASSIGNMENT', 
    'MOD_ASSIGNMENT',
    'INCREMENT', 
    'DECREMENT', 
    'CONCAT', 
    'COLON', 
    'QUESTION'
# ARIANA FIN   

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

# STEVEN INICIO 
t_NOT = r'!'
t_SIMPLE_ASSIGNMENT = r'='
t_ADDITION_ASSIGNMENT = r'\+='
t_SUBTRACTION_ASSIGNMENT = r'-='

t_LT = r'<'
t_GT = r'>'
# STEVEN FIN

# ARIANA INICIO
t_EQ = r'=='
t_NEQ = r'!='
t_IDENTICAL = r'==='
t_NOT_IDENTICAL = r'!=='
t_LE = r'<='
t_GE = r'>='
t_INCREMENT = r'\+\+'
t_DECREMENT = r'--'
t_CONCAT = r'\.'
t_COLON = r':'
t_QUESTION = r'\?'
# ARIANA FIN

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
    # r'\$[a-zA-Z_][a-zA-Z_0-9]*'   CREO QUE DEBERIA SER ASI        
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
t_ignore = ' \t\n'

# Error handling rule
def t_error(t):
    print(f"Illegal character '{t.value[0]}'")  # Manejo de errores más detallado
    t.lexer.skip(1)
# GAONA FIN

# STEVEN INICIO  
# Ignorar comentarios de una línea (// o #) y comentarios de múltiples líneas (/* ... */)
def t_SIMPLE_COMMENT(t):
    r'//.*|\#.*'
    pass  # Ignorar los comentarios
    if t.value.startswith("//"):
        t.value = t.value[2:].strip()  # Elimina '//' y los espacios en blanco al inicio y al final
    elif t.value.startswith("#"):
        t.value = t.value[1:].strip()  # Elimina '#' y los espacios en blanco al inicio y al final
    return t

def t_MULTIPLE_COMMENT(t):
    r'/\*[\s\S]*?\*/'
    pass  # Ignorar los comentarios 
    t.value = t.value.replace('\n', ' ').replace('\r', ' ')  # Reemplaza los saltos de línea con espacios
    t.value = t.value[2:-2].strip()  # Devuelve el token del comentario múltiple sin '/*    */'
    return t

def t_TUPLE(t):
    r'\(.*?\)'  # Captura contenido entre paréntesis
    return t


# STEVEN FIN  

# Construir el lexer
lexer = lex.lex()

# Test it out


data2 = '''
"SOY STEVEN" #TENGO 24
3 + 4 * 10 if || % &&
  + -20 *2 3.5 2 {} , ; $hola "HOla" 4%5
// hola 
 #hola
/*
125 hola
*/
/*23 holsf
fdfh
hfdhf*/
/* 25 */
t=25
1 == 1


'''

# Darle al lexer una entrada
lexer.input(data2)

# Tokenizar
while True:
    tok = lexer.token()
    if not tok:
        break  # No hay más entrada
    print(tok)  # Muestra los tokens
