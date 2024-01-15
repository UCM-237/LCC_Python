function divis(x)
%Este programa recibe un numero entero como variable de entrada. y muestra
%por pantalla un mensaje indicando si el numero recibido es par. Si no es
%par, comprueba si es divisible por 3 y si lo es muestra un mensaje por  
%pantalla indicandolo. Si no es par ni divisible por tres muestra un
%mensaje diciendo que no es par ni disible por tres. 



%Empleamos una estructura if - else -end para decidir que mensaje mostrar

if rem(x,2)==0
    %si el resto es cero el número es par
    disp('el número es par')
elseif rem(x,3)==0
    %El número es divisble por tres
    disp('el número es divisible por 3')
else
    %el numero no es par ni divisible por tres
end