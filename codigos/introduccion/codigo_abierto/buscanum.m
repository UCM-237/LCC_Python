function posicion=buscanum(x,n)
%este programa emplea un bucle for y un break para buscar en el vector x, 
%la primera ves que aparece el número n

%obtenemos la longitud del vector
l1=length(x);
%iniciamos posicion a un valor absurdo
posicion=-1;
for i=1:l1
    if x(i)==n
        posicion=i;
        break
    end
end
if posicion==-1
    disp('el numero pedido no se encuentra en el vector x') 
end