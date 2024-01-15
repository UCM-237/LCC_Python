function s=sumafor(x,y)
%este programa emplea un bucle for sencillo para sumar dos vectores
%primero comprueba si son del mismo tamaño. Si no lo son da un mensaje de
%aviso

l1=length(x);
l2=length(y);
if l1==l2
    %construimos un vector de ceros del mismo tamaño que x e y paraa
    %guardar el resultado de la suma,
    s=zeros(size(x));
    %si son iguales los suma elemento a elemento usando un bucle for
    for i=1:l1
        s(i)=x(i)+y(i);
    end
else
    disp('los vectores son de distinto tamaño')
end