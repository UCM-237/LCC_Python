function y=taylorsin(x,n)
%Esta funci�n aproxima el valor del seno de un numero
%empleando para ello un polinomio de Taylor de grado 2n+1 desarrollado en 
%torno a x=0. Las variables de entrada son: x, valor para el que se desea 
%calcular el logaritmo. n Grado del polinomio que se emplear� en el 
%c�lculo. La variable de salida y es el logaritmo de x. (nota si x
%es un vector, calcular� el logaritmo para todos los puntos del vector)

%iniciliazamos la variable de salida y
y=0;
%construimos un b�cle para ir a�adiendo t�rminos al desarrollo
%es importante darse cuenta que para valores de n grandes el factorial(prod(1:2*n) no
%da ya resultados muy fiables.... 
for i=0:n
    y=y+(-1)^(i)*(x).^(2*i+1)/(prod(1:(2*i+1)));
end
