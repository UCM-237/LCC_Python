function p=primos(n)
%generador de números primos. Genera un vector con los primeros n números
%primos. (si n es muy grande tardará mucho en acabar.

%creamos un vector de salida en el que incluimos el 2 como primer número
%primo...
p=zeros(1,n);
p(1)=2;

%iniciamos un contador a 1, puesto que ya tenemos el primer número primo

j=1;

%creamos un segundo contador que recorra los números impares, a a partir
%del 3
s=3;
%creamos un bucle while, que realiza las iteraciones necesarias hasta tener
%los n números primos deseados.
while j<n
    %creamos un bucle for que recorra todos los primos encontrados hasta la
    %fecha
    pr=1; %Activamos un aviso
    for i=2:j
        %calculamos el resto de la división entera con cada primo de p
        if rem(s,p(i))==0
            %si el numero es divisible por algun primo anterior
            pr=0; %Desactivamos el aviso: el número no el primo...
            break %... y cortamos la búsqueda
        end
    end
      
    if pr==1 %si el número es primo
        p(j+1)=s; %lo guardamos...
        %...e incrementamos el contador de números primos encontrados
        j=j+1; 
    end
    %por ultimo, generamos un nuevo candidato para ver si es primo...
    s=s+2;
end
    