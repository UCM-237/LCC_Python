function pares=buscapar(x)
%este programa emplea un bucle for y un continue para construir un vector
%de salida con los numeros pares contenidos en el vector de entrada.

%obtenemos la longitud del vector
l1=length(x);
%iniciamos el vector de salida a un vector vacío,
pares=[];
for i=1:l1
    if rem(x(i),2)~=0
        continue
    end
    pares=[pares x(i)];
end