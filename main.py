import ply.yacc as yacc
from lexico import tokens

def p_asignacion(p):
    'asignacion : DOLAR VARIABLE SIMPLE_ASSIGNMENT valor'

def p_asignacion_EA (p):
    'asignacion : DOLAR VARIABLE SIMPLE_ASSIGNMENT operadorAritmetica'


def p_valor(p):
    '''
    valor : INTEGER 
            | FLOAT
            | VARIABLE 
    '''
    
def p_valor_bool(p): #da problemas
    '''
    valor : VERDADERO
            | FALSO 
            '''
    
def p_valor_OperacionAritmetica(p):
    '''
    valor : valor operador valor
    '''

def p_operador(p):
    ''' 
    operadorAritmetica : PLUS 
            | MINUS
            | TIMES
            | DIVIDE
            | MOD 
    '''        
    

# Error rule for syntax errors
def p_error(p):
    print("Error de sintaxis en la línea %d" % p.lineno)

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