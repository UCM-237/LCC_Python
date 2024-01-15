function signo(x)
%este programa emplea una estructura switch para informarnos del signo de
%un número.

%NOTA EL PROGRAMA NO COMPRUEBA QUE LA VARIABLE DE ENTRADA X SEA UN NUMERO,
%SI ES UN VECTOR O UNA MATRIZEL RESULTADO NO TIENE SENTIDO
  
s=sign(x); %obtnemos el signo del número mediante la función sign

%construimos la estructura switch,

switch s
    case 1
        disp('el número es positivo')
    case -1
        disp('el número es negativo')
    otherwise
        disp('el número es cero')
end
