grammar marzo;

program : 
statements* 
             ;

declaration   : 
              'int' Name     #declaracion
              ;
assignacion :
            Name '=' Numero     #assign
            ;

expression: 
    expression '+' expression #suma
    | Numero                  #primaria
    ;

printstmt: 
    'print' Numero             
;
statements :
        ifstatement                         
    |  expression                          
    | printstmt  
    | assignacion  
    | declaration              
;
comparation:
        Name '==' Numero
;

ifstatement:
        'if'   comparation  '{' statements* '}'                    #ifSinElse
        | 'if'   comparation   '{' statements* '}' 'else' '{'  statements* '}'                  #ifConElse
        ;


Name : [a-z]+;
Numero : [0-9]+;


WS : [ \t\n\r]+ -> skip ;