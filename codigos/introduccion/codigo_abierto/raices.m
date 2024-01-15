function [x1,x2]=raices(a,b,c)
%Esta funci�n calcula las raices de una ecuaci�n de segundo grado ax^2+b^x+c=0
%las variables de entrada son los coeficientes a, b, c de la ecuaci�n. 
%las variables de salida x1 , x2 son las dos raices de la ecuaci�n

%calculo de la primera raiz
x1=(-b+(b^2-4*a*c)^(1/2))/(2*a)

%calculo de la segunda raiz
x2=(-b-(b^2-4*a*c)^(1/2))/(2*a)