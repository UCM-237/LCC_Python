function salida=ejemplo2(entrada)
%esta funcion toma el valor de entrada lo eleva al cuadrado y pasa el
%resultado aun segunda funci�n que calcula la raiz cuadrada...
%entrada y salida deber�an ser iguales al final

x=entrada^2;

%%%%llamada a la segunda funci�n%%%%
salida=raiz(x);

%%%%%%codigo de la segunda funcion%%%%%
function out=raiz(in)
disp('version incluida en el archivo ejemplo2.m')

out=in^(t);

%%%%%codigo de la tercera funci�n%%%%
function y=expo(a)
y=a/2