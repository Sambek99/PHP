
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'ABSTRACT ADDITION_ASSIGNMENT AND ARRAY AS BOOL BOOLEAN CALLABLE CASE CATCH CLASS CLONE COLON COMA CONCAT CONST DECLARE DECREMENT DEFAULT DIE DIVIDE DIVISION_ASSIGNMENT DO DOLAR ECHO ELSE ELSEIF EMPTY ENDFOR ENDFOREACH ENDIF ENDSWITCH ENDWHILE EQ EXIT EXTENDS FALSE FALSO FINAL FINALLY FLOAT FOR FOREACH FUNCTION GE GLOBAL GOTO GT IDENTICAL IF IMPLEMENTS INCLUDE INCLUDE_ONCE INCREMENT INSTANCEOF INT INTEGER INTERFACE ISSET LBRACE LCOR LE LIST LPAREN LT MINUS MOD MOD_ASSIGNMENT MULTIPLE_COMMENT MULTIPLICATION_ASSIGNMENT NAMESPACE NEQ NEW NOT NOT_IDENTICAL NULL OBJECT OR PLUS PRINT PRIVATE PROTECTED PUBLIC PUNTOYCOMA QUESTION RBRACE RCOR REQUIRE REQUIRE_ONCE RETURN RPAREN SIMPLE_ASSIGNMENT SIMPLE_COMMENT STATIC STRING SUBTRACTION_ASSIGNMENT SWITCH THROW TIMES TRAIT TRUE TRY TUPLE UNSET USE VAR VARIABLE VERDADERO VOID WHILE YIELDimprimir : impresion\n    impresion : ECHO expresiones \n              | ECHO\n    \n    expresiones : expresion \n                | expresion COMA expresiones\n    \n    expresion : STRING\n              | INTEGER \n              | FLOAT\n              | VARIABLE\n    asignacion : DOLAR VARIABLE SIMPLE_ASSIGNMENT valorasignacion : DOLAR VARIABLE SIMPLE_ASSIGNMENT operadorAritmetica\n    valor : INTEGER \n          | FLOAT\n          | VARIABLE \n    \n    valor : VERDADERO\n          | FALSO \n    \n    operadorAritmetica : valor operador valor\n     \n    operador : PLUS \n            | MINUS\n            | TIMES\n            | DIVIDE\n            | MOD \n    '
    
_lr_action_items = {'ECHO':([0,],[3,]),'$end':([1,2,3,4,5,6,7,8,9,11,],[0,-1,-3,-2,-4,-6,-7,-8,-9,-5,]),'STRING':([3,10,],[6,6,]),'INTEGER':([3,10,],[7,7,]),'FLOAT':([3,10,],[8,8,]),'VARIABLE':([3,10,],[9,9,]),'COMA':([5,6,7,8,9,],[10,-6,-7,-8,-9,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'imprimir':([0,],[1,]),'impresion':([0,],[2,]),'expresiones':([3,10,],[4,11,]),'expresion':([3,10,],[5,5,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> imprimir","S'",1,None,None,None),
  ('imprimir -> impresion','imprimir',1,'p_imprimir','main.py',7),
  ('impresion -> ECHO expresiones','impresion',2,'p_impresion','main.py',11),
  ('impresion -> ECHO','impresion',1,'p_impresion','main.py',12),
  ('expresiones -> expresion','expresiones',1,'p_expresiones','main.py',22),
  ('expresiones -> expresion COMA expresiones','expresiones',3,'p_expresiones','main.py',23),
  ('expresion -> STRING','expresion',1,'p_expresion','main.py',34),
  ('expresion -> INTEGER','expresion',1,'p_expresion','main.py',35),
  ('expresion -> FLOAT','expresion',1,'p_expresion','main.py',36),
  ('expresion -> VARIABLE','expresion',1,'p_expresion','main.py',37),
  ('asignacion -> DOLAR VARIABLE SIMPLE_ASSIGNMENT valor','asignacion',4,'p_asignacion','main.py',53),
  ('asignacion -> DOLAR VARIABLE SIMPLE_ASSIGNMENT operadorAritmetica','asignacion',4,'p_asignacion_EA','main.py',56),
  ('valor -> INTEGER','valor',1,'p_valor','main.py',60),
  ('valor -> FLOAT','valor',1,'p_valor','main.py',61),
  ('valor -> VARIABLE','valor',1,'p_valor','main.py',62),
  ('valor -> VERDADERO','valor',1,'p_valor_bool','main.py',67),
  ('valor -> FALSO','valor',1,'p_valor_bool','main.py',68),
  ('operadorAritmetica -> valor operador valor','operadorAritmetica',3,'p_operadorAritmetica','main.py',73),
  ('operador -> PLUS','operador',1,'p_operador','main.py',78),
  ('operador -> MINUS','operador',1,'p_operador','main.py',79),
  ('operador -> TIMES','operador',1,'p_operador','main.py',80),
  ('operador -> DIVIDE','operador',1,'p_operador','main.py',81),
  ('operador -> MOD','operador',1,'p_operador','main.py',82),
]
