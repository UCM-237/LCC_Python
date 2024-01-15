function b=dec2bin_entero(d)
%convertir un numero entero de a un vector de cifras en binario,
%(El vector tiene tantas cifras como se precisen)

%el rollo está en dividir el numero por dos y guardar el resto hasta que el
%cociente sea 1....

%sacamos el digito mas pequeño antes de empezar
b=rem(d,2)
d=floor(d/2);
%a continuación seguimos con el resto hasta que el cociente sea cero

while d>1
    b=[rem(d,2) b] %bigendian
    d=floor(d/2)
end
%metemos el ultimo 1
b=[1 b];


