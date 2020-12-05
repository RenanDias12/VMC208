# Máquina Virtual

Projeto feito para disciplina de Arquitetura de Computadores, não é Case-sensitive e além dos comandos que serão apresentados também suporta o comando 'EXIT' para finalizar a execução.

O Projeto funciona com a seguinte sixtaxe:
'Operação' 'Variavel destino' 'Variave l origem1' 'Variavel origem 2'/'Constante'

>Operações: SUMC, MULC, SUMV, MULV, AND, OR.

>Variaveis: VAR[0-8].

>Constantes: Suporta até 5 bits. 

>Exemplos de comandos:
```
sumc var1 var2 4
sumc var2 var3 24
mulc var3 var1 5
sumv var4 var1 var2
mulv var5 var1 var2
sumc var0 var0 43
AND var7 var0 var3
or var8 var0 var1 
mulv var0 var0 var0 
mulv var0 var0 var0
mulv var5 var5 var5 
mulv var5 var5 var5
```
