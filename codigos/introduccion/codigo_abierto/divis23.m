function divis23(x)
%Este programa recibe un numero entero como variable de entrada. y muestra
%por pantalla un mensaje indicando si el numero recibido es par. 
%si el numero es par y divisible entre tres,
%si es divisible entre tres  
%Si no es par ni divisible por tres 



%Empleamos una estructura if - else -end para decidir que mensaje mostrar

if rem(x,2)==0
    %si el resto es cero el número es par
    %comprobamos con un if anidado si además es divisible entre tres
    if rem(x,3)==0
        disp('el número es par y divisible entre tres')
    else
        disp('el número es par')
    end
elseif rem(x,3)==0
    %El número es divisble entre tres
    disp('el número es divisible entre 3')
else
    %el numero no es par ni divisible entre tres
    disp('el número no es par ni divisible entre tres')
end