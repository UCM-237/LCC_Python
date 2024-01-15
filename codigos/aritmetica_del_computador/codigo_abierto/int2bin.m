function a=int2bin(x)
%Este programa enplea un método iterativo para convertir un entero >0 en 
%base 10 en un array que representa a dicho entero en binario. 
%El array tiene 32 elementos (tipicos 4 bytes de la representacion 
%de un entero).  
%El método se emplea en electrónica en los conversores análogico-digital 
%más sencillos. La idea es ir comprobando si los bits deben valer cero o
%uno, empezando por el más significativo. Si el numero que se quiere
%representar es mayor o igual que 2^31, el bit 32 sera 1, si es mas pequeño
%será cero etc...

%Limitamos el tamano del número a cuatro bytes... (tipico tamaño de entero
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