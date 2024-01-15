function d=bin2dec_decimal(b)
%pasamos un array que contiene un numero decimal binarion sin parte entera
%a un numero en base 10

%primero obtenemos la longitud del vector

l=length(b);

%inicializamos el numero en base diez
d=0;
%y luego contruimos un bucle para recondtruir el numero

for i=1:l
   d=d+b(i)*2^-i;
end