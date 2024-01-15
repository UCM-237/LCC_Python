function y=taylorln(x,n)
%Esta funci�n aproxima el valor del logaritmo natural de un numero
%empleando para ello un polinomio de Taylor de grado n desarrollado en 
%torno a x=1. Las variables de entrada son: x, valor para el que se desea 
%calcular el logaritmo. n Grado del polinomio que se emplear� en el 
%c�lculo. La variable de salida y es el logaritmo de x. (nota si x
%es un vector, calcular� el logaritmo para todos los puntos del vector)

%iniciliazamos la variable de salida y
y=0;

%construimos un b�cle para ir a�adiendo t�rminos al desarrollo
for i=1:n
    y=y+(-1)^(i+1)*(x-1).^i/i;
end