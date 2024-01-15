function d=bin2dec_entero(b)
%pasar de vector en binario a numero en decimal...

%miramos como de largo es...

l=length(b);

%inicializo en decimal a cero...
d=0;
% y ahora montamos un secillo bucle que nos haga la cuenta...(supongo
% bigendian, jojo!, jojo!, jojo!, jojooo!)

for i=l:-1:1
d=d+b(i)*2^(l-i);
end
