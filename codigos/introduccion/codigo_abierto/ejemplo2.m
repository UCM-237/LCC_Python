function salida=ejemplo2(entrada)
%esta funcion toma el valor de entrada lo eleva al cuadrado y pasa el
%resultado aun segunda función que calcula la raiz cuadrada...
%entrada y salida deberían ser iguales al final

x=entrada^2;

%%%%llamada a la segunda función%%%%
salida=raiz(x);

%%%%%%codigo de la segunda funcion%%%%%
function out=raiz(in)
disp('version incluida en el archivo ejemplo2.m')

out=in^(t);

%%%%%codigo de la tercera función%%%%
function y=expo(a)
y=a/2