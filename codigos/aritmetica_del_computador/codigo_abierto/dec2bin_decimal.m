function b=dec2bin_decimal(d)

%aquí hay varias historias interesantes... La primera es hasta donde se
%desea sacar decimales... porque claro, podemos sacar muchos o pocos
%decimales. Vamos a sacar 52 (una mantisa conmpleta)  a parti del primero
%distinto de cero
%el vector resultante solo contiene los numeros en binario en bigendian...

%saco el primero

b=fix(d*2);
d=d*2-b;
%creo un bucle para ir añadiendo el resto.
n=1
while b(n)==0
    n=n+1;
    b(n)=fix(d*2);
    d=d*2-fix(d*2);
end
% y a partir de aqui saco 52...
for i=n+1:52+n
    b(i)=fix(d*2);
    d=d*2-fix(d*2);
end
