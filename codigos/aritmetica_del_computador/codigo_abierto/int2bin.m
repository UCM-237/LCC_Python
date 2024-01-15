function a=int2bin(x)
%Este programa enplea un m�todo iterativo para convertir un entero >0 en 
%base 10 en un array que representa a dicho entero en binario. 
%El array tiene 32 elementos (tipicos 4 bytes de la representacion 
%de un entero).  
%El m�todo se emplea en electr�nica en los conversores an�logico-digital 
%m�s sencillos. La idea es ir comprobando si los bits deben valer cero o
%uno, empezando por el m�s significativo. Si el numero que se quiere
%representar es mayor o igual que 2^31, el bit 32 sera 1, si es mas peque�o
%ser� cero etc...

%Limitamos el tamano del n�mero a cuatro bytes... (tipico tama�o de entero
%largo)
a=zeros(1,32);

%Codigo con un bulce for decreciente
% for i=32:-1:1
%     if 2^(i-1)>x;
%         a(i)=0
%     else
%         a(i)=1
%         x=x-2^(i-1)
%     end
% end
        
%El codigo para que quede al derecho el bucle tampoco es muy complicado...
for i=1:32
    if 2^(32-i)>x;
        a(i)=0
    else
        a(i)=1
        x=x-2^(32-i)
    end
end