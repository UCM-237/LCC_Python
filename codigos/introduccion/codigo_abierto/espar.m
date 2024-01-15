function espar(x)
%Este programa recibe un numero entero como variable de entrada. y muestra
%por pantalla un mensaje indicando si el numero recibido es par o impar.

%Calculamos el resto de la division por dos
resto=rem(x,2);

%Empleamos una estructura if - else -end para decidir que mensaje mostrar

if resto==0
    %si el resto es cero el número es par
    disp('el número es par')
else
    %si el resto no es cero el número es impar
    disp('el número es impar')
end