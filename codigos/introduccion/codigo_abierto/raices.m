function [x1,x2]=raices(a,b,c)
%Esta función calcula las raices de una ecuación de segundo grado ax^2+b^x+c=0
%las variables de entrada son los coeficientes a, b, c de la ecuación. 
%las variables de salida x1 , x2 son las dos raices de la ecuación

%calculo de la primera raiz
x1=(-b+(b^2-4*a*c)^(1/2))/(2*a)

%calculo de la segunda raiz
x2=(-b-(b^2-4*a*c)^(1/2))/(2*a)