function signo(x)
%este programa emplea una estructura switch para informarnos del signo de
%un n�mero.

%NOTA EL PROGRAMA NO COMPRUEBA QUE LA VARIABLE DE ENTRADA X SEA UN NUMERO,
%SI ES UN VECTOR O UNA MATRIZEL RESULTADO NO TIENE SENTIDO
  
s=sign(x); %obtnemos el signo del n�mero mediante la funci�n sign

%construimos la estructura switch,

switch s
    case 1
        disp('el n�mero es positivo')
    case -1
        disp('el n�mero es negativo')
    otherwise
        disp('el n�mero es cero')
end
