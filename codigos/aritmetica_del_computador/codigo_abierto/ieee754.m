function d=ieee754(b)
%convierte de un numero escrito en es estandar a un numero en base diez,

%se supone que el numero en binario es un vector de 64 elementos dados en
%el orden signo (1), exponente (11), mantisa (52)

%calculamos el valor del exponente
%empezamos por 'restar' el exceso
exponente=-1023
for i=2:12
    exponente=exponente+ b(i)*2^(12-i)
end


%calculamos el valor de la mantisa y el numero
if exponente >1023
    %el numero ha desbordado no cabe
    if any(mantisa)
        d=nan;
    else
        d=inf;
    end
elseif exponente>-1023
    %numero normalizado normal y corriente
    mantisa=1 %uno implicito de la mantisa
    %calculamos el resto de la mantisa
    for i=13:64
        mantisa=mantisa+b(i)*2^(12-i)
    end
    %calculamos el numero
    d=(-1)^b(1)*mantisa*2^exponente
else
    %numero desnormalizado
    mantisa=0
    for i=13:64
        mantisa=mantisa+b(i)*2^(12-i)
    end

    %calculamos el número
    d=(-1)^b(1)*mantisa*2^-1022
end
