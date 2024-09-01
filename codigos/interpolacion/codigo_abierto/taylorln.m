function y=taylorln(x,n)
%Esta función aproxima el valor del logaritmo natural de un numero
%empleando para ello un polinomio de Taylor de grado n desarrollado en 
%torno a x=1. Las variables de entrada son: x, valor para el que se desea 
%calcular el logaritmo. n Grado del polinomio que se empleará en el 
%cálculo. La variable de salida y es el logaritmo de x. (nota si x
%es un vector, calculará el logaritmo para todos los puntos del vector)

%iniciliazamos la variable de salida y
y=0;

%construimos un búcle para ir añadiendo términos al desarrollo
for i=1:n
    y=y+(-1)^(i+1)*(x-1).^i/i;
end